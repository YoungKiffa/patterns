from abc import ABC, abstractmethod

class Transport(ABC):
    @abstractmethod
    def move(self):
        pass

class Car(Transport):
    def move(self):
        return 'Машина едит по дороге'

class Bicycle(Transport):
    def move(self):
        return 'Велосипед едит по дорожке'

class Plane(Transport):
    def move(self):
        return 'Самолет летит по воздуху'

class TransportFactory():
    @staticmethod
    def create_transport(transport_type: str):
        if transport_type == "car":
            return Car()
        elif transport_type == "bicycle":
            return Bicycle()
        elif transport_type == "plane":
            return Plane()
        else:
            raise ValueError(f"Неподдерживаемый тип транспорта: {transport_type}")


if __name__ == "__main__":
    transport_type = input("Введите тип транспорта (car, bicycle, plane): ")

    try:
        transport = TransportFactory.create_transport(transport_type)
        print(transport.move())
    except ValueError as e:
        print(e)