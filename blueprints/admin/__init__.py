from flask import Blueprint, url_for, request, redirect, render_template, flash
from passlib.hash import argon2
from controllers.user_controller import get_user_by_id

bp_admin = Blueprint('bp_admin', __name__)


@bp_admin.get('/changePassword/<user_id>')
def change_password_get(user_id):
    user_id = int(user_id)
    user = get_user_by_id(user_id)
    return render_template('changePassword.html', user=user)


@bp_admin.post('/changePassword/<user_id>')
def change_password(user_id):
    user_id = int(user_id)
    password = request.form['new password']
    if password != request.form['confirm']:
        flash("Your password don't match")
        return redirect(url_for('bp_admin.change_password_get', user_id=user_id))

    else:
        hashed_password = argon2.using(rounds=10).hash(password)
        user = get_user_by_id(user_id)
        user.password = hashed_password
        from app import db
        db.session.commit()

    return redirect(url_for('bp_user.user_get'))


@bp_admin.post('/profile/<user_id>')
def delete_user(user_id):
    from models import User
    user_to_delete = User.query.get_or_404(user_id)
    from app import db
    db.session.delete(user_to_delete)
    db.session.commit()

    return redirect(url_for('bp_user.user_get'))
