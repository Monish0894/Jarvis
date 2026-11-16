n=input("enter the value")
if n==1:
    stop_flag=True
else:
    stop_flag=False

def my_function(stop_flag):
    while not stop_flag():
        print("Running...")
    
    print("Function stopped.")
