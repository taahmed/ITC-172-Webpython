from django.test import TestCase
from .models import Tracks, RecordLabels
from django.urls import reverse

# Create your tests here.
class TracksTest(TestCase):
    def test_stringOutput(self):
        track=Track(tracktitle='I can fly')
        self.assertEqual(str(resource), track.tracktitle)
    
    def test_tablename(self):
        self.assertEqual(str(Track._meta.db_table), 'track')


class RecordLabelsTest(TestCase):
    def test_stringOutput(self):
        recordlabels=RecordLabels(recordlabelstitle='Life of responsibility')
        self.assertEqual(str(recordlabels), recordlabels.recordlabelstitle)

    def test_tablename(self):
        self.assertEqual(str(RecordLabels._meta.db_table), 'recordlabels')
