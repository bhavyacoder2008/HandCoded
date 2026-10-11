balance = 100
inventory = [{"name": "apple",  "price":5, "stock": 50 }, {"name":"bread", "price": 10, "stock": 100}]
item_names = [i["name"] for i in inventory]
spending_limit = 50
amount_spent = 0

def get_balance() -> dict:
    return {
        "success": True,
        "data": {"balance": balance},
        "error": None
    }

def get_item_price(item: str) -> dict:
    for i in inventory:
        if i["name"] == item:
            return {"success": True, "data": i, "error": None}
        
    return {"success": False, "data": None, "error": "Item not found"}

def buy_item(item, quantity) -> dict:
    global balance, amount_spent
    if item not in item_names:
        return {"success": False, "data": None, "error": "Item not found"}
    if quantity <= 0:
        return {"success": False, "data": None, "error": "quantity less than zero"}
    item_details: dict = {}
    for i in inventory:
        if i["name"] == item:
            item_details = i
            break
    if quantity > item_details["stock"]:
        return {"success": False, "data": None, "error": "Insufficient items"}
    total_amount = item_details["price"] * quantity
    if total_amount > balance:
        return {"success": False, "data": None, "error": "Insufficient balance"}
    if amount_spent + total_amount > spending_limit:
        return {"success": False, "data": None, "error": "Spending limit exceeded"}
    balance -= total_amount
    amount_spent += total_amount
    item_details["stock"] -= quantity
    return {"success": True, "data": {"item": item, "quantity": quantity, "total": total_amount, "remaining_balance": balance, "remaining_stock": item_details["stock"]}, "error": None}
