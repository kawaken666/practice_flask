# スクリプトモジュールを実行できるようにするためのファイル

from flask_script import Manager
from flask_blog import create_app

from flask_blog.scripts.db import InitDB, DropDB

if __name__ == "__main__":
    manager = Manager(create_app)
    # init_dbコマンドを実行できるようにする
    manager.add_command('init_db', InitDB())
    # drop_dbコマンドを実行できるようにする
    manager.add_command('drop_db', DropDB())
    manager.run()