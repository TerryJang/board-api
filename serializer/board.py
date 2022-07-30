from marshmallow import Schema, fields, validates_schema, ValidationError


class BaseBoardResponseSchema(Schema):
    pass


class BaseBoardBodySchema(Schema):
    pass


class CreateBoardBodySchema(BaseBoardBodySchema):
    title = fields.String(required=True)
    content = fields.String(required=True)
    writer = fields.String(required=True)
    password = fields.String(required=True)


class UpdateBoardBodySchema(BaseBoardBodySchema):
    title = fields.String()
    content = fields.String()
    writer = fields.String()
    password = fields.String()


class DeleteBoardBodySchema(BaseBoardBodySchema):
    writer = fields.String()
    password = fields.String()


class GetBoardResponseSchema(BaseBoardResponseSchema):
    id = fields.Integer()
    title = fields.String()
    content = fields.String()
    writer = fields.String()
    created_at = fields.DateTime()



class GetBoardListResponseSchema(BaseBoardResponseSchema):
    class Response(Schema):
        class BoardList(Schema):
            id = fields.Integer()
            title = fields.String()
            writer = fields.String()
            created_at = fields.DateTime()

        boards = fields.Nested(BoardList(), many=True)

    response = fields.Nested(Response())
