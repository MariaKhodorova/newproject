from Src.Models.storage_turn_model import storage_turn_model
from Src.Models.storage_row_model import storage_row_model
from Src.reference import reference
from Src.exceptions import exception_proxy, operation_exception
from Src.Logics.basic_convertor import basic_convertor
from Src.Logics.datetime_convertor import datetime_convertor
from Src.Logics.start_factory import start_factory
import datetime

#
# расчет оборотов
#
class process_storage_turn(storage_row_model):
    def calculate(self, field: str, object: reference) -> dict:

        super().calculate(field, object)
        
        factory = process_factory()
        return factory.calculate(object)


#
# Фабрика процессов
#
class process_factory:
    _maps = {}
    
    def __init__(self) -> None:
        # Связка с простыми типами
        self._maps[datetime] = datetime_convertor
        self._maps[int] = basic_convertor
        self._maps[str] = basic_convertor
        self._maps[bool] = basic_convertor
        self._turnover[int] = 0
    
        
        # Связка для всех моделей
        for  inheritor in reference.__subclasses__():
            self._maps[inheritor] = process_storage_turn

    def calculate(create_journal, process_turn_key) -> process_storage_turn:

        _turnover = 0
    

        
    

