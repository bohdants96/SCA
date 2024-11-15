from django.db import models

from .validators import validate_int, validate_breed


class SpyCat(models.Model):
    Name = models.CharField(max_length=50)
    Years_of_Experience = models.IntegerField(validators=[validate_int])
    Breed = models.CharField(max_length=50, validators=[validate_breed])
    Salary = models.IntegerField(validators=[validate_int])

    def __str__(self):
        return self.Name

    class Meta:
        ordering = ["Salary"]
        verbose_name = "SpyCat"
        verbose_name_plural = "SpyCats"
