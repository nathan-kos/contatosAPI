from uuid import UUID
from fastapi import APIRouter

from ..repository.ContactRepository import ContactRepository
from ..service import CreateContact, DeleteContact, FindContactById, ListContact, UpdateContact

from .Validator.Models import ContactCreateModel, ContactUpdateModel

router = APIRouter()

@router.get("/")
async def list_contacts():
    try:
        repository = ContactRepository();
        service = ListContact.ListContact(repository);
        contacts = await service.execute();
        return contacts;
    except Exception as e:
        return {"error": str(e)};

@router.get("/{con_id}")
async def get_contact(con_id: UUID):
    try:
        repository = ContactRepository();
        service = FindContactById.FindContactById(repository);
        contact = await service.execute(con_id);
        return contact;
    except Exception as e:
        return {"error": str(e)};

@router.delete("/{con_id}")
async def delete_contact(con_id: UUID):
    try:
        repository = ContactRepository();
        service = DeleteContact.DeleteContact(repository);
        await service.execute(con_id);
        return {"message": "Contact deleted"};
    except Exception as e:
        return {"error": str(e)};

@router.post("/")
async def create_contact(contact: ContactCreateModel):
    try:
        repository = ContactRepository();
        service = CreateContact.CreateContact(repository);
        newContact = await service.execute(contact.con_name, contact.con_email, contact.con_phone);
        return newContact;
    except Exception as e:
        return {"error": str(e)};

@router.put("/{con_id}")
async def update_contact(con_id: UUID, contact: ContactUpdateModel):
    try:
        repository = ContactRepository();
        service = UpdateContact.UpdateContact(repository);
        contact = await service.execute(con_id, contact.con_name, contact.con_email, contact.con_phone);
        return contact;
    except Exception as e:
        return {"error": str(e)};
