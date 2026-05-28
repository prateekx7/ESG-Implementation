from django.http import JsonResponse


def home(request):

    return JsonResponse({
        "status": "healthy",
        "service": "Breathe ESG Backend",
        "message": "Backend is running successfully"
    })