# 🚀 AxisConnect — AI-Powered Employee Self Service (ESS) Chatbot

AxisConnect is an intelligent Employee Self-Service assistant built using **Streamlit**, **Groq LLaMA**, and **RAG (Retrieval-Augmented Generation)**.
It allows employees to log in, view their details, access HR policies, and interact with an AI assistant that understands both company documents and real employee records.

This project combines **LLM-powered chat**, **database-backed employee profiles**, and **PDF policy retrieval** to create a realistic ESS chatbot experience.

---

## 🔥 Demo Video

🎥 **Watch the full project demo:**
👉 [https://youtu.be/t94JwCQ8cq0](https://youtu.be/t94JwCQ8cq0)

---

## 🔥 Key Features

### ✅ **Employee Login System**

* Secure login using Employee Code.
* Profile card showing:

  * Name
  * Employee ID
  * Department
  * Role
  * Joining Date

### ✅ **AI Chat Assistant (Axis)**

* Powered by **Groq LLaMA 3.1 8B Instant**
* Remembers chat context
* Responds using:

  * HR policy documents (RAG)
  * Logged-in employee’s details

### ✅ **RAG (Retrieval-Augmented Generation)**

* Loads and processes HR policy PDFs
* Splits documents → embeds text → stores in ChromaDB
* Produces accurate, context-aware answers

### ✅ **Quick Action Buttons**

* Apply Leave
* View Salary Details
* View IT Assets
* Check Goals
* HR Policies
  Each triggers a predefined system prompt.

### ✅ **Modern UI**

* Clean sidebar design
* Employee card
* Smooth chat interface
* Custom theme via `gui.py`

---

## 🧠 Technology Stack

### **AI / NLP**

* Groq LLaMA 3.1 8B Instant
* LangChain
* ChromaDB
* MiniLM-L6-v2 Embeddings

### **Frontend**

* Streamlit
* Custom CSS Styling

### **Backend**

* Python
* SQLAlchemy ORM
* Supabase / PostgreSQL

### **Document Processing**

* PyPDF
* LangChain PDF Loader
* Recursive text splitter

---

## 📁 Project Structure

```
AxisConnect/
│
├── .env                     # Environment variables (ignored by Git)
├── .gitignore
├── .python-version
├── app.py                  # Main Streamlit application
├── assistant.py            # LLM conversation chain logic
├── database.py             # SQLAlchemy DB connection + engine
├── gui.py                  # Chat UI components + styling
├── models.py               # ORM Models (Employee, etc.)
├── prompts.py              # System prompts + welcome message
├── pyproject.toml
├── readme.md               # Project documentation
├── requirements.txt
├── seed_data.py            # Script to insert sample employee data
│
├── data/
│   ├── employees.py                    # Employee seed data (Python)
│   ├── umbrella_corp_policies.pdf      # HR Policy PDF (used for RAG)
│   ├── vectorstore/                    # ChromaDB persisted index
│   │     ├── chroma.sqlite3
│   │     ├── *.bin
│   │     ├── *.pickle
│   │     └── (auto-generated files)
│   └── __pycache__/
│
└── services/
    ├── employee_service.py             # Employee profile aggregation logic
    └── __pycache__/
```

✔ Matches your VS Code
✔ Nothing removed
✔ Perfect for GitHub & resume

---

## ⚙️ Environment Variables (`.env`)

```
GROQ_API_KEY=your_groq_key
SUPABASE_DB_URL=your_postgres_url
SUPABASE_DB_PASSWORD=your_password
```

---

## 🛠️ Local Setup Instructions

```
git clone <repo>
cd AxisConnect

pip install -r requirements.txt
# or using UV
uv sync

streamlit run app.py
```

---

## 🧑‍💻 Author

**Rishi**
AI ESS Chatbot Developer

---.

