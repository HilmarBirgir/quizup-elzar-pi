#define BUTTON_PIN        2  // Button
#define DELAY            20  // Delay per loop in ms

void setup()
{
  pinMode(BUTTON_PIN, INPUT);
  digitalWrite(BUTTON_PIN, HIGH);
  Serial.begin(9600);
}

boolean handle_button()
{
  int button_pressed = !digitalRead(BUTTON_PIN);
  return button_pressed;
}

void loop()
{
  boolean button_pressed = handle_button();
  Serial.println(button_pressed ? "1" : "0");
  delay(DELAY);
}
