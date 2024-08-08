from rest_framework import response
#from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework import status
from API.serializers import *
from API.models import *

class User_Views(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = User_Serializer

class Movie_Views(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = Movie_Serializer

class Location_Views(viewsets.ModelViewSet):
    queryset =Location.objects.all()
    serializer_class = Location_Serializer

class Theater_Views(viewsets.ModelViewSet):
    queryset = Theater.objects.all()
    serializer_class = Theater_Serializer

class ShowTime_Views(viewsets.ModelViewSet):
    queryset = ShowTime.objects.all()
    serializer_class = ShowTime_Serializer

class Ticket_Views(viewsets.ModelViewSet):
    queryset =Ticket.objects.all()
    serializer_class= Ticket_Serializer

class Seat_Views(viewsets.ModelViewSet):
    queryset = Seat.objects.all()
    serializer_class = Seat_Serializer

""" class User_Views(APIView):
    def getone(self,userid):
        user = User.objects.get(pk = userid)
        user_serialized = User_Serializer(user)
        
    def Get_All(self, request, format = None):
        users = User.objects.all()
        users_serialized = User_Serializer(users, many =True)
        return response(users_serialized)
    
    def Get_By_Id(self, userid):
        user = User.objects.get(pk = userid)
        user_serialized = User_Serializer(user)
        return response(user_serialized)
    
    def Post(self, request, format = None):
        user_serialized = User_Serializer(data = request.data)
        if user_serialized.is_valid():
            user_serialized.save()
            return response(user_serialized.data, status=status.HTTP_201_CREATED)
        return response(user_serialized.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def Update(self,userId, request,format =None):
        user = User.objects.get(pk = userId)
        newuser_serialized = User_Serializer(user, request.data)
        if newuser_serialized.is_valid():
            newuser_serialized.save()
            return response(newuser_serialized.data, status=status.HTTP_201_CREATED)
        return response(newuser_serialized.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def Delete(self, userId):
        user = User.objects.get(pk = userId)
        user.delete()
        return response(status=status.HTTP_204_NO_CONTENT) """