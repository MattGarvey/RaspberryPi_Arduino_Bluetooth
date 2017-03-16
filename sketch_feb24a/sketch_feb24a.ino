int ledPin = 9;
int red = 12;
int blue = 11;

void setup() {
  Serial.begin( 9600 );
  Serial.setTimeout(200);
}

void loop() {
  // looks for data
  if ( Serial.available() > 0 ) {
    // grabs input from serial
    String color = Serial.readString();
    if (color.equals("abcd"))
      getColor();
    int inputInt = color.toInt();
    // should appear in rpi terminal
    if (inputInt > 0) {
      Serial.print("Input number of blinks: ");
      Serial.println(String(inputInt));
      // blinks the LED
      blinkLED(inputInt);
    }
  }
}

void blinkLED(int count) {
  for (int i = 0; i < count; i++) {
    digitalWrite(ledPin, HIGH);
    delay(500);
    digitalWrite(ledPin, LOW);
    delay(500);
  }
}

void getColor() {
  int bCount = 0;
  int rCount = 0;
  for (int i = 0; i < 3; i++){
  if (digitalRead(blue) == HIGH){
    bCount++;}
  if (digitalRead(red) == HIGH){
    rCount++;}
  }
  if (bCount <= rCount){
    Serial.println("RED!");}
  if (bCount > rCount){
    Serial.println("BLUE!");}

}

