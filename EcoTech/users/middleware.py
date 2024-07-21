# users/middleware.py

from django.utils import timezone
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
import logging

logger = logging.getLogger(__name__)

class TrackUserVisitsMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)

        if request.user.is_authenticated:
            print("Entered USer authenticated")
            today = timezone.now().date()
            last_visit_date = request.COOKIES.get('last_visit_date')

            print(f"Last visit date from cookie: {last_visit_date}")
            print(f"Today's date: {today}")

            if last_visit_date != str(today):
                # Increment the global visit count
                if 'total_visits' in request.session:
                    request.session['total_visits'] += 1
                else:
                    request.session['total_visits'] = 1
            else:
                print("No update required as it has already been visited")
                request.session.save()  # Save the session changes
                # Set the cookie with the new visit date
                response.set_cookie('last_visit_date', str(today))
        else:
            print("Not logged in")
        return response
