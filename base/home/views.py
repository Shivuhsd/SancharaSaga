from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.response import Response
from .serializer import SerializedBooking, SerializedFeedback
from rest_framework.views import APIView
from rest_framework import status

# Create your views here.
def Home(request):
    return JsonResponse({"hi": "Hello World"})


class UserBooking(APIView):
    def post(self, request, *args, **kwargs):
        serializer = SerializedBooking(data=request.data)
        if serializer.is_valid():
            # Perform actions based on the validated data
            # For example, save to the database
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# def UserBooking(request):
#     if request.method == "POST":
#         name = request.POST['name']
#         email = request.POST['email']
#         peoples = request.POST['peoples']
#         whatsapp = request.POST['whatsapp']
#         pickup = request.POST['pickup']

#         print(name, email, peoples, whatsapp, pickup)
#     return JsonResponse({"status": "true"})


class Feedback(APIView):
    def post(self, request, *args, **kwargs):
        serializer = SerializedFeedback(data=request.data)
        if serializer.is_valid():
            # Perform actions based on the validated data
            # For example, save to the database
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


  