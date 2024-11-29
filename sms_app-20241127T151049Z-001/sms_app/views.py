from django.http import JsonResponse
from .utils import send_sms

def send_sms_view(request):
    if request.method == "POST":
        to = request.POST.get("to")
        message = request.POST.get("message")
        response = send_sms(to, message)
        return JsonResponse({"status": response})
    return JsonResponse({"error": "Invalid request method"}, status=400)

