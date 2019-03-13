from django.test import TestCase
from .models import Resource, Meeting, MeetingMinutes, Event
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

class MeetingMinutesTest(TestCase):
    def test_stringOutput(self):
        minutes=MeetingMinutes(minutestext='More Tests')
        self.assertEqual(str(minutes), minutes.minutestext)

    def test_tablename(self):
        self.assertEqual(str(MeetingMinutes._meta.db_table), 'meetingminutes')

class EventTest(TestCase):
    def test_stringOutput(self):
        event=Event(eventtitle='Salary Increment')
        self.assertEqual(str(event), event.eventtitle)

    def test_tablename(self):
        self.assertEqual(str(Event._meta.db_table), 'event')