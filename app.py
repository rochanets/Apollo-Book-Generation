from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from auth_service.routes import auth_bp
from dashboard_service.routes import dashboard_bp

app = Flask(__name__)
app.config['SECRET_KEY'] = 'change-me'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# allow blueprints to access db
from auth_service.models import init_auth
from dashboard_service.models import init_dashboard

init_auth(db)
init_dashboard(db)

db.create_all()

app.register_blueprint(auth_bp)
app.register_blueprint(dashboard_bp)

if __name__ == '__main__':
    app.run(debug=True)
