#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import math

file_path = "SDGData.xlsx"
df = pd.read_excel(file_path, "Countries_Constant", encoding='utf-16')
df = df.dropna(how='all')
countriesConstant = {} #{country:{density:100,Hospital Beds:100, Senior Population:.5,	Arrivals - Tourism:100,	Population Below Poverty Line:50}}


# In[2]:


for _,data in df.iterrows():
    countryData = {}
    countryData["density"] = data[1]
    countryData["beds"] = data[2]
    countryData["seniors"] = data[4]
    countryData["tourism"] = data[5]
    countryData["poverty"] = data[6]
    countriesConstant[data[0]] = countryData
# print(countriesConstant)


# In[9]:


#inputed values
inputFile = open('input.txt','r')    
inputs = inputFile.readlines()
inputL = []
for line in inputs: 
    inputL.append(float(line.strip()))



# inDensity = float(input("Input your population density "))
# inBeds = float(input("Input number of hospital beds per 1000 people "))
# inSeniors = float(input("Input percentage of population above 65 years old "))
# inTourism = float(input("Input number of airport arrivals "))
# inPoverty = float(input("Input fraction of people in poverty "))
inputData = {"density":inputL[0],"beds":inputL[1],"seniors":inputL[2],"tourism":inputL[3],"poverty":inputL[4]}


# In[10]:


def euclidean_distance(inputData, countryData): #[Density,Beds,Seniors,Tourism,Poverty]
    sqDiffSum=0

    for k in inputData.keys():
        if(math.isnan(inputData[k]) or math.isnan(countryData[k])):
            sqDiffSum +=0
        else:
            sqDiffSum += (inputData[k] - countryData[k])**2
    return sqDiffSum**(1/2)


# In[11]:


nearScores = {}
for country in countriesConstant.keys():
    nearness = euclidean_distance(inputData, countriesConstant[country])
    nearScores[country] = nearness
# print(nearScores)
closest = min(nearScores.keys(), key=(lambda k: nearScores[k]))
file = open("request.txt","w");
file.write(closest)
# print(closest)
file.close()






