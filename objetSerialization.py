from marshmallow import Schema, fields


class ProjectSchema(Schema):
    '''
    class to serilize project table objetcs
    '''
    id = fields.Int()
    name = fields.Str()
    description = fields.Str()
    owner_id = fields.Int()


class ItemSchema(Schema):
    '''
    class to serilize items table objects
    '''
    id = fields.Int()
    project_id = fields.Int()
    name = fields.Str()
    description = fields.Str()
    date = fields.DateTime()
    owner_id = fields.Int()


class UserSchema(Schema):
    '''
    class to serilize users objects
    '''
    id = fields.Int()
    name = fields.Str()
    password = fields.Str()
    root = fields.Boolean()
