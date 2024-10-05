class ListContact:
    def __init__(self, contact_repository):
        self.contact_repository = contact_repository;

    async def execute(self):
        return await self.contact_repository.list_contacts();
