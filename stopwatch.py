from datetime import *
def stopwatch():
    start_time=datetime.now()
    input("press enter to stop the stopwatch.....")
    end_time=datetime.now()
    elapsed_time=end_time-start_time
    print(elapsed_time)

stopwatch()

