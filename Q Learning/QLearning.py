
import numpy as np
import random
import matplotlib.pyplot as plt

reward = []
data = []
action = []


def RewardGrid():
    for i in range(225):
        reward.append(0)


def DataGrid():
    for i in range(225):
        data.append([])
        for j in range(4):
            data[i].append(0)


def ActionGrid():
    for i in range(225):
        action.append([])
        Row = int(i / 15)
        Col = i % 15
        
        # State Up
        if(Row - 1 < 0):
            action[i].append(i)
        else:
            action[i].append(i - 15)
        # State Down
        if(Row + 1 > 14):
            action[i].append(i)
        else:
            action[i].append(i + 15)
        # State Left
        if(Col - 1 < 0):
            action[i].append(i)
        else:
            action[i].append(i - 1)
        # State Right
        if(Col + 1 > 14):
            action[i].append(i)
        else:
            action[i].append(i + 1)



def plotGraph(iterationCountList, stepCountList):
    plt.plot(iterationCountList, stepCountList)
    plt.xlabel('Iterations')
    plt.ylabel('Step Count')
    plt.show()


def algorithm():    
    stepList = []
    iterationList = []
    iteration = 1
    for k in range(300):
        currentStateIndex = 0
        prevStateIndex = 0
        finishStateIndex = 224
        randomActionIndex = 0
        possibleActionIndex = [0, 1, 2, 3]
        epsilonGreedy = .1
        discountFactor = 0.75
        stepCount = 0
        while (True):
            stepCount += 1
            if(currentStateIndex == finishStateIndex):
                data[prevStateIndex][randomActionIndex] = 100
                break    
            maxRewardIndexList = [i for i, x in enumerate(data[currentStateIndex]) if x == max(data[currentStateIndex])]
            #print maxRewardIndexList
            otherRewardIndexList = list(set(possibleActionIndex) - set(maxRewardIndexList))
            if(random.uniform(0, 1) <= epsilonGreedy and len(otherRewardIndexList)>0):
                randomActionIndex = np.random.choice(possibleActionIndex, 1)[0]
            else:
                randomActionIndex = np.random.choice(maxRewardIndexList, 1)[0]
            
            prevStateIndex = currentStateIndex
            currentStateIndex = action[currentStateIndex][randomActionIndex]
            data[prevStateIndex][randomActionIndex] = reward[prevStateIndex] + discountFactor * (max(data[currentStateIndex]) + reward[currentStateIndex])
    
        print("Iteration : " + str(iteration) + ", StepCount : " + str(stepCount))
        iterationList.append(iteration)
        stepList.append(stepCount)
        iteration += 1
    
    plotGraph(iterationList, stepList)
    
RewardGrid()
DataGrid()
ActionGrid()
algorithm()   
