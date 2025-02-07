numbers = [1,2,3,3,3,4,4,5,5,5,5,5,5,5,6,33,2,1,2,3,4]

def mostFrequent(lst):
    maxCount = 0
    mostFreq = None

    for item in lst:
        count = lst.count(item)
        if count > maxCount:
            maxCount = count
            mostFreq = item
        
    return mostFreq
    
print(mostFrequent(numbers))