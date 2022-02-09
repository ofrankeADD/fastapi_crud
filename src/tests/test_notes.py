import json
import pytest
from app.api import crud


def test_create_note(test_app, monkeypatch):
    test_request_payload = {"title": "something", "description": "something else"}
    test_response_payload = {"id": 1, "title": "something", "description": "something else"}

    async def mock_post(payload):
        return 1

    monkeypatch.setattr(crud, "post", mock_post)

    response = test_app.post("/notes/", data=json.dumps(test_request_payload))

    assert response.status_code == 201
    assert response.json() == test_response_payload


def test_create_note_invalid_json(test_app):
    response = test_app.post("/notes/", data=json.dumps({"title": "something"}))
    assert response.status_code == 422


def test_read_one_note_invalid(test_app, monkeypatch):
    async def mock_get_one(id):
        return None

    monkeypatch.setattr(crud, "get_one", mock_get_one)
    
    response = test_app.get("/notes/9/")
    assert response.status_code == 404
    assert response.json()["detail"] == "Note with id 9 not found!"
    
    response = test_app.get("/notes/0/")
    assert response.status_code == 422
    

def test_read_one_note(test_app, monkeypatch):
    test_data = {"id": 1, "title": "something", "description": "something else"}

    async def mock_get_one(id):
        return test_data

    monkeypatch.setattr(crud, "get_one", mock_get_one)

    response = test_app.get("/notes/1/")
    assert response.status_code == 200
    assert response.json() == test_data


def test_read_all_notes(test_app, monkeypatch):
    test_data = [
        {"title": "something", "description": "something else", "id": 1},
        {"title": "someone", "description": "someone else", "id": 2}
    ]

    async def mock_get_all():
        return test_data

    monkeypatch.setattr(crud, "get_all", mock_get_all)

    response = test_app.get("/notes/")
    assert response.status_code == 200
    assert response.json() == test_data


def test_update_note(test_app, monkeypatch):
    test_data = {"title": "updated sth", "description": "updated sth else", "id": 1}
    
    async def mock_get_one(id):
        return test_data

    monkeypatch.setattr(crud, "get_one", mock_get_one)
    
    async def mock_put(id, payload):
        return 1

    monkeypatch.setattr(crud, "put", mock_put)
    
    response = test_app.put("/notes/1/", data=json.dumps(test_data))
    assert response.status_code == 200
    assert response.json() == test_data
    
    response = test_app.get("/notes/0/")
    assert response.status_code == 422
    

def test_delete_note(test_app, monkeypatch):
    test_data = {"title": "something", "description": "something else", "id": 1}

    async def mock_get_one(id):
        return test_data

    monkeypatch.setattr(crud, "get_one", mock_get_one)

    async def mock_delete(id):
        return None

    monkeypatch.setattr(crud, "delete", mock_delete)

    response = test_app.delete("/notes/1/")
    assert response.status_code == 200
    assert response.json() == None
    
    response = test_app.get("/notes/0/")
    assert response.status_code == 422
