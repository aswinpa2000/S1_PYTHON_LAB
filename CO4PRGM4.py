#4. Create a class Time with private attributes hour, minute and second. Overload ‘+’ operator to find sum of 2 time.

class Time:
    def __init__(self,h=0,m=0,s=0):
        self.__hours=h
        self.__minutes=m
        self.__seconds=s
        
        
    def __add__(self,other):
        t=Time()
        t.__seconds = self.__seconds+other.__seconds
        t.__minutes = self.__minutes+other.__minutes
        t.__hours = self.__hours+other.__hours
        if t.__seconds>=60:
            t.__minutes+=t.__seconds//60
            t.__seconds%=60
        if t.__minutes>=60:
            t.__hours+=t.__minutes//60
            t.__minutes%=60
        return t
        
    def __str__(self):
        return "%d:%d:%d"%(self.__hours,self.__minutes,self.__seconds)
		
hour=int(input("Enter the hour : "))
minute=int(input("Enter the minute : "))
second=int(input("Enter the second : "))
time1=Time(hour,minute,second)
print("............\n")
hour=int(input("Enter the hour : "))
minute=int(input("Enter the minute : "))
second=int(input("Enter the second : "))
time2=Time(hour,minute,second)

timesum=time1 + time2
print(timesum)



