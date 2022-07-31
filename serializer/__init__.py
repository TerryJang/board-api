from marshmallow import Schema, fields


class OffsetPaginationSchema(Schema):
    total_count = fields.Integer()
    has_prev_page = fields.Boolean()
    has_next_page = fields.Boolean()
    current_page = fields.Integer()
    current_count = fields.Integer()
