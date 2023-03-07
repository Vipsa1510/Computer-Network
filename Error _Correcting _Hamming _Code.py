from scipy.optimize import fsolve
from math import log2
def solve_inequality(k):#Calculate the total no of r
    r = fsolve(lambda r: 2**r - (k+r+1), log2(k))
    return r[0]
def decimal_to_binary(n):
    if n == 0: 
        return [0]
    binary = []
    while n > 0:
        binary = [(n % 2)] + binary
        n //= 2
    return binary

#Sender
l = [] #Sender list
n = int(input("Enter the total data bits :"))
for i in range(n):
    b = int(input("Enter the bit for Sender:"))
    l.append(b)
r = int(solve_inequality(n))
rl = []

for i in range(r+1):
    l.insert((2**i)-1,0)
    rl.append((2**i)-1)#rl is redundant bit number of list


#Calculate the parity of each redundant bit    
k = -1
bi = []
for i in rl:
  a = []
  count = 0
  for j in range(i+1,len(l)+1):#Calculate the VRC bit
    bi = decimal_to_binary(j)
    try :
      if bi[k] == 1:
        a.append(j)
    except:
      pass
  for v in a: #Check the VRC bit is 1 or not 
    if l[v-1] == 1:
       count +=1 
  if count % 2 == 0:
        l[i] = 0
        
  else:
        l[i] = 1
  k = k - 1  

#Receiver
l1 = [] #Receiver list
for m in range(len(l)):
  re = int(input("Enter the bits for receiver : "))
  l1.append(re)
print("Bits from Sender Side : ",l)
print("Bits from Receiver Side : ",l1)
for m in rl:
  print("Redundant bit is : ",m+1)

#Compare redundant bit 
iscount = 0
for n in rl:
  if l1[n] == l[n]:
    iscount += 1
  else:
    iscount = 0
    break

#Check error is occure or not
e = [] #Not match redundant bit list
eno = []#Error bit list

if iscount == 0:
  print("Error")
  #Check which bit is error
  for n in rl:
    if l1[n] != l[n]:#Check which redundant bit is not match
      e.append(n)
  #Calculate VRC bit for not mached reduant bit
  for f in e:
    a = []
    count = 0
    kr = -(rl.index(f)+1)
    for j in range(f+1,len(l)+1):
      bi = decimal_to_binary(j)
      try :
        if bi[kr] == 1:
          a.append(j)
      except:
        pass
    #Check the bit which is not matched of Sender side 
    for v in a:
      if l1[v-1] != l[v-1]:
        eno.append(v-1)
  eno = list(set(eno)) # Remove the duplicates
  for n in eno:
      if rl.count(n):#Check the bit is redundant or not
        continue
      else:
        print("Error bit number : ",n+1)
     
else:
  print("No Error")