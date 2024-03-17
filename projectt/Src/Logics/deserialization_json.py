from Src.Logics.basic_convertor import basic_convertor
from Src.Logics.datetime_convertor import datetime_convertor
from Src.Logics.convert_factory import convert_factory
from Src.Logics.convert_factory import reference_convertor
from Src.exceptions import exception_proxy, operation_exception
from Src.reference import reference
import datetime
        
#
# Десериализация json
#
class deserialization_json:

    # Код взят: https://stackoverflow.com/questions/15476983/deserialize-a-json-string-to-an-object-in-python
    
    def from_json(self, data, cls):
        annotations = cls.__annotations__ if hasattr(cls, '__annotations__') else None
        if issubclass(cls, list):
            list_type = cls.__args__[0]
            instance = []
            for value in data:
                instance.append(self.from_json(value, list_type))
            return instance
        elif issubclass(cls, dict):
            key_type = cls.__args__[0]
            val_type = cls.__args__[1]
            instance = {}
            for key, value in data.items():
                instance.update({self.from_json(key, key_type): self.from_json(value, val_type)})
            return instance
        else:
            instance = cls()
            for name, value in data.items():
                field_type = annotations.get(name)
                if isinstance(field_type, type) and isinstance(value, dict):
                    setattr(instance, name, self.from_json(value, field_type))
                else:
                    setattr(instance, name, value)
            return instance

