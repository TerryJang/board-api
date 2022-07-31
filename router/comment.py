import logging
from http import HTTPStatus

from flask import Blueprint, request, make_response, jsonify

from serializer.comment import CreateCommentBodySchema, GetCommentListResponseSchema, GetCommentListParamSchema
from service.comment import CommentService

comment = Blueprint('comment', __name__, url_prefix='/boards/<int:board_id>/comments')
logger = logging.getLogger('server')


@comment.route('', methods=['POST'])
def create_comments(board_id):
    validated_data = CreateCommentBodySchema().load(request.json)
    CommentService.create_comment(board_id=board_id, data=validated_data)
    return make_response(jsonify({'response': {}}), HTTPStatus.OK)


@comment.route('', methods=['GET'])
def get_comments(board_id):
    params = GetCommentListParamSchema().load(request.args)
    pagination, comments = CommentService.get_comments(board_id=board_id, params=params)
    return make_response(jsonify(GetCommentListResponseSchema().dump({'response': {'pagination': pagination, 'comments': comments}})), HTTPStatus.OK)
