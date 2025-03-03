
from enum import Enum


class OrderStatus(Enum):
    PENDING = "Pending"
    COMPLETED = "Completed"
    REFUND = "REFUND"
    ERROR = "Error"
    PAID = "Payment Done"