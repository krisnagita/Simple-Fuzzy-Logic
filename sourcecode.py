import csv

# open file csv


def splitData():
    filecsv = open(
        "C:\\Users\ASUS\Desktop\influencers.csv", "r")
    theDataLine = filecsv.read().split("\n")
    filecsv.close

    # array to separate data
    arrSprData = []
    splitData = []

    for i in theDataLine:
        splitData.append(i.split(","))

    for i in range(1, 101):
        arrSprData.append(splitData[i])

    return arrSprData

# Fuzzyfication Conditions and Values followerCount


def conditionFollower(value):
    limitA = 25000
    limitB = 50000
    limitC = 75000
    value = float(value)

    if (value >= 0 and value <= limitA):
        condition1 = "Low"
        condition2 = "Middle"
    elif (value >= limitA and value <= limitB):
        condition1 = "Low"
        condition2 = "Middle"
    elif (value >= limitB and value <= limitC):
        condition1 = "Middle"
        condition2 = "High"
    elif (value >= limitC):
        condition1 = "Middle"
        condition2 = "High"

    return condition1, condition2


def valueFollowers(value):
    limitA = 25000
    limitB = 50000
    limitC = 75000
    value = float(value)

    if (value >= 0 and value <= limitA):
        value1 = 1
        value2 = 0
    elif (value >= limitA and value <= limitB):
        value1 = (limitB-value)/(limitB-limitA)
        value2 = (value-limitA)/(limitB-limitA)
    elif (value >= limitB and value <= limitC):
        value1 = (limitC-value)/(limitC-limitB)
        value2 = (value-limitB)/(limitC-limitB)
    elif (value >= limitC):
        value1 = 0
        value2 = 1

    return round(value1, 2), round(value2, 2)

# Fuzzification Condition and Value EngamentsRate


def conditionEngagements(value):
    limitA = 2.5
    limitB = 5.0
    limitC = 7.5
    value = float(value)

    if (value >= 0 and value <= limitA):
        condition1 = "Low"
        condition2 = "Middle"
    elif (value >= limitA and value <= limitB):
        condition1 = "Low"
        condition2 = "Middle"
    elif (value >= limitB and value <= limitC):
        condition1 = "Middle"
        condition2 = "High"
    elif (value >= limitC):
        condition1 = "Middle"
        condition2 = "High"

    return condition1, condition2


def valueEngagements(value):
    limitA = 2.5
    limitB = 5.0
    limitC = 7.5
    value = float(value)

    if (value >= 0 and value <= limitA):
        value1 = 1
        value2 = 0
    elif (value >= limitA and value <= limitB):
        value1 = (limitB-value)/(limitB-limitA)
        value2 = (value-limitA)/(limitB-limitA)
    elif (value >= limitB and value <= limitC):
        value1 = (limitC-value)/(limitC-limitB)
        value2 = (value-limitB)/(limitC-limitB)
    elif (value >= limitC):
        value1 = 0
        value2 = 1

    return round(value1, 2), round(value2, 2)

# Finding minimum value from two values


def min(valueFoll, valueEng):
    if (valueFoll < valueEng):
        worthiness = valueEng
    else:
        worthiness = valueFoll

    return worthiness

# Finding maksimum value from two value


def max(valueX, valueY):
    if (valueX > valueY):
        finalvalue = valueX
    else:
        finalvalue = valueY

    return finalvalue

# Finding worthiness with low condition


def findLowCondition(arrCond, arrVal):
    valueMaxLow = 0
    thevalueMaxLow = 0

    for i in range(len(arrCond)):
        if (arrCond[i] == "Low"):
            valueMaxLow = max(valueMaxLow, arrVal[i])
            if (valueMaxLow > thevalueMaxLow):
                thevalueMaxLow = valueMaxLow

    return thevalueMaxLow

# Finding worthiness with High Condition


def findHighCondition(arrCond, arrVal):
    valueMaxHigh = 0
    thevalueMaxHigh = 0

    for i in range(len(arrCond)):
        if (arrCond[i] == "High"):
            valueMaxHigh = max(valueMaxHigh, arrVal[i])
            if (valueMaxHigh > thevalueMaxHigh):
                thevalueMaxHigh = valueMaxHigh

    return thevalueMaxHigh

# Finding value of worthiness
# Sugeno's Rule


