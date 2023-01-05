import datetime

def pace_calculator():
    circuit = int(input("Please input how long is one lap in meters: "))
    distance = int(input("Please input the distance that you are running in meters: "))
    target = input("What is your target total time: ")
    # for target input in the form of min:sec e.g. 25:00
    my_dict = {}
    time_list = target.split(':')
    sec_total = int(time_list[0])*60+int(time_list[1])
    speed_req = distance/sec_total
    for i in range(distance//circuit):
        sec = circuit/speed_req*(i+1)
        my_dict['circuit'+str(i)] = str(datetime.timedelta(seconds=sec))
    if distance//circuit != distance/circuit:
        my_dict['last circuit'] = str(datetime.timedelta(seconds=sec_total))
    return my_dict
