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

enginee = SortedArray(sorted_array, pair_validation)
enginee.validad_array()
