from marshmallow import Schema, fields


class UserSerializer(Schema):
    username = fields.String(required=True)
    firs_name = fields.String(required=False)
    last_name = fields.String(required=False)
    email = fields.String(required=True)
    is_staff = fields.Boolean(default=False)
    is_active = fields.Boolean(default=True)
    date_joined = fields.DateTime()
    last_login = fields.DateTime()
