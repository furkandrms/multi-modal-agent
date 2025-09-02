import os
from database.mongodb import save_task_log
from langchain_community.utilities import SerpAPIWrapper
from services.llm_service import call_openai  

class SearchAgent:
    def __init__(self):
        self.search = SerpAPIWrapper(serpapi_api_key=os.getenv("SERPAPI_API_KEY"))
    
    def handle(self, task: str, session_id: str, chat_history: str = "") -> str:
        raw_result = self.search.run(task)
        prompt = (f"""
        Previous conversations with the user:
        {chat_history if chat_history else "(There is no previous conversation.)"}

        Using the following web search result, provide the user with a concise, clear, and up-to-date summary in English.
        Only use information that is truly useful. Avoid unnecessary repetition and filler sentences.
        If available, give examples from reliable sources.
        The user's main question: {task}

        Web search result:
        {raw_result}
        """
        )
        output = call_openai(prompt)
        save_task_log("SearchAgent", task, output, session_id)
        return output
