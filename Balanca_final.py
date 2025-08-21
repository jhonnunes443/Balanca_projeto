import serial
import time
import sys
import select
import termios
import tty
import subprocess


subprocess.run("clear", shell=True, check=True)


print("""
---------------------- x ------------------------
           ___
          |   |
     _____|   |_____
    |               |
    |      ??       |    TESTE DE BALANÇA
 ___|_______________|___
|                       |
|  @jheanphabio         |
|  Comercial Reis       |
|_______________________|


""")

speed = int(input("Velocidade da balança (2400, 4200 ou 9600): "))

ser = serial.Serial(
    port='/dev/ttyS0',
    baudrate=speed,
    bytesize=serial.SEVENBITS,
    parity=serial.PARITY_EVEN,
    stopbits=serial.STOPBITS_ONE,
    timeout=1
)

print("Lendo peso da balança... (pressione Ctrl+E para exibir peso, Ctrl+C para sair)")

def extrair_peso_em_kg(pacote):
    if len(pacote) != 7 or pacote[0] != 0x02 or pacote[-1] != 0x03:
        return None
    try:
        peso_str = pacote[1:6].decode('ascii')
        peso = int(peso_str) / 1000
        return peso
    except:
        return None


fd = sys.stdin.fileno()
old_settings = termios.tcgetattr(fd)
tty.setcbreak(fd)

mostrar_peso = False

try:
    while True:
        ser.write(b'\x05')
        time.sleep(0.5)

        data = ser.read(ser.in_waiting or 64)

        if data and len(data) >= 7:
            bytes_validos = (len(data) // 7) * 7
            for i in range(0, bytes_validos, 7):
                pacote = data[i:i+7]
                peso = extrair_peso_em_kg(pacote)
                if peso is not None and mostrar_peso:
                    print(f"Peso: {peso:.3f} kg")

        
        if select.select([sys.stdin], [], [], 0)[0]:
            key = sys.stdin.read(1)
            if ord(key) == 5:
                mostrar_peso = not mostrar_peso
                print("[INFO] Alternar exibição do peso:", "ativado" if mostrar_peso else "desativado")

        time.sleep(1)

except KeyboardInterrupt:
    print("Encerrando leitura.")
    ser.close()
    termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
