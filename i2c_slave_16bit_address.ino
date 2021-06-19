
#include <Wire.h>
volatile uint8_t  address_upper;
volatile uint8_t  address_lower;
volatile uint16_t address;
volatile uint8_t  data;
volatile uint8_t  memory_map [16383]; // array is initialize all low values, 14 bit addressing, there is only 32k bytes ram on samd21

#define SLAVE_ID 0x0A

void setup()
{
  Wire.begin(SLAVE_ID);         // join i2c bus with slave_id SLAVE_ID
  Wire.onReceive(receiveEvent); // register write to slave
  Wire.onRequest(requestEvent); // register read from slave
  pinMode(7, OUTPUT); // digital pin 7 is an output
}

void loop()
{
  delay(100);
}

// function that executes when the master writes data to this slave
void receiveEvent(int bytes)
{
  address_upper = Wire.read() & 0x3F; // read first  byte to determine address[11:8]
  address_lower = Wire.read();        // read second byte to determine address[7:0]
  address = (address_upper << 8) + address_lower;
  while (Wire.available())
  {
    data = Wire.read();
    memory_map[address++] = data;
  }

}

// function that executes when the master reads from this slave
void requestEvent()
{
  Wire.write(memory_map[address++]);
  for (int i = 0; i < 32; i++) // this is needed for multibyte reads, up to 32 bytes
  {
    Wire.write(memory_map[address++]);
  }
}
