from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^login$', views.login),
    url(r'^logout$', views.logout),
    url(r'^register$', views.register),
    url(r'^dashboard$', views.dashboard),
    url(r'^create$', views.create_product, name="create"),
    url(r'^add/(?P<product_id>\d+)$', views.add, name="add_it"),
    url(r'^remove/(?P<product_id>\d+)$', views.remove, name="remove_it"),
    url(r'^delete$', views.delete)
    #url(r'^wishlist$', views.wishlist),
    #url(r'^wishlist/add/(?P<wishlist_to_add_id>\d+)$', views.add_a_product),
    #url(r'^wishlist/remove/(?P<wishlist_to_remove_id>\d+)$', views.remove_a_product),
]