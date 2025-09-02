import uuid
from langchain_openai import OpenAI
from langchain.agents import initialize_agent, Tool, AgentType
from langchain.memory import ConversationBufferMemory
from agents.code_agent import CodeAgent
from agents.content_agent import ContentAgent
from agents.search_agent import SearchAgent

class PeerAgent:
    def __init__(self):
        self.llm = OpenAI(temperature=0)
        self.code_agent = CodeAgent()
        self.content_agent = ContentAgent()
        self.search_agent = SearchAgent()
        self.session_id = str(uuid.uuid4())
        self.memory_map = {
            self.session_id: ConversationBufferMemory(memory_key="chat_history", return_messages=True)
        }
        self.tools = [
            Tool(
                name="Kod Aracı",
                func=lambda task: self.code_agent.handle(task,  self.session_id),
                description="Solves code or script generation tasks."
            ),
            Tool(
                name="İçerik Aracı",
                func=lambda task: self.content_agent.handle(task, self.session_id),
                description="Solves blog, article, content generation tasks."
            ),
            Tool(
                name="Arama Aracı",
                func=lambda task: self.search_agent.handle(task, self.session_id),
                description="Used for tasks that require up-to-date information, news and search on the web."
            ),
            Tool(
                name="Fallback Aracı",
                func=lambda task: self.code_agent.handle(task, self.session_id),
                description="Fallback agent for tasks that do not fit other categories."
            )
        ]

    def route_task(self, task: str) -> dict:
        memory = self.memory_map[self.session_id]
        agent = initialize_agent(
            self.tools,
            self.llm,
            agent=AgentType.CONVERSATIONAL_REACT_DESCRIPTION,
            memory=memory,
            verbose=True
        )
        try:
            result = agent.run(input=task)
            return {
                "session_id": self.session_id,
                "task": task,
                "response": result,
                "memory_summary": memory.buffer
            }
        except Exception as e:
            return {"error": str(e)}
