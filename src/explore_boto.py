from urllib.parse import urlparse

import boto3


def parse_s3_path(s3_path):
    parsed = urlparse(s3_path, allow_fragments=False)
    bucket = parsed.netloc
    key = parsed.path.lstrip("/")
    return bucket, key


def download(bucket, key):
    client = boto3.client('s3')
    with open('ids', 'wb') as f:
        client.download_fileobj(bucket, key, f)


download(*parse_s3_path("s3://karthik-dev-experiment/sample"))
for id in open('ids'):
    print(id)