def findConditionWorth(condF, condE):
    condWorth = ""
    if (condF == "Low" and condE == "Low"):
        condWorth = "Low"
    elif (condF == "Low" and condE == "Middle"):
        condWorth = "Low"
    elif (condF == "Low" and condE == "High"):
        condWorth = "Low"
    elif (condF == "Middle" and condE == "Low"):
        condWorth = "Low"
    elif (condF == "Middle" and condE == "Middle"):
        condWorth = "High"
    elif (condF == "Middle" and condE == "High"):
        condWorth = "High"
    elif (condF == "High" and condE == "Low"):
        condWorth = "High"
    elif (condF == "High" and condE == "Middle"):
        condWorth = "High"
    elif (condF == "High" and condE == "High"):
        condWorth = "High"

    return condWorth

# Defuzification finding value y*


def Defuzification(arrMaxLow, arrMaxHigh):
    limitLow = 60
    limitHigh = 85
    arrYStar = []
    for i in range(len(arrMaxLow)):
        YStar = (arrMaxLow[i]*limitLow + arrMaxHigh[i]
                 * limitHigh)/(arrMaxLow[i]+arrMaxHigh[i])
        arrYStar.append(YStar)

    return arrYStar


def main():
    arrValueFol = []
    arrValueEg = []
    arrConditionFol = []
    arrConditionEg = []
    arrConditionWorth = []
    arrWorth = []
    arrMaxLow = []
    arrMaxHigh = []
    arrYStar = []
    splittheData = []

    splittheData = splitData()

    # Finding Value and Condition from followersCount
    for i in range(len(splittheData)):
        arrValueFol.append(valueFollowers(splittheData[i][1]))
        arrConditionFol.append(conditionFollower(splittheData[i][1]))

    # Finding Vakue and Condition from EngagementRate
    for i in range(len(splittheData)):
        arrValueEg.append(valueEngagements(splittheData[i][2]))
        arrConditionEg.append(conditionEngagements(splittheData[i][2]))

    for i in range(len(splittheData)):
        arrConditionWorth = []
        arrWorth = []

        condF1 = arrConditionFol[i][0]
        condF2 = arrConditionFol[i][1]
        condE1 = arrConditionEg[i][0]
        condE2 = arrConditionEg[i][1]
        valF1 = arrValueFol[i][0]
        valF2 = arrValueFol[i][1]
        valE1 = arrValueEg[i][0]
        valE2 = arrValueEg[i][1]

        arrConditionWorth.append(findConditionWorth(condF1, condE1))
        arrConditionWorth.append(findConditionWorth(condF1, condE2))
        arrConditionWorth.append(findConditionWorth(condF2, condE1))
        arrConditionWorth.append(findConditionWorth(condF2, condE2))
        arrWorth.append(min(valF1, valE1))
        arrWorth.append(min(valF1, valE2))
        arrWorth.append(min(valF2, valE1))
        arrWorth.append(min(valF2, valE2))
        arrMaxLow.append(findLowCondition(arrConditionWorth, arrWorth))
        arrMaxHigh.append(findHighCondition(arrConditionWorth, arrWorth))

    arrYStar = Defuzification(arrMaxLow, arrMaxHigh)
    arrSortIndexData = []

    # Sorting Array Y Star with Selection Sort
    for i in range(len(splittheData)):
        arrSortIndexData.append(splittheData[i][0])

    # Traverse through all Array elements
    for i in range(len(arrYStar)):
        min_idx = i
        for j in range(i+1, len(arrYStar)):
            if arrYStar[min_idx] < arrYStar[j]:
                min_idx = j

    # Swap the found minimum element with the first element
        arrYStar[i], arrYStar[min_idx] = arrYStar[min_idx], arrYStar[i]
        arrSortIndexData[i], arrSortIndexData[min_idx] = arrSortIndexData[min_idx], arrSortIndexData[i]

    print("Result 20 Influencers: ")
    for i in range(20):
        print('ID = ', arrSortIndexData[i], "| Worthiness = ", arrYStar[i])

    # Output Result in csv file
    fileChosen = open("theChosen.csv", "w")
    for i in range(20):
        fileChosen.write(arrSortIndexData[i])
        fileChosen.write("\n")


if __name__ == "__main__":
    main()
