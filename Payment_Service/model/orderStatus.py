
from enum import Enum


class OrderStatus(Enum):
    PENDING = "Pending"
    COMPLETED = "Completed"
    REFRESH = "Refresh"
    ERROR = "Error"