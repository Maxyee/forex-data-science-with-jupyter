#opening file for read data
myFile = open('food-price-tables.csv','r')

#read the data from file and stored in into a list
listOfLines = myFile.read().splitlines()

#print the first line of that file
print(listOfLines[0])

#breaking into a single line

#print the secound line of that myFile
print(listOfLines[1])

#printing the last line from that myFile
print(listOfLines[len(listOfLines) - 1])


'''
Series_reference,Period,Data_value,STATUS,UNITS,Subject,Group,Series_title_1
CPIM.SE901,1960.01,45.923461,FINAL,Index,Consumers Price Index - CPI,Food Price Index for New Zealand,Food
CPIM.SE901502,2018.12,1045,FINAL,Index,Consumers Price Index - CPI,Food Price Index Level 3 Classes for New Zealand,Ready-to-eat food
'''

################################################ SINGLE LINE INFORMATION START#################################################################
aLine = listOfLines[1]
lineItems = aLine.split(',')
print(lineItems)

'''
['CPIM.SE901', '1960.01', '45.923461', 'FINAL', 'Index', 'Consumers Price Index - CPI', 'Food Price Index for New Zealand', 'Food']
'''

series = lineItems[0]
data = lineItems[2]

print('series = ', series)
print('data = ', data)

#lets split series
seriesSplit = series.split('.')
seriesHeader = seriesSplit[0]
seriesLast = seriesSplit[1]

print('seriesHeader = ', seriesHeader, 'seriesLast = ', seriesLast)

################################################ SINGLE LINE INFORMATION END #################################################################
