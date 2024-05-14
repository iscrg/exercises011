from solution1 import AirConditioning

conditioning = AirConditioning()
print(conditioning)
print(conditioning.temperature)
print(conditioning.status)
conditioning.status = True
print(conditioning)
print(conditioning.status)
conditioning.temperature = 20
print(conditioning.temperature)
conditioning.reset()
print(conditioning)
print(conditioning.get_temperature())
conditioning.raise_temperature()
print(conditioning.get_temperature())
conditioning.lower_temperature()
print(conditioning.get_temperature())
conditioning.switch_on()
print(conditioning)
print(conditioning.get_temperature())
print(conditioning.temperature)
conditioning.temperature = 30
print(conditioning.temperature)
conditioning.status = False
print(conditioning)
for _ in range(16):
    conditioning.lower_temperature()
print(conditioning.get_temperature())
for _ in range(5):
    conditioning.lower_temperature()
print(conditioning.get_temperature())
for _ in range(40):
    conditioning.raise_temperature()
print(conditioning)
for _ in range(5):
    conditioning.raise_temperature()
print(conditioning)
conditioning.switch_off()
print(conditioning)
