import network
import sys

SSID = "YOUR_SSID_HERE"
KEY = "YOUR_KEY_HERE"

sta_if = network.WLAN(network.STA_IF)
if not sta_if.is_connected():
    print(f"Connecting to network {SSID}...")
    sta_if.active(True)
    sta_if.connect(SSID, KEY)
    while not sta_if.is_connected():
        sys.stdout.write(".")
    print("Connected!")
