#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Carrega as bibliotecas
import Adafruit_DHT
import RPi.GPIO as GPIO
import time

# Define o tipo de sensor
sensor = Adafruit_DHT.DHT11

GPIO.setmode(GPIO.BOARD)

# Define a GPIO conectada ao pino de dados do sensor
pino_sensor = 25 # pino 22

# função para criar escrever no arquivo
def gravar_arquivo(texto):
        arq = open('/tmp/dht11.txt', 'w');
        arq.write(texto);
        arq.close();

# Informacoes iniciais
print ("*** Lendo os valores de temperatura e umidade");
texto = "";

while(1):
   # Efetua a leitura do sensor
   umidade, temperatura = Adafruit_DHT.read_retry(sensor, pino_sensor);
   # Caso leitura esteja ok, mostra os valores na tela
   if umidade is not None and temperatura is not None:
     texto = "ok;" + str(temperatura) + ";" + str(umidade);
     gravar_arquivo(texto);
     print ("Temperatura *C= {0:0.1f}  Umidade = {1:0.1f}").format(temperatura, umidade);
     print ("Aguarda 5 segundos para efetuar nova leitura...\n");
     time.sleep(5)
   else:
     # Mensagem de erro de comunicacao com o sensor
     print("Falha ao ler dados do DHT11 !!!")
     texto = "nok;";
