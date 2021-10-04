

import requests
import threading
import numpy as np
import pprint

urls = "https://order.dominos.ca/power/store/10354/coupon/{}?lang=en"


def check_codes(codes):
    for i in codes:
        combiend_urls = urls.format(i)

        response = requests.get(combiend_urls)

        if response.status_code != 404:
            conv_json = response.json()
            print(conv_json["Code"],conv_json["Price"],conv_json["Name"])
            #pprint.pprint(response.json())

numbers = list(range(0,9999))



thread_count = 30
threads = []

cut_up = np.array_split(numbers,thread_count)


for i in range(thread_count):
    print(i)
    t = threading.Thread(target=check_codes, args=(cut_up[i],))
    threads.append(t)
    t.start()

for i in threads:
    i.join()