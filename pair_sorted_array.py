sorted_array = [2,3,5,7,11,13]
pair_validation = 14

class SortedArray:
    def __init__(self, array_input, t):
        self.array = array_input
        self.t = t

    def validad_array(self):
        #validation ever with de first position of array

        p1 = 0
        for index in range(len(self.array)): 
            #p1 = index # get key
            p1 = self.array[index] # get key
            for j in range(len(self.array)):
                calc = p1 + self.array[j]
                if calc == 14:
                    print(p1)
                    print(self.array[j])  
                    break 

            #print(f"{p1}")
            
        return print(f"{p1} and {self.array[j]}")
    

    def find_pair_with_sun(self):
        left = 0
        right = len(self.array) - 1

        while left < right:
            current_sum = self.array[left] + self.array[right]

            if current_sum == self.t:
                   return self.array[left], self.array[right]
            elif current_sum < self.t:
                   left += 1
            else:
                   right -= 1 
        
        return None

enginee = SortedArray(sorted_array, pair_validation)
pair = enginee.find_pair_with_sun()
print(pair)