from unittest import TestCase, main
from rigeocoder import *

class test_rigeocoder(TestCase):

    def setUp(self):

        self.street = "82 Smith Street"
        self.city = "Providence"
        self.zip_code = "02903"

    def test_uri_geocoder(self):
        result = geocode_address_uri(self.street, self.city, self.zip_code)
        self.assertEqual(result,
                         [{'lat': 41.83109769968133, 'lng': -71.41494403284543, 'address': u'82 SMITH ST, PROVIDENCE 02908'}, {'lat': 41.84791036607282, 'lng': -71.45576688783409, 'address': u'82 SMITH ST, PROVIDENCE 02911'}])


    def test_uri_geocoder_fail(self):
        result = geocode_address_uri(self.street, "Nebraska", self.zip_code)
        self.assertEqual(result, [])

    def test_google_geocoder(self):
        result = geocode_address_google(self.street, self.city, self.zip_code)
        self.assertEqual(result, [{u'lat': 41.831098,
                                   u'lng': -71.41494399999999,
                                   'address': u'82 Smith Street, Providence, RI 02903, USA'}])

    def test_dotus_geocoder(self):
        result = geocode_address_dotus(self.street, self.city, self.zip_code, "RI")
        self.assertEqual(result,
            [{'lat': 41.8312, 'lng': -71.413701, 'address': u'82 Smith St, Providence, RI 02908'}])

    def test_full_geocoder(self):
        """ This test should return the uri results"""
        result = geocode_address(self.street, self.city, self.zip_code)
        self.assertEqual(result,
                         [{'lat': 41.83109769968133, 'lng': -71.41494403284543, 'address': u'82 SMITH ST, PROVIDENCE 02908'}, {'lat': 41.84791036607282, 'lng': -71.45576688783409, 'address': u'82 SMITH ST, PROVIDENCE 02911'}])

    def test_outofstate(self):
        result = geocode_address("414 Grant Street","Pittsburgh", "PA")


if __name__ == '__main__':
	main()
