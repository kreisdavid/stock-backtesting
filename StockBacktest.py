"""

infile = open("/Users/user/Desktop/Example.csv", "r")
>>> report = infile.read().split()
>>> report
['10/1/15,511,520.799988,506,520.719971,3741100,520.719971', '9/30/15,505.440002,512.799988,501.670013,511.890015,3990400,511.890015', '9/29/15,506,511.480011,490.5,496.070007,4443200,496.070007', '9/28/15,520.02002,520.280029,494.329987,504.059998,5383200,504.059998', '9/25/15,542.570007,542.799988,521.400024,524.25,3910300,524.25', '9/24/15,530.549988,534.559998,522.869995,533.75,3481800,533.75', '9/23/15,538.299988,541.210022,534,536.070007,2228100,536.070007', '9/22/15,539.710022,543.549988,532.659973,538.400024,3824200,538.400024', '9/21/15,544.330017,549.780029,539.590027,548.390015,3265300,548.390015', '9/18/15,534.619995,546.23999,531.349976,540.26001,6125600,540.26001']
>>> nnn = []
>>> for t in report:
	nnn += [t.split(",")]

	
>>> nnn
[['10/1/15', '511', '520.799988', '506', '520.719971', '3741100', '520.719971'], ['9/30/15', '505.440002', '512.799988', '501.670013', '511.890015', '3990400', '511.890015'], ['9/29/15', '506', '511.480011', '490.5', '496.070007', '4443200', '496.070007'], ['9/28/15', '520.02002', '520.280029', '494.329987', '504.059998', '5383200', '504.059998'], ['9/25/15', '542.570007', '542.799988', '521.400024', '524.25', '3910300', '524.25'], ['9/24/15', '530.549988', '534.559998', '522.869995', '533.75', '3481800', '533.75'], ['9/23/15', '538.299988', '541.210022', '534', '536.070007', '2228100', '536.070007'], ['9/22/15', '539.710022', '543.549988', '532.659973', '538.400024', '3824200', '538.400024'], ['9/21/15', '544.330017', '549.780029', '539.590027', '548.390015', '3265300', '548.390015'], ['9/18/15', '534.619995', '546.23999', '531.349976', '540.26001', '6125600', '540.26001']]
>>> nnn[0]
['10/1/15', '511', '520.799988', '506', '520.719971', '3741100', '520.719971']
>>> nnn[0][0]
'10/1/15'
>>> gg = []
>>> gg += [nnn]
>>> gg += [nnn]
>>> gg[0]
[['10/1/15', '511', '520.799988', '506', '520.719971', '3741100', '520.719971'], ['9/30/15', '505.440002', '512.799988', '501.670013', '511.890015', '3990400', '511.890015'], ['9/29/15', '506', '511.480011', '490.5', '496.070007', '4443200', '496.070007'], ['9/28/15', '520.02002', '520.280029', '494.329987', '504.059998', '5383200', '504.059998'], ['9/25/15', '542.570007', '542.799988', '521.400024', '524.25', '3910300', '524.25'], ['9/24/15', '530.549988', '534.559998', '522.869995', '533.75', '3481800', '533.75'], ['9/23/15', '538.299988', '541.210022', '534', '536.070007', '2228100', '536.070007'], ['9/22/15', '539.710022', '543.549988', '532.659973', '538.400024', '3824200', '538.400024'], ['9/21/15', '544.330017', '549.780029', '539.590027', '548.390015', '3265300', '548.390015'], ['9/18/15', '534.619995', '546.23999', '531.349976', '540.26001', '6125600', '540.26001']]
>>> gg[0][0]
['10/1/15', '511', '520.799988', '506', '520.719971', '3741100', '520.719971']
>>> gg[0][0][0]
'10/1/15'
>>> gg[1][1][1]
'505.440002'
>>> gg[1][0][0]
'10/1/15'


"""
import random

#this function takes stocks and returns the filepaths the stocks can be found at
def makeFilePaths(ls):
    retList = []
    for name in ls:
        retList += ["/Users/kreis/Documents/StockData/" + name + ".csv"]
    return retList

