# -*- coding: utf-8 -*-
"""
Created on Sun Feb 20 04:34:47 2022

@author: User
"""
def twoscomplement(number):
    number=str(number)  #nofinish
    onescom=""
    for char in number:
        if char=="0":
            onescom="1"+onescom
        else:
            onescom="0"+onescom
    
    twoscom=""
    reminder="1"
    if onescom[0]=="0":
        for char in onescom:
            twoscom=char+twoscom
        twoscom=list(twoscom)
        twoscom[-1]="1"
        twoscom=str(' '.join(twoscom)).replace(" ","")
   
    if onescom[0]=="1":
        for char in onescom:
            if char=="1"and reminder=="1":
                twoscom="0"+twoscom
                reminder="1"
            elif char=="0"and reminder=="1":
                twoscom="1"+twoscom
                reminder="0"
            else:
                twoscom=char+twoscom
    return twoscom
        
    
def binaryaddtional(number1, number2):
    number1=(str(number1))[::-1] #reverse string
    number2=(str(number2))[::-1]
    reminder="0"
    result=""
    for char1, char2 in zip(number1, number2):
        if char1=="1"and char2=="1"and reminder=="0":
            result="0"+result
            reminder="1"
        elif char1=="1"and char2=="1"and reminder=="1":
            result="1"+result
            reminder="1"
        elif char1=="0"and char2=="0"and reminder=="0":
            result="0"+result
            reminder="0"
        elif char1=="0"and char2=="0"and reminder=="1":
            result="1"+result
            reminder="0" 
        elif char1=="0"and char2=="1"and reminder=="0":
            result="1"+result
            reminder="0"
        elif char1=="0"and char2=="1"and reminder=="1":
            result="0"+result
            reminder="1"
        elif char1=="1"and char2=="0"and reminder=="0":
            result="1"+result
            reminder="0"
        elif char1=="1"and char2=="0"and reminder=="1":
            result="0"+result
            reminder="1"
        
        
    return result
    
    
    
    

dividend= input("Enter decimal Dividend from 8 bits range: ")
divisor= input("Enter decimal Divisor from 8 bits range: ")
dividend=int(dividend)
divisor=int(divisor)
print("decimal number:",dividend,"/",divisor)
dividend_signbit=0
divisor_signbit=0
if dividend<0:
    dividend_signbit=1
if divisor<0:
    divisor_signbit=1

dividend_bin=abs(dividend)
dividend_bin=str(bin(dividend_bin)[2:])
divisor_bin=abs(divisor)
divisor_bin=str(bin(divisor_bin)[2:])


if len(dividend_bin)<8:
        while(len(dividend_bin)!=8):
            dividend_bin="0"+dividend_bin
if len(divisor_bin)<8:
        while(len(divisor_bin)!=8):
            divisor_bin="0"+divisor_bin

negativeM=twoscomplement(divisor_bin)    
A="00000000"
Q=dividend_bin
M=divisor_bin

    
print("A=",A,"Q=",Q,"M=",M,"-M=",negativeM)

A=list(A)
Q=list(Q)
count=0
while (count<8):
    #shift
    shiftchar=Q[0]
    A.pop(0)
    A.append(shiftchar)
    Q.pop(0)
    Q.append("0")
    
    
    #A=A-M
    A=str(' '.join(A)).replace(" ","")
    newA=binaryaddtional(A, negativeM)
    A=list(newA)
    
    
    #a<0? 
    # no
    if A[0]=="0":
        Q[-1]="1"
        
    elif A[0]=="1":
        Q[-1]="0"
        A=str(' '.join(A)).replace(" ","")
        newA=binaryaddtional(A,M)
        A=list(newA)
    
    # yes
    
    #print(A,Q)
    
    count=count+1

A=str(' '.join(A)).replace(" ","")
Q=str(' '.join(Q)).replace(" ","")
A1=A
Q1=Q
Sign_mag=Q1
A=int(A, 2)
Q=int(Q, 2)
if dividend_signbit==1 and divisor_signbit==0:
    Q=-abs(Q)
    Sign_mag=list(Q1)
    Sign_mag[0]="1"
    Sign_mag=str(' '.join(Sign_mag)).replace(" ","")
elif dividend_signbit==0 and divisor_signbit==1:
    Q=-abs(Q)
    Sign_mag=list(Q1)
    Sign_mag[0]="1"
    Sign_mag=str(' '.join(Sign_mag)).replace(" ","")
    
print("After final cycle:")
print("A=",A1,"Q=",Q1,"Sign/magnitude is",Sign_mag ,"2S COMPLEMENT is",twoscomplement(Q1))
print(Q,"R",A)  





        


