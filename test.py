import threading
import time
import concurrent.futures
import requests
import multiprocessing

def task(i):
    print(f"Task {i} starts")
    time.sleep(1)
    print(f"Task {i} ends")
start = time.perf_counter()
t1 = threading.Thread(target=task, args=[1]) # création de la thread
t1.start() # je démarre la thread
t1.join() # j'attends la fin de la thread
end = time.perf_counter()
print(f"Tasks ended in {round(end - start, 2)} second(s)")

T = []

for i in range(100):
    T.append(threading.Thread(target=task, args=[i]))
for i in range(len(T)):
    T[i].start()


def task():
    print(f"Task starts for 1 second")
    time.sleep(1)
    print(f"Task ends")
if __name__ == '__main__':
    start = time.perf_counter()
    p1 = multiprocessing.Process(target=task)
    p2 = multiprocessing.Process(target=task)
    p1.start()
    p2.start()
    end = time.perf_counter()
    print(f"Tasks ended in {round(end - start, 2)} second(s)")

img_urls = ["https://cdn.pixabay.com/photo/2015/04/23/22/00/tree-736885__340.jpg"]
def download_image(img_url):
    img_bytes = requests.get(img_url).content
    img_name = img_url.split('/')[len(img_url.split('/'))-1]
    with open(img_name, 'wb') as img_file:
        img_file.write(img_bytes)
        print(f"{img_name} was downloaded")
start = time.perf_counter()
with concurrent.futures.ThreadPoolExecutor() as executor:
    executor.map(download_image, img_urls)
    end = time.perf_counter()
print(f"Tasks ended in {round(end - start, 2)} second(s)")