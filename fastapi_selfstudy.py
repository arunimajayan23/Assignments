from fastapi import FastAPI, HTTPException
from pymongo import MongoClient
from pydantic import BaseModel

client = MongoClient("mongodb://intern_23:intern%40123@192.168.0.220:2717/interns_b2_23")
db = client["interns_b2_23"]
collection = db["arunima_jayan"]
app = FastAPI()


# User model
class User(BaseModel):
    name : str
    email: str
    password: str


# Menu item model
class MenuItem:
    def __init__(self, name, description, price):
        self.name = name
        self.description = description
        self.price = price


class Cart(BaseModel):
    items: list
# Cart model
class Cart:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item):
        self.items.remove(item)


# Order model
class Order:
    def __init__(self, items, total):
        self.items = items
        self.total = total


# Dummy data
users = []
menus = [
    MenuItem("Burger", "Juicy burger with lettuce, tomato, and cheese.", 200),
    MenuItem("Pizza", "Large pizza with pepperoni and mushrooms.", 199),
    MenuItem("Salad", "Fresh salad with mixed greens and vegetables.", 350)
]
cart = Cart()
orders = []



# User endpoints
@app.post("/users")
def create_user(user: User):
    collection.insert_one(user.dict())
    return {"message": "User created successfully"}

@app.get("/get-all-users")
def get_user():
    users = list(collection.find())
    for user in users:
        del user["_id"]
    return users
# Menu endpoints

@app.get("/menus")
def get_menus():
    return menus


# Cart endpoints
@app.post("/cart")
def add_to_cart(item_name: str):
    item = next((menu_item for menu_item in menus if menu_item.name == item_name), None)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    cart.add_item(item)
    return {"message": "Item added to cart"}


@app.get("/cart")
def view_cart():
    return {"items": cart.items}


# Order endpoints
@app.post("/order")
def place_order():
    if not cart.items:
        raise HTTPException(status_code=400, detail="Cart is empty")
    total = sum([item.price for item in cart.items])
    order = Order(cart.items, total)
    orders.append(order)
    cart.items = []
    return {"message": "Order placed successfully"}


@app.get("/orders")
def view_orders():
    return orders


@app.put("/orders/{id}")
def update_order(id: int):
    order = next((o for o in orders if o.id == id), None)
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")
    order.status = "updated"
    return {"message": "Order updated successfully"}


@app.delete("/orders/{id}")
def delete_order(id: int):
    order = next((o for o in orders if o.id == id), None)
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")
    orders.remove(order)
    return {"message": "Order deleted successfully"}
