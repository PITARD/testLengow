from django.conf.urls import url


from . import views
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^add', views.add, name='add'),
    url(r'^addOrders', views.addOrders, name='addOrders'),
    url(r'^list/(?P<order_id>[a-zA-Z0-9-]+)', views.detail, name='detail'),
    url(r'^list', views.list, name='list'),

]
