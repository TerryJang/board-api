from . import OffsetPaginationSchema
from marshmallow import Schema, fields


class BaseCommentResponseSchema(Schema):
    pass


class BaseCommentBodySchema(Schema):
    pass


class CreateCommentBodySchema(BaseCommentBodySchema):
    content = fields.String(required=True)
    writer = fields.String(required=True)
    password = fields.String(required=True)
    parent = fields.Integer()


class GetCommentListResponseSchema(BaseCommentResponseSchema):
    class Response(Schema):
        class CommentList(Schema):
            id = fields.Integer()
            writer = fields.String()
            content = fields.String()
            created_at = fields.DateTime()

        comments = fields.Nested(CommentList(), many=True)
        pagination = fields.Nested(OffsetPaginationSchema())

    response = fields.Nested(Response())


class GetCommentListParamSchema(Schema):
    page = fields.Integer()
    size = fields.Integer()
