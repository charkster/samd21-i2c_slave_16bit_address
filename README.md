# samd21-i2c_slave_16bit_address
This implements an i2c slave with a register map of 16k bytes in sram (SAMD21 has a total of 32kB ram). A 2 byte write is needed to load a 14bit address. The slave supports multi-byte writes and reads. It uses the "Wire" library.
