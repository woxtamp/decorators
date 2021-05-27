import json
from main import decorator_with_path, LOG_FILE_PATH


class CountryIterate:
    def __init__(self, url, path):
        self.url = url
        self.path = path

    def __iter__(self):
        with open(self.path, encoding='utf=8') as f:
            data = json.load(f)
            country_set = set()
            for item in data:
                country_set.add(item['name']['common'].replace(' ', '_'))
            self.country = iter(sorted(country_set))
            return self

    @decorator_with_path(LOG_FILE_PATH)
    def __next__(self):
        link = next(self.country)
        links = f'{link.replace("_", " ")} - {self.url + link}'
        return links
