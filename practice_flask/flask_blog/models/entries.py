from flask_blog import db
from datetime import datetime

class Entry(db.Model):
    __tablename__ = 'entries'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), unique=True)
    text = db.Column(db.Text)
    # なぜかコンストラクタでcreated_atに日時を格納できないので応急処置で以下デフォルトを設けている
    # ビューの呼び出し側、またはINSERT処理に問題ある可能性もあり
    created_at = db.Column(db.DateTime, default=datetime.utcnow())

def __init__(self, title=None, text=None):
    self.title = title
    self.text = text
    # 下記でdatetimeが入れれてない、もしくは、呼び出し側orINSERT処理に問題ある可能性あり
    self.created_at = datetime.utcnow()

def __repr__(self):
    return 'Entry id:{} title:{} text:{}'.format_map(self.id, self.title, self.text)
