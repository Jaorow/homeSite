import adafruit_dht
import board
import time
from datetime import datetime

def get_temp(device):
    temp = device.temperature
    return temp

def get_humid(device):
    hum = device.humidity
    return hum




def run():
    device = adafruit_dht.DHT11(board.D17)
    max_retries = 10
    retries = 0

    while retries < max_retries:
        try:
            temp = get_temp(device)
            humid = get_humid(device)

            if temp is not None and humid is not None:
                print(f"{temp:.2f}°, {humid:.2f}%")
                device.exit()
                return temp, humid
            else:
                raise RuntimeError("Invalid readings from sensor")

        except RuntimeError as e:
            print(f"Error: {e}")
            retries += 1
            time.sleep(2)  # Wait before retrying

        except Exception as e:
            print(f"Unexpected error: {e}")
            retries += 1
            time.sleep(2)  # Wait before retrying

    print("Failed to read sensor data after multiple attempts")
    device.exit()
    return None, None


def schedule(interval:int=600):
    """
    Schedule runs
        interval: the amount of seconds waited between mesurements

    1800 = 30m
    600 = 10m
    """

    try:
        while True:
            temp,humid = run()

            with open('outputs/temps.csv', 'a') as f:
                f.write(f"{datetime.now()}, {temp}, {humid}\n")
            
            print(f"sleeping for {interval} seconds")
            time.sleep(interval)
    except:
        pass

if __name__ == "__main__":
    schedule(300)
