import argparse
import requests

def arg_parser():
    parser = argparse.ArgumentParser(description="Simple HTTP servers tester")
    parser.add_argument('-H', '--hosts', help="Set hosts to test")
    parser.add_argument('-C', '--counts', type=int, help="Set number of requests")
    args = parser.parse_args()
    return args

def response_getting(args):
    for _ in range(args.counts):
        try:
            response = requests.get(args.hosts)
            #print(f'The answer is: {response.status_code}') #отладка
        except requests.exceptions.ConnectionError:
            print('Dns lookup failed')
        except requests.exceptions.ReadTimeout:
            print('Read timeout')

args = arg_parser()
response_getting(args)