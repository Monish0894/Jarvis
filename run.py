import multiprocessing

# To run jarvis
def startjarvis():
    print("Process 1 is running.")
    from main import start
    start()



if __name__ =='__main__':
    p1 = multiprocessing.Process(target=startjarvis) 
    p1.start()
    p1.join()


    print("system stop")
