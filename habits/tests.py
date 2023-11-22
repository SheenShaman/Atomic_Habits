from rest_framework import status

from habits.models import Habit

from django.contrib.auth import get_user_model
from django.test import TestCase

from rest_framework.test import APIClient

User = get_user_model()


class HabitModelTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create(email='test@user.com', is_active=True, password='123')
        self.client.force_authenticate(user=self.user)
        self.user.set_password('123')
        self.user.save()

        self.habit = Habit.objects.create(
            user=self.user, place="Кухня", time="08:00:00", action="Выпить стакан воды",
            is_pleasant_habit=False, frequency=7, reward="Позавтракать", time_to_completed=60, is_public=True
        )

    def test_create_habit(self):
        data = {
            "user": self.user.id,
            "action": "Выпить стакан воды",
            "is_pleasant_habit": False,
            "frequency": 7,
            "reward": "Позавтракать",
            "time_to_completed": 120
        }
        response = self.client.post('/habits/', data=data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_user_field(self):
        self.assertEqual(self.habit.user, self.user)

    def test_place_field(self):
        self.assertEqual(self.habit.place, "Кухня")

    def test_time_field(self):
        self.assertEqual(self.habit.time, "08:00:00")

    def test_action_field(self):
        self.assertEqual(self.habit.action, "Выпить стакан воды")

    def test_is_pleasant_habit_field(self):
        habit = Habit.objects.create(
            user=self.user,
            action="Выпить стакан воды",
            is_pleasant_habit=True,
            frequency=7,
            time_to_completed=60,
            is_public=False,
        )
        self.assertTrue(habit.is_pleasant_habit)

    def test_related_habit_field(self):
        habit1 = Habit.objects.create(
            user=self.user,
            action="Медитировать",
            is_pleasant_habit=True,
            frequency=7,
            time_to_completed=120,
            is_public=False,
        )
        habit2 = Habit.objects.create(
            user=self.user,
            action="Выпить стакан воды",
            is_pleasant_habit=False,
            associated_habit=habit1,
            frequency=7,
            time_to_completed=60,
            is_public=False,
        )
        self.assertEqual(habit2.associated_habit, habit1)

    def test_frequency_field(self):
        self.assertEqual(self.habit.frequency, 7)

    def test_reward_field(self):
        self.assertEqual(self.habit.reward, "Позавтракать")

    def test_time_to_completed_field(self):
        self.assertEqual(self.habit.time_to_completed, 60)

    def test_is_public_field(self):
        self.assertTrue(self.habit.is_public)
