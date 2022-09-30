import time

hora_actual=12
#imprir la hora
while True:
    hora_actual=time.strftime("%H:%M:%S")
    print(hora_actual)

    
    time.sleep(60)

if int(hora_actual)>=7:
    print("Es hora de ir se a casa")
else:
    hora_actual=time.time()
    hora_final=time.time()
    tiempo_restante = hora_final-hora_actual
