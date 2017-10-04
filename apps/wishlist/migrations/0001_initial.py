# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-10-04 01:21
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Add',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Wisher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('username', models.CharField(max_length=100, unique=True)),
                ('date_hired', models.DateField()),
                ('password', models.CharField(max_length=255)),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='creator',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='created_products', to='wishlist.Wisher'),
        ),
        migrations.AddField(
            model_name='add',
            name='adder',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='added_products', to='wishlist.Wisher'),
        ),
        migrations.AddField(
            model_name='add',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='added', to='wishlist.Product'),
        ),
    ]