#this function takes a set of stocks and finds the 5 best windows
#from 30 to 60 days for the stocks performance
#this function specifically deals with shorting stocks
def findWindow(ls):
    bestWindows = []
    bestStartDate = -1
    bestWindowWidth = -1
    bestResult = 0

    profitFromShortSell = 0
    
    stocks = []
    report = []

    for stock in ls:
        infile = open(stock, "r")
        garbage = infile.readline() #unneeded column headers
        stockDetails = infile.read().split()
        for line in list(reversed(stockDetails)):
            report += [line.split(",")]
        stocks += [report]   #creates triply nested values
        infile.close()



    for startDate in range(61): #start short selling stock between day 0 and day 30
        for windowWidth in range(121): #hold stock for between 0 and 60 days
            for stockName in stocks:
                priceAtStart = float(stockName[startDate][4])
                priceAtCover = float(stockName[startDate+windowWidth][4])
                profitFromShortSell += priceAtStart-priceAtCover

            averageProfit = profitFromShortSell / len(stocks)
            if averageProfit > bestResult:
                bestStartDate = startDate
                bestWindowWidth = windowWidth
                bestResult = averageProfit

    retVal = [bestStartDate] + [bestWindowWidth]
    return retVal
                
def applyWindow(ls, window):
    stocks = []
    report = []
    profitFromShortSell = 0

    for stock in ls:
        infile = open(stock, "r")
        garbage = infile.readline() #unneeded column headers
        stockDetails = infile.read().split()
        for line in list(reversed(stockDetails)):
            report += [line.split(",")]
        stocks += [report]
        infile.close()

    #window is [startDate, windowWidth]
    for stockName in stocks:
        priceAtStart = float(stockName[window[0]][4])
        priceAtCover = float(stockName[window[0]+window[1]][4])
        profitFromShortSell += priceAtStart-priceAtCover

    averageProfit = profitFromShortSell / len(stocks)

    return averageProfit
                
#determine if there was a good date to start shorting and a good window during which to hold before covering
def shortBasedOnDate(learn, test):
    learnSet = makeFilePaths(learn)
    testSet = makeFilePaths(test)
    
    window = findWindow(learnSet)
    if window[0] != -1:
        result = applyWindow(testSet, window) #implement
    else:
        window = [46, 99] #the average values from previous trials
        result = applyWindow(testSet, window) 

    retVal = []
    retVal += [window] + [result]
    # [ [start, width], n ] 
    return retVal

def main():
    num = 0
    aggregateResults = 0
    timesThisWorks = 0
    timesToTry = 10000
    
    aggregateStartDate = 0
    aggregateWindowWidth = 0
    aggregateNegativeResults = 0
    while num < timesToTry:
        stocks = open("/Users/kreis/Documents/Programs/stock-backtesting/StockList.txt", "r")
        #opens a text file of stocks that inlcudes all the stocks we want to test
        ### that we have csv files for
        
        stockList = stocks.read().split() #splits input into a list
        learningSet = []
        testSet = []
        #splitting stocks into a learning and test set
        #half in each
        for name in stockList:
            rand = random.randint(0, 9)
            if rand < 7:
                learningSet += [name]
            else:
                testSet += [name]

        results = shortBasedOnDate(learningSet, testSet)
        if results[1] > 0:
            timesThisWorks += 1
            aggregateResults += results[1]
            aggregateStartDate += results[0][0]
            aggregateWindowWidth += results[0][1]
        else:
            aggregateNegativeResults += results[1]
        num += 1
        if num % 500 == 0:
            print("num = " + str(num))
        stocks.close()

    averageTotalOverAllSimulations = (aggregateResults + aggregateNegativeResults) / float(timesToTry)
    averageTotalOverSuccessfulSimulations = aggregateResults / float(timesThisWorks)
    averageStartDate = aggregateStartDate / float(timesThisWorks)
    averageWindowWidth = aggregateWindowWidth /float(timesThisWorks)
    print(" ")
    print("This strategy worked " + str(timesThisWorks) + " time(s) out of " + str(timesToTry) + " trials.")
    print("When the strategy worked, you would make an average profit of $" + str(averageTotalOverSuccessfulSimulations) + " per share.")
    print("The average start date for the times it worked was " + str(averageStartDate) + " day(s) after IPO.")
    print("The average time to hold each stock was " + str(averageWindowWidth) + " day(s)")
    print(" ")
    if averageTotalOverAllSimulations > 0:
        print("The total average profit over both successful and nonsuccessful simulations was $" + str(averageTotalOverAllSimulations) + " per share.")
    else:
        print("The total average loss over both successful and nonsuccessful simulations was -$" + str(averageTotalOverAllSimulations) + " per share.")

    #print("It has been found that by short selling an internet stock " + str(results[0][0]) + " days after its IPO, and holding for " + str(results[0][1]) + " days will on average make you a profit of $" + str(results[1]) + " per share.")
    #used for when running once at a time
    
    
if __name__ == "__main__":
    main()  #Invoke the main function
