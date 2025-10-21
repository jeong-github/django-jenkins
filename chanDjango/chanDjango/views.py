from django.shortcuts import render
from rest_framework.views import APIView
from django.db import connections
from django.db.utils import OperationalError

# Optionally import your models if you want to check data too
# from content.models import Feed

class Main(APIView):
    def get(self, request):
        # Check if the database is connected
        try:
            with connections['default'].cursor() as cursor:
                cursor.execute('SELECT 1')
            db_status = 'Database is connected.'
        except OperationalError:
            db_status = 'Database connection failed.'

        # Pass the db_status to the template
        return render(request, 'chanDjango/main.html', {'db_status': db_status})


#class Main(APIView):
#    def get(self, request):
#        return render(request, 'chanDjango/main.html')

#class Main(APIView):
#    def get(self, request):
#        feed_list = Feed.objects.all()
#        return render(request, 'chanDjango/main.html', context=dict(feed_list=feed_list))

