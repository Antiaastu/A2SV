class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
        fahrenheit=(celsius*1.80)+32.00
        kelvin=celsius+273.15
        return [kelvin,fahrenheit]
