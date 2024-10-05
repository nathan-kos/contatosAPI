from src.shared.database.models import Contact 
from tortoise.exceptions import DoesNotExist

class ContactRepository:
    async def create_contact(self, name, email, phone) -> Contact:
        contact = await Contact.create(con_name=name, con_email=email, con_phone=phone);
        return contact;

    async def get_contact(self, con_id) -> Contact:
        try:
            contact = await Contact.get(con_id=con_id);
            return contact;
        except DoesNotExist:
            return None;

    async def list_contacts(self) -> list:
        contacts = await Contact.all();
        return contacts;

    async def update_contact(self, con_id, name, email, phone) -> Contact:
        try:
            contact = await Contact.get(con_id=con_id);
            contact.con_name = name;
            contact.con_email = email;
            contact.con_phone = phone;
            await contact.save();
            return contact;
        except DoesNotExist:
            return None;

    async def delete_contact(self, con_id) -> bool:
        try:
            contact = await Contact.get(con_id=con_id);
            await contact.delete();
            return True;
        except DoesNotExist:
            return False;
