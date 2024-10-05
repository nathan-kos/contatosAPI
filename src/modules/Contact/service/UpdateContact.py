from  ....shared.exceptions.BadRequest import BadRequest
from  ....shared.exceptions.EntityNotFound import EntityNotFound

class UpdateContact:
    def __init__(self, contact_repository):
        self.contact_repository = contact_repository;

    async def execute(self, contact_id, name, email, phone):
        
        contact = await self.contact_repository.get_contact(contact_id);

        if not contact:
            raise EntityNotFound("Contact not found");
    
        #Validate inputs
        if email and "@" not in email:
            raise BadRequest("Invalid email");
    
        if phone and len(phone) < 9:
            raise BadRequest("Invalid phone number");

        return await self.contact_repository.update_contact(contact_id, name, email, phone);
