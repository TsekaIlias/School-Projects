int button1 = 3;
int button2 = 4;
int button3 = 7;
int greenLED = 8;
int redLED = 13;

const int secretCode[] = {3, 4, 7};
const int code = 3;

int userInput[code];
int inputIndex = 0;

void setup() {
  Serial.begin(9600);
  pinMode(button1, INPUT);
  pinMode(button2, INPUT);
  pinMode(button3, INPUT);
  pinMode(greenLED, OUTPUT);
  pinMode(redLED, OUTPUT);
  digitalWrite(greenLED, LOW);
  digitalWrite(redLED, LOW);
}

void loop() {
  if (digitalRead(button1) == HIGH) {
    Serial.println("Button 1 Pressed");
    userInput[inputIndex] = 3;
    inputIndex++;
    delay(200);
  }

  if (digitalRead(button2) == HIGH) {
    Serial.println("Button 2 Pressed");
    userInput[inputIndex] = 4;
    inputIndex++;
    delay(200);
  }

  if (digitalRead(button3) == HIGH) {
    Serial.println("Button 3 Pressed");
    userInput[inputIndex] = 7;
    inputIndex++;
    delay(200);
  }

  if (inputIndex == code) {
    if (checkCode()) {
      Serial.println("Yupieee!");
      digitalWrite(greenLED, HIGH);
      digitalWrite(redLED, LOW);
    } else {
      Serial.println("AHHHHHHH!!!");
      digitalWrite(redLED, HIGH);
      digitalWrite(greenLED, LOW);
    }
    inputIndex = 0; 
    delay(2000); 
    digitalWrite(greenLED, LOW);
    digitalWrite(redLED, LOW);
  }
}

bool checkCode() {
  for (int i = 0; i < code; i++) {
    if (userInput[i] != secretCode[i]) {
      return false;
    }
  }
  return true;
}
