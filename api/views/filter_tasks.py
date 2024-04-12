from datetime import datetime

from django.utils import timezone
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


class TaskFilterByDateView(APIView):
    def get(self, request):
        keyword = request.query_params.get("keyword", "")
        start_date_str = request.query_params.get("startDate", "")
        end_date_str = request.query_params.get("endDate", "")

        if not keyword:
            return Response(
                "No keyword provided.", status=status.HTTP_400_BAD_REQUEST
            )

        try:
            start_date = (
                datetime.strptime(start_date_str, "%Y-%m-%d").date()
                if start_date_str
                else None
            )
            end_date = (
                datetime.strptime(end_date_str, "%Y-%m-%d").date()
                if end_date_str
                else None
            )
        except ValueError:
            return Response(
                "Invalid date format. Please provide dates in YYYY-MM-DD format.",
                status=status.HTTP_400_BAD_REQUEST,
            )

        tasks = Task.objects.filter(description__icontains=keyword)
        if start_date:
            tasks = tasks.filter(created_at__date__gte=start_date)
        if end_date:
            tasks = tasks.filter(
                created_at__date__lte=end_date + timezone.timedelta(days=1)
            )

        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)
