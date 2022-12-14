from . import OffsetPaginationSchema
from marshmallow import Schema, fields


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
    password = fields.String(required=True)


class DeleteBoardBodySchema(BaseBoardBodySchema):
    password = fields.String(required=True)


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
        pagination = fields.Nested(OffsetPaginationSchema())

    response = fields.Nested(Response())


class GetBoardListParamSchema(Schema):
    page = fields.Integer()
    size = fields.Integer()
    writer = fields.String()
    title = fields.String()
