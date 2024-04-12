from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from ..models import Task


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
