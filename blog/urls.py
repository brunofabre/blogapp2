from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^posts/$', views.posts, name='posts'),
    url(r'^detalhe/(?P<slug>[\w_-]+)/$', views.detail, name='detail'),
    url(r'^create/$', views.create, name='create'),
    url(r'^editar/(?P<slug>[\w_-]+)/$', views.edit, name='edit'),
    url(r'^post/(?P<slug>[\w_-]+)/delete/$', views.delete, name='delete'),

    url(r'^registro/$', views.register, name='register'),
]
