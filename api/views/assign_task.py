from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from ..models import Member, Task
from ..serializers import AssignTaskSerializer


class AssignTaskView(APIView):
    def post(self, request):
        serializer = AssignTaskSerializer(data=request.data)
        if serializer.is_valid():
            task_id = serializer.validated_data["task_id"]
            assigned_to_ids = serializer.validated_data["assigned_to"]

            try:
                task = Task.objects.get(id=task_id)
            except Task.DoesNotExist:
                return Response(
                    "Task not found.", status=status.HTTP_404_NOT_FOUND
                )

            for assigned_to_id in assigned_to_ids:
                try:
                    member = Member.objects.get(id=assigned_to_id)
                    task.assigned_to.add(member)
                except Member.DoesNotExist:
                    pass

            return Response(
                "Task assigned successfully.", status=status.HTTP_200_OK
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
