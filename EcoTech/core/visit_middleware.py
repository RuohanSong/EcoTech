# core/visit_middleware.py
import datetime
from django.utils.deprecation import MiddlewareMixin

class VisitMiddleware(MiddlewareMixin):
    def process_request(self, request):
        now = datetime.datetime.now()
        current_date = now.strftime('%Y-%m-%d')
        print(f'Processing request at {now}')

        if 'visit_counted' not in request.session:
            request.session['visit_counted'] = True
            # request.session['total_visits'] = request.session.get('total_visits', 0) + 1
            # print(f"New session visit counted: total_visits={request.session['total_visits']}")

        # Initialize daily visits counter based on cookies
        last_visit_date = request.COOKIES.get('last_visit_date')
        if last_visit_date != current_date:
            request.session['daily_visits'] = 1
        else:
            request.session['daily_visits'] = request.session.get('daily_visits', 0) + 1

        request.session['last_visit_date'] = current_date

        # print(f"Session visits updated: total_visits={request.session['total_visits']}, daily_visits={request.session['daily_visits']}")

    def process_response(self, request, response):
        # Set cookies for last visit date, daily visits, and total visits
        response.set_cookie('last_visit_date', request.session.get('last_visit_date'))
        response.set_cookie('daily_visits', request.session.get('daily_visits', 0))
        # response.set_cookie('total_visits', request.session.get('total_visits', 0))
        return response
