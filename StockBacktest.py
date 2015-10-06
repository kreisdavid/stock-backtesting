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



"""
#this function takes stocks and returns the filepaths the stocks can be found at
def makeFilePaths(ls):
    retList = []
    for name in ls.split():
        retList += ["/Users/user/Documents/StockData/" + name + ".csv"]
    return retList

#determine if there was a good date to start shorting and a good window during which to hold before covering
def shortBasedOnDate(learn, test):
    learnSet = makeFilePaths(learn)
    testSet = makeFilePaths(test)
    
    windows = findWindows(learnSet) #implement
    results = applyWindow(testSet, windows) #implement

    retVal = []
    for i in range(0, len(windows)):
        middleman = [windows[i]] + [results[i]]
        retVal += middleman
    # [ [[start, end], n1 ], [[start, end], n2], [[start, end], n3] ]
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
        rand = random.randInt(0, 1)
        if rand == 0:
            learningSet += [name]
        else:
            testSet += [name]

    resultsList = shortBasedOnDate(learningSet, testSet) #NEED TO IMPLEMENT

    
    
    
if __name__ == "__main__":
    main()  #Invoke the main function
