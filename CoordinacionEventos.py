import random
import threading
import time

#crear evento carrera
carrera_iniciada=threading.Event()


def corredor(id_corredor):
    print(f"Corredor {id_corredor} en posición, esperando señal de salida...")
    carrera_iniciada.wait()#esperar a que inicie la carrera
    tiempo= random.uniform(1,3)#tiempo aleatorio para la carrera de cada corredor
    time.sleep(tiempo)#esperar a que acabe la carrera para mostrar el mensaje final
    print(f"Corredor {id_corredor} ha llegado a la meta. Su tiempo ha sido: {tiempo:.4f}")

def iniciar_carrera():
    print("Señal de salida en 2 segundos...")
    time.sleep(2)#simular tiempo de espera hasta que inicie la carrera
    carrera_iniciada.set()#inicia el evento carrera para que se activen los corredores
    print("¡Salida! Los corredores han comenzado.")

#crear e iniciar hilos para 5 corredores
corredores=[]
for i in range(5):
    t=threading.Thread(target=corredor, args=(i,))
    corredores.append(t)
    t.start()

#iniciar la carrera después de un tiempo
carrera=threading.Thread(target=iniciar_carrera())
carrera.start()

#esperar a que los corredores terminen
for t in corredores:
    t.join()
carrera.join()


