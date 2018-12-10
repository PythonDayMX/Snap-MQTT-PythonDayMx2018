import http.server
import socketserver
import paho.mqtt.client as mqtt

class RequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        path = self.path[1:]
        topic, msg = path.split("?")
        print(topic, " - ", msg)
        client.publish(topic, msg, qos=1)
        self.send_response(204)
        self.end_headers()

def on_connect(client, userdata, flags, rc):
    print('Conectado a broker')
    pass

if __name__ == "__main__":
    print("Snap-MQTT")

    client = mqtt.Client()
    client.connect("192.168.4.1")

    client.on_connect = on_connect
    client.loop_start()

    handler = RequestHandler

    httpd = socketserver.TCPServer(("", 1330), handler)

    httpd.serve_forever()
