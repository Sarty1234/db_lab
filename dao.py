
import os
from dotenv import load_dotenv
import mysql.connector
from mysql.connector.abstracts import MySQLCursorAbstract
from ModelsDTO import ShipItem, UserItem, OrderItem, OrderHasShipItem

load_dotenv()

DB_HOST = os.getenv("DB_HOST")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_NAME = os.getenv("DB_NAME")


mydb = mysql.connector.connect(
    host = DB_HOST,
    user = DB_USER,
    password = DB_PASSWORD,
    database = DB_NAME,
)
my_cursor: MySQLCursorAbstract = mydb.cursor()


def Destruct():
    if mydb.is_connected():
        my_cursor.close()
        mydb.close()




####################### SHIP #######################


def GetShip(
        strictIDFilter: int = 0, 
        softSearchFilter: str = "", 
        softShipTypeFilter = None, 
        softWeightClassFilter = None
):
    query = "SELECT * FROM mydb.ship WHERE 1=1"
    params = []

    if strictIDFilter:
        query += " AND id = %s"
        params.append(strictIDFilter)
        
    if softSearchFilter:
        query += " AND (header_title LIKE %s OR description LIKE %s)"
        params.append(f"%{softSearchFilter}%")
        params.append(f"%{softSearchFilter}%")
        
    if softShipTypeFilter is not None and softShipTypeFilter != "":
        query += " AND ship_type_id = %s"
        params.append(softShipTypeFilter)
        
    if softWeightClassFilter is not None and softWeightClassFilter != "":
        query += " AND weight_class_id = %s"
        params.append(softWeightClassFilter)
        
    query += ";"
    
    my_cursor.execute(query, tuple(params))
    
    result = [ShipItem(*x) for x in my_cursor]
    return result


def UpdateShip(updatedShip: ShipItem):
    query = """
        UPDATE `mydb`.`ship` 
        SET 
            `header_title` = %s, 
            `passengers` = %s, 
            `weight` = %s, 
            `description` = %s, 
            `price_hour` = %s, 
            `price_day` = %s, 
            `image_src` = %s, 
            `ship_type_id` = %s, 
            `weight_class_id` = %s
        WHERE `id` = %s;
    """
    
    params = [
        updatedShip.header_title, 
        updatedShip.passengers,
        updatedShip.weight,
        updatedShip.description,
        updatedShip.price_hour,
        updatedShip.price_day,
        updatedShip.image_src,
        updatedShip.ship_type_id,
        updatedShip.weight_class_id,
        updatedShip.id
    ]

    my_cursor.execute(query, tuple(params))
    mydb.commit()
    
    return my_cursor.rowcount > 0


def CreateShip(
        newShip: ShipItem
):
    query = "INSERT INTO `mydb`.`ship` " \
    "(`header_title`, `passengers`, `weight`, `description`, `price_hour`, `price_day`, `image_src`, `ship_type_id`, `weight_class_id`) " \
    "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s);"
    params = [
        newShip.header_title, 
        newShip.passengers,
        newShip.weight,
        newShip.description,
        newShip.price_hour,
        newShip.price_day,
        newShip.image_src,
        newShip.ship_type_id,
        newShip.weight_class_id
    ]

    my_cursor.execute(query, tuple(params))
    mydb.commit()
    
    return my_cursor.rowcount > 0


def DeleteShip(ship_id: int):
    query = "DELETE FROM `mydb`.`ship` WHERE `id` = %s;"
    
    my_cursor.execute(query, (ship_id,))
    mydb.commit()
    
    return my_cursor.rowcount > 0


def GetShipsByOrder(order_id: int):
    query = """
        SELECT s.* 
        FROM mydb.ship s
        JOIN mydb.order_has_ship ohs ON s.id = ohs.ship_id
        WHERE ohs.order_id = %s;
    """
    my_cursor.execute(query, (order_id,))
    result = [ShipItem(*x) for x in my_cursor]
    return result






####################### USER #######################

def GetUser(strictIDFilter: int = 0, softLoginFilter: str = ""):
    query = "SELECT * FROM mydb.user WHERE 1=1"
    params = []

    if strictIDFilter:
        query += " AND id = %s"
        params.append(strictIDFilter)
        
    if softLoginFilter:
        query += " AND login LIKE %s"
        params.append(f"%{softLoginFilter}%")
        
    query += ";"
    
    my_cursor.execute(query, tuple(params))
    result = [UserItem(*x) for x in my_cursor]
    return result


