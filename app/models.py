# -*- coding:utf-8 -*-
from app import db


class AdminUser(db.Document):
    adminname = db.StringField(max_length=255, required=True)
    password = db.StringField(max_length=255, required=True)

    # def get_absolute_url(self):
    #     return url_for('adminuser', kwargs={"slug": self.slug})

    def __unicode__(self):
        return self.adminname
    # meta = {
    #     'allow_inheritance': True,
    #     'indexes': ['-created_at', 'slug'],
    #     'ordering': ['-created_at']
    # }
