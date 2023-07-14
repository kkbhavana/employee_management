from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response

from .models import Employee
from .serializers import EmployeeSerializer


# Create your views here.
class EmployeeListView(generics.ListCreateAPIView):
    serializer_class = EmployeeSerializer
    queryset = Employee.objects.all()

    def list(self, request):
        queryset = self.get_queryset()
        serializer = EmployeeSerializer(queryset, many=True)
        return Response(serializer.data)

class EmployeeUpdateView(generics.UpdateAPIView):
    serializer_class = EmployeeSerializer
    queryset = Employee.objects.all()

class EmployeeDeleteView(generics.DestroyAPIView):
    serializer_class = EmployeeSerializer
    queryset = Employee.objects.all()

class EmployeeDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = EmployeeSerializer
    queryset = Employee.objects.all()

    def get(self,request,*args,**kwargs):
        queryset = self.get_object()
        if queryset is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = EmployeeSerializer(queryset,many=False)
        return Response(serializer.data)
