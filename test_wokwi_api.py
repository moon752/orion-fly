import requests
payload = {
  "board": "arduino_uno",
  "sketch": "#include <Arduino.h>\nvoid setup() {}\nvoid loop() {}"
}
r = requests.post("https://wokwi.com/projects/api/v1/simulate", json=payload)
print(r.status_code, r.text)
