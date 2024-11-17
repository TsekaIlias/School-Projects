int cRed = 2; 
int cYellow = 4;
int cGreen = 7;
int hGreen = 12;
int hRed = 8; 

void setup() {
  Serial.begin(9600);
  pinMode(cRed, OUTPUT);
  pinMode(cYellow, OUTPUT);
  pinMode(cGreen, OUTPUT);
  pinMode(hRed, OUTPUT);
  pinMode(hGreen, OUTPUT); 
}

void loop() {
  digitalWrite(cYellow, LOW); 
  digitalWrite(cRed, HIGH); 
  digitalWrite(hGreen, HIGH);
  digitalWrite(hRed, LOW);
  delay(7000);  
  
  digitalWrite(cRed, LOW);
  digitalWrite(cGreen, HIGH);
  digitalWrite(hGreen, LOW);
  digitalWrite(hRed, HIGH);
  delay(5000);
  digitalWrite(cGreen, LOW); 
  digitalWrite(cYellow, HIGH);
  delay(2000); 
}
