from typing import List, Optional
from app.models import TDocument



class Processor:
    def process(self, documents: List[TDocument]) -> TDocument:
        if not documents:
            raise ValueError("No documents to process")

        documents.sort(key=lambda doc: doc.fetch_time)              # Сортировка по fetch_time
        latest_fetch_doc = documents[-1]                # Документ с последним fetch_time
        earliest_fetch_doc = documents[0]               # Документ с первым fetch_time

        return TDocument(               # Возвращаем документ с необходимыми полями
            url=latest_fetch_doc.url,
            pub_date=earliest_fetch_doc.pub_date,
            fetch_time=latest_fetch_doc.fetch_time,
            text=latest_fetch_doc.text,
            first_fetch_time=earliest_fetch_doc.fetch_time
        )




