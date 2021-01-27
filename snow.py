'''
2019 (most recent) Swiss Climate Report, in German: 
https://www.meteoschweiz.admin.ch/content/dam/meteoswiss/de/service-und-publikationen/Publikationen/doc/klimareport_2019_de.pdf

Relevant: 
page 82: Snow measurements at 4 locations in CH; Luzern data is relevant
page 60: Precipitation; page 61 has data for winter precipitation in central Switzerland
page 54: Temperature
pages 18-19: Temperature and precipitation in Bern and Lugano
page 24: Unusual strong precipitation
Irrelevant: 
page 42: Record snow levels

Swiss temperature and precipitation data by month since ~1870 at multiple locations throughout the country
https://www.meteoswiss.admin.ch/home/climate/swiss-climate-in-detail/homogeneous-data-series-since-1864.html?region=Table
https://www.meteoswiss.admin.ch/product/output/climate-data/climate-diagrams-normal-values-station-processing/LUZ/climsheet_LUZ_np8110_e.pdf

Snow formation info: 
https://nsidc.org/cryosphere/snow/science/formation.html
Snow will not form above 5 degrees Celsius
https://www.metoffice.gov.uk/weather/learn-about/weather/types-of-weather/snow/how-does-snow-form
Must be under 2 degrees Celsius
'''
'''
TO DO: 
Get average and Stdv of temp and precipitation by month in Luzern for last 20 years
Create weighted random function for snowfall based on temperature

Code sources: 
https://stackabuse.com/read-a-file-line-by-line-in-python/
Random module docs
https://docs.python.org/3/library/statistics.html

'''

import matplotlib.pyplot as plt
import random as r
import statistics as stats

avgt = [0.5,1.4,5.4,9.1,13.7,16.9,19.1,18.3,14.6,10.2,4.6,1.6]
avgp = [51,54,74,88,128,154,151,146,107,76,73,72]
snowcm = [16,20,8,1,0,0,0,0,0,0,5,15]
snowdays = [3.8,4.4,1.9,0.6,0.0,0.0,0.0,0.0,0.0,0.0,1.1,3.6]
st = [1.8890032645110313, 2.497093548603294, 1.4625320509308506, 1.6914209298411682, 1.4138262842035305, 1.4991902576295737, 1.6554815153359606, 1.625598790775703, 1.4776590237521614, 1.4289523301722706, 1.0633057169126139, 1.449006227598435]
sp = [27.828088226305912, 25.253965360709383, 32.83023604991244, 52.1261778063423, 54.51384812309812, 51.712649276923486, 60.56368923302757, 56.68237797401513, 41.973468026130384, 28.887460107699376, 41.157127705875354, 37.74338884308806]
p20 = [21,31,50,58,80,113,91,106,66,43,38,35]
p40 = [42,43,60,75,116,144,128,131,86,70,55,49]
p60 = [54,55,70,86,147,171,151,157,117,79,72,71]
p80 = [83,71,94,129,179,189,209,185,157,103,108,104]
dayTemp = 0
monthPrecip = 0
rainDays = 0
data = []
thisYear = 0
year = 0
x = []
allYears = []

# function to determine if precipitation at that temperature is snow or rain
def createSnow(temp): 
    if temp > 2: 
        return 0
    elif temp > 0:
        return r.choices([0,1],[0.4,0.6])
    elif temp > -2:
        return r.choices([0,1],[0.1,0.9])
    else:
        return 1

# "month" values in the loop start counting from 0, as do the list indexes, so I don't need to correct the values by 1
# create two functions to generate random temperatures and precipitations
def newTemp(month):
    return r.gauss(avgt[month],st[month])

def newPrecip(month):
    #precip = r.gauss(avgp[month],sp[month])
    choice = r.choices([0,1,2],[0.3,0.4,0.3])
    print(choice)
    if choice == [0]:
        precip = r.randrange(p20[month],p40[month],1)
    elif choice == [1]: 
        precip = r.randrange(p40[month],p60[month],1)
    elif choice == [2]: 
        precip = r.randrange(p60[month],p80[month],1)
    return precip

#setting up axes
for num in range(180):
    data.append(0)

for num in range(180):
    x.append(num)

#here I assume that all months have 30 days; since the precipitation values are divided by the number of days in a month, this doesn't actually matter much
while year < 10000:
    for month in range(12): 
        monthPrecip = newPrecip(month)
        for day in range(10): # 9 is an approximate number for the average days of precipitation every winter month
            dayTemp = newTemp(month)
            daySnow = createSnow(dayTemp)
            if daySnow == [1]:
                thisYear += (monthPrecip / 10)
            day += 1
    thisYear = round(thisYear)
    print(thisYear)
    allYears.append(thisYear)
    data[thisYear] += 1
    year += 1
    thisYear = 0

#outputs
print("Mean: ")
print(stats.mean(allYears))
plt.plot(x,data)
plt.show()