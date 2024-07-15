from app.models import TDocument
from app.producer import send_document

doc1 = TDocument(url="http://example.com", pub_date=1, fetch_time=2, text="Old Version")
doc2 = TDocument(url="http://example.com", pub_date=3, fetch_time=5, text="New Version")

send_document(doc1)
send_document(doc2)
