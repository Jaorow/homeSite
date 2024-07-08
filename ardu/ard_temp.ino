#include <math.h>

void setup()
{
  Serial.begin(9600);
}

float get_temp(){
  double val=analogRead(0);
  double fenya=(val/1023)*5;
  double r=(5-fenya)/fenya*4700;
  float o = (1/(  log(r/10000) /3950 + 1/(25+273.15))-273.15);
  return o;
}

void loop()
{
  char dataString[50] = {0};
  float t = get_temp();
  sprintf(dataString,"%02X",t);
  Serial.println(dataString);
  delay(1000);
}