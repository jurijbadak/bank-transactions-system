# Bank Transactions System

## Überblick
Dieses Projekt implementiert ein System zur Verarbeitung von Banktransaktionen mit Kafka für Messaging, Spark für Stream-Verarbeitung und einem Microservice-Ansatz.

## Komponenten
- **Zookeeper**: Manages Kafka Broker.
- **Kafka**: Messaging-System für die Verarbeitung von Transaktionen.
- **Producer**: Generiert und sendet Transaktionsdaten an Kafka.
- **Consumer**: Verarbeitet Transaktionsdaten von Kafka.
- **Spark**: Führt Stream-Verarbeitung auf Transaktionsdaten durch.

## Setup und Ausführung
Um das Bank-Transaktionssystem einzurichten und auszuführen, folgen Sie diesen Schritten:

Vorbereitung der Umgebung:

Stellen Sie sicher, dass Docker und Docker Compose auf Ihrem System installiert sind, da das Projekt in Docker-Containern ausgeführt wird.
Installieren Sie Apache Kafka und Apache Spark, falls diese noch nicht installiert sind. Diese sind für das Datenstreaming und die Datenverarbeitung erforderlich.
Klonen des Projekts:

Klonen Sie das Repository des Projekts von GitHub oder einem anderen Versionierungssystem auf Ihren lokalen Computer.
Konfiguration:

Überprüfen Sie die Konfigurationsdateien, insbesondere docker-compose.yml, um sicherzustellen, dass alle Dienste korrekt konfiguriert sind.
Passen Sie bei Bedarf die Konfigurationseinstellungen an, z.B. Portnummern oder Umgebungsvariablen.
Starten der Docker-Container:

Öffnen Sie ein Terminal und navigieren Sie zum Hauptverzeichnis des Projekts.
Führen Sie docker-compose up aus, um die Docker-Container für Kafka, Zookeeper, die Microservices und alle anderen erforderlichen Dienste zu starten.
Ausführen der Microservices:

Starten Sie den Producer-Service, der Transaktionsdaten generiert und an Kafka sendet.
Starten Sie den Consumer-Service, der Transaktionsdaten von Kafka liest und verarbeitet.
Diese Services können direkt in ihren jeweiligen Docker-Containern ausgeführt werden.
Spark-Streaming-Job starten:

Führen Sie den Spark-Streaming-Job aus, der die Daten aus Kafka liest und verarbeitet. Dieser Job führt Echtzeit-Analysen und -Verarbeitungen der Transaktionsdaten durch.
Überwachung und Wartung:

Überwachen Sie die Systemlogs, um sicherzustellen, dass alle Komponenten ordnungsgemäß funktionieren.
Nehmen Sie bei Bedarf Anpassungen oder Updates an den Services oder der Konfiguration vor.
Herunterfahren des Systems:

Wenn das System nicht mehr benötigt wird, können Sie die Docker-Container mit docker-compose down sicher herunterfahren.

## Lizenz
Fügen Sie Informationen zur Lizenzierung Ihres Projekts hinzu.
