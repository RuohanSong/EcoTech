import datetime
from django.utils.deprecation import MiddlewareMixin

class VisitMiddleware(MiddlewareMixin):
    def process_request(self, request):
        now = datetime.datetime.now()
        current_date = now.strftime('%Y-%m-%d')
        print(f'Processing request on {current_date}')

        # Check if the visit has already been counted for today
        if 'visit_counted' not in request.session or request.session['visit_counted_date'] != current_date:
            request.session['visit_counted'] = True
            request.session['visit_counted_date'] = current_date
            if 'daily_visits' in request.session:
                request.session['daily_visits'] += 1
            else:
                request.session['daily_visits'] = 1

        request.session['last_visit_date'] = current_date

    def process_response(self, request, response):
        # Set cookies for last visit date and daily visits
        response.set_cookie('last_visit_date', request.session.get('last_visit_date'), max_age=60 * 60 * 24)
        response.set_cookie('daily_visits', request.session.get('daily_visits'), max_age=60 * 60 * 24)
        return response
