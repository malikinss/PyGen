'''
TODO:
    Using inheritance and the diagram below, build a hierarchy of empty
    classes that describe vehicles:

        Vehicle
        |-- LandVehicle
        |   |-- Car
        |   |-- Motorcycle
        |   |__ Bicycle
        |
        |-- WaterVehicle
        |__ AirVehicle
            |-- Propeller
            |__ Jet
'''


class Vehicle:
    """
    Base class for all vehicles.

    This class serves as the root of the vehicle hierarchy, encompassing all
    types of vehicles including land, water, and air vehicles.
    """
    pass


class LandVehicle(Vehicle):
    """
    Base class for vehicles that operate on land.

    Inherits from Vehicle and serves as the parent class for land-based
    vehicles such as cars, motorcycles, and bicycles.
    """
    pass


class WaterVehicle(Vehicle):
    """
    Base class for vehicles that operate on water.

    Inherits from Vehicle and represents water-based vehicles such as boats
    and ships.
    """
    pass


class AirVehicle(Vehicle):
    """
    Base class for vehicles that operate in the air.

    Inherits from Vehicle and serves as the parent class for air-based
    vehicles such as propeller planes and jets.
    """
    pass


class Car(LandVehicle):
    """
    Class representing a car.

    Inherits from LandVehicle and represents a four-wheeled motor vehicle
    designed for road travel.
    """
    pass


class Motorcycle(LandVehicle):
    """
    Class representing a motorcycle.

    Inherits from LandVehicle and represents a two-wheeled motor vehicle.
    """
    pass


class Bicycle(LandVehicle):
    """
    Class representing a bicycle.

    Inherits from LandVehicle and represents a human-powered, pedal-driven
    vehicle.
    """
    pass


class Propeller(AirVehicle):
    """
    Class representing a propeller-driven aircraft.

    Inherits from AirVehicle and represents aircraft powered by propellers.
    """
    pass


class Jet(AirVehicle):
    """
    Class representing a jet aircraft.

    Inherits from AirVehicle and represents aircraft powered by jet engines.
    """
    pass
