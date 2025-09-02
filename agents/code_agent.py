from services.llm_service import call_openai
from database.mongodb import save_task_log

class CodeAgent:
    def handle(self, task: str, session_id: str, chat_history: str = "") -> str:
        prompt = (f"""
        Previous conversations with the user:

        {chat_history if chat_history else "(There is no previous conversation.)"}

        Take into account the above conversation history and the following new task:

        Task: {task}

        Guidelines:
        - Please consider the above previous requests and the most recent question to generate a complete and understandable Python code.
        - Add sufficient comments and explanations in the code.
        - At the beginning, include a brief explanation of what the code does.
        - If necessary, add a sample usage line.
        - Return only the code and the explanation. Do not include unnecessary extra comments.
        """ 
        )

        output = call_openai(prompt)
        save_task_log("CodeAgent", task, output, session_id)
        return output
