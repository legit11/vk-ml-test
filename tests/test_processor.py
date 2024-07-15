import unittest
from app.models import TDocument
from app.processor import Processor

class TestProcessor(unittest.TestCase):
    def test_document_processing(self):
        documents = [
            TDocument(url="http://example.com", pub_date=1, fetch_time=2, text="Old Version"),
            TDocument(url="http://example.com", pub_date=3, fetch_time=5, text="New Version")
        ]

        processor = Processor()
        processed_doc = processor.process(documents)

        self.assertEqual(processed_doc.text, "New Version")
        self.assertEqual(processed_doc.pub_date, 3)
        self.assertEqual(processed_doc.first_fetch_time, 2)

if __name__ == '__main__':
    unittest.main()
