from flask import render_template, session, redirect, url_for, request
from app.models import AdminUser
from . import admin


@admin.route('/admin/login', methods=['GET', 'POST'])
def Admin_Login():
    if request.method == 'POST':
        print(request.form['adminname'])
        print(AdminUser.objects.get(adminname=request.form['adminname']))
        # user = AdminUser.objects.get(adminname=request.form['adminname'])
        # if user.password == request.form['password']:
        return render_template('admin/success.html')
    return render_template('admin/Admin_Login.html')
