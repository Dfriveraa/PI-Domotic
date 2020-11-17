#include <Arduino.h>
#include <math.h>
#include <analogWrite.h>
#include <PubSubClient.h>
#include <WiFi.h>
int rojo = 2;
int verde = 13;
int azul = 14;

int canal=0;
int colores[3]={rojo,verde,azul};

//**************************************
//*********** MQTT CONFIG **************
//**************************************
const char *mqtt_server = "192.168.1.67";
const int mqtt_port = 1883;


//**************************************
//*********** WIFICONFIG ***************
//**************************************
const char* ssid = "ArcilaR";
const char* password =  "2NB112105561";
int state=0;


//**************************************
//*********** GLOBALES   ***************
//**************************************
WiFiClient espClient;
PubSubClient client(espClient);
char msg[25];
long count=0;


//************************
//** F U N C I O N E S ***
//************************
void callback(char* topic, byte* payload, unsigned int length);
void reconnect();
void setup_wifi();

void setup() {
  Serial.begin(115200);
  setup_wifi();
  pinMode(rojo,OUTPUT);
  pinMode(verde,OUTPUT);
  pinMode(azul,OUTPUT);

  client.setServer(mqtt_server, mqtt_port);
  client.setCallback(callback);
}

void loop() {

  if (!client.connected()) {
		reconnect();
	}

  if (client.connected()){
    // String str = "La cuenta es -> " + String(count);
    // str.toCharArray(msg,25);
    // client.publish("home/cosa",msg);
    // count++;
    // delay(300);
  }
  client.loop();

}




//*****************************
//***    CONEXION WIFI      ***
//*****************************
void setup_wifi(){
	delay(10);
	// Nos conectamos a nuestra red Wifi
	Serial.println();
	Serial.print("Conectando a ssid: ");
	Serial.println(ssid);

	WiFi.begin(ssid, password);

	while (WiFi.status() != WL_CONNECTED) {
		delay(500);
		Serial.print(".");
	}

	Serial.println("");
	Serial.println("Conectado a red WiFi!");
	Serial.println("Dirección IP: ");
	Serial.println(WiFi.localIP());
}



//*****************************
//***    CONEXION MQTT      ***
//*****************************

void reconnect() {
  // Loop until we're reconnected
  while (!client.connected()) {
    Serial.print("Attempting MQTT connection...");
    // Attempt to connect
    if (client.connect("oled")) {
      Serial.println("connected");
      client.subscribe("home/tv");
    } else {
      Serial.print("failed, rc=");
      Serial.print(client.state());
      Serial.println(" try again in 5 seconds");
      // Wait 5 seconds before retrying
      delay(5000);
    }
  }
}


//*****************************
//***       CALLBACK        ***
//*****************************

void callback(char* topic, byte* payload, unsigned int length){
	String incoming = "";

	// for (int i = 0; i < length; i++) {
	// 	incoming += (char)payload[i];
	// }
	// incoming.trim();
  if ((char)payload[0]=='1'){
    if(state==0){
      Serial.println("Prendiendo");
      digitalWrite(colores[canal],HIGH);
      state=1;
    }
    else{
    	Serial.println("Apagar");
      digitalWrite(colores[canal],LOW);
      state=0;
    }
  }
  else if ((char)payload[0]=='2' && state==1){
      Serial.println("SubiendoCanal");
      digitalWrite(colores[canal],LOW);
      canal=(canal+1)%3;
      digitalWrite(colores[canal],HIGH);
  }
  else if ((char)payload[0]=='3' && state==1){
      Serial.println("BajandoCanal");
      digitalWrite(colores[canal],LOW);
      canal=canal-1;
      if(canal<0) {canal=2;}
      digitalWrite(colores[canal],HIGH);
  }
  else{
      Serial.println("Acción desconocida");
  }        


}