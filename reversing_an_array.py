my_array = [1,2,3,4,5,6]
test = []

print(f"{my_array}")
class ReversingAnArray:
    
    def __init__(self, original_array):
        self.int = original_array

    def invert_array(self):
        #print(f"i'm in invert array method | {self.int}")

        new_array = []
        #print(f"new_array :{new_array}")

        for index in self.int[::-1]:
            new_array.append(index)
            #print(index)
        return new_array


enginee = ReversingAnArray(my_array)
new_array = enginee.invert_array()
#print(new_array)

def normalize_array(first_array, second_array):
    for index in range(0, len(my_array), 1):
       first_array[index] = second_array[index]
    
    return print(f"{first_array}")

normalize_array(my_array, new_array)