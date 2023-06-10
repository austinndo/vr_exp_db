from django.db import models
from django.core.validators import MinValueValidator


class Experience(models.Model):
    HEADSETS = [
        ("Oculus Rift", "Oculus Rift"),
        ("HTC Vive", "HTC Vive"),
        ("PlayStation VR", "PlayStation VR"),
        ("Meta Quest", "Meta Quest"),
        ("Other", "Other")]
    MOTION_SICKNESS_CHOICES = [(i, i) for i in range(1, 11)]
    IMMERSION_LEVEL_CHOICES = [(i, i) for i in range(1, 6)]

    user_age = models.PositiveIntegerField(
        validators=[MinValueValidator(18)])
    headset_type = models.CharField(choices=HEADSETS)
    duration_of_use = models.PositiveIntegerField(
        validators=[MinValueValidator(1)])
    motion_sickness = models.PositiveIntegerField(
        choices=MOTION_SICKNESS_CHOICES)
    immersion_level = models.PositiveIntegerField(
        choices=IMMERSION_LEVEL_CHOICES)

    def __str__(self):
        return self.name
