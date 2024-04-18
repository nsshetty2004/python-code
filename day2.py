#!/usr/bin/env python
# coding: utf-8

# In[6]:


Name=input("Enter the name: ")
age=int(input("Enter the age: "))

if age>=18:
    print(Name)
    print("person is eligible to vote")
else:
    print(Name)
    print("person is not eligible to vote")
    


# In[ ]:


int a,b;
printf("Enter the Two numbers:");
scanf("%d%d",&a,&b);
if(a>b)
 printf("%d is bigger than %d",a,b);
else 
printf("%d is bigger than %d",b,a);


# In[10]:


a= int(input())
b= int(input())
c= int(input())

if a>b:
    if a>c:
        print("a is Largest")
    else:
        print("c is Largest")
else:
     if b>c:
        print("b is Largest")
     else:
        print("c is Largest")


# In[ ]:





# In[1]:


marks=int(input("Enter the marks:"))
if marks>=90 and marks<=100:
    print("Grade = A+")
else:
    if marks>=80 and marks<90:
        print("Grade is A")
    else:
         if marks>=70 and marks<80:
                print("Grade is B+")
         else:
            if marks>=60 and marks<70:
                print("Grade is B")
            else:
                if marks>=50 and marks<60:
                    print("Grade is C")
                else:
                    if marks>=40 and marks<50:
                        print("Grade is D")
                    else:
                         if marks>=30 and marks<40:
                                print("Grade is E")
                         else:
                             if marks>=0 and marks<30:
                                    print("Grade is F")
                             else:
                                print("Invalid Input")
                


# In[ ]:


day = int(input("Enter the day number:"))
match day:
    case 1: print("Sunday")
    case 2: print("Monday")
    case 3: print("Tuesday")
    case 4: print("Wednesday")
    case 5: print("Thursday")
    case 6: print("Friday")
    case 7: print("Saturday")
    case _ if day == 10:
        print("Ten")
    case _ if day >=13 and day<=19:
        print("Teens")
    case _ : print("invalid")  


# In[ ]:


n=int(input("Enter the Number:"))
a=0
b=1
#a=int(input("Enter A value:"))
#b=int(input("Enter B Value:"))
print(a,b,end=" ")
for x in range(0,n-2):
    c=a+b
    a=b
    b=c
    print(c,end=" ")

