import os

os.system("clear")
print("1- Encode message inside photo ..")
print("                                          ")
print("2- Decode the photo to get the message ..")
print("""
    """)
ch = input(" What do you wanna do ? ")
if ch =="1":
    imagefile = input(' drop your image  : ')
    m = input (' drop your message :')
    os.system('echo "          " >> '+imagefile)
    os.system('echo "'+m+'" >> '+imagefile)
#DECODE
elif ch == "2" :
    imagefile = input(' drop your image  : ')
    print("                                 ")
    os.system("tail -1 "+imagefile)   
else:
    print("are you kidding me ? of course Error")