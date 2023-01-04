import time
import network

# Micropython uses a main loop by convention
# rather than a if __name__ == '__main__'

while True:
    nic = network.WLAN()
    print(f"{nic.isconnected()=}")
    time.sleep(1)
