import os
import logging
import streamlit as st
from dotenv import load_dotenv

from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma

from langchain_groq import ChatGroq

from assistant import Assistant
from prompts import SYSTEM_PROMPT, WELCOME_MESSAGE
from gui import AssistantGUI

# DB
from database import SessionLocal
from services.employee_service import (
    get_employee_by_code,
    get_full_employee_profile
)


# ---------------------------------------------------------
# MAIN
# ---------------------------------------------------------
if __name__ == "__main__":
    load_dotenv()
    logging.basicConfig(level=logging.INFO)

    st.set_page_config(page_title="AxisConnect", page_icon="🤖", layout="wide")

    # ---------------------------------------------------------
    # CACHING HELPERS (performance improvements)
    # ---------------------------------------------------------
    @st.cache_resource(show_spinner="Loading LLM…")
    def load_llm():
        """Cache LLM instance so it's created once per app instance."""
        try:
            return ChatGroq(model="llama-3.1-8b-instant")
        except Exception as e:
            logging.error(f"LLM init error: {e}")
            raise

    @st.cache_resource(show_spinner="Loading Embeddings…")
    def load_embedding():
        """Cache HuggingFace embeddings object."""
        try:
            return HuggingFaceEmbeddings(
                model_name="sentence-transformers/all-MiniLM-L6-v2"
            )
        except Exception as e:
            logging.error(f"Embedding init error: {e}")
            raise

    @st.cache_resource(ttl=3600, show_spinner="Loading Company Policies…")
    def init_vector_store(pdf_path):
        """
        Initialize or load a persistent Chroma vectorstore.
        - If ./data/vectorstore exists and looks populated, attempt to open it (fast).
        - Otherwise, create vectorstore from PDF, persist it, and return.
        Returns None on failure (the app will show existing error handling).
        """
        try:
            embedding_function = load_embedding()
            persistent_path = "./data/vectorstore"

            # If persistent path exists and looks like a saved chroma DB, try to load
            if os.path.isdir(persistent_path):
                # check if main DB file exists (common name used by Chroma)
                sqlite_path = os.path.join(persistent_path, "chroma.sqlite3")
                if os.path.exists(sqlite_path):
                    try:
                        vectorstore = Chroma(persist_directory=persistent_path, embedding=embedding_function)
                        logging.info("Loaded vectorstore from persistent directory.")
                        return vectorstore
                    except Exception as e:
                        logging.warning(f"Failed to open persisted vectorstore, will attempt recreate: {e}")

            # If pdf doesn't exist, return None (error handled by caller)
            if not os.path.isfile(pdf_path):
                logging.error(f"Vector Store Error: PDF not found at {pdf_path}")
                return None

            # Load PDF → split → embeddings → persist
            loader = PyPDFLoader(pdf_path)
            docs = loader.load()

            text_splitter = RecursiveCharacterTextSplitter(
                chunk_size=2000,
                chunk_overlap=200,
            )
            splits = text_splitter.split_documents(docs)

            # Create vectorstore
            vectorstore = Chroma.from_documents(
                documents=splits,
                embedding=embedding_function,
                persist_directory=persistent_path,
            )

            logging.info("Created vectorstore and persisted to disk.")
            return vectorstore

        except Exception as e:
            logging.error(f"Vector Store Error: {str(e)}")
            return None

    # ---------------------------------------------------------
    # CREATE/LOAD LLM + VECTOR STORE
    # ---------------------------------------------------------
    # LLM is now cached and reused across requests (faster).
    llm = load_llm()

    # Vector store is cached (or None if something failed)
    vector_store = init_vector_store("data/umbrella_corp_policies.pdf")

    # ---------------------------------------------------------
    # SESSION STATE
    # ---------------------------------------------------------
    if "messages" not in st.session_state:
        st.session_state.messages = [{"role": "ai", "content": WELCOME_MESSAGE}]

    if "employee_profile" not in st.session_state:
        st.session_state.employee_profile = None

    if "quick_action" not in st.session_state:
        st.session_state.quick_action = None

    # ---------------------------------------------------------
    # SIDEBAR (BRANDING + LOGIN + PROFILE CARD)
    # ---------------------------------------------------------
    with st.sidebar:

        # ---------- BRANDING ----------
        st.markdown("""
        <div class="sidebar-header">
            <div class="sidebar-logo">
                <img src="https://i.pinimg.com/1200x/f8/33/15/f83315a9855a4c0d41269f3980b2404b.jpg" width="60"/>
            </div>
            <div class="title-text">
                <h1>AxisConnect</h1>
                <p>Employee Self Service Chatbot</p>
            </div>
        </div>
        """, unsafe_allow_html=True)

        # ---------- LOGIN ----------
        if st.session_state.employee_profile is None:

            with st.form("login_form"):
                employee_code = st.text_input("Enter Employee Code (e.g., EMP001)")
                submit = st.form_submit_button("Login")

            if submit:
                db = SessionLocal()
                emp = get_employee_by_code(db, employee_code)

                if not emp:
                    st.error("❌ Employee not found")
                else:
                    profile = get_full_employee_profile(db, emp.id)
                    st.session_state.employee_profile = profile
                    st.session_state["show_welcome"] = True
                    st.rerun()

                db.close()

        # ---------- AFTER LOGIN ----------
        else:
            profile = st.session_state.employee_profile

            st.markdown("<hr style='border:0.5px solid #555;'>", unsafe_allow_html=True)

            st.markdown(f"""
            <div style="
                background-color: #111;
                padding: 15px;
                border-radius: 10px;
                color: #fafafa;
                border: 1px solid #333;
            ">
                <h3 style="margin:0;color:#fff;">👤 {profile.get('name')}</h3>
                <p><b>ID:</b> {profile.get('employee_code')}</p>
                <p><b>Department:</b> {profile.get('department')}</p>
                <p><b>Role:</b> {profile.get('role')}</p>
                <p><b>Joined:</b> {profile.get('join_date')}</p>
            </div>
            """, unsafe_allow_html=True)

            # -------------------------------------------------------------
            # ⭐ PROPER STYLED QUICK ACTION BUTTONS (works + matches UI)
            # -------------------------------------------------------------
            st.markdown("""
            <style>
            .stButton > button {
                background-color: #000000 !important;
                color: #fafafa !important;
                border: 1px solid #333 !important;
                padding: 12px !important;
                border-radius: 10px !important;
                width: 100% !important;
                text-align: left !important;
                font-size: 15px !important;
                margin-bottom: 10px !important;
                white-space: nowrap !important;
            }
            .stButton > button:hover {
                background-color: #222 !important;
                border-color: #555 !important;
            }
            </style>
            """, unsafe_allow_html=True)

            st.markdown("<h4 style='color:#ccc; margin-top:20px;'>Quick Actions</h4>", unsafe_allow_html=True)

            col1, col2 = st.columns(2)

            with col1:
                if st.button("📝 Apply Leave"):
                    st.session_state.quick_action = "I want to apply for leave. Show leave application steps."
                    st.rerun()

                if st.button("📄 Salary Details"):
                    st.session_state.quick_action = "Show my salary details."
                    st.rerun()

            with col2:
                if st.button("🎯 My Goals"):
                    st.session_state.quick_action = "Show my goals and performance."
                    st.rerun()

                if st.button("🛠 IT Assets"):
                    st.session_state.quick_action = "Show all IT assets assigned to me."
                    st.rerun()

            if st.button("🗂 HR Policies"):
                st.session_state.quick_action = "Show me all HR policies."
                st.rerun()

    # ---------------------------------------------------------
    # STOP CHAT IF NOT LOGGED IN
    # ---------------------------------------------------------
    if st.session_state.employee_profile is None:
        st.info("🔒 Please log in using your Employee Code to use Axis.")
        st.stop()

    # ---------------------------------------------------------
    # LLM + ASSISTANT
    # ---------------------------------------------------------
    assistant = Assistant(
        system_prompt=SYSTEM_PROMPT,
        llm=llm,
        message_history=st.session_state.messages,
        vector_store=vector_store,
    )

    assistant.employee_information = st.session_state.employee_profile

    gui = AssistantGUI(assistant)

    # ---------------------------------------------------------
    # HANDLE QUICK ACTION PROMPT
    # ---------------------------------------------------------
    if st.session_state.quick_action:
        user_query = st.session_state.quick_action
        st.session_state.quick_action = None

        st.session_state.messages.append({"role": "user", "content": user_query})

        response_generator = assistant.get_response(user_query)
        final_response = st.write_stream(response_generator)

        st.session_state.messages.append({"role": "ai", "content": final_response})
        st.rerun()

    # ---------------------------------------------------------
    # RENDER CHAT
    # ---------------------------------------------------------

# ---------------------------------------------------------
# ⭐ WELCOME BANNER (shows only once after login)
# ---------------------------------------------------------
if "show_welcome" in st.session_state and st.session_state.show_welcome:
    employee_name = st.session_state.employee_profile.get("name", "Employee")

    st.markdown(f"""
        <div style="
            background-color: #f5f5f5;
            padding: 18px;
            border-radius: 12px ;
            border-left: 5px solid #000000;
            margin-bottom: 20px;
        ">
            <h2 style="margin:0; color:#222;">🎉 Welcome {employee_name}!</h2>
            <p style="margin:5px 0 0 0; font-size:16px; color:#000000;">
                I'm your <b>AI Assistant, Axis</b>.  
                How can I help you today?
            </p>
        </div>
    """, unsafe_allow_html=True)

    # show only once
    st.session_state.show_welcome = False

# Now render chat normally
gui.render()
