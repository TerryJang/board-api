from marshmallow import Schema, fields, validates_schema, ValidationError


class BaseCommentResponseSchema(Schema):
    pass


class BaseCommentBodySchema(Schema):
    pass


class CreateCommentBodySchema(BaseCommentBodySchema):
    content = fields.String(required=True)
    writer = fields.String(required=True)
    password = fields.String(required=True)


class GetCommentListResponseSchema(BaseCommentResponseSchema):
    class Response(Schema):
        class CommentList(Schema):
            id = fields.Integer()
            writer = fields.String()
            content = fields.String()
            created_at = fields.DateTime()

        comments = fields.Nested(CommentList(), many=True)

    response = fields.Nested(Response())
