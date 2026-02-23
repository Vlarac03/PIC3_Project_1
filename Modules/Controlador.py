import random
import datetime
import json
import socket

HOST = "127.0.0.1"
PORT = 65432

temperatura =  random.uniform(-4,40)
humitat = random.uniform(0,100)
irrigacio = random.uniform(0,1)
plujometre = random.uniform(0,100)

def sensor_temperatura():
    global temperatura
    temperatura = round(temperatura + random.uniform(-0.5, 0.5), 2)
    if temperatura < -10:
        temperatura = -10
    if temperatura > 45:
        temperatura = 45
    return temperatura    

def sensor_humitat():
    global humitat
    humitat = round(humitat + random.uniform(-1, 1), 2)
    if humitat < 0:
        humitat = 0
    if humitat > 100:
        humitat = 100
    return humitat

def sensor_irrigacio():
    global irrigacio
    irrigacio = round(irrigacio + random.uniform(-0.1, 0.1), 2)
    if irrigacio < 0:
        irrigacio = 0
    if irrigacio > 1:
        irrigacio = 1
    return irrigacio

def sensor_plujometre():
    global plujometre
    plujometre = round(plujometre + random.uniform(-0.5, 0.5), 2)
    if plujometre < 0:
        plujometre = 0
    if plujometre > 100:
        plujometre = 100
    return plujometre

def generar_enviar_dades():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        print("Conecció establerta")

        proxima_execucio = datetime.datetime.now()
        
        while True:
            hora_ara = datetime.datetime.now()
            if hora_ara >= proxima_execucio:
                dades = {
                    "temperatura": sensor_temperatura(),
                    "humitat": sensor_humitat(),
                    "irrigacio": sensor_irrigacio(),
                    "plujometre": sensor_plujometre()
                }
                
                print(dades)
                s.sendall(json.dumps(dades).encode())
                proxima_execucio = hora_ara + datetime.timedelta(seconds=3)

if __name__ == "__main__":
    try:
        generar_enviar_dades()
    except KeyboardInterrupt:
        print("Controlador aturat manualment.")