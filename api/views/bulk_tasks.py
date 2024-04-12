from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from ..models import Task
from ..serializers import TaskSerializer


class BulkTasksView(APIView):
    def post(self, request):
        serializer = TaskSerializer(data=request.data, many=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DeleteTasksView(APIView):
    def post(self, request):
        task_ids = request.data.get("task_ids", [])
        if not task_ids:
            return Response(
                "No task IDs provided.", status=status.HTTP_400_BAD_REQUEST
            )
        try:
            tasks = Task.objects.filter(id__in=task_ids)
            tasks.delete()
            return Response(
                "Tasks deleted successfully.",
                status=status.HTTP_204_NO_CONTENT,
            )
        except Exception as e:
            return Response(
                str(e), status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
