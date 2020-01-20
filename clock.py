time=input("Enter time as hour:minute=")
time=time.split(':')
hour=int(time[0])
minute=int(time[1])
print(time)
print(hour)
print(minute)

if((minute/5)>6):
    angle=abs((hour-float((minute/5)))*30)
else:
    angle=abs((hour-(12-float((minute/5))))*30)
print("angle:",angle)    
  
   
