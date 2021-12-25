from typing import List

from object_model import ObjectModel

class Dummy:
    def dummyList(self) -> List[ObjectModel]:
        list = [
            ObjectModel(1, "Dekom", 24, "Male"),
            ObjectModel(2, "Dewa Komang", 30, "Male"),
            ObjectModel(3, "John Doe", 27, "Male"),
        ]
        return list