from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough

from database import SessionLocal
from services.employee_service import (
    get_employee_by_code,
    get_full_employee_profile
)


class Assistant:
    def __init__(
        self,
        system_prompt,
        llm,
        message_history=[],
        vector_store=None,
    ):
        self.system_prompt = system_prompt
        self.llm = llm
        self.messages = message_history
        self.vector_store = vector_store

        # Will be set AFTER employee login
        self.employee_code = None
        self.employee_information = None

        self.chain = self._get_conversation_chain()

    # ---------------------------------------------------------
    # Load employee profile after login
    # ---------------------------------------------------------
    def set_employee(self, employee_code: str):
        """Fetch employee profile from DB and store internally."""
        db = SessionLocal()

        emp = get_employee_by_code(db, employee_code)
        if not emp:
            db.close()
            raise ValueError(f"Employee '{employee_code}' not found")

        self.employee_information = get_full_employee_profile(db, emp.id)
        self.employee_code = employee_code

        db.close()
        print(f"✅ Employee profile loaded: {employee_code}")

    # ---------------------------------------------------------
    # Chat Response
    # ---------------------------------------------------------
    def get_response(self, user_input):
        return self.chain.stream(user_input)

    # ---------------------------------------------------------
    # LangChain Pipeline
    # ---------------------------------------------------------
    def _get_conversation_chain(self):
        prompt = ChatPromptTemplate(
            [
                ("system", self.system_prompt),
                MessagesPlaceholder("conversation_history"),
                ("human", "{user_input}"),
            ]
        )

        parser = StrOutputParser()

        chain = (
            {
                "retrieved_policy_information": self.vector_store.as_retriever(),
                "employee_information": lambda x: self.employee_information,
                "user_input": RunnablePassthrough(),
                "conversation_history": lambda x: self.messages,
            }
            | prompt
            | self.llm
            | parser
        )

        return chain

