from django.test import TestCase
from .forms import CalendarWidget
# Create your tests here.
class setUp(TestCase):
    def form(self):
        a = CalendarWidget()
        print(a.media, 'sssssss')
