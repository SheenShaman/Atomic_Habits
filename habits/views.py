from rest_framework import viewsets

from habits.models import Habit
from habits.serializers import HabitSerializer
from habits.permissions import IsOwnerOrReadOnly, CanReadPublicHabits


class HabitViewSet(viewsets.ModelViewSet):
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    permission_classes = [IsOwnerOrReadOnly]
    # pagination_class =

    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)


class PublicHabitViewSet(viewsets.ModelViewSet):
    serializer_class = HabitSerializer
    queryset = Habit.objects.filter(is_public=True)
    permission_classes = [CanReadPublicHabits]
