class Animal:
    """Базовый класс для всех животных"""

    def __init__(self, name: str, age: int):
        """Инициализация атрибутов животного

        :param name: Имя животного
        :param age: Возраст животного в годах
        """
        self.__name = name
        self.__age = age

    def __str__(self) -> str:
        """Возвращает строковое представление животного"""
        return f"Животное: {self.__name}, возраст: {self.__age} лет"

    def __repr__(self) -> str:
        """Возвращает формальное строковое представление животного"""
        return f"Animal(name='{self.__name}', age={self.__age})"

    def make_sound(self) -> str:
        """Возвращает звук, который издает животное (общий для всех животных)"""
        return "Звук животного"


class Dog(Animal):
    """Класс Собака, наследующий от класса Животное"""

    def __init__(self, name: str, age: int, breed: str):
        """Инициализация атрибутов собаки, расширенного по сравнению с животным

        :param name: Имя собаки
        :param age: Возраст собаки в годах
        :param breed: Порода собаки
        """
        super().__init__(name, age)
        self.__breed = breed

    def __str__(self) -> str:
        """Возвращает строковое представление собаки"""
        return f"Собака: {self._Animal__name}, возраст: {self._Animal__age} лет, порода: {self.__breed}"

    def __repr__(self) -> str:
        """Возвращает формальное строковое представление собаки"""
        return f"Dog(name='{self._Animal__name}', age={self._Animal__age}, breed='{self.__breed}')"

    def make_sound(self) -> str:
        """Возвращает звук, который издает собака (перегрузка метода)"""
        return "Гав!"

