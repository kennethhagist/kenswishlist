# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from .models import Wisher, Product, Add

def verify_session_user(request):
    try:
        request.session['id']
    except KeyError:
        return redirect('/')

# Create your views here.
def index(request):
    return render(request, 'wishlist/index.html')

def login(request):
    errors_or_user = Wisher.objects.validate_login(request.POST)

    if errors_or_user[0]:
        for fail in errors_or_user[0]:
            messages.error(request, fail)
        return redirect('/')
    request.session['id'] = errors_or_user[1].id
    messages.success(request, "Hello, {{ name }}")
    return redirect('/dashboard')

def register(request):
    errors_or_user = Wisher.objects.validate_registration(request.POST)

    if errors_or_user[0]:
        for fail in errors_or_user[0]:
            messages.error(request, fail)
        return redirect('/')
    request.session['id'] = errors_or_user[1].id
    messages.success(request, "Hello, {{ name }}")
    return redirect('/dashboard')

def logout(request):
    del request.session['id']
    return redirect('/')

def dashboard(request):
    context = {
        "user": Wisher.objects.get(id=request.session['id']),
        "users_products": Product.objects.filter(creator_id=request.session['id']),
        "most_recently_added": Product.objects.all().order_by('-added__created_at').first(),
        "not_been_added": Product.objects.exclude(added__adder_id = request.session['id']).exclude(creator_id=request.session['id']),
        "added_products": Product.objects.filter(added__adder_id = request.session['id']).exclude(creator_id=request.session['id'])
    }
    return render(request, 'wishlist/dashboard.html', context)

def create_product(request):
    Product.objects.create(
        name = request.POST['name'],
        creator = Wisher.objects.get(id = request.session['id'])
    )
    return redirect('/create.html')

def add(request, product_id):
    Add.objects.create(
        adder_id = request.session['id'],
        product_id = product_id
    )
    return redirect('/dashboard')

def remove(request, add_id):
    product = Product.objects.get(id=product_id)
    wisher = Wisher.objects.get(id=request.session['id'])
    product.added.remove(wisher)

    return redirect('/dashboard')

def delete(request, product_id):
    product = Product.objects.get(id=product_id)
    product.remove(id=product_id)
    
    return redirect('/dashboard')

# def wishlist(reqeust, product_id):
#     return redirect('/dashboard')

# def add_a_product(request, product_id):
#     return redirect('/dashboard')

# def remove_a_product(request, product_id):
#     return redirect('/dashboard')