from starlette.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_ping():
    response = client.get("/ping")
    assert response.status_code == 200
    assert response.json() == {"ping": "pong!"}

def test_items():#(item_id: int, q: Optional[str] = None):
    response = client.get("/items/42")
    assert response.status_code == 200
    assert response.json() == {"item_id": 42, "q": None}
    
    response = client.get("/items/foo")
    assert response.status_code == 422

def test_query():
    response = client.get("/items/423?q=bar123")
    assert response.status_code == 200
    assert response.json() == {"item_id": 423, "q": "bar123"}
    
def test_postItem():
    json_item = {"name": "Mais", "price": 2.45}
    response = client.post("/items/", json=json_item)
    assert response.status_code == 200
    assert response.json() == {"item_name": "Mais", "item_price": 2.45}
    
def test_putItem():
    json_item = {"name": "Gurke", "price": 1.33, "is_offer": True}
    response = client.put("/items/112", json=json_item)
    assert response.status_code == 200
    assert response.json() == {"item_name": "Gurke", "item_id": 112}
    
       
    
    
