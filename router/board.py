import logging
from http import HTTPStatus

from flask import Blueprint, request, make_response, jsonify

from serializer.board import CreateBoardBodySchema, UpdateBoardBodySchema, GetBoardListResponseSchema, GetBoardResponseSchema
from service.board import BoardService

board = Blueprint('board', __name__, url_prefix='/boards')
logger = logging.getLogger('server')


@board.route('', methods=['POST'])
def create_board():
    validated_data = CreateBoardBodySchema().load(request.json)
    BoardService.create_board(validated_data)
    return make_response(jsonify({'response': {}}), HTTPStatus.OK)


@board.route('/<int:board_id>', methods=['PUT'])
def update_board(board_id):
    validated_data = UpdateBoardBodySchema().load(request.json)
    BoardService.update_board(board_id=board_id, data=validated_data)
    return make_response(jsonify({'response': {}}), HTTPStatus.OK)


@board.route('/<int:board_id>', methods=['DELETE'])
def delete_board(board_id):
    validated_data = UpdateBoardBodySchema().load(request.json)
    # 작성자와 비밀번호가 맞는지 확인
    BoardService.delete_board(board_id=board_id)
    return make_response(jsonify({'response': {}}), HTTPStatus.OK)


@board.route('', methods=['GET'])
def get_boards():
    boards = BoardService.get_boards()
    return make_response(GetBoardListResponseSchema().dump({'response': {'boards': boards}}), HTTPStatus.OK)


@board.route('/<int:board_id>', methods=['GET'])
def get_board(board_id):
    board = BoardService.get_board(board_id=board_id)
    return make_response(jsonify({'response': GetBoardResponseSchema().dump(board)}), HTTPStatus.OK)
