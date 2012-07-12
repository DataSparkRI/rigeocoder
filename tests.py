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
	
	def test_google_geocoder(self):
		result = geocode_address_google(self.street, self.city, self.zip_code)
		self.assertEqual(result, self.google_result)




if __name__ == '__main__':
	main()
