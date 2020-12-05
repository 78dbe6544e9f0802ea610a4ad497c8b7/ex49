direction_words = ('north', 'south', 'east', 'west', 'down', 'up', 'left', 'right', 'back', 'on')
verbs = ('go', 'stop', 'kill', 'eat', 'sleep', 'dance')
stop_words = ('the', 'in', 'of', 'from', 'at', 'it')
nouns = ('door', 'bear', 'princess', 'cabinet', 'monster', 'fire')

def scan(arg):
    # Splits input into individual words and puts each word into a tuple
    # along with the word's category; then puts tuples into a list
    directions = []
    words = arg.split()
    for x in words:
        if x.lower() in direction_words:
            directions.append(('direction', x))
        if x.lower() in verbs:
            directions.append(('verb', x))
        if x.lower() in stop_words:
            directions.append(('stop', x))
        if x.lower() in nouns:
            directions.append(('noun', x))
        try:
            directions.append(('number', int(x)))
        except ValueError:
            if x.lower() not in direction_words and x.lower() not in verbs and x.lower() not in stop_words and x.lower() not in nouns:
                directions.append(('error', x))

    return directions
