from flask import Flask

from router.main import main
from router.board import board
from router.comment import comment
from engine.mysql import mysql_connection_pool
from settings import get_config
from exception import register_error_handler


app = Flask(__name__)

app.register_blueprint(main)
app.register_blueprint(board)
app.register_blueprint(comment)


if __name__ == '__main__':
    config = get_config()
    mysql_connection_pool.setup(config=config)
    register_error_handler(app)
    app.run()
