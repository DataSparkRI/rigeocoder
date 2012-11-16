from unittest import TestCase, main
from rigeocoder import *

class test_rigeocoder(TestCase):

    def setUp(self):
        self.street = "82 Smith Street"
        self.city = "Providence"
        self.zip_code = "02903"
        self.uri_result = (41.83109770000004, -71.41494403299998)
        self.google_result = (41.831568, -71.414824)

    def test_uri_geocoder(self):
        result = geocode_address_uri(self.street, self.city, self.zip_code)
        self.assertEqual(result,self.uri_result)

    def test_uri_geocoder_fail(self):
        result = geocode_address_uri(self.street, "Nebraska", self.zip_code)
        self.assertEqual(result, None)

    def test_google_geocoder(self):
        result = geocode_address_google(self.street, self.city, self.zip_code)
        self.assertEqual(result, self.google_result)

    def test_dotus_geocoder(self):
        result = geocode_address_dotus("1600 Pennsylvania Ave","Washington DC")
        # this will return None :( so for now just test that we dont crash
        self.assertEqual(result,(38.898748, -77.037684))

    def test_full_geocoder(self):
        """ This test should return the uri results"""
        result = geocode_address(self.street, self.city, self.zip_code)
        self.assertEqual(result, self.uri_result)

    def test_full_geocoder_geous_backup(self):
        """
            This test should return the some results results cause the address is not in RI
        """
        result = geocode_address("1600 Pennsylvania Ave","Washington DC")
        self.assertEqual(result,(38.898748, -77.037684))



if __name__ == '__main__':
	main()
