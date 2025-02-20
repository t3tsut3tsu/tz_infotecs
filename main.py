import argparse
import requests
import time

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
        cnt_err = 0
        pinging = []
        print('------------------------------------')
        print(f'Host: {host}')
        for _ in range(args.counts):
            try:
                start_ping = time.time() #начало запроса
                response = requests.get(host)
                end_ping = time.time() #конец запроса
                ping = end_ping - start_ping
                pinging.append(ping)
                if response.status_code == 200:
                    cnt_suc += 1
                elif response.status_code == 400 or response.status_code == 500:
                    cnt_fail += 1
                #print(f'The answer is: {response.status_code} for {host}') #отладка
            except requests.exceptions.ConnectionError:
                print(f'Dns lookup failed for {host}')
                cnt_err += 1
            except requests.exceptions.ReadTimeout:
                print(f'Read timeout for {host}')
                cnt_err += 1
        if pinging:
            print(f'Min: {round(min(pinging), 3)}')
            print(f'Max: {round(max(pinging), 3)}')
            print(f'Avg: {round((sum(pinging)/args.counts), 3)}')
        print(f'Success: {cnt_suc}')
        print(f'Failed: {cnt_fail}')
        print(f'Errors: {cnt_err}')

args = arg_parser()
response_getting(args)