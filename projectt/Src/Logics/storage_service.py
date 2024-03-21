from Src.Logics.convert_factory import convert_factory
from Src.Logics.process_factory import process_factory
from Src.Logics.storage_prototype import storage_prototype
from Src.exceptions import argument_exception, exception_proxy
from datetime import datetime
import json

class storage_service:
    __data = []
    
    def __init__(self, data: list) -> None:
        if len(data) == 0:
            raise argument_exception("Некорректно переданы параметры!")
        
        self.__data = data
        self.__convert = convert_factory()
        
        
    def create_turns(self, start_period: datetime, stop_period:datetime ) -> dict:
        """
            Получить обороты за период
        Args:
            start_period (datetime): _description_
            stop_period (datetime): _description_

        Returns:
            dict: _description_
        """
        exception_proxy.validate(start_period, datetime)
        exception_proxy.validate(stop_period, datetime)
        
        if start_period > stop_period:
            raise argument_exception("Некорректно переданы параметры!")
        
        # Фильтруем      
        prototype = storage_prototype(  self.__data )  
        filter = prototype.filter( start_period, stop_period)
            
        # Подобрать процессинг    
        key_turn = process_factory.turn_key()
        processing = process_factory().create( key_turn  )
    
        # Обороты
        turns =  processing().process( filter.data )
        return turns
    
    def create_turns_nomenclature(self, nomenclature_id: str) -> dict:
        """
            Получить обороты по конкретной номенклатуре
        Args:
            nomenclature_id: int
        Returns:
            dict: _description_
        """
        exception_proxy.validate(nomenclature_id, str)

        if len(nomenclature_id) <= 0:
            raise argument_exception("Некорректно переданы параметры!")

        # Фильтруем
        prototype = storage_prototype( self.__data )
        filtred_data = prototype.filter_nomenclature( nomenclature_id )

        # Подобрать процессинг  
        key_turn = process_factory.turn_key()
        processing = process_factory().create( key_turn )

        # Обороты
        turns = processing().process( filtred_data )
        return turns
    
    def create_turns_receipes(self, storage_key: str) -> dict:
        """
            проверка возможности списания, формирования списка транзакций на списание согласно рецепту
        Args:
            nomenclature_id: int
        Returns:
            dict: _description_
        """
        exception_proxy.validate(storage_key, str)

        if len(storage_key) <= 0:
            raise argument_exception("Некорректно переданы параметры!")

        # Фильтруем
        prototype = storage_prototype( self.__data )
        filtred_data = prototype.filter_receipes( storage_key )
        filtred_data = prototype.filter( filtred_data )
        filtred_data = prototype.filter_nomenclature( filtred_data )

        # Подобрать процессинг  
        key_turn = process_factory.turn_key()
        processing = process_factory().create( key_turn )

        # Обороты
        turns = processing().process( filtred_data )
        
        return turns
    
        
    @staticmethod        
    def create_response( data: list, app):
        """"
            Сформировать данные для сервера
        """
        if app is None:
            raise argument_exception("Некорректно переданы параметры!")

        # Преоброзование
        data = convert_factory().serialize( data )
        json_text = json.dumps( data, sort_keys = True, indent = 4,  ensure_ascii = False)  
   
        # Подготовить ответ    
        result = app.response_class(
            response = f"{json_text}",
            status = 200,
            mimetype = "application/json; charset=utf-8"
        )
        
        return result