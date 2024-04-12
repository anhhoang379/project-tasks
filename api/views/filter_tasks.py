from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from ..models import Task
from ..serializers import TaskSerializer


class TaskFilterByKeywordView(APIView):
    def get(self, request):
        keyword = request.query_params.get("keyword", "")
        if not keyword:
            return Response(
                "No keyword provided.", status=status.HTTP_400_BAD_REQUEST
            )
        tasks = Task.objects.filter(description__icontains=keyword)
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)
