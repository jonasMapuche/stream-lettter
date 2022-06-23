void setup() {
  Serial.begin(9600);
}

void loop() {
  if (Serial.available() > 0) {
    String data = Serial.readStringUntil('\n');
    if (data == "d") {
      Serial.println("Selecionei a letra 'd'");
    } else if (data = "s") {
      Serial.println("Selecionei a letra 's'");
    }
  }
}
