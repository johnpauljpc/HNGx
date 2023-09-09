from datetime import datetime
from django.http import JsonResponse
from rest_framework.views import APIView

class InfoAPIView(APIView):
    def get(self, request):
        # Get query parameters from the request
        slack_name = request.GET.get('slack_name')
        track = request.GET.get('track')

        if not slack_name or not track:
            return JsonResponse({'error': 'Missing parameters'}, status=400)

        # Get the current day of the week
        current_day_of_week = datetime.utcnow().strftime('%A')

        # Get the current UTC time
        current_utc_time = datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%SZ')

        # Define GitHub repository information
        github_repo_url = "https://github.com/johnpauljpc/hngx_task1"
        github_file_url = "https://github.com/johnpauljpc/hngx_task1/blob/main/api/views.py"

        # Create the response JSON
        response_data = {
            'slack_name': slack_name,
            'current_day': current_day_of_week,
            'utc_time': current_utc_time,
            'track': track,
            'github_file_url': github_file_url,
            'github_repo_url': github_repo_url,
            'status_code': 200
        }

        return JsonResponse(response_data, status=200)
