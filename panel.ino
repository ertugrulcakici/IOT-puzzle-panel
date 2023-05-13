#define button A0
#define ROLE 2
#define BUZZER 3

#define DEBUG

unsigned long int lastTime = 0;
bool isActive = false;
bool notDone = true;

void setup()
{
#ifdef DEBUG
    Serial.begin(9600);
#endif
pinMode(BUZZER,OUTPUT);
pinMode(ROLE,OUTPUT);
}

void loop()
{

    if (analogRead(button) > 500)
    {
      #ifdef DEBUG
      Serial.println(analogRead(button));
      #endif
        digitalWrite(ROLE, HIGH);
        notDone = false;
        digitalWrite(BUZZER, LOW);
    }

    if (millis() >= lastTime + 700)
    {
#ifdef DEBUG
        //Serial.println(lastTime);
#endif
        lastTime += 700;
        if (notDone) {
            if (isActive)
            {
                digitalWrite(BUZZER, HIGH);
                isActive = false;
            }
            else
            {
                digitalWrite(BUZZER, LOW);
                isActive = true;
            }
        }
    }
    
    delay(100);
}
