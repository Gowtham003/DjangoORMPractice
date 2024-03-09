from core.models import Restaurant, Rating, Sale
from django.contrib.auth.models import User
from django.utils import timezone
from django.db import connection
from pprint import pprint

def run():
    print(Restaurant.objects.filter(name__contains="Donald"))
    pprint(connection.queries)