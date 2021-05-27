import datetime
import os
import country_iterator
import re

WIKI_URL = 'https://en.wikipedia.org/wiki/'
COUNTRY_FILE_PATH = 'files/countries.json'
OUTPUT_FILE_PATH = 'files/wiki_links.txt'
LOG_FILE_PATH = 'files/log.txt'


def write_countries_to_file(url, path_to_input, path_to_output):
    if os.path.exists(path_to_output):
        os.remove(path_to_output)
    for link in country_iterator.CountryIterate(url, path_to_input):
        with open(path_to_output, 'a', encoding='utf-8') as f:
            f.write(f'{link}\n')
            f.close()


def decorator_with_path(log_file_path):

    def decorator(func):
        if os.path.exists(log_file_path):
            os.remove(log_file_path)

        def logger(*args, **kwargs):
            pattern_for_args = r'\({1}(.*)\){1}'
            result = func(*args, **kwargs)
            with open(log_file_path, 'a', encoding='utf-8') as f:
                f.write(f'{datetime.datetime.now()} вызвана функция "{func.__name__}" с аргументами args: '
                        f'{re.findall(pattern_for_args, str(args))}, kwargs: {kwargs}, возвращён результат: '
                        f'"{result}"\n')
            f.close()
            return result

        return logger

    return decorator


if __name__ == '__main__':
    write_countries_to_file(WIKI_URL, COUNTRY_FILE_PATH, OUTPUT_FILE_PATH)
