from kafka import KafkaConsumer
import json
from app.models import TDocument
from app.processor import Processor
from app.database import save_document, get_documents_by_url

def main():
    consumer = KafkaConsumer(
        'documents',
        bootstrap_servers='kafka:9092',
        value_deserializer=lambda m: TDocument(**json.loads(m.decode('utf-8')))
    )

    processor = Processor()

    for message in consumer:
        document = message.value
        existing_documents = get_documents_by_url(document.url)
        existing_documents.append(document)
        processed_doc = processor.process(existing_documents)
        save_document(processed_doc)

if __name__ == '__main__':
    main()






