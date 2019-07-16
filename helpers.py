from urllib.parse import urlparse, parse_qs
import re

noNameCount = 0


def group_counter(url_items):
    counter = {}
    for idx, item in enumerate(url_items):
        if item.group in counter:
            counter[item.group] += 1
        else:
            counter[item.group] = 1

    return counter


def search_by_group(url_items, target_group):

    return filter(lambda i: i.group == target_group, url_items)


def parse_url(url):
    res = urlparse(url)
    group = res.path[1:-5]
    if parse_qs(res.query).get('ItemName') is not None:
        name = parse_qs(res.query).get('ItemName')[0]
    else:
        name = 'no name'

    return {
        'group': ' '.join(split_on_uppercase(group)),
        'name': name,
    }


def split_on_uppercase(s):
    fix_unchained = re.sub(r"(UC)", 'Unchained', s)
    string_array = re.sub(r"([A-Z])", r" \1", fix_unchained).split()
    return filter(lambda word: word != 'Display', string_array)
