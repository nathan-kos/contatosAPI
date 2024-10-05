
from pydantic import BaseModel, Field
from typing import Optional

class ContactModel(BaseModel):
    con_name: str =  Field(...);
    con_email: str = Field(..., pattern="[^@ \t\r\n]+@[^@ \t\r\n]+\.[^@ \t\r\n]+");
    con_phone: str = Field(min_length=10, max_length=16);


class ContactCreateModel(ContactModel):
    pass;

class ContactUpdateModel(ContactModel):
    pass;