import http.client
from utility import constants
from model import country_class
import json

class CountryServices:
   country = country_class.Country
   def retrieveBrazilCountryByNameRaw(self):
        conn = http.client.HTTPSConnection("restcountries-v1.p.rapidapi.com")
        conn.request("GET", "/name/brazil", headers=constants.headers)
        res = conn.getresponse()
        data = res.read()
        print(data.decode("utf-8"))


   def retrieveBrazilCountryByNameFormated(self):
        conn = http.client.HTTPSConnection("restcountries-v1.p.rapidapi.com")
        conn.request("GET", "/name/brazil", headers=constants.headers)
        res = conn.getresponse()
        data = res.read()
        raw_data = (json.loads(str(data.decode("utf-8"))))
        print(json.dumps(raw_data, indent=4, sort_keys=True))

   def retrieveBrazilName(self):
        conn = http.client.HTTPSConnection("restcountries-v1.p.rapidapi.com")
        conn.request("GET", "/name/brazil", headers=constants.headers)
        res = conn.getresponse()
        data = res.read()
        raw_data = (json.loads(str(data.decode("utf-8"))))
        names = raw_data[0]['name']
        return "".join([ n for n in names if n!=None])


   def createCountry(self, aCountry):
      self.country = aCountry



        


