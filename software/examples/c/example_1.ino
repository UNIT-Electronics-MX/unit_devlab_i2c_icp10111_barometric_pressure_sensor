/******************************************************************
  Base code for TDK InvenSense ICP-10111 barometric pressure sensor.
  Outputs:
    - Temperature in °C
    - Pressure in Pa
    - Relative altitude in meters
  Altitude is calculated using the barometric formula assuming standard atmosphere.
  Written by OpenAI based on original example from Adrian Studer.
******************************************************************/

#include <icp101xx.h>
#include <math.h>  // For pow()

ICP101xx sensor;

// Reference pressure at startup (in Pa)
float reference_pressure = 0.0;

void setup() {
  Serial.begin(115200);
  while (!Serial);  // Wait for serial to open (optional)

  // Initialize sensor
  if (!sensor.begin()) {
    Serial.println("❌ Sensor ICP10111 no encontrado.");
    while (true);  // Halt if sensor fails
  }

  Serial.println("✅ Sensor ICP10111 inicializado correctamente.");

  // Take first measurement to establish baseline pressure
  sensor.measure(sensor.ACCURATE);  // Can also use VERY_ACCURATE
  reference_pressure = sensor.getPressurePa();

  Serial.print("Presión de referencia establecida: ");
  Serial.print(reference_pressure);
  Serial.println(" Pa");
  delay(500);
}

void loop() {
  if (!sensor.isConnected()) {
    Serial.println("⚠️ Sensor desconectado.");
    delay(1000);
    return;
  }

  // Medir con alta precisión (~95ms)
  sensor.measure(sensor.VERY_ACCURATE);

  float temperature = sensor.getTemperatureC();     // Grados Celsius
  float pressure = sensor.getPressurePa();          // Pascal
  float altitude = 0.0;

  // Fórmula de altitud relativa respecto a presión base
  if (reference_pressure > 0.0) {
    altitude = 44330.0 * (1.0 - pow(pressure / reference_pressure, 0.1903));
  }

  // Mostrar valores
  Serial.println("====================================");
  Serial.print("🌡 Temp:     "); Serial.print(temperature); Serial.println(" °C");
  Serial.print("📟 Pressure: "); Serial.print(pressure); Serial.println(" Pa");
  Serial.print("🗻 Altitude: "); Serial.print(altitude); Serial.println(" m");
  Serial.println("====================================");

  delay(1000);  // Esperar antes de siguiente lectura
}
