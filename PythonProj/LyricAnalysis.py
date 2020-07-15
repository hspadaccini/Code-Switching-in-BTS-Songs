'''Analysis of Lyrics'''

import DefinedFunctions
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from prettytable import PrettyTable
from collections import Counter

lyrics2013 = DefinedFunctions.lyrstr()
lyrics2013 = DefinedFunctions.fill("BTSlyrics2013")

lyrics2015 = DefinedFunctions.lyrstr()
lyrics2015 = DefinedFunctions.fill("BTSlyrics2015")

lyrics2016 = DefinedFunctions.lyrstr()
lyrics2016 = DefinedFunctions.fill("BTSlyrics2016")

lyrics2017 = DefinedFunctions.lyrstr()
lyrics2017 = DefinedFunctions.fill("BTSlyrics2017")

lyrics2018 = DefinedFunctions.lyrstr()
lyrics2018 = DefinedFunctions.fill("BTSlyrics2018")

lyrics2020 = DefinedFunctions.lyrstr()
lyrics2020 = DefinedFunctions.fill("BTSlyrics2020")

totalcount = lyrics2013.count + lyrics2015.count + lyrics2016.count + lyrics2017.count + lyrics2018.count + lyrics2020.count

path = "/Users/hadleyspadaccini/Desktop/SPRING2020/ContactLinguistics/PythonProj/Singers2013"
BTS2013 = DefinedFunctions.BTSsuperstruct()
BTS2013 = DefinedFunctions.MemberCount(path)

path = "/Users/hadleyspadaccini/Desktop/SPRING2020/ContactLinguistics/PythonProj/Singers2015"
BTS2015 = DefinedFunctions.BTSsuperstruct()
BTS2015 = DefinedFunctions.MemberCount(path)

path = "/Users/hadleyspadaccini/Desktop/SPRING2020/ContactLinguistics/PythonProj/Singers2016"
BTS2016 = DefinedFunctions.BTSsuperstruct()
BTS2016 = DefinedFunctions.MemberCount(path)

path = "/Users/hadleyspadaccini/Desktop/SPRING2020/ContactLinguistics/PythonProj/Singers2017"
BTS2017 = DefinedFunctions.BTSsuperstruct()
BTS2017 = DefinedFunctions.MemberCount(path)

path = "/Users/hadleyspadaccini/Desktop/SPRING2020/ContactLinguistics/PythonProj/Singers2018"
BTS2018 = DefinedFunctions.BTSsuperstruct()
BTS2018 = DefinedFunctions.MemberCount(path)

path = "/Users/hadleyspadaccini/Desktop/SPRING2020/ContactLinguistics/PythonProj/Singers2020"
BTS2020 = DefinedFunctions.BTSsuperstruct()
BTS2020 = DefinedFunctions.MemberCount(path)

BTSall = DefinedFunctions.BTSsuperstruct()
BTSall = DefinedFunctions.CombineMemberData(BTS2013,BTS2015,BTS2016,BTS2017,BTS2018,BTS2020)

#Compare the percentages of each year's EN lyrics sang by each member

years = ["2013", "2015", "2016", "2017",
              "2018", "2020", "Overall"]
bandmembers = ["RM", "V", "Jin",
           "Jimin", "J-Hope", "Suga", "Jungkook"]

avg13 = DefinedFunctions.GenAverages(BTS2013,lyrics2013.count)
avg15 = DefinedFunctions.GenAverages(BTS2015,lyrics2015.count)
avg16 = DefinedFunctions.GenAverages(BTS2016,lyrics2016.count)
avg17 = DefinedFunctions.GenAverages(BTS2017,lyrics2017.count)
avg18 = DefinedFunctions.GenAverages(BTS2018,lyrics2018.count)
avg20 = DefinedFunctions.GenAverages(BTS2020,lyrics2020.count)
avgall = DefinedFunctions.GenAverages(BTSall,totalcount)

#Percent of lyrics per Member

lyricspermember = np.array([[avg13[0], avg13[1], avg13[2], avg13[3], avg13[4], avg13[5], avg13[6]],
                    [avg15[0], avg15[1], avg15[2], avg15[3], avg15[4], avg15[5], avg15[6]],
                    [avg16[0], avg16[1], avg16[2], avg16[3], avg16[4], avg16[5], avg16[6]],
                    [avg17[0], avg17[1], avg17[2], avg17[3], avg17[4], avg17[5], avg17[6]],
                    [avg18[0], avg18[1], avg18[2], avg18[3], avg18[4], avg18[5], avg18[6]],
                    [avg20[0], avg20[1], avg20[2], avg20[3], avg20[4], avg20[5], avg20[6]],
                    [avgall[0], avgall[1], avgall[2], avgall[3], avgall[4], avgall[5], avgall[6]]])

fig, ax = plt.subplots()
im = ax.imshow(lyricspermember)

