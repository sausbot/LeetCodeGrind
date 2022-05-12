'''
Interview Question

Print out characters at a fixed bitrate of 10kbps or 1250 chars/sec
'''
import time

def print_my_message(msg):
    # 1250 chars per second is desired printrate
    length = len(msg)
    is_finished = False

    index_1 = 0
    index_2 = 1250
    
    while not is_finished:
        if index_2 >= length:
            index_2 = length
            is_finished = True

        print (msg[index_1:index_2])

        index_1 = index_2
        index_2 += 1250

        # Could improve by taking the max of timedelta from start and 1 second
        # since the computation in the loop also takes some time
        time.sleep(1)

# test
print_my_message("hello world "*1250)