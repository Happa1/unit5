n = str(input("Please enter the message"))
count=0
error=True

for i in range(1, len(n)):
    if n[i]=='1':
        count+=1

if count%2!=int(n[0]):
    error=False

if error == True:
    print("This is an error message.")

else:
    print("This is not an error message.")