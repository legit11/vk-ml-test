from typing import List, Optional
from pydantic import BaseModel

class TDocument(BaseModel):
    url: str
    pub_date: int
    fetch_time: int
    text: str
    first_fetch_time: Optional[int] = None

    class Config:
        allow_mutation = False
        anystr_strip_whitespace = True

class Processor:
    def process(self, documents: List[TDocument]) -> TDocument:
        if not documents:
            raise ValueError("No documents to process")

        documents.sort(key=lambda doc: doc.fetch_time)              # Сортировка по fetch_time
        latest_fetch_doc = documents[-1]                # Документ с последним fetch_time
        earliest_fetch_doc = documents[0]               # Документ с первым fetch_time

        return TDocument(               # Возвращаем документ соответствующий условиям
            url=latest_fetch_doc.url,
            pub_date=earliest_fetch_doc.pub_date,
            fetch_time=latest_fetch_doc.fetch_time,
            text=latest_fetch_doc.text,
            first_fetch_time=earliest_fetch_doc.fetch_time
        )

