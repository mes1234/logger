from marshmallow import Schema, fields


class ProjectSchema(Schema):
    id = fields.Int()
    name = fields.Str()
    description = fields.Str()
    owner_id = fields.Int()


class ItemSchema(Schema):
    id = fields.Int()
    project_id = fields.Int()
    name = fields.Str()
    description = fields.Str()
    date = fields.DateTime()
    owner_id = fields.Int()
