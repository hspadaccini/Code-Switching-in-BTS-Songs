'''Hadley Spadaccini BTS Lyrics Analysis'''

from collections import Counter

class lyrstr:
    def count(self):
        self.count = 0
    def words_list(self):
        words_list = []

class BTSsuperstruct:
    def RM(self):
        self = lyrstr()
    def V(self):
        self = lyrstr()
    def JN(self):
        self = lyrstr()
    def JK(self):
        self = lyrstr()
    def JM(self):
        self = lyrstr()
    def JH(self):
        self = lyrstr()
    def SG(self):
        self = lyrstr()
    def All(self):
        self = lyrstr()

def isalpha(word):
    if(word[0] in ('a','b','c','d','e','f','g','h','i',
    'j','k','l','m','n','o','p','q','r','s','t','u','v',
    'w','x','y','z')):
        return True
    else:
        return False

def fill(text):
    data = open(text,"r")
    lyricdat = lyrstr()
    temp_list = []
    tempcount = 0
    line = data.readline()
    for line in data:
        for tempstr in line.split():
            if(isalpha(tempstr[0].lower()) == True):
                tempcount += 1
                temp_list.append(tempstr.lower())
                lyricdat.words_list = temp_list
                lyricdat.count = tempcount
            else:
                continue
    data.close
    return lyricdat

