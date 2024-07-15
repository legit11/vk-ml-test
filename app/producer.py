from kafka import KafkaProducer
import json
from app.models import TDocument

producer = KafkaProducer(
    bootstrap_servers='kafka:9092',
    value_serializer=lambda v: json.dumps(v.dict()).encode('utf-8')
)

def send_document(doc: TDocument):
    producer.send('documents', value=doc)
    producer.flush()
