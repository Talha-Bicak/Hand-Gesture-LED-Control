const int led2 = 2;
const int led3 = 3;
const int led4 = 4;
const int led5 = 5;
const int led6 = 6;

void setup() {
  pinMode(led2, OUTPUT);
  pinMode(led3, OUTPUT);
  pinMode(led4, OUTPUT);
  pinMode(led5, OUTPUT);
  pinMode(led6, OUTPUT);
  
  Serial.begin(9600); // Seri iletişimi başlat
}

void loop() {
  if (Serial.available() > 0) {
    int command = Serial.read() - '0'; // Seri porttan gelen komutu oku
    
    // Tüm LED'leri kapat
    digitalWrite(led2, LOW);
    digitalWrite(led3, LOW);
    digitalWrite(led4, LOW);
    digitalWrite(led5, LOW);
    digitalWrite(led6, LOW);
    command = command + 1;
    // Gelen komuta göre LED'leri yak
    if (command <= 1) digitalWrite(led2, HIGH);
    if (command <= 2) digitalWrite(led3, HIGH);
    if (command <= 3) digitalWrite(led4, HIGH);
    if (command <= 4) digitalWrite(led5, HIGH);
    if (command <= 5) digitalWrite(led6, HIGH);
   
  }
}
