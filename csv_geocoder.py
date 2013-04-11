#!/usr/bin/env python
# encoding: utf-8

import csv
import rigeocoder
import sys

def main(path_to_csv, path_to_outcsv):
    try:
        outfile = open(path_to_outcsv, 'wb')
        outcsv = csv.writer(outfile)
        with open(path_to_csv, 'rb') as file:
            reader = csv.reader(file)
            header = reader.next()
            outcsv.writerow(['street','city','state','linkid2', 'lat','lng'])
           # count = 0
            for row in reader:
                #count +=1
                #if count > 5:
                #    break
                street1 = row[0]
                street2 = row[1]
                city2 = row[3]
                state = row[4]
                linkid2=row[5]
                street_used = ''

                # try the first combination then try with street1
                print 'Tryin first geocoder with address: ' + street1
                geo = rigeocoder.geocode_address(street1, city2)
                if geo != None:
                    lat, lng = geo
                    street_used = street1
                else:
                    # try the second combo
                    print 'Tryin first geocoder with address: ' + street2
                    geo = rigeocoder.geocode_address(street2, city2)
                    if geo != None:
                        lat, lng = geo
                        street_used=street2
                    else:
                        # try google!
                        print 'Tryin google geocoder with address: ' + street1
                        geo = rigeocoder.geocode_address_google(street1, city2)
                        if geo != None:
                            lat, lng = geo
                            street_used=street1
                        else:
                            # try the second address
                            print 'Tryin google geocoder with address: ' + street2
                            geo = rigeocoder.geocode_address_google(street2, city2)
                            if geo != None:
                                lat, lng = geo
                                street_used=street2
                            else:
                                street_used = street1
                                print street_used, city2 , linkid2, " Failed to geocode"
                                lat = 0
                                lng = 0

                #output row
                out = [street_used, city2, state, linkid2, lat, lng]
                outcsv.writerow(out)
    finally:
        outfile.close()





if __name__ == '__main__':
    #print sys.argv[1]
    main(sys.argv[1], sys.argv[2])

