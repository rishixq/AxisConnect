import streamlit as st

def load_theme():
    st.markdown("""
    <style>

    /* ---------------- SIDE BAR ---------------- */

    /* Sidebar background */
    [data-testid="stSidebar"] {
        background-color: #000000 !important;     /* Charcoal Grey */
    }

    /* ---- SIDEBAR HEADER (Logo + Title Side-by-Side) ---- */
    .sidebar-header {
        display: flex !important;
        align-items: center !important;
        gap: 15px !important;
        padding-left: 10px !important;
        padding-top: 15px !important;
        padding-bottom: 20px !important;
    }

    .sidebar-logo {
        width: 55px !important;
        height: 55px !important;
        background-color: white !important;
        padding: 5px !important;
        border-radius: 8px !important;
        display: flex;
        justify-content: center;
        align-items: center;
    }

    .sidebar-logo img {
        width: 100% !important;
        height: 100% !important;
        object-fit: contain !important;
    }

    .title-text {
        display: flex;
        flex-direction: column;
        line-height: 1.1;
    }

    .title-text h1 {
        margin: 0 !important;
        padding: 0 !important;
        font-size: 26px !important;
        color: #F7F1DE !important;
        font-weight: 700 !important;
    }

    .title-text p {
        margin: 2px 0 2px 0 !important;
        padding: 2px !important;
        color: #E8EBE4 !important;
        font-size: 14px !important;
    }

    /* ---------------- CHAT MESSAGES ---------------- */

    .stChatMessage.human {
        background-color: #F0F0F0 !important;
        color: #222 !important;
        border: 1px solid #D0D0D0 !important;
        border-radius: 12px !important;
        padding: 12px !important;
    }

    .stChatMessage.ai {
        background-color: #FFF7F7 !important;
        border-left: 4px solid #C71F1F !important;
        color: #222 !important;
        border-radius: 10px !important;
        padding: 14px !important;
    }

    /* ---------------- CHAT INPUT BOX ---------------- */

    .stChatInput > div > div {
        background-color: #f5f5f5 !important;
        border: 2px solid #000000 !important;
        border-radius: 12px !important;
    }

    .stChatInput input {
        color: #000000 !important;
        font-size: 16px !important;
        padding-left: 10px !important;
    }

    .stChatInput input::placeholder {
        color: #00000 !important;
        opacity: 100 !important;
    }

    /* ---------------- PAGE BACKGROUND ---------------- */

    body, .stApp {
        background-color: #FFFFFF !important;
    }

    </style>
    """, unsafe_allow_html=True)



class AssistantGUI:
    def __init__(self, assistant):
        self.assistant = assistant
        self.messages = assistant.messages
        self.employee_information = assistant.employee_information

    def get_response(self, user_input):
        return self.assistant.get_response(user_input)

    def render_messages(self):
        for message in self.messages:
            if message["role"] == "user":
                st.chat_message("human").markdown(message["content"])
            elif message["role"] == "ai":
                st.chat_message("ai").markdown(message["content"])

    def set_state(self, key, value):
        st.session_state[key] = value

    def render_user_input(self):
        user_input = st.chat_input("Type here...", key="input")
        if user_input and user_input.strip() != "":
            st.chat_message("human").markdown(user_input)

            response_generator = self.get_response(user_input)
            with st.chat_message("ai"):
                response = st.write_stream(response_generator)

            # Save to chat history
            self.messages.append({"role": "user", "content": user_input})
            self.messages.append({"role": "ai", "content": response})

            self.set_state("messages", self.messages)

    def render(self):
        load_theme()

        # CHAT BODY
        self.render_messages()
        self.render_user_input()
