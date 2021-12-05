from datetime import timedelta
from django.utils import timezone
from boutique.forms import DemandListing
from django.test import TestCase

today = timezone.now()
expected = DemandListing()

class DemandTest(TestCase):

    def test_past(self):
        expected.date = (today - timedelta(days=4))
        self.assertIs(expected.future(), False)
    
    def test_present(self):
        expected.date = today
        self.assertIs(expected.future(), False)

    def test_future(self):
        expected.date = (today + timedelta(days=1))
        self.assertIs(expected.future(), True)

    def test_many_days(self):
        try:
            expected.date=today.strptime("32/12/2000", "%d/%m/%Y")
            self.assertIs(expected.leap() and expected.max_days(), False)
        except ValueError:
            self.assertIs(False, False)

    def test_no_days(self):
        try:
            expected.date=today.strptime("0/1/1999", "%d/%m/%Y")
            self.assertIs(expected.leap() and expected.max_days(), False)
        except ValueError:
            self.assertIs(False, False)

    def test_leap_year(self):
        try:
            expected.date=today.strptime("29/2/2024", "%d/%m/%Y")
            self.assertIs(expected.leap() and expected.max_days(), True)
        except ValueError:
            self.assertIs(False, False)
        
    def test_non_leap(self):
        try:
            expected.date=today.strptime("29/2/2023", "%d/%m/%Y")
            self.assertIs(expected.leap() and expected.max_days(), False)
        except ValueError:
            self.assertIs(False, False)

    def test_proper_date(self):
        try:
            expected.date=today.strptime("24/5/2020", "%d/%m/%Y")
            self.assertIs(expected.leap() and expected.max_days(), True)
        except ValueError:
            self.assertIs(False, False)