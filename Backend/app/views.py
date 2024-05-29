from django.shortcuts import render
from .models import *
from .serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer
import io
import json
from rest_framework.parsers import JSONParser
from django.http import HttpResponse

from django.views.decorators.csrf import csrf_exempt


# Create your views here.
@csrf_exempt
def stulist(request):
    if request.method=='GET':
        stu_list=Student.objects.all()
        print("Query_set=",stu_list)
        serializer=StudentSerializer(stu_list,many=True)
        print("Serializer=",serializer)
        print("Python_data(serializer.data)=",serializer.data)
        json_data=JSONRenderer().render(serializer.data)
        print("Json_Data=",json_data)
        return HttpResponse(json_data,content_type='application/json') 
    elif request.method=='POST':
    
        json_data=request.body
        stream=io.BytesIO(json_data) 
        python_data=JSONParser().parse(stream)
        serializer=StudentSerializer(data=python_data)
        if serializer.is_valid():
            serializer.save()
            res={'msg':'Data Created'}
            json_data=JSONRenderer().render(res)
            return HttpResponse(json_data,content_type='application/json')
        json_data=JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data,content_type='application/json')
    
    elif request.method=='PUT':
        json_data=request.body
        stream=io.BytesIO(json_data)
        python_data=JSONParser().parse(stream)
        id=python_data.get('id')
        stu=Student.objects.get(id=id)
        # serializer-StudentSerializer(stu,data=python_data)
        serializer=StudentSerializer(stu,data=python_data)
        if serializer.is_valid():
            serializer.save()
            res={'msg':'Data Updated!!'}
            json_data=JSONRenderer().render(res)
            return HttpResponse(json_data,content_type='application/json')
        json_data=JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data,content_type='application/json')




# from .models import *
# from .serializers import *

# def stulist(request):
#     return HttpResponse(content_type='application/json')

    
