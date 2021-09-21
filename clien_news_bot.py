import requests
from bs4 import BeautifulSoup as bs
import os
from logg import *
from time import sleep
import json

base = os.path.join(os.path.dirname(os.path.abspath(__file__)),'')

def get_home() -> str:
    r = requests.get('https://www.clien.net/service/board/news').content.decode('utf-8')
    return r

def parse_home(s :str) -> dict:
    d = dict()
    history = read_history()
    s_bs = bs(s, 'html.parser')
    list_content = s_bs.find('div', class_='list_content')
    list_item = list_content.find_all('div', class_='list_item')
    for item in list_item:
        sn = item['data-board-sn'] # addition point should be post-post
        title = item.find('a', class_='list_subject').get_text().strip()
        href = item.find('a', class_='list_subject')['href'] # partial
        if sn in history:
            continue
        else:
            d[title] = href
            add_to_history(str(sn))
    return d

def read_history() -> list:
    with open(os.path.join(base, 'history.db')) as f:
        history = [x.strip() for x in f.read().split('\n') if x != '']
    return history

def add_to_history(s :str):
    with open(os.path.join(base, 'history.db'), 'a') as fa:
        fa.write('\n' + s)

def sort_history():
    history = read_history()
    history.sort()
    cand = list()
    for hist in history:
        if hist not in cand:
            cand.append(hist)
    with open(os.path.join(base, 'history.db'), 'w') as fw:
        fw.write('\n'.join(cand))

def parse_body(s :str) -> str: # TODO if media inside
    s_bs = bs(s, 'html.parser')
    main_body = s_bs.find('div', class_='post_article')
    ps = main_body.find_all('p')
    res = str()
    for p in ps:
        if p.get_text().strip() == 'LINK':
            continue
        res += '\n' + p.get_text().strip()
    res = res.strip()
    return res

def send_toot(m): # TODO if media inside
    with open(os.path.join(base, 'config.json')) as f:
        j = json.load(f)
        acc = j['id'] # acc
    head = {'Authorization': 'Bearer ' + acc}
    data = dict()
    data['status'] = m
    data['visibility'] = 'unlisted' # local rule
    requests.post('https://twingyeo.kr/api/v1/statuses', headers=head, data=data)

if __name__=='__main__':
    res = get_home()
    d_ = parse_home(res)
    for di in d_:
        href = 'https://clien.net' + d_[di]
        r2 = requests.get(href).content.decode('utf-8')
        m = parse_body(r2)
        if len(m) + len(href) + 8 > 500:
            m = m[:500-len(href)-9]
        m += '…\n\nvia: ' + href
        logger.debug('m: ' + str(m))
        send_toot(m)
        sleep(10)
    sort_history()
    os.system('/bin/bash ' + base + 'tail.sh')
