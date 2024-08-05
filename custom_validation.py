# Class to validate lists whit unique elements
# By Ed Scrimaglia

from typing import Any

class ValidateUniqueInList():
    @classmethod
    def validate_unique_list_objects(cls, lista: list[Any]) -> list:
        if not lista is None:        
            unique_list = []
            for ele in lista:
                if ele in unique_list:
                    raise ValueError(f"list of {lista[0].__class__.__name__} has not unique objects")
                unique_list.append(ele)
        return lista
    