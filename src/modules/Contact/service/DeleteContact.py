
class DeleteContact:
    def __init__(self, contact_repository):
        self.contact_repository = contact_repository;

    async def execute(self, con_id):
        contact = await self.contact_repository.get_contact(con_id);

        if not contact:
            raise ValueError("Contact not found");
        
        return await self.contact_repository.delete_contact(con_id);
