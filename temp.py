import adafruit_dht
import board
import time

# Initialize the DHT11 device, with the data pin connected to GPIO4
device = adafruit_dht.DHT11(board.D17)
print("Running")


def get_temp(device):
    temp = device.temperature
    return f"{temp:.2f}"

def get_humid(device):
    hum = device.humidity
    return f"{hum:.2f}"


try:
    # Get temperature and humidity values
    print(get_temp(device))
    print(get_humid(device))

except RuntimeError as error:
    # Errors happen fairly often, DHT's are hard to read, just keep going
    print(error.args[0])

# time.sleep(1800)


device.exit()
