from datetime import datetime
from extensions import db


class DashboardItem(db.Model):
    __tablename__ = 'dashboards'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, nullable=False)
    name = db.Column(db.String(120))
    data = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
