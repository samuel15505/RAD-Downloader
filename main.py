import sys
import requests
import re
from os import mkdir
from shutil import rmtree
import datetime
from bs4 import BeautifulSoup

main_page = 'https://www.nm.eurocontrol.int/RAD'

def get_airac_cycle():
    date = datetime.date.today()
    initial = datetime.date(2020, 1, 2)
    year_start = initial + datetime.timedelta((datetime.date(date.year, 1, 28) - initial).days // 28 * 28)
    month_part = (date - year_start).days // 28 + 1
    cycle = f'{date.year % 100}{month_part:02}'
    return cycle

def main():
    rmtree('RAD')
    try:
        mkdir('RAD')
    except OSError as error:
        print(error)
        exit()
    error_message = 'Cycle must be 4 digits, try again.'
    while True:
        cycle = input('Enter desired cycle or leave blank for current cycle: ')
        if cycle == '':
            cycle = get_airac_cycle()
            break
        if cycle.isdigit() == False:
            print(error_message)
            continue
        if len(cycle) != 4:
            print(error_message)
            continue
        break

    print(f'Ok, using cycle {cycle}.')

    r = requests.get(f'{main_page}/{cycle}/index.html')

    validate_code(r)

    soup = BeautifulSoup(r.content, 'html.parser')
    relative_paths = [link['href'] for link in soup.find_all(href = re.compile('doc'))]

    for path in relative_paths:
        file_name = path.split('/')[-1]
        print(f'Retrieving {file_name}')
        with open('RAD\\' + file_name, 'wb') as f:
            r = requests.get(f'{main_page}/{cycle}/{path}')
            validate_code(r)
            f.write(r.content)
        print('Done!')
    
    input()

def validate_code(r):
    if r.status_code != requests.codes.ok:
        sys.exit('Website returned an incorrect response')

if __name__ == '__main__':
    main()