const int led = 8;
const int led2 = 9;
char c;
char comando;

void setup() {
  Serial.begin(115200);
  pinMode(led, OUTPUT);
  pinMode(led2, OUTPUT);
}
void loop() {
  
  while (Serial.available()) {
    c = Serial.read();
    if (c == 'f' || c == 'b' || c == 'l' || c == 'r' || c == 's') {
       comando = c;
    } else {
     
    }
  }

    switch (comando) {
    case 'f': // si verde titila 2 veces es f
      digitalWrite(led, HIGH);
      delay(500);
      digitalWrite(led, LOW);
      delay(500);
      digitalWrite(led, HIGH);
      delay(500);
      digitalWrite(led, LOW);
      delay(500);
      break;

    case 'b': // si rojo titila 2 veces es b
      digitalWrite(led2, HIGH);
      delay(500);
      digitalWrite(led2, LOW);
      delay(500);
      digitalWrite(led2, HIGH);
      delay(500);
      digitalWrite(led2, LOW);
      delay(500);
      break;

    case 'l': // si rojo titila 1 vez es l
      digitalWrite(led2, HIGH);
      delay(500);
      digitalWrite(led2, LOW);
      delay(500);
      break;

    case 'r': // si verde titila 1 ves es r
      digitalWrite(led, HIGH);
      delay(500);
      digitalWrite(led, LOW);
      delay(500);
      break;

    case 's': //devuelve los dos a la vez
    digitalWrite(led, HIGH);
    digitalWrite(led2, HIGH);
    delay(1000);
    digitalWrite(led, LOW);
    digitalWrite(led2, LOW);
    delay(1000);
    break;
  }
}







