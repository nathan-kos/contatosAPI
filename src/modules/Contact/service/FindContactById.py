from  ....shared.exceptions.EntityNotFound import EntityNotFound

class FindContactById:
    def __init__(self, contact_repository):
        self.contact_repository = contact_repository;

    async def execute(self, con_id):

        contact = await self.contact_repository.get_contact(con_id);

        if not contact:
            raise EntityNotFound("Contact not found");
    
        return contact;
