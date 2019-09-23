#include <Adafruit_NeoPixel.h>

// How many NeoPixels are attached to the Arduino?
#define NUMPIXELS 82 // Popular NeoPixel ring size

// Which pin are the neopixels connected to
#define PIN 6

Adafruit_NeoPixel pixels(NUMPIXELS, PIN, NEO_GRB + NEO_KHZ800);

void setup() {
  // Setup serial communications
  Serial.begin(9600);

  // Setup neopixels
  pixels.begin();
}

void loop() {
  // Wait for serial information
  while(Serial.available() > 0){
    int red = Serial.parseInt();
    int green = Serial.parseInt();
    int blue = Serial.parseInt();

    if (Serial.read() == '\n') {
      // constrain the values to 0 - 255 and invert
      // if you're using a common-cathode LED, just use "constrain(color, 0, 255);"
      red = constrain(red, 0, 255);
      green = constrain(green, 0, 255);
      blue = constrain(blue, 0, 255);

      // Update neopixels
      for(int i = 0; i < NUMPIXELS; i++){
        pixels.setPixelColor(i, pixels.Color(red, green, blue));
      }
      pixels.show();
    }

    // Reply that information was successful
    Serial.println("OK");
  }
}