def MemberCount(text):
    data = open(text,"r")
    tempcountR = 0
    templist_R = []
    tempcountV = 0
    templist_V = []
    tempcountM = 0
    templist_M = []
    tempcountN = 0
    templist_N = []
    tempcountK = 0
    templist_K = []
    tempcountH = 0
    templist_H = []
    tempcountS = 0
    templist_S = []
    tagvar = 'NULL'
    BandDat = BTSsuperstruct()
    RM = lyrstr()
    V = lyrstr()
    M = lyrstr()
    N = lyrstr()
    K = lyrstr()
    H = lyrstr()
    S = lyrstr()
    line = data.readline()
    for line in data:
        for tempstr in line.split():
            temptagvar = WhoSings(tempstr)
            if(temptagvar != 'None'):
                tagvar = temptagvar
            if(temptagvar == 'None'):
                if(isalpha(tempstr[0].lower()) == True):
                    if(tagvar == 'R'):
                            tempcountR += 1
                            templist_R.append(tempstr.lower())
                            RM.words_list = templist_R
                            RM.count = tempcountR
                    if(tagvar == 'V'):
                            tempcountV += 1
                            templist_V.append(tempstr.lower())
                            V.words_list = templist_V
                            V.count = tempcountV
                    if(tagvar == 'M'):
                            tempcountM += 1
                            templist_M.append(tempstr.lower())
                            M.words_list = templist_M
                            M.count = tempcountM
                    if(tagvar == 'N'):
                            tempcountN += 1
                            templist_N.append(tempstr.lower())
                            N.words_list = templist_N
                            N.count = tempcountN
                    if(tagvar == 'K'):
                            tempcountK += 1
                            templist_K.append(tempstr.lower())
                            K.words_list = templist_K
                            K.count = tempcountK
                    if(tagvar == 'H'):
                            tempcountH += 1
                            templist_H.append(tempstr.lower())
                            H.words_list = templist_H
                            H.count = tempcountH
                    if(tagvar == 'S'):
                            tempcountS += 1
                            templist_S.append(tempstr.lower())
                            S.words_list = templist_S
                            S.count = tempcountS
                    if(tagvar == 'All'):
                            tempcountS += 1
                            templist_S.append(tempstr.lower())
                            S.words_list = templist_S
                            S.count = tempcountS
                            tempcountH += 1
                            templist_H.append(tempstr.lower())
                            H.words_list = templist_H
                            H.count = tempcountH
                            tempcountK += 1
                            templist_K.append(tempstr.lower())
                            K.words_list = templist_K
                            K.count = tempcountK
                            tempcountN += 1
                            templist_N.append(tempstr.lower())
                            N.words_list = templist_N
                            N.count = tempcountN
                            tempcountM += 1
                            templist_M.append(tempstr.lower())
                            M.words_list = templist_M
                            M.count = tempcountM
                            tempcountV += 1
                            templist_V.append(tempstr.lower())
                            V.words_list = templist_V
                            V.count = tempcountV
                            tempcountR += 1
                            templist_R.append(tempstr.lower())
                            RM.words_list = templist_R
                            RM.count = tempcountR
                    if(tagvar == 'KM'):
                            tempcountM += 1
                            templist_M.append(tempstr.lower())
                            M.words_list = templist_M
                            M.count = tempcountM
                            tempcountK += 1
                            templist_K.append(tempstr.lower())
                            K.words_list = templist_K
                            K.count = tempcountK
                    if(tagvar == 'SK'):
                            tempcountS += 1
                            templist_S.append(tempstr.lower())
                            S.words_list = templist_S
                            S.count = tempcountS
                            tempcountK += 1
                            templist_K.append(tempstr.lower())
                            K.words_list = templist_K
                            K.count = tempcountK
                    if(tagvar == 'NM'):
                            tempcountM += 1
                            templist_M.append(tempstr.lower())
                            M.words_list = templist_M
                            M.count = tempcountM
                            tempcountN += 1
                            templist_N.append(tempstr.lower())
                            N.words_list = templist_N
                            N.count = tempcountN
                    if(tagvar == 'HV'):
                            tempcountH += 1
                            templist_H.append(tempstr.lower())
                            H.words_list = templist_H
                            H.count = tempcountH
                            tempcountV += 1
                            templist_V.append(tempstr.lower())
                            V.words_list = templist_V
                            V.count = tempcountV
                    if(tagvar == 'KMR'):
                            tempcountK += 1
                            templist_K.append(tempstr.lower())
                            K.words_list = templist_K
                            K.count = tempcountK
                            tempcountR += 1
                            templist_R.append(tempstr.lower())
                            RM.words_list = templist_R
                            RM.count = tempcountR
                            tempcountM += 1
                            templist_M.append(tempstr.lower())
                            M.words_list = templist_M
                            M.count = tempcountM
                    if(tagvar == 'KMS'):
                            tempcountK += 1
                            templist_K.append(tempstr.lower())
                            K.words_list = templist_K
                            K.count = tempcountK
                            tempcountS += 1
                            templist_S.append(tempstr.lower())
                            S.words_list = templist_S
                            S.count = tempcountS
                            tempcountM += 1
                            templist_M.append(tempstr.lower())
                            M.words_list = templist_M
                            M.count = tempcountM
                    if(tagvar == 'NVKM'):
                            tempcountK += 1
                            templist_K.append(tempstr.lower())
                            K.words_list = templist_K
                            K.count = tempcountK
                            tempcountN += 1
                            templist_N.append(tempstr.lower())
                            N.words_list = templist_N
                            N.count = tempcountN
                            tempcountM += 1
                            templist_M.append(tempstr.lower())
                            M.words_list = templist_M
                            M.count = tempcountM
                            tempcountV += 1
                            templist_V.append(tempstr.lower())
                            V.words_list = templist_V
                            V.count = tempcountV
                        
    BandDat.RM = RM
    BandDat.V = V
    BandDat.M = M
    BandDat.N = N
    BandDat.K = K
    BandDat.H = H
    BandDat.S = S
    data.close
    return BandDat

def WhoSings(word):
    if (word == "[R]"):
        return 'R'
    elif(word == "[M]"):
        return 'M'
    elif(word == "[N]"):
        return 'N'
    elif(word == "[H]"):
        return 'H'
    elif(word == "[K]"):
        return 'K'
    elif(word == "[S]"):
        return 'S'
    elif(word == "[V]"):
        return 'V'
    elif(word == "[All]"):
        return 'All'
    elif(word == "[KM]"):
        return 'KM'
    elif(word == "[KMS]"):
        return 'KMS'
    elif(word == "[SK]"):
        return 'SK'
    elif(word == "[HV]"):
        return 'HV'
    elif(word == "[NVKM]"):
        return 'NVKM'
    elif(word == "[KMR]"):
        return 'KMR'
    elif(word == "[NM]"):
        return 'NM'
    else:
        return 'None'

