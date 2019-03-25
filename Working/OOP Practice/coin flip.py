import random

class Coin(object):

    def __init__(self):
        self.face = random.choice(["heads", "tails"])

    def get_face(self):
        return self.face

    def flip(self):
        self.face = random.choice(["heads", "tails"])

def main():

    heads = 0
    tails = 0

    for i in range(1000):
        myCoin = Coin()
        myCoin.flip()

        if myCoin.get_face() == "heads":
            heads += 1
        elif myCoin.get_face() == "tails":
            tails += 1

    print("Total Heads: " + str(heads) + "\nTotal Tails: " + str(tails))

main()
