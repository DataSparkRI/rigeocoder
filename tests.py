#!/usr/bin/python

from unittest import TestCase, main
from rigeocoder import *

class test_rigeocoder(TestCase):
	def setUp(self):
		self.street = "82 Smith Street"
		self.city = "Providence"
		self.zip_code = "02903"

	def test_uri_geocoder(self):
		result = gecode_address_uri(self.street, self.city, self.zip_code)
		
		print result

		self.assertEqual(1,1)

if __name__ == '__main__':
	main()
