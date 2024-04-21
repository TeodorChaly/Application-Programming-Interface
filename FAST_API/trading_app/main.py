from fastapi import FastAPI

app = FastAPI(title="Trading App", description="A simple trading app", version="0.1")

test_users = [
    {"id": "1", "name": "John", "email": "john@gmail.com", "role": "admin"},
    {"id": "2", "name": "Jane", "email": "jone@gmail.com", "role": "user"},
    {"id": "3", "name": "Alice", "email": "alice@gmail.com", "role": "user"},
]


@app.get("/users/{user_id}")
def get_user(user_id: int):
    return [user for user in test_users if user.get("id") == user_id]


test_trades = [
    {"id": "1", "symbol": "AAPL", "quantity": 10, "price": 100.0},
    {"id": "2", "symbol": "GOOGL", "quantity": 5, "price": 2000.0},
    {"id": "3", "symbol": "AMZN", "quantity": 2, "price": 3000.0},
]


@app.get("/trades")
def get_trades(limit: int = 1, offset: int = 0):
    return test_trades[offset:][:limit]


test_users2 = [
    {"id": "1", "name": "John", "email": "john@gmail.com", "role": "admin"},
    {"id": "2", "name": "Jane", "email": "jone@gmail.com", "role": "user"},
    {"id": "3", "name": "Alice", "email": "alice@gmail.com", "role": "user"},
]

@app.post("/users/{user_id}")
def change_user_name(user_id: int, new_name: str):
    current_user = list(filter(lambda user: int(user.get("id")) == user_id, test_users2))[0]
    current_user["name"] = new_name
    return {"status": "200", "message": f"User name updated successfully to {current_user['name']}"}
