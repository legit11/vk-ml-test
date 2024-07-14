from kafka import KafkaConsumer, KafkaProducer
import json
from processor import TDocument, Processor
from collections import defaultdict
from typing import List, Dict
import logging
from db import ClickHouseClient

# Настройка логирования
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('logs/app.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)


KAFKA_BOOTSTRAP_SERVERS = ['localhost:9092']                # Kafka
KAFKA_INPUT_TOPIC = 'input_topic'
KAFKA_OUTPUT_TOPIC = 'output_topic'

consumer = KafkaConsumer(
    KAFKA_INPUT_TOPIC,
    bootstrap_servers=KAFKA_BOOTSTRAP_SERVERS,
    value_deserializer=lambda m: json.loads(m.decode('utf-8'))
)

producer = KafkaProducer(
    bootstrap_servers=KAFKA_BOOTSTRAP_SERVERS,
    value_serializer=lambda m: json.dumps(m).encode('utf-8')
)

processor = Processor()
db_client = ClickHouseClient()


documents_by_url: Dict[str, List[TDocument]] = defaultdict(list)                # Основной цикл

for message in consumer:
    try:
        incoming_documents = [TDocument(**doc) for doc in message.value]

        for doc in incoming_documents:
            documents_by_url[doc.url].append(doc)

        for url, docs in documents_by_url.items():
            processed_doc = processor.process(docs)
            producer.send(KAFKA_OUTPUT_TOPIC, processed_doc.dict())
            logger.info(f"Processed Document for URL {url}: {processed_doc}")

            # Вставка обработанного документа в ClickHouse
            db_client.insert_document(processed_doc.dict())

        documents_by_url.clear()
    except Exception as e:
        logger.error(f"Error processing message: {e}", exc_info=True)



