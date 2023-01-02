from django.db import models

# Create your models here.


class Location(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=300)

    def __str__(self):
        return f"{ self.name} ({ self.address })"

class Participant(models.Model):
    email = models.EmailField(max_length=200, unique=True)

    def __str__(self):
        return f"{ self.email }"

class Meetup(models.Model):
    title = models.CharField(max_length=255)
    organizer_email =  models.EmailField(null=True)
    date = models.DateField(null=True)
    slug = models.SlugField(unique=True)
    description = models.TextField()
    image = models.ImageField(upload_to='images', default='test.jpg')
    location = models.ForeignKey(Location, on_delete=models.CASCADE, null=True)
    participants = models.ManyToManyField(Participant, blank=True)

    def __str__(self):
        return f"{ self.title } - { self.slug }"
