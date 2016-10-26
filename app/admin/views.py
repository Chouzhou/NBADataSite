from flask import render_template, session, redirect, url_for

from . import admin


@admin.route('/', methods=['GET', 'POST'])
def Admin_Login():
    return render_template('admin/Admin_Login.html', name='success')
