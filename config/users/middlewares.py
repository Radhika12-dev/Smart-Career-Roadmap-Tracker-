import time
from django.http import JsonResponse
from collections import defaultdict

class RateLimitMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self.visitors = defaultdict(list)

    def __call__(self, request):
        #Get user IP Address
        user_ip = request.META.get("REMOTE_ADDR")
        current_time = time.time()

        #Max request allowed within time window
        time_window = 60
        limit = 100

        #Remove old timestamps that are outside tme window
        self.visitors[user_ip] = [timestamp for timestamp in self.visitors[user_ip] if current_time-timestamp < time_window]

        #Check if number of request exceed 
        if len(self.visitors[user_ip]) >= limit:
            return JsonResponse({"error": "Rate Limit Exceeded. Try Again Later"}, status = 429)
        
        #Add current timestamp to user
        self.visitors[user_ip].append(current_time)

        #Proceed to nexr middleware or view
        return self.get_response(request)
