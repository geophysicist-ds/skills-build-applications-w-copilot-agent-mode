
from djongo import models
from bson import ObjectId

class Team(models.Model):
    id = models.CharField(primary_key=True, editable=False, max_length=24, default=lambda: str(ObjectId()))
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)
    class Meta:
        db_table = 'teams'
    def __str__(self):
        return self.name

class User(models.Model):
    id = models.CharField(primary_key=True, editable=False, max_length=24, default=lambda: str(ObjectId()))
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    team = models.ForeignKey(Team, on_delete=models.SET_NULL, null=True, related_name='members')
    class Meta:
        db_table = 'users'
    def __str__(self):
        return self.name

class Activity(models.Model):
    id = models.CharField(primary_key=True, editable=False, max_length=24, default=lambda: str(ObjectId()))
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='activities')
    type = models.CharField(max_length=50)
    duration = models.IntegerField()  # minutes
    calories = models.IntegerField()
    date = models.DateField()
    class Meta:
        db_table = 'activities'
    def __str__(self):
        return f"{self.type} - {self.user.name}"

class Workout(models.Model):
    id = models.CharField(primary_key=True, editable=False, max_length=24, default=lambda: str(ObjectId()))
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    suggested_for = models.ManyToManyField(Team, related_name='workouts')
    class Meta:
        db_table = 'workouts'
    def __str__(self):
        return self.name

class Leaderboard(models.Model):
    id = models.CharField(primary_key=True, editable=False, max_length=24, default=lambda: str(ObjectId()))
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='leaderboard')
    points = models.IntegerField(default=0)
    class Meta:
        db_table = 'leaderboard'
    def __str__(self):
        return f"{self.team.name}: {self.points}"
