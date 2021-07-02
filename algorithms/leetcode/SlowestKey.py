# 1629 slowest key
#A newly designed keypad was tested, where a tester pressed a sequence of n keys, one at a time.

#You are given a string keysPressed of length n, where keysPressed[i] was the ith key pressed in the testing sequence, and a sorted list releaseTimes, 
#where releaseTimes[i] was the time the ith key was released. Both arrays are 0-indexed. The 0th key was pressed at the time 0, 
#and every subsequent key was pressed at the exact time the previous key was released.

#The tester wants to know the key of the keypress that had the longest duration. The ith keypress had a duration of releaseTimes[i] - releaseTimes[i - 1], 
#and the 0th keypress had a duration of releaseTimes[0].

#Note that the same key could have been pressed multiple times during the test, and these multiple presses of the same key may not have had the same duration.

#Return the key of the keypress that had the longest duration. If there are multiple such keypresses, return the lexicographically largest key of the keypresses.


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
