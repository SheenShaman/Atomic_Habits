from rest_framework import serializers

from habits.models import Habit


class HabitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Habit
        fields = '__all__'

    def validate(self, data):
        associated_habit = data.get('associated_habit')
        reward = data.get('reward')
        is_pleasant_habit = data.get('is_pleasant_habit')
        time_to_completed = data.get('time_to_completed')
        frequency = data.get('frequency')

        if associated_habit and reward:
            raise serializers.ValidationError('Нельзя выбирать связанную привычку и награду вместе!')

        if time_to_completed > 120:
            raise serializers.ValidationError('Время выполнения должно быть не больше 120 секунд!')

        if associated_habit and not associated_habit.is_pleasant_habit:
            raise serializers.ValidationError('Связанными привычками должны быть приятные привычки!')

        if is_pleasant_habit:
            if associated_habit or reward:
                raise serializers.ValidationError('У приятной привычки не может быть связанной привычки или награды!')

        if frequency < 7:
            raise serializers.ValidationError('Нельзя выполнять привычки реже одного раза в 7 дней!')

        return data
