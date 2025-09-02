from services.llm_service import call_openai
from database.mongodb import save_task_log

class ContentAgent:
    def handle(self, task: str, session_id: str, chat_history: str = "") -> str:
        prompt = (f"""
        Previous conversations with the user:

        {chat_history if chat_history else "(There is no previous conversation.)"}

        Take into account the above conversation history and the following new task:

        Task: {task}

        Guidelines:
        - Considering the above conversation history and the new task, produce a comprehensive and informative blog post.
        - Add a short summary at the beginning of the article.
        - The article should be coherent, clear, and fluent.
        - Refer to at least two reliable sources and list them at the end of the article.
        - Avoid unnecessary repetition and filler sentences.
        - Return only the article and the sources.
        """
        )

        output = call_openai(prompt)
        save_task_log("ContentAgent", task, output, session_id)
        return output
