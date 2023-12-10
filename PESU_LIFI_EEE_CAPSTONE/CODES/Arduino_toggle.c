const int inputPin = 2;  
const int outputPins[] = {3, 4, 5}; 
const int numOutputPins = 3; 

void setup() {
  pinMode(inputPin, INPUT); 
  for (int i = 0; i < numOutputPins; i++) {
    pinMode(outputPins[i], OUTPUT); 
  }
  Serial.begin(9600);  
}
// 50 -> 2000
// 75 -> 3000
// 40 thres
// 80 thres
void loop() {
  int pwmValue = pulseIn(inputPin, HIGH);  

  int selectedPin = map(pwmValue, 9, 3950, 0, numOutputPins - 1);
  selectedPin = constrain(selectedPin, 0, numOutputPins-1);

  for (int i = 0; i < numOutputPins; i++) {
    if ((i == selectedPin)) {
      digitalWrite(outputPins[i], HIGH);  
    } else {
      digitalWrite(outputPins[i], LOW);   
    }
  }


  Serial.print("Selected Pin: ");
  Serial.print(outputPins[selectedPin]);
  Serial.print(", PWM Value: ");
  Serial.println(pwmValue);

  delay(100);  
}
