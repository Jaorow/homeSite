#include <math.h>

void setup() {
  pinMode(LED_BUILTIN, OUTPUT);
  digitalWrite(LED_BUILTIN, LOW);
  Serial.begin(9600);
}

float get_temp() {
  double val = analogRead(0);
  double fenya = (val / 1023.0) * 5.0;
  double r = (5.0 - fenya) / fenya * 4700.0;
  float temperatureC = 1 / (log(r / 10000.0) / 3950.0 + 1 / (25.0 + 273.15)) - 273.15;
  return temperatureC;
}

void loop() {
  char dataString[50] = {0};
  float temperatureC = get_temp();
  int temperatureC_int = (int)(temperatureC * 100); // Multiply by 100 and cast to int to preserve two decimal places
  sprintf(dataString, "%04X", temperatureC_int); // Format as a 4-digit hexadecimal number
  Serial.println(dataString);
  delay(10000);
}
