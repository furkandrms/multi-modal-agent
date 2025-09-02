from services.llm_service import call_openai
from database.mongodb import save_task_log

class FallbackAgent:
    def handle(self, task: str, session_id: str, chat_history: str = "") -> str:
        prompt = (f"""
                    Previous conversations with the user:

                    {chat_history if chat_history else "(There is no previous conversation.)"}

                    The following user request could not be matched to any of the supported tasks (coding, content creation, or web search):

                    Task: {task}

                    Guidelines:
                    - Politely inform the user that this task cannot be handled.
                    - Briefly list which types of tasks you can help with (such as coding, blog/article writing, or web searches).
                    - If possible, suggest how the user might rephrase their request to fit the supported task types.
                    - Be concise and clear.

                    Return only your response to the user.
                    """
        )

        output = call_openai(prompt)
        save_task_log("FallbackAgent", task, output, session_id)
        return output