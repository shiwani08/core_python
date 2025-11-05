from enum import Enum

class BookStatus(Enum):
    IN_LIBRARY = "in_library"
    BORROWED = "borrowed"
    NOT_OWNED = "not_owned"

    
    