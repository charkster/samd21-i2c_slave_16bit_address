# samd21-i2c_slave_16bit_address
This implements an i2c slave with a register map of 16k bytes in sram (SAMD21 has a total of 32kB ram). A 2 byte write is needed to load a 14bit address. The slave supports multi-byte writes and reads. It uses the arduino "Wire" library, and can be easily ported to other MCUs.

I use this to model ASICs which use 16bit addressing with an i2c interface. A UF2 file is included for easy programming and the i2c pins are as documented in Seeeduino Xiao and QT PY pin diagrams.
