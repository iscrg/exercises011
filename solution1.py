class AirConditioning:
    """
    This class represents an Air Conditioning unit.
    """
    def __init__(self) -> None:
        """
        Initializes the AirConditioning object with status set to False and temperature set to None.
        :return: None
        """
        self.__status = False
        self.__temperature = None

    @property
    def status(self) -> bool:
        """
        Returns the status of the air conditioner.
        :return: The status of the air conditioner.
        """
        return self.__status

    @status.setter
    def status(self, value: bool):
        """
        Sets the status of the air conditioner.
        :param value: The new status of the air conditioner.
        :return: None
        """
        if isinstance(value, bool):
            self.__status = value
            if self.__status:
                self.__temperature = 18
            else:
                self.__temperature = None

    @property
    def temperature(self):
        """
        Returns the temperature of the air conditioner.
        :return: The temperature of the air conditioner.
        """
        return self.__temperature

    @temperature.setter
    def temperature(self, value: int) -> None:
        """
        Sets the temperature of the air conditioner.
        :param value: The new temperature of the air conditioner.
        :return: None
        """
        if self.__status and isinstance(value, int) and 0 <= value <= 43:
            self.__temperature = value

    def reset(self) -> None:
        """
        Resets the temperature of the air conditioner to 18 if it's on.
        :return: None
        """
        if self.__status:
            self.__temperature = 18

    def get_temperature(self):
        """
        Returns the temperature of the air conditioner.
        :return: The temperature of the air conditioner.
        """
        return self.__temperature

    def raise_temperature(self) -> None:
        """
        Increases the temperature of the air conditioner by 1 if it's on and the current temperature is less than 43.
        :return: None
        """
        if self.__status and self.__temperature < 43:
            self.__temperature += 1

    def lower_temperature(self) -> None:
        """
        Decreases the temperature of the air conditioner by 1 if it's on and the current temperature is more than 0.
        :return: None
        """
        if self.__status and self.__temperature > 0:
            self.__temperature -= 1

    def switch_on(self) -> None:
        """
        Turns on the air conditioner.
        :return: None
        """
        self.status = True

    def switch_off(self) -> None:
        """
        Turns off the air conditioner.
        :return: None
        """
        self.status = False

    def __str__(self):
        """
        Returns a string representation of the air conditioner's status.
        :return: A string representing the air conditioner's status.
        """
        if self.__status:
            return f"Кондиционер включен. Температурный режим: {self.__temperature} градусов."
        else:
            return "Кондиционер выключен."
