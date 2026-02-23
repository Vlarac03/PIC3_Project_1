# PIC3_Project_1
Aquest projecte consisteix en una simulació d'un camp de blat sensoritzat. Hem desenvolupat un sistema de comunicació client-servidor utilitzant Python i Sockets per recollir dades de quatre tipus de sensors i emmagatzemar-les localment en format JSON.

Inicialment, he creat una carpeta Modules on tindrem els nostres arxius, dins d'aquesta carpeta podem trobar la carpeta Dades, on es guardaran els .json de cada sensor i dia i els arxius Controlador.py i Servidor.py

## Controlador.py
Aquest script actua com un simulador de sensors els quals a partir d'un valor d'inici aleatori anirem cridant funcions (una per cada sensor) que faran pujar i baixar aquell valor respecte al temps (cada 3 segons, a través de la llibreria datatime), mantenint sempre dades el més "reals" possibles. Per fer-ho hem utilitzat la llibreria random i hem ficat uns límits per no sobrepassar-nos en els valors.

A part també actua com a connexió amb el servidor a través de la llibreria socket amb la qual enviarà aquestes dades al nostre servidor.

Finalment, hem determinat el main on correm la funció principal per generar les dades amb un except per portar un control de seguretat i poder apagar l'execució en qualsevol moment.

## Servidor.py
Aquest script actua com el receptor de la informació. La seva funció principal és "escoltar" les connexions entrants a través de sockets i processar les dades enviades pel controlador.

Un cop rep la informació, el servidor s'encarrega d'organitzar-la i emmagatzemar-la en format JSON dins de la carpeta "Dades" la qual crea si no existeix. Ho hem fet de tal manera perquè creï un fitxer independent per a cada tipus de sensor (Temperatura, Humitat, Irrigació i Pluviòmetre) i per a cada dia, facilitant així la lectura i gestió de la base de dades.

Finalment, hem determinat el main d'inici del servidor on cridem la funció de guardar les dades amb un except per portar un control de seguretat i poder apagar l'execució en qualsevol moment.