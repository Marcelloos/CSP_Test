from multiprocessing import Process , Pool
import sys
import time
from cpu_usage import CPU
from Ram_usage import RAM
from bytesRecieved import bytesR
#import Ram_usage

cpu_temp = CPU()
ram_per = RAM()
bytese = bytesR
def func1():
    print("start cpu : ")
    cpu_temp.get_Cpu_Persentage()
    ram_per.get_Ram_Persentage()
    bytese.get_bytes_recieved()

#def func2():
  #  print("start ram : ")
   # ram_per = RAM()
   # ram_per.get_Ram_Persentage()

#def func3():
   # print("start bytes : ")
   # bytese = bytesR
   # bytese.get_bytes_recieved()
    


if __name__=='__main__':
    #cpu_temp = CPU()
    p = Pool(5)
    p.map(func1)
   # p1 = Process(target = func1)
   # p1.start()
   # p2 = Process(target = func2)
   # p2.start()
   # p3 = Process(target = func4)
   # p3.start()
  #  p1.join()
   # p2.join()
    #p3.join()
