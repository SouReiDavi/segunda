#include "LiquidCrystal.h"
LiquidCrystal lcd(8,7,6,5,4,3);

int LDR_VAL = 0;

void setup()
{
  pinMode(A0, INPUT);
  Serial.begin(9600);
  lcd.begin(16,2);
  
  lcd.setCursor(0,0);
  lcd.print(" TRIP ZOO ");

  pinMode(10, OUTPUT);

 
}

void loop()
{
  LDR_VAL = analogRead(A0);
  Serial.println(LDR_VAL);
  
  lcd.setCursor(0,1);
  lcd.print(LDR_VAL);

 if (LDR_VAL < 700)
 {
    digitalWrite(10, LOW);
    lcd.setCursor(0,1);
    lcd.print(" LUZES DESLIGADO   ");
  } 
else
 {
    digitalWrite(10, HIGH);
    lcd.setCursor(0,1);
    lcd.print("LUZES LIGADO    ");
  }
  
  delay(10); // Delay a little bit to improve simulation performance
}
