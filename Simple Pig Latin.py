

My solution:
def pig_it(text):
    #your code here
    result=[]   
    
    for word in text.split(' '):
        if word.isalpha():
            if len(word) > 1:
                result.append(word[1:] + word[0] + 'ay')
            else:
                result.append(word + 'ay')
        else:
            result.append(word)
            
    return ' '.join(result)


Best practice voted:

def pig_it(text):
    lst = text.split()
    return ' '.join( [word[1:] + word[:1] + 'ay' if word.isalpha() else word for word in lst])