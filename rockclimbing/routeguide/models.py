from django.db import models

class Gym(models.Model):
    name = models.CharField(max_length=250)
    province = models.CharField(max_length=100)
    city = models.CharField(max_length=250)
    address = models.CharField(max_length=500)
    gym_logo = models.CharField(max_length=1000)

    def __str__(self):
        return self.name + ' - ' + self.city + ', ' + self.province

class Route(models.Model):
    gym = models.ForeignKey(Gym, on_delete=models.CASCADE)
    difficulty = models.CharField(max_length=100)
    climb_type = models.CharField(max_length=100)
    climb_picture = models.CharField(max_length=500)
    is_up = models.BooleanField(default=True)

    def __str__(self):
        return self.climb_type + ' - ' + self.difficulty