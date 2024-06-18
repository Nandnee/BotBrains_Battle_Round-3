#include <ESP8266WiFi.h>
#include <ESP8266HTTPClient.h>

const char* ssid = "your_SSID";
const char* password = "your_PASSWORD";
const char* serverUrl = "http://xyz.000webhostapp.com/writefile.php";

void setup() {
    Serial.begin(115200);
    WiFi.begin(ssid, password);
    while (WiFi.status() != WL_CONNECTED) {
        delay(1000);
        Serial.println("Connecting to WiFi...");
    }
    Serial.println("Connected to WiFi");

    // Example: Send data to server
    String dataToSend = "drone_data_here";
    sendToServer(dataToSend);
}

void loop() {
    // Any continuous operations can be added here
    delay(1000);
}

void sendToServer(String data) {
    HTTPClient http;

    // Construct the URL with data parameter
    String url = serverUrl + "?data=" + data;

    http.begin(url);
    int httpCode = http.GET();
    if (httpCode > 0) {
        if (httpCode == HTTP_CODE_OK) {
            String payload = http.getString();
            Serial.println("Server response: " + payload);
        }
    } else {
        Serial.printf("HTTP GET request failed, error: %s\n", http.errorToString(httpCode).c_str());
    }
    http.end();
}
