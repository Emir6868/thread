import time
import threading

if __name__ == '__main__':
    try:
        a = float(input("a: "))
        b = float(input("b: "))
        res = a/b
    except ValueError as err:
        print(f"Please enter a float: {err}")
    except ZeroDivisionError as err:
        print("b should not be 0: {err}")
    else:
        print(res)



def task(i):
    print(f"Task {i} starts")
    time.sleep(1)
    print(f"Task {i} ends")
start = time.perf_counter()
task(1)
task(2)
end = time.perf_counter()
for i in range(100):
    thread = threading.Thread(target=task, args=[i])
    thread .start()
print(f"Tasks ended in {round(end -start, 2)} second(s)")


