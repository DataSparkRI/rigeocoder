import urllib
import json
from geopy import geocoders

base_url = 'http://maps.edc.uri.edu/ArcGIS/rest/services/Atlas_location/address_locator/GeocodeServer/findAddressCandidates'
wkid = '4269' #GCS_North_American_1983
out_form = 'json'

def geocode_address_uri(street, city, zip_code = ''):
    urllib.quote_plus(street)
    urllib.quote_plus(city)
    req_url = "%s?Street=%s&City=%s&ZIP=%s&outSR=%s&f=%s" % (base_url, street, city, zip_code, wkid, out_form)
    raw_data = urllib.urlopen(req_url)
    json_data = json.loads(raw_data.read())
    results = []
    if 'candidates' in json_data: #address was geocoded
        if json_data['candidates']:
            for cand in json_data['candidates']:
                if float(cand['score']) > 80:
                    results.append((cand['address'], (cand['location']['y'], cand['location']['x'])))
            return results

	return None

def geocode_address_google(street, city, zip_code=''):
	address = "%s %s %s" % (street, city, zip_code)
	try:
		google = geocoders.Google()
		geocode = google.geocode(address)
		place, (lat,lng) = geocode
		return (lat,lng)
	except Exception:
		return None

def geocode_address_dotus(street, city, zip_code=''):
    address = "%s %s, %s" % (street, city, zip_code)
    try:
        us = geocoders.GeocoderDotUS()
        return list(us.geocode(address, exactly_one=False))
    except Exception:
        return None

def geocode_address(street, city, zip_code=''):
	result = geocode_address_uri(street, city, zip_code)

	# try dotus if it fails
	if result == None:
		result = geocode_address_dotus(street, city, zip_code)

	return result



