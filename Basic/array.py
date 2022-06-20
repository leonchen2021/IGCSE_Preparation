from array import array
from select import select
#create a new array using built in array method
test_scores = array("i", [90,70,80])

#add another test score to end of our array 
test_scores.append(100)

#iterate over the array
for score in test_scores:
    print(score)

#get length of the array
length = len(test_scores)
print("length of the array(number of scores): ", length)

i = [1,2]
element = []
for index in i:
    element.append(test_scores[index])
print(element)