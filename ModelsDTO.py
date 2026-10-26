from pydantic import BaseModel
from datetime import datetime

class ShipItem:
    id: int
    header_title: str
    passengers: int
    weight: float
    description: str
    price_hour: int
    price_day: int
    image_src: str
    ship_type_id: int
    weight_class_id: int

    def __init__(self, 
            id: int,
            header_title: str,
            passengers: int,
            weight: float,
            description: str,
            price_hour: int,
            price_day: int,
            image_src: str,
            ship_type_id: int,
            weight_class_id: int
            ):
        self.id = id
        self.header_title = header_title
        self.passengers = passengers
        self.weight = weight
        self.description = description
        self.price_hour = price_hour
        self.price_day = price_day
        self.image_src = image_src
        self.ship_type_id = ship_type_id
        self.weight_class_id = weight_class_id


class NewShipItem(BaseModel):
    id: int
    header_title: str
    passengers: int
    weight: float
    description: str
    price_hour: int
    price_day: int
    image_src: str
    ship_type_id: int
    weight_class_id: int




class UserItem:
    id: int
    login: str
    password: str
    gmail: str

    def __init__(self, id: int, login: str, password: str, gmail: str):
        self.id = id
        self.login = login
        self.password = password
        self.gmail = gmail

class NewUserItem(BaseModel):
    id: int
    login: str
    password: str
    gmail: str




class OrderItem:
    id: int
    date: datetime
    user_id: int
    payed: bool
    completed: bool

    def __init__(self, id: int, date: datetime, user_id: int, payed: bool, completed: bool):
        self.id = id
        self.date = date
        self.user_id = user_id
        self.payed = payed
        self.completed = completed

class NewOrderItem(BaseModel):
    id: int
    date: datetime
    user_id: int
    payed: bool
    completed: bool




class OrderHasShipItem:
    order_id: int
    ship_id: int
    order_start: datetime
    order_end: datetime

    def __init__(self, order_id: int, ship_id: int, order_start: datetime, order_end: datetime):
        self.order_id = order_id
        self.ship_id = ship_id
        self.order_start = order_start
        self.order_end = order_end

class NewOrderHasShipItem(BaseModel):
    order_id: int
    ship_id: int
    order_start: datetime
    order_end: datetime
