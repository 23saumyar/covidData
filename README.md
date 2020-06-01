# SpaceApps: Bits N Bytes
Predicting future pandemic cases and pollution based on inputted key factors.
If you would like to run the Julia file and you do not have Julia installed, please use this: https://mybinder.org/v2/gh/23saumyar/covidData/master . Please note you may have to install additional features in the .toml files in order for the jupyter notebook to run as desired.

## Files + their purpose

**CovidPollutionOverTimeJulia.ipynb** is the main Julia Jupyter Notebook that asks for user input and produces 3 visuals on COVID-19 cases and NO2 pollution numbers using nearest neighbor.

**Mainfest.toml** and **Project.toml** and **environment.yml** allows you to run Julia on https://mybinder.org/v2/gh/23saumyar/covidData/master 

**SDGData.xlsx** contains key factor and COVID-19 cases data for each country.

**codePredictSimilarCountry.py** and **codePredictSimilarCountry.ipynb** are the python script called by the julia Jupyter notebook and contains details on the nearest neighbor process.

**covid_data.csv** and **covid_data_no2.csv** are created by the Julia file when current covid-19 data is downloaded from a separate repo.

**no2csvData.csv** contains NO2 data for each country.

**input.txt** and **request.txt** is used to store the inputs and nearest neighbor request, respectively.
