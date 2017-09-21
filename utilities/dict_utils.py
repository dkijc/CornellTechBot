def modified_pop(dictionary, key):
    return {
        k: dictionary[k] 
        for k in dictionary 
        if k != key
    }