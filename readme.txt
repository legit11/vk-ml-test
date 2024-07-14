Тесты:
1. Настройка и запуск сервера Kafka, zookeeper(создание input_topic, output_topic)
2. Запуск main.py в PyCharm
3. Отправка тестовых сообщений в input_topic(
    Откройте новый терминал и перейдите в каталог Kafka
    Запуск консольного производителя сообщений:
    .\bin\windows\kafka-console-producer.bat --topic input_topic --bootstrap-server localhost:9092
    Ввод тестовых документов в формате JSON по типу: [
    {"url": "doc1", "pub_date": 2, "fetch_time": 4, "text": "Text4"},
    {"url": "doc1", "pub_date": 2, "fetch_time": 3, "text": "Text3"},
    {"url": "doc1", "pub_date": 2, "fetch_time": 1, "text": "Text1"},
    {"url": "doc1", "pub_date": 2, "fetch_time": 2, "text": "Text2"}
]
4. Проверка обработанных сообщений в output_topic:
    .\bin\windows\kafka-console-consumer.bat --topic output_topic --from-beginning --bootstrap-server localhost:9092

