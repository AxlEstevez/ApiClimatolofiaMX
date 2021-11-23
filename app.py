import urllib3
import io
import gzip
import json

http = urllib3.PoolManager()
response = http.request(
    "Get",
    "https://smn.conagua.gob.mx/webservices/?method=1",
    headers={
        "Accept-Encoding": "gzip",
    }
)
gzipFile = io.BytesIO(response.data)
raw_data = gzip.decompress(gzipFile.read())
json_data = json.loads(raw_data)

