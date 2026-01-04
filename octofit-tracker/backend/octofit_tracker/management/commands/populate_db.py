from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Workout, Leaderboard
from datetime import date

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Drop collections directly using Djongo's raw connection
        from django.db import connection
        db = connection.cursor().db_conn
        for coll in ['users', 'teams', 'activities', 'workouts', 'leaderboard']:
            if coll in db.list_collection_names():
                db.drop_collection(coll)

        # Create teams
        marvel = Team.objects.create(name='Marvel', description='Marvel Superheroes')
        dc = Team.objects.create(name='DC', description='DC Superheroes')

        # Create users
        users = [
            User.objects.create(name='Iron Man', email='ironman@marvel.com', team=marvel),
            User.objects.create(name='Captain America', email='cap@marvel.com', team=marvel),
            User.objects.create(name='Spider-Man', email='spiderman@marvel.com', team=marvel),
            User.objects.create(name='Superman', email='superman@dc.com', team=dc),
            User.objects.create(name='Batman', email='batman@dc.com', team=dc),
            User.objects.create(name='Wonder Woman', email='wonderwoman@dc.com', team=dc),
        ]

        # Create activities
        Activity.objects.create(user=users[0], type='Running', duration=30, calories=300, date=date.today())
        Activity.objects.create(user=users[1], type='Cycling', duration=45, calories=400, date=date.today())
        Activity.objects.create(user=users[3], type='Swimming', duration=60, calories=500, date=date.today())

        # Create workouts
        cardio = Workout.objects.create(name='Cardio Blast', description='High intensity cardio workout')
        strength = Workout.objects.create(name='Strength Training', description='Build muscle strength')
        cardio.suggested_for.add(marvel, dc)
        strength.suggested_for.add(dc)

        # Create leaderboard
        Leaderboard.objects.create(team=marvel, points=250)
        Leaderboard.objects.create(team=dc, points=300)

        self.stdout.write(self.style.SUCCESS('Test data populated successfully!'))
