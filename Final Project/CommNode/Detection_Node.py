#Emulates detection of a bus and transmits data to Interface Node

import argparse
from datetime import datetime
from random import normalvariate
import struct
import sys
import time
import traceback

from nrf24 import *
import pigpio


if __name__ == "__main__":    
    print("Python NRF24 Fixed Sender Example.")
    
    # Parse command line argument.
    parser = argparse.ArgumentParser(prog="Detection_Node.py", description="Emulate Bus Detection and transmit to interface node.")
    parser.add_argument('-n', '--hostname', type=str, default='localhost', help="Hostname for the Raspberry running the pigpio daemon.")
    parser.add_argument('-p', '--port', type=int, default=8888, help="Port number of the pigpio daemon.")
    parser.add_argument('address', type=str, nargs='?', default='1SNSR', help="Address to send to (3 to 5 ASCII characters).")
    
    args = parser.parse_args()
    hostname = args.hostname
    port = args.port
    address = args.address

    if not (2 < len(address) < 6):
        print(f'Invalid address {address}. Addresses must be 3 to 5 ASCII characters.')
        sys.exit(1)

    # Connect to pigpiod
    print(f'Connecting to GPIO daemon on {hostname}:{port} ...')
    pi = pigpio.pi(hostname, port)
    if not pi.connected:
        print("Not connected to Raspberry Pi ... goodbye.")
        exit()

    # Create NRF24 object.
    # PLEASE NOTE: PA level is set to MIN, because test sender/receivers are often close to each other, and then MIN works better.
    nrf = NRF24(pi, ce=25, payload_size=9, channel=100, data_rate=RF24_DATA_RATE.RATE_250KBPS, pa_level=RF24_PA.MIN)
    nrf.set_address_bytes(len(address))
    nrf.open_writing_pipe(address)

    # Display the content of NRF24L01 device registers.
    #nrf.show_registers()

    count = 0
    print(f'Send to {address}')
    
    #emulate vehicle detection
    Bus_Detection_flag = 1
    
    try:
        while True:

            # Emulate that we read temperature and humidity from a sensor, for example
            # a DHT22 sensor.  Add a little random variation so we can see that values
            # sent/received fluctuate a bit.
            temperature = normalvariate(23.0, 0.5)
            humidity = normalvariate(62.0, 0.5)
            print(f'Sensor values: temperature={temperature}, humidity={humidity}')

            # Pack temperature and humidity into a byte buffer (payload) using a protocol 
            # signature of 0x01 so that the receiver knows that the bytes we are sending 
            # are a temperature and a humidity (see "simple-receiver.py").
            payload = struct.pack("<Bff", 0x01, Bus_Detection_flag)

            # Send the payload to the address specified above.
            nrf.reset_packages_lost()
            nrf.send(payload)
            try:
                nrf.wait_until_sent()
                
            except TimeoutError:
                print("Timeout waiting for transmission to complete.")
                time.sleep(10)
                continue
            
            if nrf.get_packages_lost() == 0:
                print(f"Success: lost={nrf.get_packages_lost()}, retries={nrf.get_retries()}")
            else:
                print(f"Error: lost={nrf.get_packages_lost()}, retries={nrf.get_retries()}")
            
            
            
            #For Test Purposes, data is sent every sec
            time.sleep(1)

    except:
        traceback.print_exc()
        nrf.power_down()
        pi.stop()






