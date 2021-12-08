# Module for simulating dice throws
import random 

D4List = []
D6List = []
D8List = []
D10List = []
D12List = []
D20List = []
D100List = []

def throwD4(num):
    for numb in range(num):
        D4List.append(random.randint(1,4))       
 
def throwD6(num):
    for numb in range(num):
        D6List.append(random.randint(1,6))

def throwD8(num):
    for numb in range(num):
        D8List.append(random.randint(1,8))    
    
def throwD10(num):
    for numb in range(num):
        D10List.append(random.randint(1,10))
    
def throwD12(num):
    for numb in range(num):
        D12List.append(random.randint(1,12))

def throwD20(num):
    for numb in range(num):
        D20List.append(random.randint(1,20))

def throwD100(num):
    for numb in range(num):
        D100List.append(random.randint(1,100))
