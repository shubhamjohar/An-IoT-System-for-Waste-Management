/. Connnect digital pin of MQ6 to digital pin with value 'sensor'  
int sensor=7;
//for stori
int gas_value;
void setup()
{

pinMode(sensor,INPUT);
Serial.begin(9600);

}

void loop()
{
//To read digital values use DigitalRead() function
gas_value=analogRead(sensor);
Serial.println(gas_value);
}
