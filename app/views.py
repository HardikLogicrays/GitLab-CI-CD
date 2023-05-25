from django.shortcuts import render
from .serializers import StudentSerializer
from .models import Student
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.


class StudentView(APIView):
    
    serializer_class = StudentSerializer
    
    
    def get(self, request):
        student = Student.objects.all()
        serializer = self.serializer_class(student, many=True)
        return Response(serializer.data)
        
        
    def post(self, request):
        
        data = request.data
        
        serializer = self.serializer_class(data=data)
        if serializer.is_valid(raise_exception=True):
            return Response(serializer.data, status=201)
        
        return Response(serializer.errors, status=400)
         


