from django.db import models

class Location(models.Model):
    lat = models.FloatField(null=True, blank=True)
    lng = models.FloatField(null=True, blank=True)

    def __str__(self):
        return f"Lat: {self.lat}, Lng: {self.lng}"

class Funeral(models.Model):
    name = models.CharField(max_length=200, blank=False)
    region = models.CharField(max_length=100, unique=False, blank=False)
    address = models.CharField(max_length=300, unique=True, blank=False)
    phone = models.CharField(max_length=20, blank=False) # PhoneNumberField()라는 것도 있는데 일단 사용 안함
    image = models.ImageField(upload_to='funeral_images/', blank=True, null=True)
    website = models.URLField(max_length=255, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    location = models.OneToOneField(Location, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name