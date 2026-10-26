from fastapi import FastAPI, HTTPException
import uvicorn
import dao
import atexit
import ModelsDTO

# http://127.0.0.1:8000/docs

app = FastAPI()




####################### SHIP #######################
@app.get(
    "/ships",
    tags=['Ships'],
    summary = "Get all ships"
)
def read_ships(id: int = None, search: str = None, type: str = None, weight_class: str = None):
    result = dao.GetShip(id, search, type, weight_class)
    if not result:
        raise HTTPException(status_code=404, detail="Ship not found")
    return result


@app.post(
    "/ships",
    tags = ['Ships'],
    summary = "Create new ship"
)
def create_ship(new_ship: ModelsDTO.NewShipItem):
    dao.CreateShip(new_ship)
    return {"success": True, "message": "Ship added successfully"}


@app.put(
    "/ships",
    tags = ['Ships'],
    summary = "Update ship"
)
def update_ship(new_ship: ModelsDTO.NewShipItem):
    result = dao.UpdateShip(new_ship)
    if not result:
        raise HTTPException(status_code=404, detail="Ship not found")
    
    return {"success": True, "message": "Ship updated successfully"}


@app.delete(
    "/ships/{ship_id}",
    tags = ['Ships'],
    summary = "Delete ship"
)
def delete_ship(ship_id: int):
    result = dao.DeleteShip(ship_id)
    if not result:
        raise HTTPException(status_code=404, detail="Ship not found")
    
    return {"success": True, "message": "Ship removed successfully"}






####################### USER #######################

@app.get("/users", tags=['Users'], summary="Get all users")
def read_users(id: int = None, search_login: str = None):
    result = dao.GetUser(id or 0, search_login or "")
    if not result:
        raise HTTPException(status_code=404, detail="User not found")
    return result


@app.post("/users", tags=['Users'], summary="Create new user")
def create_user(new_user: ModelsDTO.NewUserItem):
    dao.CreateUser(new_user)
    return {"success": True, "message": "User added successfully"}


@app.put("/users", tags=['Users'], summary="Update user")
def update_user(user: ModelsDTO.NewUserItem):
    result = dao.UpdateUser(user)
    if not result:
        raise HTTPException(status_code=404, detail="User not found")
    return {"success": True, "message": "User updated successfully"}


@app.delete("/users/{user_id}", tags=['Users'], summary="Delete user")
def delete_user(user_id: int):
    result = dao.DeleteUser(user_id)
    if not result:
        raise HTTPException(status_code=404, detail="User not found")
    return {"success": True, "message": "User removed successfully"}


@app.get(
    "/users/{user_id}/orders",
    tags=['Users'],
    summary="Get all orders for a specific client/user"
)
def get_user_orders(user_id: int):
    result = dao.GetOrdersByUser(user_id)
    if not result:
        raise HTTPException(status_code=404, detail="No orders found for this user")
    return result




####################### ORDER #######################

@app.get("/orders", tags=['Orders'], summary="Get all orders")
def read_orders(id: int = None, user_id: int = None):
    result = dao.GetOrder(id or 0, user_id or 0)
    if not result:
        raise HTTPException(status_code=404, detail="Order not found")
    return result


@app.post("/orders", tags=['Orders'], summary="Create new order")
def create_order(new_order: ModelsDTO.NewOrderItem):
    dao.CreateOrder(new_order)
    return {"success": True, "message": "Order added successfully"}


@app.put("/orders", tags=['Orders'], summary="Update order")
def update_order(order: ModelsDTO.NewOrderItem):
    result = dao.UpdateOrder(order)
    if not result:
        raise HTTPException(status_code=404, detail="Order not found")
    return {"success": True, "message": "Order updated successfully"}


@app.delete("/orders/{order_id}", tags=['Orders'], summary="Delete order")
def delete_order(order_id: int):
    result = dao.DeleteOrder(order_id)
    if not result:
        raise HTTPException(status_code=404, detail="Order not found")
    return {"success": True, "message": "Order removed successfully"}


@app.get(
    "/orders/{order_id}/ships",
    tags=['Orders'],
    summary="Get all ships in a specific order"
)
def get_order_ships(order_id: int):
    result = dao.GetShipsByOrder(order_id)
    if not result:
        raise HTTPException(status_code=404, detail="No ships found for this order")
    return result



####################### ORDER_HAS_SHIP #######################

@app.get("/order-ships", tags=['Order Ships'], summary="Get order-ship relations")
def read_order_ships(order_id: int = None, ship_id: int = None):
    result = dao.GetOrderHasShip(order_id or 0, ship_id or 0)
    if not result:
        raise HTTPException(status_code=404, detail="Relation not found")
    return result


@app.post("/order-ships", tags=['Order Ships'], summary="Create order-ship relation")
def create_order_ship(new_relation: ModelsDTO.NewOrderHasShipItem):
    dao.CreateOrderHasShip(new_relation)
    return {"success": True, "message": "Relation added successfully"}


@app.put("/order-ships", tags=['Order Ships'], summary="Update order-ship relation")
def update_order_ship(relation: ModelsDTO.NewOrderHasShipItem):
    result = dao.UpdateOrderHasShip(relation)
    if not result:
        raise HTTPException(status_code=404, detail="Relation not found")
    return {"success": True, "message": "Relation updated successfully"}


@app.delete("/order-ships/{order_id}/{ship_id}", tags=['Order Ships'], summary="Delete order-ship relation")
def delete_order_ship(order_id: int, ship_id: int):
    result = dao.DeleteOrderHasShip(order_id, ship_id)
    if not result:
        raise HTTPException(status_code=404, detail="Relation not found")
    return {"success": True, "message": "Relation removed successfully"}





def OnAppClose():
    dao.Destruct()

if __name__ == "__main__":
    atexit.register(OnAppClose)
    uvicorn.run("main:app", reload=True)

    