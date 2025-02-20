import argparse
import requests

def arg_parser():
    parser = argparse.ArgumentParser(description="Simple HTTP servers tester")
    parser.add_argument('-H', '--hosts', nargs='+', help="Set hosts to test")
    parser.add_argument('-C', '--counts', type=int, help="Set number of requests")
    args = parser.parse_args()
    return args

def response_getting(args):
    for host in args.hosts:
        cnt_suc = 0
        cnt_fail = 0
        print(f'Host: {host}')
        for _ in range(args.counts):
            try:
                response = requests.get(host)
                print(f'Time: {response.elapsed.total_seconds()}')
                if response.status_code == 200:
                    cnt_suc += 1
                elif response.status_code == 400 or response.status_code == 500:
                    cnt_fail += 1
                #print(f'The answer is: {response.status_code} for {host}') #отладка
            except requests.exceptions.ConnectionError:
                print(f'Dns lookup failed for {host}')
            except requests.exceptions.ReadTimeout:
                print(f'Read timeout for {host}')
        print(f'Success: {cnt_suc}')
        print(f'Failed: {cnt_fail}')

args = arg_parser()
response_getting(args)