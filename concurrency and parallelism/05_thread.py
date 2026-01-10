import threading
import time

def prepare_order(type_, wait_time):
    print(f"{type_} order: Getting ready")
    time.sleep(wait_time)
    print(f"{type_} order: ready")
    
t1= threading.Thread(target=prepare_order, args = ("Bao", 2))
t2 = threading.Thread(target= prepare_order, args=("Kung pao", 3))

t1.start()
t2.start()
t1.join()
t2.join()