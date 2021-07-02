# slowest key
def slowest_key(keyTimes):
    end_time=0
    char_with_longest_interval=None
    longest_time=0
    for i in range(len(keyTimes)):
        key_combination=keyTimes[i]
        #print("key combination: ", key_combination)
        start_time=keyTimes[i][1]  ##opposite in test i.e end_time=start_time
        interval=start_time-end_time    ##this will obviously opposite because of upper opposite allocation
        #print("interval: ", interval)
        end_time=start_time     ##this will obviously opposite because of upper opposite allocation
        #print("end time: ",end_time)
        if interval> longest_time:
            longest_time=interval
            #print("longest interval: ",longest_time)
            char_with_longest_interval=key_combination[0]
            ##in test because of change in key_combination here char_with...=key_combination[0]
    return chr(char_with_longest_interval + 97)
            ## then in return chr(char_with_longest_interval +97)
    #print("CHARACTER: ", char_with_longest_interval)


keyTimes=[[0,2],[1,5],[0,9],[2,15]]
slowest_key(keyTimes)
