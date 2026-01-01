# Convert the Temperature
class Solution(object):
    def convertTemperature(self, celsius):
       kelvin=celsius + 273.15
       fahrenhit = celsius * 1.80 +32
       return [kelvin,fahrenhit]
s=Solution()
print(s.convertTemperature(36.50))  # Output: [309.65,97.7]
print(s.convertTemperature(122.11))  # Output: [395.26,251.798]