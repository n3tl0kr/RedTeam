import requests
import argparse
import urllib3
import httplib2

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--infile', type=argparse.FileType('r', encoding='UTF-8'),
                        required=True)
    args = parser.parse_args()
    infile = args.infile

    print("Working with:", infile.name)

for url in infile:
    url = url.rstrip('\n')
    r = requests.options(url, verify=False)
    if 'Allow' in r.headers:
        methods = r.headers['Allow']
    else:
        methods = "none"
    print(url, ": " + methods)

args.infile.close()
