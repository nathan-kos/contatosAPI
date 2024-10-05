
class CreateContact:
    def __init__(self, contact_repository):
        self.contact_repository = contact_repository;

    async def execute(self, name, email, phone):
        # validate inputs
        if not name or not email or not phone:
            raise ValueError('Invalid input');

        # Validate email
        if("@" not in email):
            raise ValueError("Invalid email");

        # Validate phone
        if(len(phone) < 10):
            raise ValueError("Invalid phone number");

        contact = await self.contact_repository.create_contact(name, email, phone);

        return contact;
