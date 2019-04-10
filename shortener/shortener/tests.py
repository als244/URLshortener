from django.test import TestCase


# TODO: Add more validation to these tests.
class Tests(TestCase):

    def test_shorten(self):
        response = self.client.post('/shorten/')
        assert response.status_code == 200

    def test_recent(self):
        response = self.client.get('/recent/')
        assert response.status_code == 200

    def test_top(self):
        response = self.client.get('/top/')
        assert response.status_code == 200

    def test_count(self):
        response = self.client.get('/count/')
        assert response.status_code == 200
