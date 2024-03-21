from Src.Models.storage_model import storage_model
from Src.reference import reference
from Src.Models.unit_model import unit_model
from Src.Logics.datetime_convertor import datetime_convertor
from Src.exceptions import exception_proxy
from Src.Models.nomenclature_model import nomenclature_model

#
# Класс описание одной записи складского журнала
#
class storage_row_model(reference):
    __storage: storage_model = None
    __nomenclature: nomenclature_model = None 
    __unit: unit_model = None
    __action: bool = False
    __count: int = 0
    __period: datetime_convertor

    def __init__(self, _storage: storage_model, _nomenclature: nomenclature_model, _unit: unit_model,
                  _action: bool, _count: int, _period: datetime_convertor):

        exception_proxy.validate(_storage, reference)
        exception_proxy.validate(_nomenclature, reference)
        exception_proxy.validate(_unit, reference)
        exception_proxy.validate(_period, reference)
         
        self.__storage = _storage
        self.__nomenclature = _nomenclature
        self.__unit = _unit
        self.__action = _action
        self.__count = _count
        self.__period = _period
        
        super().__init__( f"{_storage.name}, {_nomenclature.name} , {_unit.name}, {_action.name}, 
                         {_count.name}, {_period.name}")
    
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
    def action(self):
        """
           действие: True или False

        Returns:
            _type_: _description_
        """
        return self.__action 
    
    @action.setter
    def action(self, value: bool):
        self.__action = value
    
    @property    
    def count(self):
        """
           Количество

        Returns:
            _type_: _description_
        """
        return self.__count
    
    @count.setter
    def count(self, value: int):
        self.__count = value
    
    @property    
    def period(self):
        """
           Дата

        Returns:
            _type_: _description_
        """
        return self.__period
    




