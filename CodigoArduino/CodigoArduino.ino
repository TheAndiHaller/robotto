const int led = 8;
const int led2 = 9;
char c;
char comando;
int giro = 100;
int velocidad = 150;
#define pin_Enable_Mot_Der 2
#define Mot_Der_Negativo 3
#define Mot_Der_Positivo 4
#define pin_Enable_Mot_Izq 5
#define Mot_Izq_Negativo 6
#define Mot_Izq_Positivo 7

void setup() {
  Serial.begin(115200);
  pinMode(led, OUTPUT);
  pinMode(led2, OUTPUT);
   pinMode(Mot_Der_Negativo, OUTPUT);
  pinMode(Mot_Der_Positivo, OUTPUT);
  pinMode(Mot_Izq_Negativo, OUTPUT);
  pinMode(Mot_Izq_Positivo, OUTPUT);
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
      Adelante();
      break;

    case 'b': // si rojo titila 2 veces es b
     Reversa();
     break;

    case 'l': // si rojo titila 1 vez es l
    Izquierda();
    break;

    case 'r': // si verde titila 1 ves es r
      Derecha();
      break;

    case 's': //devuelve los dos a la vez
    Parar();
    comando = 'x';
    break;
    
default: 
Parar();
break;
  }
  
}


void Adelante(void)
{

  digitalWrite(Mot_Der_Positivo, HIGH);
  digitalWrite(Mot_Der_Negativo, LOW);
  digitalWrite(Mot_Izq_Positivo, HIGH);
  digitalWrite(Mot_Izq_Negativo, LOW);
  for (int i = 0; i < 255; i++)
  {
    analogWrite(pin_Enable_Mot_Der, i);
    analogWrite(pin_Enable_Mot_Izq, i);
    delay(100);
  }

}
void Derecha(void)
{
  digitalWrite(Mot_Der_Positivo, LOW);
  digitalWrite(Mot_Der_Negativo, HIGH);
  digitalWrite(Mot_Izq_Positivo, HIGH);
  digitalWrite(Mot_Izq_Negativo, LOW);

  {
    analogWrite(pin_Enable_Mot_Der, velocidad);
    analogWrite(pin_Enable_Mot_Izq, velocidad);
    delay(100);
  }
}
void Izquierda(void)
{
  digitalWrite(Mot_Der_Positivo, HIGH);
  digitalWrite(Mot_Der_Negativo, LOW);
  digitalWrite(Mot_Izq_Positivo, LOW);
  digitalWrite(Mot_Izq_Negativo, HIGH);

  {
    analogWrite(pin_Enable_Mot_Der, velocidad);
    analogWrite(pin_Enable_Mot_Izq, velocidad);
    delay(100);
  }
}
void Reversa(void)
{
  digitalWrite(Mot_Der_Positivo, LOW);
  digitalWrite(Mot_Der_Negativo, HIGH);
  digitalWrite(Mot_Izq_Positivo, LOW);
  digitalWrite(Mot_Izq_Negativo, HIGH);

  {
    analogWrite(pin_Enable_Mot_Der, velocidad);
    analogWrite(pin_Enable_Mot_Izq, velocidad);
    delay(100);
  }
}
void Parar(void)
{
  digitalWrite(Mot_Der_Positivo, LOW);
  digitalWrite(Mot_Der_Negativo, LOW);
  digitalWrite(Mot_Izq_Positivo, LOW);
  digitalWrite(Mot_Izq_Negativo, LOW);
}











