from django.db import models

# Create your models here.

from django.db import models

# Create your models here.
class User(models.Model):
    UserID = models.BigAutoField(primary_key=True)
    Name = models.CharField(max_length=30)
    LastName = models.CharField(max_length=30)
    Email = models.EmailField(max_length=30)
    Password = models.CharField(max_length=30)

CATEGORY_CHOICES =[
    ('comedy','Comedy'),
    ('action','Action'),
    ('horror', 'Horror'),
    ('romance', 'Romance'),
    ('drama', 'Drama'),
    ('thriller', 'Thriller')
]

CLASIFICATION_CHOICES =[
    ('A','A'),
    ('B','B'),
    ('C','C'),
    ('D','D')
]

THEATER_TYPES_CHOICES =[
    ('normal','Normal'),
    ('vip', 'VIP')
]

SHOWTIME_TYPE_CHOICES = [
    ('normal', 'Normal'),
    ('3d','3D')
]

SHOWTIME_LANGUAGE = [
    ('Sub', 'Sub'),
    ('Dob', 'Dob'),
]

class Movie(models.Model):
    MovieID = models.BigAutoField(primary_key=True)
    Name = models.CharField(max_length=30)
    Description = models.TextField()
    Category = models.CharField(max_length=50, choices= CATEGORY_CHOICES)
    Clasification = models.CharField(max_length=50, choices = CLASIFICATION_CHOICES)
    New = models.BooleanField(default = True)


class Location(models.Model):
    LocationID = models.BigAutoField(primary_key=True)
    Name = models.CharField(max_length=50)
    Region = models.CharField(max_length=50, null = True)
    Address = models.CharField(max_length=50)

class Theater(models.Model):
    TheaterID = models.BigAutoField(primary_key=True)
    LocationID = models.ForeignKey('Location', on_delete=models.CASCADE)
    TheaterName = models.CharField(max_length = 30)
    Capacity = models.IntegerField()
    Type = models.CharField(max_length=50, choices= THEATER_TYPES_CHOICES)


class Ticket(models.Model):
    TicketID = models.BigAutoField(primary_key=True)
    UserID = models.ForeignKey('User', on_delete= models.CASCADE)
    ShowTimeID = models.ForeignKey('ShowTime', on_delete= models.SET_NULL,null=True)
    Total = models.DecimalField(max_digits=6, decimal_places=2)
    Date = models.DateField()

class ShowTime(models.Model):
    ShowTimeID= models.BigAutoField(primary_key=True)
    MovieID = models.ForeignKey('Movie', on_delete=models.CASCADE)
    TheaterID = models.ForeignKey('Theater', on_delete=models.CASCADE)
    Price = models.DecimalField(max_digits=6, decimal_places=2)
    Date = models.DateField()
    Hour = models.TimeField()
    Type = models.CharField(max_length=50, choices= SHOWTIME_TYPE_CHOICES)
    Language = models.CharField(max_length=50, choices=SHOWTIME_LANGUAGE, null = True)

class Seat(models.Model):
    SeatID = models.BigAutoField(primary_key=True)
    TheaterID = models.ForeignKey('Theater', on_delete=models.CASCADE)
    TicketID = models.ForeignKey('Ticket', on_delete=models.SET_NULL,null = True)
    State = models.BooleanField()

