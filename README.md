# Puente Snap-MQTT

Presentado en pythonday.mx 2018

Descripción detallada en el notebook

-----------------

Que necesitas:
* Python 3.x
* librería paho-mqtt (`pip3 install paho-mqtt`)
* Un broker MQTT broker (mosquitto o uno enlinea)

¿Cómo utilizar?
1. Configura la dirección de tu broker en Snap-MQTT.py (en la línea: `client.connect("localhost")`).
2. Corre `python3 Snap-MQTT.py`.
3. Inicia Snap (https://snap.berkeley.edu/).
4. Importa `Snap-MQTT.xlm`.
5. Manda mensajes MQTT usando el bloque importado  (en 'Variables').

