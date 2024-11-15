from django.db import models
from SpyCat.models import SpyCat


class Mission(models.Model):
    Cat = models.ForeignKey(SpyCat, on_delete=models.SET_NULL, null=True, blank=True, related_name='missions')
    Complete_state = models.BooleanField(default=False)

    def __str__(self):
        return self.id

    class Meta:
        ordering = ["id"]


class Target(models.Model):
    Mission = models.ForeignKey(Mission, on_delete=models.CASCADE, related_name='targets')
    Name = models.CharField(max_length=100)
    Country = models.CharField(max_length=100)
    Notes = models.TextField(blank=True)
    Complete_state = models.BooleanField(default=False)

    def __str__(self):
        return self.Name
