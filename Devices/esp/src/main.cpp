#include <Arduino.h>
#include <math.h>
#include <analogWrite.h>
int rojo = 2;
int verde = 13;
int azul = 15;
// the setup function runs once when you press reset or power the board
void setup() {
  // initialize digital pin LED_BUILTIN as an output.
  Serial.begin(115200);
  digitalWrite(14,LOW);
  digitalWrite(rojo,HIGH);
  digitalWrite(rojo,HIGH);
  digitalWrite(rojo,HIGH);

}


double R;
double G;
double B;

// the loop function runs over and over again forever
void loop() {
  double j=4;
  for(double i = 0;i<6.28;i+=0.01){
    R = cos(i)+1;
    G = cos(i+2.1)+1;
    B = cos(i+4.2)+1;

    R = int((R*85)+85);
    G = int(G*255);
    B = int(B*255);

    Serial.println(i);

    // analogWrite(rojo,R);
    // analogWrite(verde,G);
    // analogWrite(azul,B);
  } 

}

// #include <Arduino.h>
// #include <WiFi.h>
// #include <PubSubClient.h>

// //**************************************
// //*********** MQTT CONFIG **************
// //**************************************
// const char *mqtt_server = "192.168.1.67";
// const int mqtt_port = 1883;


// //**************************************
// //*********** WIFICONFIG ***************
// //**************************************
// const char* ssid = "ArcilaR";
// const char* password =  "2NB112105561";
// int state=0;


// //**************************************
// //*********** GLOBALES   ***************
// //**************************************
// WiFiClient espClient;
// PubSubClient client(espClient);
// char msg[25];
// long count=0;


// //************************
// //** F U N C I O N E S ***
// //************************
// void callback(char* topic, byte* payload, unsigned int length);
// void reconnect();
// void setup_wifi();

// void setup() {
//   Serial.begin(115200);
//   setup_wifi();
//   client.setServer(mqtt_server, mqtt_port);
//   client.setCallback(callback);
// }

// void loop() {

//   if (!client.connected()) {
// 		reconnect();
// 	}

//   if (client.connected()){
//     // String str = "La cuenta es -> " + String(count);
//     // str.toCharArray(msg,25);
//     // client.publish("home/cosa",msg);
//     // count++;
//     // delay(300);
//   }
//   client.loop();

// }




// //*****************************
// //***    CONEXION WIFI      ***
// //*****************************
// void setup_wifi(){
// 	delay(10);
// 	// Nos conectamos a nuestra red Wifi
// 	Serial.println();
// 	Serial.print("Conectando a ssid: ");
// 	Serial.println(ssid);

// 	WiFi.begin(ssid, password);

// 	while (WiFi.status() != WL_CONNECTED) {
// 		delay(500);
// 		Serial.print(".");
// 	}

// 	Serial.println("");
// 	Serial.println("Conectado a red WiFi!");
// 	Serial.println("Dirección IP: ");
// 	Serial.println(WiFi.localIP());
// }



// //*****************************
// //***    CONEXION MQTT      ***
// //*****************************

// void reconnect() {
//   // Loop until we're reconnected
//   while (!client.connected()) {
//     Serial.print("Attempting MQTT connection...");
//     // Attempt to connect
//     if (client.connect("oled")) {
//       Serial.println("connected");
//       client.subscribe("home/tv");
//     } else {
//       Serial.print("failed, rc=");
//       Serial.print(client.state());
//       Serial.println(" try again in 5 seconds");
//       // Wait 5 seconds before retrying
//       delay(5000);
//     }
//   }
// }


// //*****************************
// //***       CALLBACK        ***
// //*****************************

// void callback(char* topic, byte* payload, unsigned int length){
// 	String incoming = "";

// 	// for (int i = 0; i < length; i++) {
// 	// 	incoming += (char)payload[i];
// 	// }
// 	// incoming.trim();
//   if ((char)payload[0]=='1'){
//     if(state==0){
//       Serial.println("Prendiendo");
//     }
//     else{
//     	Serial.println("Apagar");
//     }
//   }
//   else if ((char)payload[0]=='1'){
//       Serial.println("otracosa");
//   }

// }