# We want to show all ticks...
ax.set_xticks(np.arange(len(bandmembers)))
ax.set_yticks(np.arange(len(years)))
# ... and label them with the respective list entries
ax.set_xticklabels(bandmembers)
ax.set_yticklabels(years)

# Rotate the tick labels and set their alignment.
plt.setp(ax.get_xticklabels(), rotation=45, ha="right",
         rotation_mode="anchor")

# Loop over data dimensions and create text annotations.
for i in range(len(years)):
    for j in range(len(bandmembers)):
        text = ax.text(j, i, lyricspermember[i, j],
                       ha="center", va="center", color="w")

ax.set_title("Percentages of English Lyrics Said (per year)")
fig.tight_layout()
plt.show()

#Number of Code-Switched Lyrics per Member

years2 = ["2013", "2015", "2016", "2017",
              "2018", "2020", "Overall"]
bandmembers2 = ["RM", "V", "Jin",
           "Jimin", "J-Hope", "Suga", "Jungkook","Total Lyrics"]



switchespermember = np.array([[BTS2013.RM.count, BTS2013.V.count, BTS2013.N.count, BTS2013.M.count, BTS2013.H.count, BTS2013.S.count, BTS2013.K.count, lyrics2013.count],
                    [BTS2015.RM.count, BTS2015.V.count, BTS2015.N.count, BTS2015.M.count, BTS2015.H.count, BTS2015.S.count, BTS2015.K.count,lyrics2015.count],
                    [BTS2016.RM.count, BTS2016.V.count, BTS2016.N.count, BTS2016.M.count, BTS2016.H.count, BTS2016.S.count, BTS2016.K.count,lyrics2016.count],
                    [BTS2017.RM.count, BTS2017.V.count, BTS2017.N.count, BTS2017.M.count, BTS2017.H.count, BTS2017.S.count, BTS2017.K.count,lyrics2017.count],
                    [BTS2018.RM.count, BTS2018.V.count, BTS2018.N.count, BTS2018.M.count, BTS2018.H.count, BTS2018.S.count, BTS2018.K.count,lyrics2018.count],
                    [BTS2020.RM.count, BTS2020.V.count, BTS2020.N.count, BTS2020.M.count, BTS2020.H.count, BTS2020.S.count, BTS2020.K.count,lyrics2020.count],
                    [BTSall.RM.count, BTSall.V.count, BTSall.N.count, BTSall.M.count, BTSall.H.count, BTSall.S.count, BTSall.K.count,totalcount]])

fig, ax = plt.subplots()
im = ax.imshow(switchespermember)

# We want to show all ticks...
ax.set_xticks(np.arange(len(bandmembers2)))
ax.set_yticks(np.arange(len(years2)))
# ... and label them with the respective list entries
ax.set_xticklabels(bandmembers2)
ax.set_yticklabels(years2)

# Rotate the tick labels and set their alignment.
plt.setp(ax.get_xticklabels(), rotation=45, ha="right",
         rotation_mode="anchor")

# Loop over data dimensions and create text annotations.
for i in range(len(years2)):
    for j in range(len(bandmembers2)):
        text = ax.text(j, i, switchespermember[i, j],
                       ha="center", va="center", color="w")

ax.set_title("Number of English Code-Switches Uttered (per year)")
fig.tight_layout()
plt.show()

#Create a table for word frequencies

#most common five words per year
#not including "me","i","we","you","us","your","my","how","and"
# "with","a","yeah","an","the","are","is","it","what","that","it's"

x = PrettyTable()

x.field_names = ["Year", "Word 1", "Word 2", "Word 3","Word 4","Word 5"]

most_occur2013 = DefinedFunctions.FindFive(lyrics2013.words_list)
most_occur2015 = DefinedFunctions.FindFive(lyrics2015.words_list)
most_occur2016 = DefinedFunctions.FindFive(lyrics2016.words_list)
most_occur2017 = DefinedFunctions.FindFive(lyrics2017.words_list)
most_occur2018 = DefinedFunctions.FindFive(lyrics2018.words_list)
most_occur2020 = DefinedFunctions.FindFive(lyrics2020.words_list)

x.add_row(["2013", most_occur2013[0],most_occur2013[1],most_occur2013[2],most_occur2013[3],most_occur2013[4]])
x.add_row(["2015", most_occur2015[0],most_occur2015[1],most_occur2015[2],most_occur2015[3],most_occur2015[4]])
x.add_row(["2016", most_occur2016[0],most_occur2016[1],most_occur2016[2],most_occur2016[3],most_occur2016[4]])
x.add_row(["2017", most_occur2017[0],most_occur2017[1],most_occur2017[2],most_occur2017[3],most_occur2017[4]])
x.add_row(["2018", most_occur2018[0],most_occur2018[1],most_occur2018[2],most_occur2018[3],most_occur2018[4]])
x.add_row(["2020", most_occur2020[0],most_occur2020[1],most_occur2020[2],most_occur2020[3],most_occur2020[4]])

print(x)