from services import country_services
from model import country_class

# print(country_services.CountryServices.retrieveBrazilCountryByNameRaw(None))
# print(country_services.CountryServices.retrieveBrazilCountryByNameFormated(None))
countryName   = country_services.CountryServices.retrieveBrazilName(None)
countryBrazil = country_class.Country(countryName, None )

countryBrazil.printCountry()


