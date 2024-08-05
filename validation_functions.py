# Class to validate list whit unique elements
# By Ed Scrimaglia

from typing import TypeVar
import data_model as dm

class ValidateUniqueInList():
    T = TypeVar('T')
    @classmethod
    def validate_unique_list_objects(self, lista: list[T]) -> list:
        if not lista is None:
            if isinstance(lista[0], (dm.Interface, dm.Vlan)):
                new_list = {str(d.model_dump()):d for d in lista}
            elif isinstance(lista[0], (int, str, float)):
                new_list = set(lista)
            elif isinstance(lista[0], dict):
                new_list = {str(d):d for d in lista}
            if len(new_list) != len(lista):
                    raise ValueError(f"list of {lista[0].__class__.__name__} has not unique objects")
        return lista
    