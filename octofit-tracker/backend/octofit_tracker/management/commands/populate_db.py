from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        # Delete existing data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Create teams
        marvel = Team.objects.create(name='marvel')
        dc = Team.objects.create(name='dc')

        # Create users
        ironman = User.objects.create(email='ironman@marvel.com', name='Iron Man', team='marvel', is_superhero=True)
        captain = User.objects.create(email='captain@marvel.com', name='Captain America', team='marvel', is_superhero=True)
        batman = User.objects.create(email='batman@dc.com', name='Batman', team='dc', is_superhero=True)
        superman = User.objects.create(email='superman@dc.com', name='Superman', team='dc', is_superhero=True)

        # Create activities
        Activity.objects.create(user=ironman, type='run', duration=30, date='2026-03-19')
        Activity.objects.create(user=batman, type='cycle', duration=45, date='2026-03-19')

        # Create leaderboard
        Leaderboard.objects.create(team=marvel, points=150)
        Leaderboard.objects.create(team=dc, points=120)

        # Create workouts
        Workout.objects.create(name='Pushups', description='Do pushups', suggested_for='marvel')
        Workout.objects.create(name='Situps', description='Do situps', suggested_for='dc')

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data'))
