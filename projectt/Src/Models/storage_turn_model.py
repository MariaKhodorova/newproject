from Src.Models.storage_model import storage_model
from Src.reference import reference
from Src.Models.unit_model import unit_model
from Src.Logics.datetime_convertor import datetime_convertor
from Src.exceptions import exception_proxy
from Src.Models.nomenclature_model import nomenclature_model

#
# Модель описывающая складской оборот
#
class storage_turn_model(reference):
    __storage: storage_model = None
    __turnover: int = 0     # оборот
    __nomenclature: nomenclature_model = None 
    __unit: unit_model = None

    def __init__(self, _storage: storage_model, _nomenclature: nomenclature_model, _unit: unit_model, _turnover: int):

        exception_proxy.validate(_storage, reference)
        exception_proxy.validate(_nomenclature, reference)
        exception_proxy.validate(_unit, reference)
         
        self.__storage = _storage
        self.__nomenclature = _nomenclature
        self.__unit = _unit
        self.__turnover = _turnover
        
        super().__init__( f"{_storage.name}, {_nomenclature.name} , {_unit.name}, {_turnover.name} ")
    
    @property
    def storage(self):
        """
            Склад
        Returns:
            _type_: _description_
        """
        return self.__storage
    
    
    @property
    def nomenclature(self):
        """
            Номенклатура
        Returns:
            _type_: _description_
        """
        return self.__nomenclature
    
    @property    
    def unit(self):
        """
           Единица измерения

        Returns:
            _type_: _description_
        """
        return self.__unit  
    
    @property    
    def turnover(self):
        """
           действие: True или False

        Returns:
            _type_: _description_
        """
        return self.__turnover 
    
    @turnover.setter
    def turnover(self, value: int):
        self.__turnover = value
    