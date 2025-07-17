from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = None

class DashboardItem(db.Model if db else object):
    __tablename__ = 'dashboards'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, nullable=False)
    name = db.Column(db.String(120))
    data = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

def init_dashboard(database):
    global db, DashboardItem
    db = database
    class DashboardItem(db.Model):
        __tablename__ = 'dashboards'
        id = db.Column(db.Integer, primary_key=True)
        user_id = db.Column(db.Integer, nullable=False)
        name = db.Column(db.String(120))
        data = db.Column(db.Text)
        created_at = db.Column(db.DateTime, default=datetime.utcnow)
    globals()['DashboardItem'] = DashboardItem
