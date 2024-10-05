
class UpdateContact:
    def __init__(self, contact_repository):
        self.contact_repository = contact_repository;

    async def execute(self, contact_id, name, email, phone):
        
        contact = await self.contact_repository.get_contact(contact_id);

        if not contact:
            raise ValueError("Contact not found");
    
        if email and "@" not in email:
            raise ValueError("Invalid email address");
    
        if phone and len(phone) < 9:
            raise ValueError("Invalid phone number");

        return await self.contact_repository.update_contact(contact_id, name, email, phone);
