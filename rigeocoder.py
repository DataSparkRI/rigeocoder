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
    results = []
    try:
        json_data = json.loads(raw_data.read())

        if 'candidates' in json_data: #address was geocoded
            if json_data['candidates']:
                for cand in json_data['candidates']:
                    if cand['score'] >= 85:
                        results.append({'address':cand['address'],
                                        'lat':cand['location']['y'],
                                        "lng":cand['location']['x']})
            return results

    except ValueError:
        pass

    return results

def geocode_address_google(street, city, zip_code=''):
    address = "%s %s %s" % (street, city, zip_code)
    results = []
    google = geocoders.GoogleV3()
    try:
        place, geocode = google.geocode(address)
        results.append({'address':place,
                        'lat':geocode[0],
                        'lng':geocode[1]
                        })
    except Exception as e:
        # Found more than one
        for r in google.doc['results']:
            d = r['geometry']['location'].copy()
            d['address'] = r['formatted_address']
            results.append(d)

    return results

def geocode_address_dotus(street, city, zip_code='', state=None):
    """ NOTE: This geocoder is particular about having a state"""
    if state:
        state = ", " + state
    else:
        state = ""
    address = "%s,  %s, %s" % (street, city, state)
    us = geocoders.GeocoderDotUS()
    results = []
    try:
        place, (lat, lng) = us.geocode(address)
        results.append({'address':place,
                        'lat':lat,
                        'lng':lng})
    except Exception as e:
        pass

    return results

def geocode_address(street, city, zip_code=''):
	result = geocode_address_uri(street, city, zip_code)

	# try dotus if it fails
	if result == None:
		result = geocode_address_dotus(street, city, zip_code)

	return result



