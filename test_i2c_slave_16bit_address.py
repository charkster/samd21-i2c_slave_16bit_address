#/usr/bin/python3

from __future__ import print_function
import smbus

device_address = 0x0A
bus = smbus.SMBus(1)

def write_list_16addr(dev_addr=0x00, addr=0x0000, wdata=[]):
	addr_upper = (addr >> 8) & 0xFF
	addr_lower =  addr       & 0xFF
	bus.write_i2c_block_data(dev_addr, addr_upper, [addr_lower] + wdata)
	print("Write to device_address 0x{:02x}, Address 0x{:04x}, Data:".format(dev_addr, addr))
	print(wdata)

def read_list_16addr(dev_addr=0x00, addr=0x0000, num_bytes=1):
	addr_upper = (addr >> 8) & 0xFF
	addr_lower =  addr       & 0xFF
	bus.write_i2c_block_data(dev_addr, addr_upper, [addr_lower])
	read_bytes = []
	for x in range(0,num_bytes):
		read_bytes.append(bus.read_byte(device_address))
	print("Read from device address 0x{:02x}, Address 0x{:04x}, Data:".format(dev_addr, addr))
	print(read_bytes)
	return read_bytes

address1 = 0x10D1
address2 = 0x20D1
write_data1 = [0xFE] #255 decimal
write_data2 = [0x10] #16 decimal

read_list_16addr( device_address, address1, 1)
read_list_16addr( device_address, address2, 1)
write_list_16addr(device_address, address1, write_data1)
read_list_16addr( device_address, address2, 1)
read_list_16addr( device_address, address1, 1)
write_list_16addr(device_address, address2, write_data2)
read_list_16addr( device_address, address1, 1)
read_list_16addr( device_address, address2, 1)
write_list_16addr(device_address, address1, [0x00])
write_list_16addr(device_address, address2, [0x00])
read_list_16addr( device_address, address1, 1)
read_list_16addr( device_address, address2, 1)

