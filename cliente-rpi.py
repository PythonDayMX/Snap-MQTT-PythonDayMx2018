import paho.mqtt.client as mqtt

inraspi = False

class fakeout():
    def __init__(self, pin, **kargs):
        self.pin = pin
    def off(self):
        print(self.pin, 'off')
    def on(self):
        print(self.pin, 'on')

if inraspi: 
    from gpiozero import DigitalOutputDevice as Dod
    m0a = Dod(2, active_high=False)
    m0b = Dod(3, active_high=False)
    m0c = Dod(4, active_high=False)
    m0d = Dod(17, active_high=False)
    m1a = Dod(5, active_high=False)
    m1b = Dod(6, active_high=False)
    m1c = Dod(13, active_high=False)
    m1d = Dod(19, active_high=False)
else:
    m0a = fakeout(2, active_high=False)
    m0b = fakeout(3, active_high=False)
    m0c = fakeout(4, active_high=False)
    m0d = fakeout(17, active_high=False)
    m1a = fakeout(5, active_high=False)
    m1b = fakeout(6, active_high=False)
    m1c = fakeout(13, active_high=False)
    m1d = fakeout(19, active_high=False)

motor0 = [m0a, m0b, m0c, m0d]
motor1 = [m1a, m1b, m1c, m1d]

pmap = [[True, True, False, False],
        [False, True, True, False],
        [False, False, True, True],
        [True, False, False, True]]

def mueve(es):
    if es['pos0'] != es['pobj0']:
        pin = es['pos0'] % 4
        if es['pos0'] < es['pobj0']:
            es['pos0'] += 1
        elif es['pos0'] > es['pobj0']:
            es['pos0'] -= 1
        pout = es['pos0'] % 4
        print('M0={}, obj={}'.format(es['pos0'], es['pobj0']))
        for m, pi, po in zip(motor0, pmap[pin], pmap[pout]):
            if po and not pi:
                m.on()
            elif not po and pi:
                m.off()
    if es['pos1'] != es['pobj1']:
        pin = es['pos1'] % 4
        if es['pos1'] < es['pobj1']:
            es['pos1'] += 1
        elif es['pos1'] > es['pobj1']:
            es['pos1'] -= 1
        pout = es['pos1'] % 4
        print('M1={}, obj={}'.format(es['pos1'], es['pobj1']))
        for m, pi, po in zip(motor1, pmap[pin], pmap[pout]):
            if po and not pi:
                m.on()
            elif not po and pi:
                m.off()

def on_connect(client, userdata, flags, rc):
    print("Conectado a broker")
    client.subscribe("rpi/motor0")
    client.subscribe("rpi/motor1")

def on_message(client, userdata, msg):
    global estado
    if msg.topic == "rpi/motor0":
        estado['pobj0'] = int(msg.payload.decode())
    elif msg.topic == "rpi/motor1":
        estado['pobj1'] = int(msg.payload.decode())

if __name__ == "__main__":
    estado = {'pos0':0, 'pos1':0, 'pobj0':0, 'pobj1':0}

    client = mqtt.Client()
    client.connect("localhost")

    client.on_connect = on_connect
    client.on_message = on_message

    while True:
        client.loop(0.02)
        mueve(estado)
