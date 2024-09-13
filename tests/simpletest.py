import threading
import time

def arra_operation(b):
    a= b
    for i in range(5):
        a += 1
        time.sleep(1)
    print(a)

threaddd = threading.Thread(target = arra_operation)
threaddd.start()
threaddd.join()
print("hi")

