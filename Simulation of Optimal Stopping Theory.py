'''Tests Optimal Stopping Theory by generating 1000 random numbers between 1 and 100'''
import random
import math

#Set the seed to always generate same set of random numbers
random.seed(10)

choices = []

for i in range(0,1000):
    choices.append(random.randint(1,100))

import matplotlib.pyplot as plt

plt.scatter(choices, range(0,1000))
plt.show()

def optimalstop():
    #Optimal Stopping Theory says coast without picking until 1/e percent of observations have been observed ~ 37%
    thresh = round((1 / math.e)*(len(choices)+1), 0)
    observedChoices = []
    #Theory says after the 1/e percent threshold is met, pick the next best observation that is better than everything seen so far
    #Save observations up until threshold
    for j in choices:
        if len(observedChoices) < thresh:
            observedChoices.append(j)
            choices.remove(j)
        else:
            break
    #Look at remaining choices and stop when the best one appears that beats the current best
    bestSoFar = max(observedChoices)
    best = max(observedChoices)
    for k in choices:
        if k <= best:
            pass
        else:
            best = k
            break
    if best == bestSoFar:
        print('The best value occurred in the first 37% and no better value was found.  :-( ')
    else:
        print('The best value found after the first 37% was:', best)

optimalstop()
