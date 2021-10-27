# Carrega as bibliotecas
#import Adafruit_DHT
#import RPi.GPIO as GPIO
import time
import urllib.request
from random import randint

myAPI = "2RBWQ3MQ5TVSMXSR"
baseURL = "https://api.thingspeak.com/update?api_key="+myAPI

temp = 0
umid = 0
#print()
def gerar_dados():
    return randint(0,50), randint(40,100)




while True:
    print("Coletando dados..")
    temp, umid = gerar_dados()
    print("Temperatura: {}, Umidade: {}".format(temp, umid))
    conn = urllib.request.urlopen(baseURL+'&field1=%s&field2=%s'%(temp, umid))
    conn.close()
    time.sleep(60)
'''
# Define o tipo de sensor
sensor = Adafruit_DHT.DHT11
#sensor = Adafruit_DHT.DHT22
GPIO.setmode(GPIO.BOARD)
 
# Define a GPIO conectada ao pino de dados do sensor
for x in range(20,31):
    pino_sensor = x
    print(f"Testando o pino {x}")
 
# Informacoes iniciais
    print("* Lendo os valores de temperatura e umidade")
 
    if(True):
   # Efetua a leitura do sensor
        umid, temp = Adafruit_DHT.read_retry(sensor, pino_sensor);
        print(umid, temp)
   # Caso leitura esteja ok, mostra os valores na tela
 
        if umid is not None and temp is not None:
            print ("Temperatura = {0:0.1f}  Umidade = {1:0.1f}n").format(temp, umid);
            print ("Aguarda 5 segundos para efetuar nova leitura...n");
            time.sleep(1)
        else:
     # Mensagem de erro de comunicacao com o sensor
            print("Falha ao ler dados do DHT11 !!!")
'''