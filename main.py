from kafka import KafkaConsumer, KafkaProducer
import json
from processor import TDocument, Processor
from collections import defaultdict
from typing import List, Dict


consumer = KafkaConsumer(               #Kafka
    'input_topic',
    bootstrap_servers=['localhost:9092'],
    value_deserializer=lambda m: json.loads(m.decode('utf-8'))
)

producer = KafkaProducer(
    bootstrap_servers=['localhost:9092'],
    value_serializer=lambda m: json.dumps(m).encode('utf-8')
)

processor = Processor()


documents_by_url: Dict[str, List[TDocument]] = defaultdict(list)                # Основной цикл обработки

for message in consumer:
    incoming_documents = [TDocument.from_dict(doc) for doc in message.value]


    for doc in incoming_documents:              # Группировка по URL
        documents_by_url[doc.url].append(doc)


    for url, docs in documents_by_url.items():              # Обработка каждой группы документов
        processed_doc = processor.process(docs)
        producer.send('output_topic', processed_doc.to_dict())
        print(f"Processed Document for URL {url}: {processed_doc}")


    documents_by_url.clear()            # Очистка после обработки

