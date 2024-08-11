from django.db import models
from accounts.models import User

EXPERIENCE_CHOICES = [
    (0, 'junior'),
    (1, 'midlevel'),
    (2, 'senior')
]

STATE_CHOICES = [
    ('P', 'Pending'),
    ('W', 'Waiting'),
    ('A', 'Assigned'),
    ('D', 'Done')
]

class Benefactor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    experience = models.SmallIntegerField(default=0, choices=EXPERIENCE_CHOICES)
    free_time_per_week = models.PositiveSmallIntegerField(default=0)

class Charity(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    reg_number = models.CharField(max_length=10)

class Task(models.Model):
    assigned_benefactor = models.ForeignKey(Benefactor, null=True, on_delete=models.PROTECT)
    charity = models.ForeignKey(Charity, on_delete=models.CASCADE)
    age_limit_from = models.IntegerField(null=True, blank=True)
    age_limit_to = models.IntegerField(null=True, blank=True)
    date = models.DateField(null=True, blank=True)
    description = models.TextField(blank=True)
    gender_limit = models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=1, null=True, blank=True)
    state = models.CharField(choices=STATE_CHOICES, default='P', max_length=1)
    title = models.CharField(max_length=60)

class TaskManager(models.Manager):
    def related_tasks_to_charity(self, user):
        pass

    def related_tasks_to_benefactor(self, user):
        pass

    def all_related_tasks_to_user(self, user):
        pass
