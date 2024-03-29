from django.shortcuts import render
from rest_framework import serializers
from rest_framework.views import APIView
from rest_framework.parsers import FormParser, MultiPartParser
from rest_framework import status
from rest_framework.response import Response
from sentiment_app.serializers import ExcelFileSerializer

# Create your views here.

class FileUploadView(APIView):
    parser_classs = (MultiPartParser, FormParser)

    def post(self, request):
        serializer = ExcelFileSerializer(data= request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

