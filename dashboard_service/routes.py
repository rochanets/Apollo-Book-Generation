from flask import Blueprint, render_template, request, redirect, url_for, session, flash
from werkzeug.utils import secure_filename
import json
import pandas as pd
from .analytics import analyze_dataframe
from .models import DashboardItem, db
from auth_service.models import User
import io


dashboard_bp = Blueprint('dashboard', __name__, url_prefix='/dashboard')

@dashboard_bp.route('/')
def dashboard():
    if 'user_id' not in session:
        return redirect(url_for('auth.login'))
    items = DashboardItem.query.filter_by(user_id=session['user_id']).all()
    return render_template('dashboard.html', items=items)

@dashboard_bp.route('/upload', methods=['POST'])
def upload():
    if 'user_id' not in session:
        return redirect(url_for('auth.login'))
    file = request.files.get('file')
    if not file:
        flash('No file selected')
        return redirect(url_for('dashboard.dashboard'))
    filename = secure_filename(file.filename)
    data = file.read().decode('utf-8')
    df = pd.read_csv(io.StringIO(data))
    summary = analyze_dataframe(df)
    dashboard_item = DashboardItem(user_id=session['user_id'], name=filename, data=json.dumps(summary))
    db.session.add(dashboard_item)
    db.session.commit()
    flash('Dashboard generated')
    return redirect(url_for('dashboard.view', item_id=dashboard_item.id))

@dashboard_bp.route('/view/<int:item_id>')
def view(item_id):
    if 'user_id' not in session:
        return redirect(url_for('auth.login'))
    item = DashboardItem.query.get_or_404(item_id)
    if item.user_id != session['user_id']:
        return redirect(url_for('dashboard.dashboard'))
    summary = json.loads(item.data)
    items = DashboardItem.query.filter_by(user_id=session['user_id']).all()
    return render_template('home.html', summary=summary, items=items, name=item.name)
