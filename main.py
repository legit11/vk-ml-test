import json
import logging
from collections import defaultdict
from typing import List, Dict

from kafka import KafkaConsumer, KafkaProducer

from processor import TDocument, Processor

logging.basicConfig(level=logging.INFO)             # логи
logger = logging.getLogger(__name__)


consumer = KafkaConsumer(               # Kafka
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
    try:
        incoming_documents = [TDocument(**doc) for doc in message.value]

        for doc in incoming_documents:
            documents_by_url[doc.url].append(doc)

        for url, docs in documents_by_url.items():
            processed_doc = processor.process(docs)
            producer.send('output_topic', processed_doc.dict())
            logger.info(f"Processed Document for URL {url}: {processed_doc}")

        documents_by_url.clear()
    except Exception as e:
        logger.error(f"Error processing message: {e}", exc_info=True)


