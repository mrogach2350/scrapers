import json
from urllib.parse import urlparse, parse_qs

noNameCount = 0
def parse_url(url):
    res = urlparse(url)
    group = res.path[1:-5]

    if parse_qs(res.query).get('ItemName') is not None:
        name = parse_qs(res.query).get('ItemName')
    else:
        name = 'no name'

    return {
        'group': group,
        'name': name,
    }


json_data = json.loads(open('./name_url_data.json').read())
urls = list(map(lambda obj: obj.get('href'), json_data))

for url in urls:
    result = parse_url(url)



