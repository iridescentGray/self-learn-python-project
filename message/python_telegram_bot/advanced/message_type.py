from enum import Enum


class RPCMessageType(str, Enum):
    COMMON = "common" 
    STATUS = "status"
    WARNING = "warning"
    GETCODE = "get_code"

    def __repr__(self):
        return self.value

    def __str__(self):
        return self.value
