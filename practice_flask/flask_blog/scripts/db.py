from flask_script import Command
from flask_blog import db

class InitDB(Command):
    # 下記はスクリプト説明のコメント
    "create database"

    def run(self):
        db.create_all()