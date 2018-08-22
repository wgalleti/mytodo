from django.conf.urls import url
from django.urls import include, path
from rest_framework import routers

from core import views

rt = routers.DefaultRouter(trailing_slash=True)
rt.register('tarefas', views.TarefaViewSet)

urlpatterns = [
    path('', views.index),
    path('drf', views.drf),
    path('api/add_tarefa', views.add_tarefa),
    path('api/remove_tarefa', views.remove_tarefa),
    path('api/list_tarefas', views.list_tarefas),
    path('api_drf/', include(rt.urls)),
]

