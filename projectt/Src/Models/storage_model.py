from Src.reference import reference
from Src.exceptions import exception_proxy

#
# Модель описывает адрес склада
#
class storage_model(reference):
    " Страна "
    _country = None
    " Город "
    _city = None
    " Улица "
    _street = None
    " Дом "
    _house = None
    
    
    def __init__(self, name:str, country: reference = None, city: reference = None, 
                 street: reference = None, house: reference = None):
        
        if not country is None:
            exception_proxy.validate(country, reference)
            self._country = country
            
        if not city is None:  
            exception_proxy.validate(city, reference)  
            self._city = city

        if not street is None:  
            exception_proxy.validate(street, reference)  
            self._street = street

        if not house is None:  
            exception_proxy.validate(house, reference)  
            self._house = house
            
        super().__init__(name)
    
    @property
    def country(self):
        return self._country
    
    @country.setter
    def country(self, value: reference):
        exception_proxy.validate(value, reference)
        self._country = value    
    
    @property
    def city(self):
        return self._city
    
    @city.setter
    def city(self, value: reference):
        exception_proxy.validate(value, reference)
        self._city = value

    @property
    def street(self):
        return self._street
    
    @street.setter
    def street(self, value: reference):
        exception_proxy.validate(value, reference)
        self._street = value

    @property
    def house(self):
        return self._house
    
    @house.setter
    def house(self, value: reference):
        exception_proxy.validate(value, reference)
        self._house = value
