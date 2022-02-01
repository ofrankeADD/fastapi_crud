def test_items(test_app):#(item_id: int, q: Optional[str] = None):
    response = test_app.get("/items/42")
    assert response.status_code == 200
    assert response.json() == {"item_id": 42, "q": None}
    
    response = test_app.get("/items/foo")
    assert response.status_code == 422

def test_query(test_app):
    response = test_app.get("/items/423?q=bar123")
    assert response.status_code == 200
    assert response.json() == {"item_id": 423, "q": "bar123"}
    
def test_postItem(test_app):
    json_item = {"name": "Mais", "price": 2.45}
    response = test_app.post("/items/", json=json_item)
    assert response.status_code == 200
    assert response.json() == {"item_name": "Mais", "item_price": 2.45}
    
def test_putItem(test_app):
    json_item = {"name": "Gurke", "price": 1.33, "is_offer": True}
    response = test_app.put("/items/112", json=json_item)
    assert response.status_code == 200
    assert response.json() == {"item_name": "Gurke", "item_id": 112}
    
       
    
    
