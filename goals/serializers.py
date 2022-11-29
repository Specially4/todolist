from rest_framework import serializers

from core.serializers import RetrieveUserSerializer
from goals.models import GoalCategory, Goal


class GoalCreateSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Goal
        read_only_fields = ("id", "created", "updated", "user")
        fields = "__all__"


class GoalSerializer(serializers.ModelSerializer):
    user = RetrieveUserSerializer(read_only=True)

    class Meta:
        model = Goal
        fields = "__all__"
        read_only_fields = ("id", "created", "updated", "user")


class GoalCategorySerializer(serializers.ModelSerializer):
    user = RetrieveUserSerializer(read_only=True)

    class Meta:
        model = GoalCategory
        fields = "__all__"
        read_only_fields = ("id", "created", "updated", "user")

    def validate_category(self, value):
        if value.is_deleted:
            raise serializers.ValidationError('not allowed in deleted category')
        if value.user != self.context['request'].user:
            raise serializers.ValidationError('not owner of category')

        return value
