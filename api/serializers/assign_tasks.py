from rest_framework import serializers


class AssignTaskSerializer(serializers.Serializer):
    task_id = serializers.IntegerField()
    assigned_to = serializers.ListField(child=serializers.IntegerField())
