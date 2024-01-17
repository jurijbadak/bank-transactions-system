from kafka import KafkaProducer
import json
import time
import random

# Kafka Producer konfigurieren
producer = KafkaProducer(
    bootstrap_servers=['localhost:9092'],
    value_serializer=lambda x: json.dumps(x).encode('utf-8'))

# Zufällige Transaktionsdaten generieren und an Kafka senden
while True:
    transaction = {
        'date': time.strftime("%Y-%m-%d"),
        'time': time.strftime("%H:%M:%S"),
        'amount': random.randint(1, 10000),
        'currency': random.choice(["EUR", "USD", "GBP", "JPY", "CHF"]),
        'sender': random.randint(10000000, 99999999),
        'receiver': random.randint(10000000, 99999999),
        'type': random.choice(["deposit", "withdrawal", "transfer", "payment"]),
        'status': random.choice(["success", "failure", "pending"])
    }
    producer.send('bank-transactions', value=transaction)
    print(f"Gesendete Transaktion: {transaction}")
    time.sleep(1)