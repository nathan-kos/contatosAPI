from tortoise import fields
from tortoise.models import Model
import uuid

class Contact(Model):
    con_id = fields.UUIDField(pk=True, default=uuid.uuid4)
    con_name = fields.CharField(max_length=255)
    con_email = fields.CharField(max_length=255)
    con_phone = fields.CharField(max_length=16)
    con_created = fields.DatetimeField(auto_now_add=True)
    con_updated = fields.DatetimeField(auto_now=True)

    def __str__(self):
        return self.name