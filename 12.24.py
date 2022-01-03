from . import calculator



print("두자리 정수에 대한 사칙연산을 입력하세요: (예) 12 + 22:")
str_input=input()
list_input=str_input.split(" ")

int_X=int(list_input[0])
int_Y=int(list_input[2])

if list_input[1]=='+':
    result=calculator.plus(int_X,int_Y)
elif list_input[1]=='-':
    result=calculator.minus(int_X,int_Y)    
elif list_input[1]=='*':
    result=calculator.multiply(int_X,int_Y)   
elif list_input[1]=='/':
    result=calculator.divide(int_X,int_Y)   
print("결과: {0} {1} {2}= {3}".format(list_input[0],list_input[1],list_input[2],result))