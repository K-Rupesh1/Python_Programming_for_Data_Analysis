#write
with open('file_handling\sample.txt','w+') as file:
    content=file.write('hello i am rupesh?')
    print(content)
    
#writelines

with open('file_handling\sample.txt','w+') as file:
    content=file.writelines('how are you \n what are you doing')
    print(content)
