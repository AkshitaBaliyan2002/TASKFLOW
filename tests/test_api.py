import pytest

from app import create_app


@pytest.fixture
def client():
    return create_app().test_client()


# TC01
def test_health(client):
    r = client.get("/health")
    assert r.status_code == 200
    assert r.get_json() == {"status": "ok"}


# TC02
def test_create_task(client):
    r = client.post("/tasks", json={"title": "Write report"})
    assert r.status_code == 201
    assert r.get_json() == {"id": 1, "title": "Write report", "done": False}


# TC03
def test_create_task_missing_title(client):
    r = client.post("/tasks", json={})
    assert r.status_code == 400


# TC04
def test_create_task_blank_title(client):
    r = client.post("/tasks", json={"title": "   "})
    assert r.status_code == 400


# TC05
def test_list_tasks(client):
    client.post("/tasks", json={"title": "A"})
    client.post("/tasks", json={"title": "B"})
    r = client.get("/tasks")
    assert r.status_code == 200
    assert len(r.get_json()) == 2


# TC06
def test_get_task(client):
    client.post("/tasks", json={"title": "A"})
    r = client.get("/tasks/1")
    assert r.status_code == 200
    assert r.get_json()["title"] == "A"


# TC07
def test_get_task_not_found(client):
    assert client.get("/tasks/99").status_code == 404


# TC08
def test_update_task_done(client):
    client.post("/tasks", json={"title": "A"})
    r = client.put("/tasks/1", json={"done": True})
    assert r.status_code == 200
    assert r.get_json()["done"] is True


# TC09
def test_update_task_empty_title(client):
    client.post("/tasks", json={"title": "A"})
    assert client.put("/tasks/1", json={"title": ""}).status_code == 400


# TC10
def test_delete_task(client):
    client.post("/tasks", json={"title": "A"})
    assert client.delete("/tasks/1").status_code == 204
    assert client.get("/tasks/1").status_code == 404


# TC11
def test_delete_task_not_found(client):
    assert client.delete("/tasks/42").status_code == 404


# TC12
def test_filter_by_done(client):
    client.post("/tasks", json={"title": "A"})
    client.post("/tasks", json={"title": "B"})
    client.put("/tasks/1", json={"done": True})
    done = client.get("/tasks?done=true").get_json()
    pending = client.get("/tasks?done=false").get_json()
    assert [t["id"] for t in done] == [1]
    assert [t["id"] for t in pending] == [2]
