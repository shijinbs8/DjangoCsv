from django.shortcuts import render

# Create your views here.

import csv
import io
from .models import *

from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework import status
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from .serializers import *


class CsvReader(APIView):
    parser_classes = [MultiPartParser, FormParser]

    def post(self, request, *args, **kwargs):
        csv_file = request.FILES.get('file')

        if not csv_file:
            return Response({"error": "No file uploaded."}, status=status.HTTP_400_BAD_REQUEST)

        if not csv_file.name.endswith('.csv'):
            return Response({"error": "Only .csv files are allowed."}, status=status.HTTP_400_BAD_REQUEST)

        decoded_file = csv_file.read().decode('utf-8')
        io_string = io.StringIO(decoded_file)
        reader = csv.DictReader(io_string)

        saved_count = 0
        rejected_count = 0
        errors = []

        for i, row in enumerate(reader, start=1):
            data = {
                'name': row.get('name', '').strip(),
                'email': row.get('email', '').strip(),
                'age': row.get('age', '').strip(),
            }

            serializer = UserProfileSerializer(data=data)

            if serializer.is_valid():
                # Save the valid data instance
                serializer.save()
                saved_count += 1
            else:
                rejected_count += 1
                errors.append({
                    "row": i,
                    "error": serializer.errors,
                })

        return Response({
            "records_saved": saved_count,
            "records_rejected": rejected_count,
            "errors": errors
        }, status=status.HTTP_200_OK)
