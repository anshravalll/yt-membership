import threading
import time
import concurrent.futures

def arra_operation():
    a= 5
    for i in range(5):
        a += 1
        time.sleep(1)
    print(a)

with concurrent.futures.ThreadPoolExecutor(max_workers=2) as fufufu:
    fufufu.submit(arra_operation)
    

print("hi")

#world: shared resource access: 

