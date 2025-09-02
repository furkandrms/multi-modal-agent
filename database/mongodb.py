import os
from pymongo import MongoClient
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()

MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017/")
client = MongoClient(MONGO_URI)
db = client.peer_agent_db
collection = db.task_logs

def save_task_log(agent: str, task: str, response: str, session_id: str):
    log = {
        "session_id": session_id,
        "agent": agent,
        "task": task,
        "response": response,
        "timestamp": datetime.utcnow()
    }
    collection.insert_one(log)
