void setup() {
  pinMode(LED_BUILTIN, OUTPUT);
}

void loop() {
  if (Serial.available() > 0) {
    String data = Serial.readStringUntil('\n');
    if (data == "d") {
      digitalWrite(LED_BUILTIN, LOW);
      Serial.println("Selecionei a letra 'd' de desligar");
    } else if (data == "s") {
      digitalWrite(LED_BUILTIN, HIGH);
      Serial.println("Selecionei a letra 's' de ligar");
    }
  }
}
