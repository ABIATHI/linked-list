class node:
  def __init__(self,d):
    self.data=d
    self.addrs=None
class sll:
  def __init__(self):
    self.head=None
slo=sll()
slo.head=node("MON")
n2=node("TUE")    
n3=node("WED")
n4=node("THU")
n5=node("FRI")
n6=node("SAT")
n7=node("SUN")
slo.head.addrs=n2
n2.addrs=n3
n3.addrs=n4
n4.addrs=n5
n5.addrs=n6
n6.addrs=n7
temp=slo.head
while temp!=None:
  print(temp.data)
  temp=temp.addrs
