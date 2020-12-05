from ex48 import lexicon

class ParserError(Exception): # Empty class allows script to provide made up error (class name) with
                                # made up exception/error message (fed in as argument); this class
                                # is placed in "dead ends" and the program will terminate when it shows
                                # up, but the class name and Exception message will show in the termination
    pass

class Sentence(object):

    def __init__(self, subject, verb, obj):
        self.subject = subject[1] # gets the second (user inputted) word from the tuple and makes it an object
        self.verb = verb[1] # same
        self.object = obj[1] # same

def peek(word_list): # called on a list of tuples
    if word_list: # loop, as long as the list hasn't been exhausted
        word = word_list[0] # names first tuple in list w/ variable
        return word[0] # returns the token from the tuple
    else:
        return None

def match(word_list, expecting): # called on a list of tuples and an expected token
    if word_list: # sets up loop
        word = word_list.pop(0) # pops first tuple from list and names w/ variable

        if word[0] == expecting: # if token from popped tuple matches expected token
            return word # return the whole tuple (WHY return a 'stop' tuple??)
        else:
            return None
    else:
        return None

def skip(word_list, word_type): # called on list of tuples and a pre-assigned token (sub obj or verb)
    while peek(word_list) == word_type: # while loop--while token of first tuple in list is the pre-assigned token...
        match(word_list, word_type) # call match() on the list and the pre-assigned token (word_list, expecting)

def parse_verb(word_list): # scans word_list for verb
    skip(word_list, 'stop') # calls skip() on the list and the 'stop' token, cycling through and popping any 'stop' tokened tuples

    if peek(word_list) == 'verb': # peeks at the list for a verb tokened tuple, if it finds one...
        return match(word_list, 'verb') # returns match called on the list and 'verb' (i.e. returns the tuple)
    else:
        raise ParserError("Expected a verb next.") # if a verb isn't found, raises an error

def parse_object(word_list): # scans word_list for object
    skip(word_list, 'stop') # calls skip() on the list and 'stop' token to pop any 'stop' tokened tuples
    next_word = peek(word_list) # peeks at the list and names the returned token with a variable

    if next_word == 'noun': # if the variable is 'noun'
        return match(word_list, 'noun') # calls match on the list and 'noun' (pops the tuple and returns it)
    elif next_word == 'direction': # if the variable is 'direction'
        return match(word_list, 'direction') # calls match on the list and 'direction' (pops the tuple and returns it)
    else:
        raise ParserError("Expected a noun or direction next.") # otherwise (not noun or direction) raises error

def parse_subject(word_list): # scans word_list for subject by checking for a noun followed by a verb,
                            # then returning that noun as the subject
    skip(word_list, 'stop') # calls skip on list and 'stop' to pop all stop tokened tuples
    next_word = peek(word_list) # peeks at the list and names token from first tuple w/ variable

    if next_word == 'noun': # if that token is 'noun'
        return match(word_list, 'noun') # calls match on the list and 'noun' and returns the tuple
    elif next_word == 'verb': # if that token is 'verb',
        return ('noun', 'player') # it returns the tuple ('noun', 'player') (this should be the case in most instances)
    else:
        raise ParserError("Expected a verb next.") # otherwise, raises an error (add pronouns to lexicon?)

def parse_sentence(word_list): # this is the function that will be called to kick everything off;
                                # call it on the list produced in the lexicon module. This is super
                                # inflexible; it needs a subj-verb-obj order and can't recognize more
                                # than one of any category
    subj = parse_subject(word_list) # parses the list for a subject, names it w/ variable
    verb = parse_verb(word_list) # parses the list for a verb, names w/ variable
    obj = parse_object(word_list) # parses for obj, names w/ variable

    return Sentence(subj, verb, obj) # pops these three into the Sentence class and returns it; this allows for
                                    # three objects (as listed in the Sentence class __init__) which can be used
                                    # in another module (to understand, respond, and/or react to user input, I assume)
