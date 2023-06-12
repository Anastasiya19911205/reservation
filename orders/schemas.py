from datetime import datetime
from enum import Enum
from typing import List, Optional
from pydantic import BaseModel, Field, ValidationError, validator

# json_schema


class WaiterSchema(BaseModel):
    waiter_id: int
    name: str
    last_name: str
    age: int


class BookingTimeTable(BaseModel):
    start_armor: datetime
    end_armor: datetime

class Category(Enum):
    restaurant = "restaurant"
    cafe = "cafe"
    bar = "bar"

class Table(BaseModel):
    table_id: int
    waiter: WaiterSchema
    booking_time_table: List[BookingTimeTable]

class Place(BaseModel):
    place_id: int = Field(ge=0)
    name: str = Field(min_length=2)
    address: str
    phone: str
    category: Category
    tables: Optional[List[Table]] = []