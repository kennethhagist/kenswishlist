# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from datetime import datetime
import re
import bcrypt

NAME_REGEX = re.compile(r'^[A-Za-z]\w+$')

# Create your models here.
class WisherManager(models.Manager):
    def validate_login(self, post_data):
        errors = []
        user = None
        if not self.filter(username=post_data['username']):
            errors.append("Invalid email/password")
        else:
            user = self.get(username=post_data['username'])
            if not bcrypt.checkpw(post_data['password'].encode(), user.password.encode()):
                errors.append("Invalid email/password")
        
        return errors, user

    def validate_registration(self, post_data):
        errors = []
        user = None
        for field, value in post_data.iteritems():
            if len(value) < 1:
                errors.append("All fields are required")
                break

        if len(post_data['name']) < 3:
            errors.append("Name field must be 3 or more")
        if len(post_data['password']) < 8:
            errors.append("Password  must be 8 or more characters")
        if post_data['password'] != post_data['password_confirm']:
            errors.append("password does not match")
        if not re.match(NAME_REGEX, post_data['name']):
            errors.append("name must be letter characters only")
        # if post_data['date_hired'] != datetime.datetime.strptime(date_text, '%Y-%m-%d'):
        #     errors.append("Invalid date format. Date Hired must be in YYYY-MM-DD format.")
        if len(post_data['username']) < 3:
            errors.append("username must be at least 3 characters")
        if len(Wisher.objects.filter(username=post_data['username'])) > 0:
            errors.append("username already in nameuse")
        if not errors:
            hashed_pw = bcrypt.hashpw(post_data['password'].encode(), bcrypt.gensalt())

            user = self.create(
                name = post_data['name'],
                username = post_data['username'],
                date_hired = post_data['date_hired'],
                password = hashed_pw
            )            
        return errors, user

class Wisher(models.Model):
    name = models.CharField(max_length=100)
    username = models.CharField(max_length=100, unique=True)
    date_hired = models.DateField()
    password = models.CharField(max_length=255)
    objects = WisherManager()
    def __str__(self):
        return "{}".format(self.username)

class Product(models.Model):
    name = models.CharField(max_length=100)
    creator = models.ForeignKey(Wisher, related_name='created_products')
    def __str__(self):
        return self.name

class Add(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    adder = models.ForeignKey(Wisher, related_name="added_products")
    product = models.ForeignKey(Product, related_name="added")

    def str(self):
        return "{} liked by {}".format(self.adder.username, self.product.name)