#!/usr/bin/env python 
import json
import bluetooth as bt
import datetime
import os
import geocoder

def get_current_location():
    g = geocoder.ip('me')
    if g.latlng:
        return g.latlng
    return None

try:
    from bluetooth.ble import DiscoveryService
except ImportError:
    DiscoveryService = None

def bluetooth_classic_scan(timeout=10):
 
    return bt.discover_devices(duration=timeout, flush_cache=True, lookup_names>

def bluetooth_low_energy_scan(timeout=10):
  
    if DiscoveryService is None:
        return None

    svc = DiscoveryService()
    return svc.discover(timeout=timeout)

def save_results_to_file(devices, filename):
    if devices:
        with open(filename, "a") as f:
            for device in devices:
                mac_address = device[0]
                device_name = device[1]
  time_found = datetime.datetime.now().isoformat()
                lat_number, long_number = get_current_location() or (0, 0)

                data = {
                    "id": mac_address,
                    "reportTime": time_found,
                    "location": {
                        "latitude": lat_number,
                        "longitude": long_number
                    },
                    "sensorName": device_name,
                    "sensorStatus": "string",
                   "imei": None ,
                    "email": None ,
                    "mobileId": None ,
                    "category":None ,
                    "reportAction":0 ,
                    "message":None  ,
"isPerson": True
                }
                json.dump(data, f)
                f.write('\n')

def save_location_to_file(filename):
    current_time = datetime.datetime.now().isoformat()
    current_location = get_current_location()
    if current_location:
        data = {
            "Scanned on": current_time,
            "Location": {
                "latitude": current_location[0],
                "longitude": current_location[1]
            }
        }
        with open(filename, "a") as f:
            json.dump(data, f, indent=4)
if __name__ == "__main__":
    scansec = 5  # how long to scan for (seconds)
    output_file = "bluetooth_scan_results.json"

    dev_classic = bluetooth_classic_scan(scansec)
    if dev_classic:
        save_results_to_file(dev_classic, output_file)

    dev_ble = bluetooth_low_energy_scan(scansec)
    if dev_ble:
        with open(output_file, "a") as f:
            for u, n in dev_ble.items():
                data = {
                    "id": u ,
                    "reportTime": datetime.datetime.now().isoformat(),
                    "location": {
                        "latitude": 0,
                        "longitude": 0
                    },
                    "sensorName": n,

"sensorStatus":" string",
                    "imei": "string",
                    "email": "string",
                    "mobileId": "string",
                    "category": "string",
                    "reportAction": 0,
                    "message": "string",
                    "isPerson": True
                    }
                json.dump(data, f)
                f.write('\n')

    save_location_to_file(output_file)
