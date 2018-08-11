#include <Wire.h>
#include <LiquidCrystal_I2C.h>

LiquidCrystal_I2C lcd(0x3f, 16, 2);

void setup() {
  Serial.begin(115200);
  lcd.init();
  lcd.backlight();

}

void loop() {
  while (Serial.available()) {
    char c = Serial.read();
    if (c == '\n' || c == '\r' || c == '$') {
      delay(500);
      lcd.clear();
      lcd.setCursor(0, 0);
    } else {
      lcd.print(c);
    }
  }
}
