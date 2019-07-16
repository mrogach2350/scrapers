import json
from helpers import group_counter, parse_url, search_by_group
import pandas as pd

json_data = json.loads(open('./name_url_data.json').read())
urls = list(map(lambda obj: obj.get('href'), json_data))
parsed_urls = []


class ParsedUrl:
    def __init__(self, n, g):
        self.name = n
        self.group = g

    def return_dict(self):
        return {
            'name': self.name,
            'group': self.group
        }


for idx, url in enumerate(urls[:-3]):
    group = parse_url(url).get('group')
    name = parse_url(url).get('name')
    if group is not None and name is not None:
        newItem = ParsedUrl(n=name, g=group)
        parsed_urls.append(newItem)


# races = list(map(lambda a: a.group == 'Races' if a else None, parsed_urls))
print(parsed_urls[0])
filtered_items = search_by_group(url_items=parsed_urls, target_group="Races")
cd = group_counter(filtered_items)
df = pd.DataFrame(cd.items(), columns=['name', 'count'])

df.to_csv('group_counter.csv')
# for idx, url in enumerate(urls):
#     if parse_url(url).get('name'):
#         print(group_counter)
