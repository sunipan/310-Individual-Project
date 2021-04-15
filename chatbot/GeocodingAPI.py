import googlemaps
import requests
from datetime import datetime

class Geocode:
    gmaps = googlemaps.Client(key='AIzaSyCLdrdbAWFM-VBiFXLSWat82irdxRVOy8I')

    # Geocoding an address
    def convert(self, address):
        geocode_result = self.gmaps.geocode(address)
        lat = str(geocode_result[0]['geometry']['location']['lat'])
        long = str(geocode_result[0]['geometry']['location']['lng'])
        print( 'Lat: ' + lat + ' ' + 'Long: ' + long)
        return lat,long
    # Geocoding the geocode into an address
    def reverseConvert(self, lat,long):
        try:
            reverse_geocode = self.gmaps.reverse_geocode((lat, long))
            print(reverse_geocode)
            return reverse_geocode[0]['formatted_address']
        except IndexError as e:
            return "Coordinates are in the ocean, cannot give a real location"



