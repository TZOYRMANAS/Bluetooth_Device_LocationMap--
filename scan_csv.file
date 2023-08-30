#!/usr/bin/env python
import csv
import bluetooth as bt
import datetime
import os
import geocoder
from io import StringIO

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
   
    return bt.discover_devices(duration=timeout, flush_cache=True, lookup_names=True)

def bluetooth_low_energy_scan(timeout=10):
 
    if DiscoveryService is None:
        return None

    svc = DiscoveryService()
    return svc.discover(timeout=timeout)

def save_results_to_file(devices):
    output_file = "results.csv"
    temp_csv = StringIO()

    if devices:
        csv_writer = csv.writer(temp_csv, delimiter='\t')
        csv_writer.writerow(["MAC adreess ", "Device_name", "Time_found", "Latitude", "Longitude"])
        for device in devices:
            mac_address = device[0]
            device_name = device[1]
            time_found = datetime.datetime.now().isoformat()
            lat_number, long_number = get_current_location() or (None, None)
            csv_writer.writerow([mac_address, device_name, time_found, lat_number, long_number])
    else:
        csv_writer = csv.writer(temp_csv, delimiter='\t')
        csv_writer.writerow(["None"] * 5)

    with open(output_file, "a", newline='') as f:
        f.write(temp_csv.getvalue())
    
    temp_csv.close()

if __name__ == "__main__":
    scansec = 10 

    dev_classic = bluetooth_classic_scan(scansec)
    if dev_classic:
        with open("results.csv", "w", newline='') as f:
            f.write("Συσκευές Bluetooth Classic:\n")
        save_results_to_file(dev_classic)

    dev_ble = bluetooth_low_energy_scan(scansec)
    if dev_ble:
        with open("results.csv", "a", newline='') as f:
            f.write("\nΣυσκευές Bluetooth Low Energy:\n")
        for u, n in dev_ble.items():
            with open("results.csv", "a", newline='') as f:
                f.write(f"{u}, {n}\n")

