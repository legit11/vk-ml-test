from typing import List, Optional


class TDocument:
    def __init__(self, url: str, pub_date: int, fetch_time: int, text: str, first_fetch_time: Optional[int] = None):
        self.url = url
        self.pub_date = pub_date
        self.fetch_time = fetch_time
        self.text = text
        self.first_fetch_time = first_fetch_time

    def to_dict(self):
        return {
            "url": self.url,
            "pub_date": self.pub_date,
            "fetch_time": self.fetch_time,
            "text": self.text,
            "first_fetch_time": self.first_fetch_time
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            url=data["url"],
            pub_date=data["pub_date"],
            fetch_time=data["fetch_time"],
            text=data["text"],
            first_fetch_time=data.get("first_fetch_time")
        )


class Processor:
    def process(self, documents: List[TDocument]) -> TDocument:
        if not documents:
            raise ValueError("No documents to process")


        documents.sort(key=lambda doc: doc.fetch_time)              # Сортировка по fetch_time


        latest_fetch_doc = documents[-1]                # Документ с последним fetch_time


        earliest_fetch_doc = documents[0]               # Документ с первым fetch_time


        result_doc = TDocument(                 # Создаем новый документ с необходимыми полями
            url=latest_fetch_doc.url,
            pub_date=earliest_fetch_doc.pub_date,
            fetch_time=latest_fetch_doc.fetch_time,
            text=latest_fetch_doc.text,
            first_fetch_time=earliest_fetch_doc.fetch_time
        )

        return result_doc
