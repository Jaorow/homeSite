import serial
from datetime import datetime

ser = serial.Serial('/dev/ttyACM0', 9600)

def log(msg):
    with open("logs/tempLogs.txt", "a") as f:
        f.write(f"{datetime.now()} --> {msg}\n")

def hex_to_float(hex_string):
    try:
        # Convert the hexadecimal string to an integer
        integer_value = int(hex_string, 16)
        # Convert the integer to a float
        return integer_value / 100.0
    except ValueError:
        # Handle the case where the hexadecimal string is invalid
        log(f"Invalid hex string: {hex_string}")
        return None

def get_temp():
    while True:
        read_serial = ser.readline().strip()
        try:
            # Decode the bytes to a string and remove any leading/trailing whitespace
            hex_string = read_serial.decode('utf-8').strip()
            temperature = hex_to_float(hex_string)
            if temperature is not None:
                return temperature
        except UnicodeDecodeError:
            log("Unicode Decode Error. Skipping this read.")
        except ValueError:
            log(f"Received invalid data: {hex_string}")

def get_minute():
    minute = []
    while len(minute) <= 3:
        minute.append(get_temp())
    return sum(minute)/len(minute)

def get_ten(test=False):
    l = []
    if test:
        l = [18.315, 18.205, 18.2875, 18.2325]
        time.sleep(1)
    while len(l) <= 3:
        l.append(get_minute())
    m = round(sum(l)/len(l),2)
    return m

def write(temp):
    with open('outputs/temps.csv', 'a') as f:
        f.write(f"{datetime.now()}, {temp}\n")

def main():
    while True():
        ten_avrage = get_ten(test=True)
        write(ten_avrage)

if __name__ == "__main__":
    main()
