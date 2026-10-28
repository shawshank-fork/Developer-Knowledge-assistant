from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_health_check():
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}


def test_get_document():
    response = client.get("/documents/42")

    assert response.status_code == 200
    assert response.json()["document_id"] == 42

def test_ask_question():
    response = client.post(
        "/ask",
        json={"question": "How do i start the backend?"}
    )  

    assert response.status_code == 200
    assert response.json() == {
        "received_question": "How do i start the backend?"
    } 

def test_ask_question_missing_field():
    response = client.post(
        "/ask",
        json={"message": "How do i start the backend?"}
    )

    assert response.status_code == 422