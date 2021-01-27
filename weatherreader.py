#run cd "c:/Users/toads/OneDrive - Choate Rosemary Hall/Python" to make this work
w = open("weather.txt", "r")

import statistics as stats

temps = {1:[],2:[],3:[],4:[],5:[],6:[],7:[],8:[],9:[],10:[],11:[],12:[]}
precips = {1:[],2:[],3:[],4:[],5:[],6:[],7:[],8:[],9:[],10:[],11:[],12:[]}
avgt = []
avgp = []
st = []
sp = []
c = 0

while c < 252:
    line = w.readline().split()
    temps[int(line[1])].append(float(line[2]))
    precips[int(line[1])].append(float(line[3]))
    c += 1
print(precips)
for i in range(12):
    avgt.append(stats.mean(temps.get(i+1)))
    avgp.append(stats.stdev(precips.get(i+1)))
    st.append(stats.pstdev(temps.get(i+1)))
    sp.append(stats.pstdev(precips.get(i+1)))
print(avgt)
print(avgp)
print(st)
print(sp)