from django.db import models

# Create your models here.

import uuid
# Create your models here.
   
class Watch(models.Model):

    id=models.UUIDField(primary_key=True ,default=uuid.uuid4,help_text="generated unique id for product")
    cost=models.IntegerField()
    name=models.CharField(max_length=40)
    company=models.CharField(max_length=30)
    link=models.CharField(max_length=9100,help_text="Image Link",default="https://via.placeholder.com/225x225")
    content=models.TextField(max_length=5000,help_text="Product discription",default="Meet Fitbit Versa—an all-day companion that helps you live your best life. This lightweight, water-resistant smartwatch empowers you to reach health and fitness goals with actionable insights, personalized guidance, on-screen workouts and more. Run your day with notifications, quick replies, apps, music and 4+ day battery life* Plus, wear it your way with fresh accessories and clock faces. *Battery life varies with use and other factors.")
    
    def __str__(self):
        return self.company

class Phone(models.Model):
    id=models.UUIDField(primary_key=True ,default=uuid.uuid4,help_text="generated unique id for product")


    cost=models.IntegerField()
    name=models.CharField(max_length=40)
    company=models.CharField(max_length=30)
    link=models.CharField(max_length=1100,help_text="Image Link",default="https://via.placeholder.com/225x225")
    content=models.CharField(max_length=5000,help_text="Product discription",default="Effortlessly manage your busy schedule with the iPhone 6. This mobile phone has 16 GB of built-in memory, so you can store your music, apps, and more. Featuring an 8-megapixel resolution camera, it lets you document your travels and experiences in impressive detail. Stay connected and entertained using this iPhone 6. This device is locked to AT&T and compatible with Cricket, metroPCS, T-Mobile Carriers.")

    def __str__(self):
        return self.company

class Laptop(models.Model):
    id=models.UUIDField(primary_key=True ,default=uuid.uuid4,help_text="generated unique id for product")


    cost=models.IntegerField()
    name=models.CharField(max_length=40)
    company=models.CharField(max_length=30,)
    link=models.CharField(max_length=1100,help_text="Image Link",default="https://via.placeholder.com/225x225")
    content=models.CharField(max_length=5000,help_text="Product discription",default="The HP 245 G6 Laptop renders performance and multi-tasking efficiency with its integrated 4 GB RAM. This device is powered by a reliable 7th Generation AMD A9-9420 that takes care of all its processing needs. Its hard drive provides storage space for digital content. Also, this laptop features a convenient 35.56cm(14-inch) display that provides a clear view of files, apps, and documents.")

    def __str__(self):
        return self.company



class Product(models.Model):
    cost=models.IntegerField()
    name=models.CharField(max_length=40)
    company=models.CharField(max_length=30,)
    items=models.IntegerField()
   
    def __str__(self):
        return self.company
