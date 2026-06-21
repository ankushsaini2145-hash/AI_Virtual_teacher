import string
# User input clean function 
def clean(user):
    user=user.lower()
    # punctuation remove
    for i in string.punctuation:
        if i=="#":
            user
        else:
            user=user.replace(i,"")
    return user
# user input word token convert function 
def token(user):
    user=user.split()
    return user
# Remove Stop word in User Input 
def Remove(user_list):
    stop_word=["a","an","the","is","am","are","was","were","be","been","being","do","does","did","doing","have",
               "has","had","having","i","me","my","mine","you","your","yours","he","him","his","she","her","hers",
               "they","them", "their","we","our","ours","what","which","who","whom","whose","when","where","why",
               "how","in","on","at","from","to","for","with","about","under","above","between","into","through",
               "during","before","after","and","or","but","because","if","while","although","however","very",
               "really","just","too","also","only","again","this","that","these","those","there","here","then","than","such","same"]
    clean_text=[]
    for i in user_list:
        if i not in stop_word:
            clean_text.append(i)
    return clean_text