#define pinM A1
#define pinN A0
int moist = 0;
int light = 0;
int state = LOW;
void setup() {
  pinMode(pinN, INPUT_PULLUP);
  pinMode(pinM, INPUT_PULLUP);
  Serial.begin(9600);
}

void loop() {
  moist = analogRead(pinM);
  light = analogRead(pinN);
  char cmd = Serial.read();
  if(cmd == 'u'){
    Serial.println(moist);
  }
  else if(cmd == 'l'){
    Serial.println(light);
  }
}
