from fastapi.testclient import TestClient
from app.main import app   # ✅ because main.py is inside app/



# Create a single client instance for all tests
client = TestClient(app)


def test_health():
    rv = client.get("/health")
    assert rv.status_code == 200
    assert rv.json()["status"] == "ok"


def test_create_user_and_wallet_flow():
    # Step 1: create user
    payload = {"name": "TestUser", "email": "tuser@example.com", "phone": "+911111111111"}
    r = client.post("/api/users", json=payload)
    assert r.status_code == 200
    user = r.json()
    assert "id" in user
    uid = user["id"]

    # Step 2: topup wallet
    r2 = client.post(f"/api/users/{uid}/wallet", json={"amount": 200.0, "description": "topup"})
    assert r2.status_code == 200
    tx = r2.json()
    assert tx["amount"] == 200.0
    assert tx["description"] == "topup"

    # Step 3: fetch transactions
    r3 = client.get(f"/api/users/{uid}/transactions")
    assert r3.status_code == 200
    arr = r3.json()
    assert isinstance(arr, list)
    assert len(arr) > 0
    assert arr[0]["amount"] == 200.0
    assert arr[0]["description"] == "topup"

    # Step 4: fetch users list and check wallet balance updated
    r4 = client.get("/api/users")
    assert r4.status_code == 200
    users = r4.json()
    match = next((u for u in users if u["id"] == uid), None)
    assert match is not None
    assert match["wallet_balance"] == 200.0
