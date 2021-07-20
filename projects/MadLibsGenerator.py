from random import randint
import copy

story=( #create a story to be filled with words
    "One day my {} friend and I decided to go to the {} game in {}. "+
    "We really wanted to see the {} play the {}. So, we {} our {} "+
    "down to the {} and bought some {}s. We got into the game and "+
    "it was a lot of fun. We ate some {} {} and drank some {} {}. "+
    "We had a great time! We plan to go again next year! "
)

word_dict = {   #words to randomly choose to complete the story
    'adjective':['greedy','abrasive','grubby','groovy','rich','harsh','tasty','slow'],
    'city name':['Chicago','New York','Charlotte','Indianapolis','Louisville','Denver'],
    'noun':['people','map','music','dog','hamster','ball','hotdog','salad'],
    'action verb':['run','fall','crawl','scurry','cry','watch','swim','jump','bounce'],
    'sports noun':['ball','mit','puck','uniform','helmet','scoreboard','player'],
    'place':['park','desert','forest', 'store','restaurant', 'waterfall']
}

#get word
def pick_word(type, temp_dict):
    word=temp_dict[type]  #to get the list for type such as type=adjective and list is all adjective words
    count=len(word)-1   #index starts with 0
    index=randint(0,count)  #set the random range
    return temp_dict[type].pop(index) #delete the already used word and return dict

#get story
#print story
def create_func():
    temp_dict=copy.deepcopy(word_dict) #changes to local_dict will not change word_dict
    return story.format(    #string format function to fill in the blanks in the story
        pick_word('adjective', temp_dict),
        pick_word('sports noun', temp_dict),
        pick_word('city name', temp_dict),
        pick_word('noun', temp_dict),
        pick_word('noun', temp_dict),
        pick_word('action verb', temp_dict),
        pick_word('noun', temp_dict),
        pick_word('place', temp_dict),
        pick_word('noun', temp_dict),
        pick_word('adjective', temp_dict),
        pick_word('noun', temp_dict),
        pick_word('adjective', temp_dict),
        pick_word('noun', temp_dict)

)

print("Story 1: ")
print(create_func())
print()
print("Story 2: ")
print(create_func())
