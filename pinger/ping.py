import os

def ping(ip):
    res = os.system("ping -c 4 -W 1 {} > /dev/null ".format(ip))
    return True if res == 0 else False