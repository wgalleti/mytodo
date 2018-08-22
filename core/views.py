import json
from time import sleep

from django.http.response import JsonResponse
from django.shortcuts import render
from rest_framework import viewsets, response
from rest_framework.decorators import action

from core.models import Tarefa
from core.serializers import TarefaSerializer
from core.service import tarefa_svc


def index(request):
    return render(request, 'index.html', {})


def drf(request):
    return render(request, 'drf.html', {})


def list_tarefas(request):
    tarefas = tarefa_svc.list_tarefas()
    return JsonResponse(tarefas, safe=False)


def add_tarefa(request):
    sleep(1)
    dtarefa = json.loads(request.POST['tarefa'])
    tarefa = tarefa_svc.add_tarefa(dtarefa)
    return JsonResponse(tarefa)


def remove_tarefa(request):
    sleep(1)
    tarefa_id = int(request.POST['tarefa_id'])
    tarefa_svc.remove_tarefa(tarefa_id)
    return JsonResponse({})


class TarefaViewSet(viewsets.ModelViewSet):
    serializer_class = TarefaSerializer
    queryset = Tarefa.objects.all().order_by('-created')

    @action(methods=['post'], detail=True)
    def finalizar(self, request, pk=None):
        tarefa = self.get_object()
        tarefa.finalizar()
        return response.Response('Ok', status=200)
