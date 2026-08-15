#try and except block
#ZeroDivisionError
try:
    num=10/0
except ZeroDivisionError:
    print("enter a denominator greather than 0")

try:
    num=10/0
except ZeroDivisionError as ex:
    print(f"error : {ex}")

#NameError
try:
    a=b
except:
    print("name error")
    
    
try:
    a=b
except NameError as ex:
    print(f"error : {ex}")
    
#try, except and else:
try:
    num=int(input("enter a number : "))
    result=24/num    
except ZeroDivisionError:
    print("enter a denominator greather than 0")
except Exception as ex:
    print(ex)
else:
    print(result)
    
    
#try,except,else and finally
try:
    num=int(input("enter a number : "))
    result=24/num    
except ZeroDivisionError:
    print("enter a denominator greather than 0")
except Exception as ex:
    print(ex)
else:
    print(result)
finally:
    print("executed successfully")
    
    
try:
    file=open('file_handling\sample.txt','r')
    content=file.read()
    a=b
except FileNotFoundError as ex:
    print(ex)
except Exception as ex1:
    print(ex1)
else:
    print(content)
finally:
    if 'file' in locals() and not file.closed:
        file.close()
        print("file successfully closed")
    