def CreateUser(newUser: UserItem):
    query = "INSERT INTO `mydb`.`user` (`login`, `password`, `gmail`) VALUES (%s, %s, %s);"
    params = [newUser.login, newUser.password, newUser.gmail]

    my_cursor.execute(query, tuple(params))
    mydb.commit()
    
    return my_cursor.rowcount > 0


def UpdateUser(updatedUser: UserItem):
    query = """
        UPDATE `mydb`.`user` 
        SET `login` = %s, `password` = %s, `gmail` = %s 
        WHERE `id` = %s;
    """
    params = [updatedUser.login, updatedUser.password, updatedUser.gmail, updatedUser.id]

    my_cursor.execute(query, tuple(params))
    mydb.commit()
    
    return my_cursor.rowcount > 0


def DeleteUser(user_id: int):
    query = "DELETE FROM `mydb`.`user` WHERE `id` = %s;"
    my_cursor.execute(query, (user_id,))
    mydb.commit()
    
    return my_cursor.rowcount > 0



####################### ORDER #######################

def GetOrder(strictIDFilter: int = 0, user_id_filter: int = 0):
    query = "SELECT * FROM mydb.order WHERE 1=1"
    params = []

    if strictIDFilter:
        query += " AND id = %s"
        params.append(strictIDFilter)
        
    if user_id_filter:
        query += " AND user_id = %s"
        params.append(user_id_filter)
        
    query += ";"
    
    my_cursor.execute(query, tuple(params))
    result = [OrderItem(*x) for x in my_cursor]
    return result


def CreateOrder(newOrder: OrderItem):
    query = "INSERT INTO `mydb`.`order` (`date`, `user_id`, `payed`, `completed`) VALUES (%s, %s, %s, %s);"
    params = [newOrder.date, newOrder.user_id, newOrder.payed, newOrder.completed]
    my_cursor.execute(query, tuple(params))
    mydb.commit()
    return my_cursor.rowcount > 0


def UpdateOrder(updatedOrder: OrderItem):
    query = """
        UPDATE `mydb`.`order` 
        SET `date` = %s, `user_id` = %s, `payed` = %s, `completed` = %s 
        WHERE `id` = %s;
    """
    params = [updatedOrder.date, updatedOrder.user_id, updatedOrder.payed, updatedOrder.completed, updatedOrder.id]
    my_cursor.execute(query, tuple(params))
    mydb.commit()
    return my_cursor.rowcount > 0


def DeleteOrder(order_id: int):
    query = "DELETE FROM `mydb`.`order` WHERE `id` = %s;"
    my_cursor.execute(query, (order_id,))
    mydb.commit()
    return my_cursor.rowcount > 0


def GetOrdersByUser(user_id: int):
    query = "SELECT * FROM mydb.order WHERE user_id = %s;"
    my_cursor.execute(query, (user_id,))
    result = [OrderItem(*x) for x in my_cursor]
    return result



####################### ORDER_HAS_SHIP #######################

def GetOrderHasShip(order_id: int = 0, ship_id: int = 0):
    query = "SELECT * FROM mydb.order_has_ship WHERE 1=1"
    params = []

    if order_id:
        query += " AND order_id = %s"
        params.append(order_id)
        
    if ship_id:
        query += " AND ship_id = %s"
        params.append(ship_id)
        
    query += ";"
    
    my_cursor.execute(query, tuple(params))
    result = [OrderHasShipItem(*x) for x in my_cursor]
    return result


def CreateOrderHasShip(newRelation: OrderHasShipItem):
    query = "INSERT INTO `mydb`.`order_has_ship` (`order_id`, `ship_id`, `order_start`, `order_end`) VALUES (%s, %s, %s, %s);"
    params = [newRelation.order_id, newRelation.ship_id, newRelation.order_start, newRelation.order_end]
    my_cursor.execute(query, tuple(params))
    mydb.commit()
    return my_cursor.rowcount > 0


def UpdateOrderHasShip(updatedRelation: OrderHasShipItem):
    query = """
        UPDATE `mydb`.`order_has_ship` 
        SET `order_start` = %s, `order_end` = %s 
        WHERE `order_id` = %s AND `ship_id` = %s;
    """
    params = [updatedRelation.order_start, updatedRelation.order_end, updatedRelation.order_id, updatedRelation.ship_id]
    my_cursor.execute(query, tuple(params))
    mydb.commit()
    return my_cursor.rowcount > 0


def DeleteOrderHasShip(order_id: int, ship_id: int):
    query = "DELETE FROM `mydb`.`order_has_ship` WHERE `order_id` = %s AND `ship_id` = %s;"
    my_cursor.execute(query, (order_id, ship_id))
    mydb.commit()
    return my_cursor.rowcount > 0
    