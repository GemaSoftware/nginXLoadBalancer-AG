import random, math, socket
import hashlib

class BackendCompute:

    def __init__(self):
        self.hashFunction = hashlib.new("sha256")
        pass

    def compSeed(self):
        myBytes = socket.gethostname().encode()
        self.hashFunction.update(myBytes)
        self.seed = int(self.hashFunction.hexdigest(),base=16) % 2**32
        random.seed(self.seed)

    #This function returns the max number of times the coin flip land on head.
    def get_random_heads(self, x):
        heads_in_a_row = 0
        max_counter = 0
        #for every flip
        for i in range(x):
            #flip the coin
            flip = random.randint(0,1)
            if flip == 0:
                #If tails, update max counter if needed and set head counter to 0.
                if max_counter < heads_in_a_row: max_counter = heads_in_a_row
                heads_in_a_row = 0
            else:
                #if heads, update heads in a row.
                heads_in_a_row += 1
        #case that heads all the way through range. update max counter.
        if max_counter < heads_in_a_row: max_counter = heads_in_a_row
        return max_counter

    def flip_until(self, total_heads):
        """
        This function will flip coins until total heads reached is reached.
        """
        i=0
        ret = 0
        while i < total_heads:
            ret += 1
            flip = random.randint(0,1)
            if 0 == flip:
                i = 0
            else:
                i += 1
        return ret
            



#Funciton to check if the number entered is a prime digit.
def isPrime(n):
    prime = True
    for i in range(2,math.floor(math.sqrt(n))):
        if 0 == n % i:
            prime = False
            break
    return prime
