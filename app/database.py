from clickhouse_driver import Client

from clickhouse_driver import Client
from typing import List
from app.models import TDocument

client = Client('clickhouse')

def save_document(doc: TDocument):
    query = '''
    INSERT INTO documents (Url, PubDate, FetchTime, Text, FirstFetchTime) VALUES (%s, %s, %s, %s, %s)
    '''
    client.execute(query, (doc.url, doc.pub_date, doc.fetch_time, doc.text, doc.first_fetch_time))

def get_documents_by_url(url: str) -> List[TDocument]:
    query = 'SELECT Url, PubDate, FetchTime, Text, FirstFetchTime FROM documents WHERE Url = %s'
    rows = client.execute(query, [url])
    return [TDocument(url=row[0], pub_date=row[1], fetch_time=row[2], text=row[3], first_fetch_time=row[4]) for row in rows]



