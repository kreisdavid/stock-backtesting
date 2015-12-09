"""

infile = open("/Users/user/Documents/StockData/Twitter.csv", "r")
infile.readline()
'Date,Open,High,Low,Close,Volume,Adj Close\n'

infile.readline().split(',')
#### ['10/1/15', '26.469999', '26.84', '24.65', '24.68', '30619200', '24.68\n']

>>> infile.readline()
'9/30/15,25.940001,27.33,25.879999,26.940001,25208200,26.940001\n'

>>> infile.readline().strip('\n').split(',')
['9/29/15', '25.23', '25.76', '24.92', '25.59', '13378700', '25.59']



>>> l = open("/Users/user/Documents/College/Year2/Semester1/Econ/TestingStockList.txt", "r")
>>> splited = l.read().split()
>>> splited
['Actua', 'AkamaiTechnologies', 'Amazon', 'AngiesList', 'Baidu', 'Bazaarvoice', 'CA', 'Carbonite', 'ChangeYou', 'ChannelAdvisor', 'Cisco', 'CitrixSystems', 'CognizantTechnologySolutions', 'ConstantContact', 'CornerstoneOndemand', 'CoStarGroup', 'Criteo', 'DemandMedia', 'Demandware', 'DHIgroup', 'eBay', 'eGain', 'EMC', 'EnduranceInternational', 'Envestnet', 'Expedia', 'F5Networks', 'Facebook', 'Gogo', 'Groupon', 'HomeAway', 'IAC', 'IntraLink', 'Intuit', 'Jive', 'Juniper', 'Limelight', 'Linkedin', 'LivePerson', 'Marchex', 'MarinSoftware', 'Marketo', 'MonsterWorldWide', 'NetEase', 'Netflix', 'NetSuite', 'Nutrisystem', 'Overstock', 'Pandora', 'PricelineGroup', 'Proofpoint', 'Qualys', 'QuinStreet', 'RackspaceHosting', 'RealNetworks', 'RedHat', 'Reis', 'Renren', 'RetailMeNot', 'RocketFuel', 'Salesforce', 'SciQuest', 'Shutterstock', 'SINA', 'SouFunHoldings', 'SparkNetworks', 'Symantec', 'TechTarget', 'Textura', 'TripAdvisor', 'Twitter', 'UnitedOnline', 'Veeva', 'VipshopHoldings', 'VMware', 'WebMD', 'Workday', 'WWWW', 'XOgroup', 'XoomCorporation', 'Yahoo', 'Yelp', 'YoukuTodou', 'YuMe', 'YY', 'Zynga']
>>> for company in splited:
	twt = "/Users/user/Documents/StockData/" + company + ".csv"
	print(twt)

	
/Users/user/Documents/StockData/Actua.csv
/Users/user/Documents/StockData/AkamaiTechnologies.csv
/Users/user/Documents/StockData/Amazon.csv
/Users/user/Documents/StockData/AngiesList.csv
/Users/user/Documents/StockData/Baidu.csv
/Users/user/Documents/StockData/Bazaarvoice.csv
/Users/user/Documents/StockData/CA.csv
/Users/user/Documents/StockData/Carbonite.csv
/Users/user/Documents/StockData/ChangeYou.csv
/Users/user/Documents/StockData/ChannelAdvisor.csv
/Users/user/Documents/StockData/Cisco.csv
/Users/user/Documents/StockData/CitrixSystems.csv
/Users/user/Documents/StockData/CognizantTechnologySolutions.csv
/Users/user/Documents/StockData/ConstantContact.csv
/Users/user/Documents/StockData/CornerstoneOndemand.csv
/Users/user/Documents/StockData/CoStarGroup.csv
/Users/user/Documents/StockData/Criteo.csv
/Users/user/Documents/StockData/DemandMedia.csv
/Users/user/Documents/StockData/Demandware.csv
/Users/user/Documents/StockData/DHIgroup.csv
/Users/user/Documents/StockData/eBay.csv
/Users/user/Documents/StockData/eGain.csv
/Users/user/Documents/StockData/EMC.csv
/Users/user/Documents/StockData/EnduranceInternational.csv
/Users/user/Documents/StockData/Envestnet.csv
/Users/user/Documents/StockData/Expedia.csv
/Users/user/Documents/StockData/F5Networks.csv
/Users/user/Documents/StockData/Facebook.csv
/Users/user/Documents/StockData/Gogo.csv
/Users/user/Documents/StockData/Groupon.csv
/Users/user/Documents/StockData/HomeAway.csv
/Users/user/Documents/StockData/IAC.csv
/Users/user/Documents/StockData/IntraLink.csv
/Users/user/Documents/StockData/Intuit.csv
/Users/user/Documents/StockData/Jive.csv
/Users/user/Documents/StockData/Juniper.csv
/Users/user/Documents/StockData/Limelight.csv
/Users/user/Documents/StockData/Linkedin.csv
/Users/user/Documents/StockData/LivePerson.csv
/Users/user/Documents/StockData/Marchex.csv
/Users/user/Documents/StockData/MarinSoftware.csv
/Users/user/Documents/StockData/Marketo.csv
/Users/user/Documents/StockData/MonsterWorldWide.csv
/Users/user/Documents/StockData/NetEase.csv
/Users/user/Documents/StockData/Netflix.csv
/Users/user/Documents/StockData/NetSuite.csv
/Users/user/Documents/StockData/Nutrisystem.csv
/Users/user/Documents/StockData/Overstock.csv
/Users/user/Documents/StockData/Pandora.csv
/Users/user/Documents/StockData/PricelineGroup.csv
/Users/user/Documents/StockData/Proofpoint.csv
/Users/user/Documents/StockData/Qualys.csv
/Users/user/Documents/StockData/QuinStreet.csv
/Users/user/Documents/StockData/RackspaceHosting.csv
/Users/user/Documents/StockData/RealNetworks.csv
/Users/user/Documents/StockData/RedHat.csv
/Users/user/Documents/StockData/Reis.csv
/Users/user/Documents/StockData/Renren.csv
/Users/user/Documents/StockData/RetailMeNot.csv
/Users/user/Documents/StockData/RocketFuel.csv
/Users/user/Documents/StockData/Salesforce.csv
/Users/user/Documents/StockData/SciQuest.csv
/Users/user/Documents/StockData/Shutterstock.csv
/Users/user/Documents/StockData/SINA.csv
/Users/user/Documents/StockData/SouFunHoldings.csv
/Users/user/Documents/StockData/SparkNetworks.csv
/Users/user/Documents/StockData/Symantec.csv
/Users/user/Documents/StockData/TechTarget.csv
/Users/user/Documents/StockData/Textura.csv
/Users/user/Documents/StockData/TripAdvisor.csv
/Users/user/Documents/StockData/Twitter.csv
/Users/user/Documents/StockData/UnitedOnline.csv
/Users/user/Documents/StockData/Veeva.csv
/Users/user/Documents/StockData/VipshopHoldings.csv
/Users/user/Documents/StockData/VMware.csv
/Users/user/Documents/StockData/WebMD.csv
/Users/user/Documents/StockData/Workday.csv
/Users/user/Documents/StockData/WWWW.csv
/Users/user/Documents/StockData/XOgroup.csv
/Users/user/Documents/StockData/XoomCorporation.csv
/Users/user/Documents/StockData/Yahoo.csv
/Users/user/Documents/StockData/Yelp.csv
/Users/user/Documents/StockData/YoukuTodou.csv
/Users/user/Documents/StockData/YuMe.csv
/Users/user/Documents/StockData/YY.csv
/Users/user/Documents/StockData/Zynga.csv



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
        retList += ["/Users/user/Documents/StockData/" + name + ".csv"]
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
        for line in stockDetails:
            report += [line.split(",")]
        stocks += [report]   #creates triply nested values



    for startDate in range(31): #start short selling stock between day 0 and day 30
        for windowWidth in range(61): #hold stock for between 0 and 60 days
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
        for line in stockDetails:
            report += [line.split(",")]
        stocks += [report]

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
    result = applyWindow(testSet, window) #implement

    retVal = []
    retVal += [window] + [result]
    # [ [start, width], n ] 
    return retVal

def main():
    stocks = open("/Users/user/Documents/College/Year2/Semester1/Econ/TestingStockList.txt", "r")
    #opens a text file of stocks that inlcudes all the stocks we want to test
    ### that we have csv files for
    
    stockList = stocks.read().split() #splits input into a list
    learningSet = []
    testSet = []
    #splitting stocks into a learning and test set
    #half in each
    for name in stockList:
        rand = random.randint(0, 1)
        if rand == 0:
            learningSet += [name]
        else:
            testSet += [name]

    results = shortBasedOnDate(learningSet, testSet)

    #have up to here. now what?
    print(results)
    
    
    
if __name__ == "__main__":
    main()  #Invoke the main function
