from django.shortcuts import render
from rest_framework import viewsets, generics
from .models import Data
from .serializer import DataSerializer, DataSerializerAdd, DataSerializerSubstract
from rest_framework.decorators import api_view

from rest_framework import generics, status
from rest_framework.response import Response

from django.http import HttpResponse
import datetime

class PostListView(generics.ListAPIView):
    queryset = Data.objects.all()
    serializer_class = DataSerializer


def PostPingView(request):
    now = datetime.datetime.now()
    html = "Server work.Time is {}".format(now)
    return HttpResponse(html)


class PostAddView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Data.objects.all()
    serializer_class = DataSerializerAdd

    def patch(self, request, *args, **kwargs):
        super(PostAddView, self).patch(request, args, kwargs)
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        data = serializer.data
        response = {"status_code": status.HTTP_200_OK,
                    "message": "Successfully updated",
                    "result": data}
        return Response(response)


class PostSubstractView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Data.objects.all()
    serializer_class = DataSerializerSubstract

    def patch(self, request, *args, **kwargs):
        super(PostSubstractView, self).patch(request, args, kwargs)
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        data = serializer.data
        response = {"status": status.HTTP_200_OK,
                    "result": "Successfully updated",
                    "addition": data,
                    "description": ""}
        return Response(response)


class PostStatusView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Data.objects.all()
    serializer_class = DataSerializer

    def get_queryset(self):

        user = self.request.user
        queryset = Data.objects.all()
        return queryset
