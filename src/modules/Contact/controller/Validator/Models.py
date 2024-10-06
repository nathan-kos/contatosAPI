
from pydantic import BaseModel, Field
from typing import Optional

class ContactModel(BaseModel):
    con_name: str =  Field(..., example="Nathan Santos");
    con_email: str = Field(..., pattern="[^@ \t\r\n]+@[^@ \t\r\n]+\.[^@ \t\r\n]+", example="nathan@gmail.com");
    con_phone: str = Field(min_length=10, max_length=16, example="99999999999");


class ContactCreateModel(ContactModel):
    pass;

class ContactUpdateModel(ContactModel):
    pass;