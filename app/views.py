from unittest import skip
from django.shortcuts import render
from .models import Terminals
from datetime import datetime

# Create your views here.
def home(request):
  data = 'inputing...'
  context = {'data':data}
  return render(request,'base.html',context)

def alert(request):
  terminal = Terminals.objects.raw("SELECT id,switch,'ping lost' as 'pingType',from_unixtime(ts) as 'times' FROM nosairis.app_terminals where t1 = 0 and t2 = 0 and t3 = 0 and t4 = 0 and t5 = 0")
  
  context = {'data':terminal}
  return render(request,'alert.html',context)

def graph(request):
  label1=[]
  data1 = []
  terminal1 = Terminals.objects.raw("SELECT * FROM nosairis.app_terminals WHERE switch = 'S1'")
  for i in terminal1:
    tsh = datetime.fromtimestamp(i.ts).strftime('%H')
    tsm = datetime.fromtimestamp(i.ts).strftime('%M')
    realts = datetime.fromtimestamp(i.ts).strftime("%d/%m/%Y, %H:%M")
    if(tsh == "00" or tsh == '06' or tsh == '12' or tsh == '18'):
      if i.t1 == 0 and i.t2 == 0 and i.t3 == 0 and i.t4 == 0 and i.t5 == 0:
        data1.append(0)
        label1.append(realts)
      else:
        data1.append(1)
        label1.append(realts)
    else:
      skip
  
  min1 = min(data1)
  max1 = max(data1)
  avg1 = round(data1.count(1) / (data1.count(1) + data1.count(0)),4)
      
  label2=[]
  data2 = []
  terminal2 = Terminals.objects.raw("SELECT * FROM nosairis.app_terminals WHERE switch = 'S2'")
  for i in terminal2:
    tsh = datetime.fromtimestamp(i.ts).strftime('%H')
    tsm = datetime.fromtimestamp(i.ts).strftime('%M')
    realts = datetime.fromtimestamp(i.ts).strftime("%d/%m/%Y, %H:%M")
    if(tsh == "00" or tsh == '06' or tsh == '12' or tsh == '18'):
      if i.t1 == 0 and i.t2 == 0 and i.t3 == 0 and i.t4 == 0 and i.t5 == 0:
        data2.append(0)
        label2.append(realts)
      else:
        data2.append(1)
        label2.append(realts)
    else:
      skip
  
  min2 = min(data2)
  max2 = max(data2)
  avg2 = round(data2.count(1) / (data2.count(1) + data2.count(0)),4)
      
  label3=[]
  data3 = []
  terminal3 = Terminals.objects.raw("SELECT * FROM nosairis.app_terminals WHERE switch = 'S3'")
  for i in terminal3:
    tsh = datetime.fromtimestamp(i.ts).strftime('%H')
    tsm = datetime.fromtimestamp(i.ts).strftime('%M')
    realts = datetime.fromtimestamp(i.ts).strftime("%d/%m/%Y, %H:%M")
    if(tsh == "00" or tsh == '06' or tsh == '12' or tsh == '18'):
      if i.t1 == 0 and i.t2 == 0 and i.t3 == 0 and i.t4 == 0 and i.t5 == 0:
        data3.append(0)
        label3.append(realts)
      else:
        data3.append(1)
        label3.append(realts)
    else:
      skip
      
  min3 = min(data3)
  max3 = max(data3)
  avg3 = round(data3.count(1) / (data3.count(1) + data3.count(0)),4)
  
  context = {
    'data1':data1,
    'label1':label1,
    'data2':data2,
    'label2':label2,
    'data3':data3,
    'label3':label3,
    'min1':min1,
    'max1':max1,
    'avg1':avg1,
    'min2':min2,
    'max2':max2,
    'avg2':avg2,
    'min3':min3,
    'max3':max3,
    'avg3':avg3
    }
  return render(request,'graph.html',context)