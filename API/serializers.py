from rest_framework import serializers
from API.models import *

class User_Serializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['Name','LastName','Email','Password']

class Movie_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ['MovieID', 'Name', 'Description', 'Category', 'Clasification']

class Location_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ['LocationID', 'Name', 'Adress']

class Theater_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Theater
        fields = ['TheaterID', 'LocationID', 'Capacity', 'Type']

class ShowTime_Serializer(serializers.ModelField):
    class Meta:
        model = ShowTime
        fields = ['ShowTimeID', 'MovieID', 'TheaterID', 'Total', 'Date']

class Seat_Serializer(serializers.ModelField):
    class Meta:
        model = Seat
        field = ['SeatID', 'TickedID', 'TheaterID', 'State']

class Ticket_Serializer(serializers.ModelField):
    class Meta:
        model = Ticket
        field = ['TicketID', 'ShowTimeID', 'UserID', 'Total','Date']