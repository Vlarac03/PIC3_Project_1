import socket
import os
import json
import datetime

HOST = "127.0.0.1"
PORT = 65432
CARPETA_PUJAR = "Dades"

if not os.path.exists(CARPETA_PUJAR):
    os.makedirs(CARPETA_PUJAR)
    
def guardar_dades(dades):    
    data_ara = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    dia = datetime.datetime.now().strftime("%Y-%m-%d")
    
    for sensor, valor in dades.items():
        nom_fitxer = f"{sensor}_{dia}.json"
        ruta_fitxer = os.path.join(CARPETA_PUJAR, nom_fitxer)
        
        registre = {
            "Data/Hora": data_ara,
            "Valor detectat": valor
        }
        
        dades_sensors = []
        if os.path.exists(ruta_fitxer):
            with open(ruta_fitxer, "r") as f:
                try:
                    dades_sensors = json.load(f)
                except:
                    dades_sensors = []
                
        dades_sensors.append(registre)       
                
        with open(ruta_fitxer, "w") as f:
            json.dump(dades_sensors, f, indent=4)
            
    print(f"Dades guardades")            
        
def iniciar_servidor():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind((HOST, PORT))
        s.listen()
        print(f"Servidor escoltant a {HOST}:{PORT}")
        while True:
            conn, addr = s.accept()
            with conn:
                print(f"Connexió establerta amb {addr}")
                while True:
                    dades = conn.recv(1024)
                    if not dades:
                        break
                    dades = json.loads(dades.decode())
                    guardar_dades(dades)
                    
if __name__ == "__main__":
    try:
        iniciar_servidor()
    except KeyboardInterrupt:
        print("Servidor atura.")