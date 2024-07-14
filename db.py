from clickhouse_driver import Client

class ClickHouseClient:
    def __init__(self, host='localhost', database='documents_db'):
        self.client = Client(host=host)
        self.database = database
        self.client.execute(f'CREATE DATABASE IF NOT EXISTS {self.database}')
        self.client.execute(f'USE {self.database}')
        self._create_table()

    def _create_table(self):
        self.client.execute('''
            CREATE TABLE IF NOT EXISTS documents (
                id UInt64,
                url String,
                pub_date DateTime,
                fetch_time DateTime,
                text String,
                first_fetch_time DateTime
            ) ENGINE = MergeTree()
            ORDER BY id;
        ''')

    def insert_document(self, document):
        query = '''
            INSERT INTO documents (id, url, pub_date, fetch_time, text, first_fetch_time) 
            VALUES (%(id)s, %(url)s, %(pub_date)s, %(fetch_time)s, %(text)s, %(first_fetch_time)s)
        '''
        self.client.execute(query, document)

    def get_documents_by_url(self, url):
        query = '''
            SELECT id, url, pub_date, fetch_time, text, first_fetch_time 
            FROM documents 
            WHERE url = %(url)s
        '''
        result = self.client.execute(query, {'url': url})
        return result


