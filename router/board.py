import logging
from http import HTTPStatus

from flask import Blueprint, request, make_response, jsonify

from serializer.board import CreateBoardBodySchema, UpdateBoardBodySchema, GetBoardListResponseSchema, GetBoardResponseSchema, GetBoardListParamSchema
from service.board import BoardService
from common.utils import Utils

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
    board = BoardService.get_board(board_id=board_id)
    Utils.check_password(validated_data['password'], board.password)
    BoardService.update_board(board_id=board_id, data=validated_data)
    return make_response(jsonify({'response': {}}), HTTPStatus.OK)


@board.route('/<int:board_id>', methods=['DELETE'])
def delete_board(board_id):
    validated_data = UpdateBoardBodySchema().load(request.json)
    board = BoardService.get_board(board_id=board_id)
    Utils.check_password(validated_data['password'], board.password)
    BoardService.delete_board(board_id=board_id)
    return make_response(jsonify({'response': {}}), HTTPStatus.OK)


@board.route('', methods=['GET'])
def get_boards():
    params = GetBoardListParamSchema().load(request.args)
    pagination, boards = BoardService.get_boards(params)
    return make_response(GetBoardListResponseSchema().dump({'response': {'pagination': pagination, 'boards': boards}}), HTTPStatus.OK)


@board.route('/<int:board_id>', methods=['GET'])
def get_board(board_id):
    board = BoardService.get_board(board_id=board_id)
    return make_response(jsonify({'response': GetBoardResponseSchema().dump(board)}), HTTPStatus.OK)