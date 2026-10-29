
from ModelsDTO import ShipItem, UserItem, OrderItem, OrderHasShipItem
import dao
from datetime import datetime





####################### SHIP #######################


def GetShip(
        strictIDFilter: int = 0, 
        softSearchFilter: str = "", 
        softShipTypeFilter = None, 
        softWeightClassFilter = None, 
        order = None
):
    result = dao.GetShip(
        strictIDFilter, 
        softSearchFilter, 
        softShipTypeFilter, 
        softWeightClassFilter, 
        order
        )
    return result


def UpdateShip(updatedShip: ShipItem):
    result = dao.UpdateShip(updatedShip)
    return result


# def CreateShip(newShip: ShipItem):
#     result = dao.CreateShip(newShip)
#     return result


def CreateShip(newShip: ShipItem):
    if newShip.name:
        newShip.name = newShip.name.strip()

    result = dao.CreateShip(newShip)
    return result


def DeleteShip(ship_id: int):
    result = dao.DeleteShip(ship_id)
    return result


def GetShipsByOrder(order_id: int):
    # result = dao.GetShipsByOrder(order_id)
    result = [ShipItem(*(x[2:])) for x in dao.GetShipsByOrder(order_id)]
    return result






####################### USER #######################

def GetUser(strictIDFilter: int = 0, softLoginFilter: str = ""):
    result = dao.GetUser(strictIDFilter, softLoginFilter)
    return result


def CreateUser(newUser: UserItem):
    if newUser.gmail:
        newUser.gmail = newUser.gmail.strip()
    
    result = dao.CreateUser(newUser)
    return result


def UpdateUser(updatedUser: UserItem):
    result = dao.UpdateUser(updatedUser)
    return result


def DeleteUser(user_id: int):
    result = dao.DeleteUser(user_id)
    return result



####################### ORDER #######################

def GetOrder(strictIDFilter: int = 0, user_id_filter: int = 0):
    result = dao.GetOrder(strictIDFilter, user_id_filter)
    return result


def CreateOrder(newOrder: OrderItem):
    if not hasattr(newOrder, 'date') or not newOrder.date or newOrder.date == "now":
        newOrder.date = datetime.now()

    result = dao.CreateOrder(newOrder)
    return result


def UpdateOrder(updatedOrder: OrderItem):
    result = dao.UpdateOrder(updatedOrder)
    return result


def DeleteOrder(order_id: int):
    result = dao.DeleteOrder(order_id)
    return result


def GetOrdersByUser(user_id: int):
    result = dao.GetOrdersByUser(user_id)
    return result



####################### ORDER_HAS_SHIP #######################

def GetOrderHasShip(order_id: int = 0, ship_id: int = 0):
    result = dao.GetOrderHasShip(order_id, ship_id)
    return result


def CreateOrderHasShip(newRelation: OrderHasShipItem):
    if not hasattr(newRelation, 'order_start') or not newRelation.order_start or newRelation.order_start == "now":
        newRelation.order_start = datetime.now()
    if not hasattr(newRelation, 'order_end') or not newRelation.order_end or newRelation.order_end == "now":
        newRelation.order_end = datetime.now()

    result = dao.CreateOrderHasShip(newRelation)
    return result


def UpdateOrderHasShip(updatedRelation: OrderHasShipItem):
    result = dao.UpdateOrderHasShip(updatedRelation)
    return result


def DeleteOrderHasShip(order_id: int, ship_id: int):
    result = dao.DeleteOrderHasShip(order_id, ship_id)
    return result
    