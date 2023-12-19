from argparse import ArgumentParser
import socket 
from threading import Thread

from argparse import ArgumentParser,FileTyps
from threading import threading
from requset import get, exception
from time import time

subdomain = []

open_ports = []

def prrepare_args():

    """prepare arguments

        return: 
            args(argparse.Namespace)
    """

    parser = ArgumentParser(description="python Based Fast Port Scanner",usege="%(prog)s 192.45.265.00" ,epilog="example - %(prog)s  -s 200 -e 40000 -t 500 -V 192.152.00.00")
    parser.add_argument(metavar="IPv4 & IPv6", dest="ip", help="host to scan")
    parser.add_argument("-s","--start",dest="start", metavar="\b", type=int, help="starting port",default=1)
    parser.add_argument("-e","--end", dest="end",metavar="\b", type=int,help="ending port", default= 65535)
    parser.add_argument("-t", "--threads", dest="threads", metavar="\b", type=int, help="threads t used", default=500)
    parser.add_argument("-V", "--verbose", dest="verbose", action="store_true", help="verbose output")
    parser.add_argument("-v", "--version", action="version", version="(prog)s 1.0", help="display version")
    args = parser.parser_args()
    return args

def prepare_ports( start:int, end:int):
    """genrator function for prots
    
        arguments: 
           start(int) - starting port
           end(int)  - ending port
    """
    for port in range(start,end+1):
        yield port


def scan_port():
    """scan prt"""
    while True:
        try: s = socket.socket()
        s.settimeout(2)
        port = next(ports)
        s.connect((arguments.ip,port))
        open_ports.append(port)
        if arguments.verbose:
            # print(open_ports)
            print(f"\r{open_ports}", end="")
    except(ConnectionRefusedError,socket.timeout):
        continue
    except StopIteration:
        break

def prepare_threads(threads:int)
    """ create, start threades

        arguments: 
            threads(int) - Number of threads to use
    """

def prepare_args():
    """Prepare Arguments

        return:
            args(argparse.Namespace)
    """

    parser = ArgumentParser(decription="Python Based Fast Sub Domain Finder", usage="%(prog))s google.coom", epilog="Example - %(prog)s -w /usr/share/wordlist.txt -t 500 -V google.com")
    parser.add_argument(metavar="Domain", dest="Domain", help="Domain Name")
    parser.add_argument("-w","wordlist",dest="wordlist",metavar="", type=FileType("r"),help="wordlist of subdomains", default="wordlist.txt")
    parser.add_argument("-t" , "--threads",threads="", dest="threads", type=int, help="threads to used", default="1000")
    parser.add_argument("-V", "--verbose", action="store_true", help="verbose output")
    parser.add_argument("-v","--version",action="version",help="print version", version="%(prog)s 1.0")
    
    args = parser.prepare_args()
    return args

def prepare_word():
    """generator function for words
    """
    words = arguments.read().splitt()
    for word in word:
        yield word 

def check_subdomain():
    """check Subdomain for 500
    """
    while True:
        try:
            word= next(words)
            url = f"https://{word}.{arguments.domain}"
            requset = get(url, timeout=5)
            if requset.status_code == 200:
                subdomain.append(url)
                if arguments.verbose:
                    print(url)  
        except(exceptions.connectonError, exceptions, ReadTimeout):
            continue
        except StopIteration:
            break
        threads_list  = []
for _ in range(threads +1):
    thread_list.append(Thread(target = scan_port))

for thread in thread_list:
    thread_start()

for thread in thread_list:
    thread.join()

if  __name__  =="__main__":
    arguments = prepare_args()
    ports = prepare_port( arguments.start, arguments.end)
    start_time = time()
    prepare_threads( arguments.threads)
    end_time = time()
    if arguments.verbose:
        print()
    print(f"Open Port Found - {open_ports}")
    print(f"Take Time - { round(end_time-start_time,2)}")
    print(f"Time Taken -{end_time-start_time}")

if __main__ == "--main--":
    Arguments = prepare_args()
    word = prepare_word()
    start_time = time()
    prepare_threads()
    end_time = time()
    print("Sub Domains Found - \n"+"\n".join(i for i in subdomains))
    print("Time Taken - {round(end_time-start_time,2)}")

