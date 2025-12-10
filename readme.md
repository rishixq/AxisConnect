# 🚀 AxisConnect — AI-Powered Employee Self Service (ESS) Chatbot

AxisConnect is an intelligent Employee Self-Service assistant built using **Streamlit**, **Groq LLaMA**, and **RAG (Retrieval-Augmented Generation)**.  
It allows employees to log in, view their details, access HR policies, and interact with an AI assistant that understands both company documents and real employee records.

This project combines **LLM-powered chat**, **database-backed employee profiles**, and **PDF policy retrieval** to create a realistic ESS chatbot experience.

---

## 🔥 Key Features

### ✅ **Employee Login System**
- Secure login using Employee Code.  
- Profile card showing:
  - Name  
  - Employee ID  
  - Department  
  - Role  
  - Joining Date  

### ✅ **AI Chat Assistant (Axis)**
- Powered by **Groq LLaMA 3.1 8B Instant**  
- Remembers conversation context  
- Responds using both:
  - HR policy documents (RAG)
  - Logged-in employee’s details  

### ✅ **RAG (Retrieval-Augmented Generation)**
- Loads PDF HR policies  
- Splits documents  
- Embeds using MiniLM  
- Stores in **ChromaDB**  
- Produces accurate policy-based answers  

### ✅ **Quick Action Buttons**
- Apply Leave  
- View Salary Details  
- View IT Assets  
- Check Goals  
- HR Policies  
Each button triggers a predefined prompt to the assistant.

### ✅ **Modern UI**
- Custom-styled dark sidebar  
- Employee card  
- Smooth chat interface  
- AI/User message formatting  
- Custom theme loaded via `gui.py`  

---

## 🏗️ Project Architecture

AxisConnect/
│
├── app.py
├── assistant.py
├── gui.py
├── prompts.py
├── database.py
│
├── models/
│   └── models.py
│
├── services/
│   └── employee_service.py
│
├── data/
│   ├── umbrella_corp_policies.pdf
│   ├── vectorstore/
│   └── employees.py
│
├── requirements.txt
├── .gitignore
└── README.md


---

## 🧠 Technology Stack

### **AI / NLP**
- Groq LLaMA 3.1 8B Instant  
- LangChain  
- ChromaDB Vector Store  
- MiniLM-L6-v2 Embeddings  

### **Frontend**
- Streamlit  
- Custom CSS Styling  

### **Backend**
- Python  
- SQLAlchemy ORM  
- Supabase / PostgreSQL (optional)  

### **Document Processing**
- PyPDF  
- LangChain document loaders  
- Text splitting  

---

## ⚙️ Environment Variables (`.env`)

Create a `.env` file (NOT committed to GitHub):


Make sure `.env` is **included in `.gitignore`** ✔

---

## 🛠️ Local Setup Instructions

🧑‍💻 Author

Rishi (AxisConnect AI Developer)
