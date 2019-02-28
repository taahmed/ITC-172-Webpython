from django.test import TestCase
from .models import Resource, Meeting 
from django.urls import reverse

# Create your tests here.
class ResourceTest(TestCase):
    def test_stringOutput(self):
        resource=Resource(resourcename='lenovo')
        self.assertEqual(str(resource), resource.resourcename)
    
    def test_tablename(self):
        self.assertEqual(str(Resource._meta.db_table), 'resource')


class MeetingTest(TestCase):
    def test_stringOutput(self):
        meeting=Meeting(meetingtitle='Salary Increment')
        self.assertEqual(str(meeting), meeting.meetingtitle)

    def test_tablename(self):
        self.assertEqual(str(Meeting._meta.db_table), 'meeting')



