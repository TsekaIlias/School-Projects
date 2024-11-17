int ledPin = 9;  
int buttonPin = 2;
int brightnessLevels[] = {0, 64, 127, 191, 255};
int currentLevel = 0;

void setup() {
  pinMode(ledPin, OUTPUT);
  pinMode(buttonPin, INPUT);  
  Serial.begin(9600);
}

void loop() {
  if (digitalRead(buttonPin) == HIGH) {  
    currentLevel = (currentLevel + 1) % 5;
    analogWrite(ledPin, brightnessLevels[currentLevel]);  
    Serial.println("The button has been pressed");
    delay(200); 
  }
}