def GenAverages(BandData, lyricscnt):
    average_list = []
    
    average_list.append(round(BandData.RM.count/lyricscnt*100,1))
    average_list.append(round(BandData.V.count/lyricscnt*100,1))
    average_list.append(round(BandData.N.count/lyricscnt*100,1))
    average_list.append(round(BandData.M.count/lyricscnt*100,1))
    average_list.append(round(BandData.H.count/lyricscnt*100,1))
    average_list.append(round(BandData.S.count/lyricscnt*100,1))
    average_list.append(round(BandData.K.count/lyricscnt*100,1))
    return average_list

def CombineMemberData(BandData2013,BandData2015,BandData2016,BandData2017,
            BandData2018,BandData2020):
    BandData = BTSsuperstruct()
    temporary = lyrstr()
    temporary.count = BandData2013.RM.count + BandData2015.RM.count + BandData2016.RM.count + BandData2017.RM.count + BandData2018.RM.count + BandData2020.RM.count
    temporary.words_list = BandData2013.RM.words_list + BandData2015.RM.words_list + BandData2016.RM.words_list + BandData2017.RM.words_list + BandData2018.RM.words_list + BandData2020.RM.words_list
    BandData.RM = temporary
    
    temporary = lyrstr()

    temporary.count = BandData2013.V.count + BandData2015.V.count + BandData2016.V.count + BandData2017.V.count + BandData2018.V.count + BandData2020.V.count
    temporary.words_list = BandData2013.V.words_list + BandData2015.V.words_list + BandData2016.V.words_list + BandData2017.V.words_list + BandData2018.V.words_list + BandData2020.V.words_list
    BandData.V = temporary
    
    temporary = lyrstr()

    temporary.count = BandData2013.M.count + BandData2015.M.count + BandData2016.M.count + BandData2017.M.count + BandData2018.M.count + BandData2020.M.count
    temporary.words_list = BandData2013.M.words_list + BandData2015.M.words_list + BandData2016.M.words_list + BandData2017.M.words_list + BandData2018.M.words_list + BandData2020.M.words_list
    BandData.M = temporary

    temporary = lyrstr()
    
    temporary.count = BandData2013.N.count + BandData2015.N.count + BandData2016.N.count + BandData2017.N.count + BandData2018.N.count + BandData2020.N.count
    temporary.words_list = BandData2013.N.words_list + BandData2015.N.words_list + BandData2016.N.words_list + BandData2017.N.words_list + BandData2018.N.words_list + BandData2020.N.words_list
    BandData.N = temporary
    
    temporary = lyrstr()

    temporary.count = BandData2013.K.count + BandData2015.K.count + BandData2016.K.count + BandData2017.K.count + BandData2018.K.count + BandData2020.K.count
    temporary.words_list = BandData2013.K.words_list + BandData2015.K.words_list + BandData2016.K.words_list + BandData2017.K.words_list + BandData2018.K.words_list + BandData2020.K.words_list
    BandData.K = temporary
    
    temporary = lyrstr()

    temporary.count = BandData2013.H.count + BandData2015.H.count + BandData2016.H.count + BandData2017.H.count + BandData2018.H.count + BandData2020.H.count
    temporary.words_list = BandData2013.H.words_list + BandData2015.H.words_list + BandData2016.H.words_list + BandData2017.H.words_list + BandData2018.H.words_list + BandData2020.H.words_list
    BandData.H = temporary
    
    temporary = lyrstr()

    temporary.count = BandData2013.S.count + BandData2015.S.count + BandData2016.S.count + BandData2017.S.count + BandData2018.S.count + BandData2020.S.count
    temporary.words_list = BandData2013.S.words_list + BandData2015.S.words_list + BandData2016.S.words_list + BandData2017.S.words_list + BandData2018.S.words_list + BandData2020.S.words_list
    BandData.S = temporary
    
    return BandData

def FindFive(word_list):
    new_list = []
    i = 0
    for i in word_list:
        if (i not in ("me","i","we","you","us","your","my","with","a","yeah","an","the","are","is","it","what","how","and","that","it's")):
            new_list.append(i)
    Counter1 = Counter(new_list)
    most_occur = Counter1.most_common(5)
    return most_occur