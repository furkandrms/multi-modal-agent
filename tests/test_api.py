import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_execute_codeagent_happy_path():
    response = client.post(
        "/v1/agent/execute",
        json={"task": "Write a Python function that calculates the sum of a list of numbers."}
    )
    assert response.status_code == 200
    data = response.json()
    assert "response" in data
    assert "Python" in data["response"] or "python" in data["response"]

def test_execute_contentagent_happy_path():
    response = client.post(
        "/v1/agent/execute",
        json={"task": "Blog about the impact of AI in education."}
    )
    assert response.status_code == 200
    data = response.json()
    assert "response" in data
    assert "AI" in data["response"] or "Artificial Intelligence" in data["response"]

def test_execute_empty_task():
    response = client.post(
        "/v1/agent/execute",
        json={"task": ""}
    )
    assert response.status_code == 400
    data = response.json()
    assert "Task cannot be empty" in data["detail"]

def test_execute_unrelated_task():
    response = client.post(
        "/v1/agent/execute",
        json={"task": "Who was the first cat in space?"}
    )
    assert response.status_code in (200, 400, 500)  

def test_execute_unrelated_task2():
    response = client.post(
        "/v1/agent/execute",
        json={"task": "use an airplane"}
    )
    assert response.status_code in (200, 400)
    data = response.json()
    assert (
        "not supported" in data.get("response", "")
        or "cannot help" in data.get("response", "")
        or "only code, content or web search" in data.get("response", "")
    )
