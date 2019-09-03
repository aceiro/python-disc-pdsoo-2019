from services.country_services import *
from model.country_class import *

# print(country_services.CountryServices.retrieveBrazilCountryByNameRaw(None))
# print(country_services.CountryServices.retrieveBrazilCountryByNameFormated(None))
services = CountryServices
countryName   = services.retrieveBrazilName(None)
countryBrazil = Country(countryName, None )

countryBrazil.printCountry()


