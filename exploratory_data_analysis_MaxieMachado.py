## References:
##https://www.linkedin.com/pulse/treating-outliers-python-lets-get-started-bushra-tasnim-zahed
##https://www.geeksforgeeks.org/data-pre-processing-wit-sklearn-using-standard-and-minmax-scaler/
##https://towardsdatascience.com/feature-selection-in-python-using-filter-method-7ae5cbc4ee05
##https://www.digitalocean.com/community/tutorials/standardscaler-function-in-python
##https://jovian.com/jamesbabu010/exploratory-data-analysis-of-cars-dataset
##https://archive.ics.uci.edu/dataset/165/concrete+compressive+strength
##https://archive.ics.uci.edu/dataset/186/wine+quality

#importing needed tools 
%matplotlib inline
import numpy as np 
import pandas as pd
import seaborn as sns
from scipy import stats 
from scipy.stats import mstats
import matplotlib.pylab as plt
from sklearn import preprocessing 
from sklearn.preprocessing import StandardScaler

##red wine quality dataset##

#import RED WINE dataset 
red_wine_data = pd.read_csv('winequality-red.csv')

#shape of RED WINE dataframe 
red_wine_data.shape

red_wine_data.dtypes

red_wine_data.info()

#first 5 rows of RED WINE dataframe 
red_wine_data.head()

#all columns in RED WINE dataframe 
red_wine_data.columns

#untouched red wine data
red_wine_df = red_wine_data[['fixed acidity', 'volatile acidity', 'citric acid', 'residual sugar',
       'chlorides', 'free sulfur dioxide', 'total sulfur dioxide', 'density',
       'pH', 'sulphates', 'alcohol']]
red_wine_untouched = sns.boxplot(data = red_wine_df, orient = "h", palette = "Set2")
plt.show()

##outliers analysis##

#calculate z-score of column 'quality'
z_score_rw = stats.zscore(red_wine_data['quality'])

#identify outliers with a z-score of greater than 3 or less than -3 
outliers_rw = red_wine_data[(z_score_rw > 3) | (z_score_rw < -3)]
outliers_rw 

#10 outliers based on 'quality'
fig, red_wine_untouched = plt.subplots(figsize=(10, 10))
sns.boxplot(x=red_wine_data['quality'], ax = red_wine_untouched)
red_wine_untouched.set_title('Quality of Red Wine', fontsize = 15)
plt.show()

#understanding the boxplot data of quality red wine 
red_wine_data['quality'].describe()

#filtering the dataframe to only include outlier with a quality over 7 
outlier_rw_qua_1 = red_wine_data[red_wine_data['quality'] > 7]
#calculating the percentage of outlier_rw_qua_1 
per_out_rw_qua_1 = (len(outlier_rw_qua_1) / len(red_wine_data)) * 100
per_out_rw_qua_1

#filtering the dataframe to only include outlier with a quality under 4 
outlier_rw_qua_2 = red_wine_data[red_wine_data['quality'] < 4]
#calculating the percentage of outlier_rw_qua_2
per_out_rw_qua_2 = (len(outlier_rw_qua_2) / len(red_wine_data)) * 100
per_out_rw_qua_2

#handling the outliers in red_wine_data
red_wine_data['quality'] = mstats.winsorize(red_wine_data['quality'], limits = [0.01, 0.1])

red_wine_data['quality'].sort_values(ascending = False).head(10)

#winsorize outliers in 'quality'
fig, red_wine_winsorize = plt.subplots(figsize = (10,10))
sns.boxplot(x = red_wine_data['quality'], ax = red_wine_winsorize)
red_wine_winsorize.set_title('Distribution of the Quality of Red Wine')
plt.show()

red_wine_data['quality'].describe()

#normalize red_wine_data using StandardScaler 
scaler_rw = StandardScaler()
scaler_rw.fit_transform(red_wine_data)

#splitting independent variables (features) and dependent variable (quality)
features_rw = red_wine_data.drop('quality', axis = 1)
quality = red_wine_data['quality']

#standardization 
scale_rw = scaler_rw.fit_transform(features_rw)
scale_rw

#Feature selection, filter method 
X_rw = red_wine_data.drop(columns = ['quality'])
X_rw

y_rw = red_wine_data['quality']
y_rw

X_y_rw = X_rw.copy()
X_y_rw['quality'] = y_rw 
X_y_rw

corr_matrix_rw = X_y_rw.corr()

#isolate the column corresponding to 'quality'
corr_tar_rw = corr_matrix_rw[['quality']].drop(labels = ['quality'])]

sns.heatmap(corr_tar_rw, annot = True, fmt = '3', cmap = 'RdBu_r')
plt.show()

##concrete compressive strength dataset## 

#import concrete dataset 
concrete_data = pd.read_csv('concrete_data.csv')

#first 5 rows of concrete dataset 
concrete_data.head()

#checking the datatype of concrete dataframe 
concrete_data.dtypes

#statistical summary of concrete dataset 
concrete_data.describe()

#print information about concrete dataframe 
concrete_data.info()

#all columns of concrete dataset 
concrete_data.columns

#renaming the columns 
concrete_data.rename(columns = { 'Cement (component 1)(kg in a m^3 mixture)' : 'cement (kg/m^3)',
       'Blast Furnace Slag (component 2)(kg in a m^3 mixture)' : 'blast furnace (kg/m^3)',
       'Fly Ash (component 3)(kg in a m^3 mixture)' : 'fly ash (kg/m^3)',
       'Water  (component 4)(kg in a m^3 mixture)' : 'water (kg/m^3)',
       'Superplasticizer (component 5)(kg in a m^3 mixture)' : 'superplasticizer (kg/m^3)',
       'Coarse Aggregate  (component 6)(kg in a m^3 mixture)' : 'coarse aggregate (kg/m^3)',
       'Fine Aggregate (component 7)(kg in a m^3 mixture)' : 'fine aggregate',
       'Concrete compressive strength(MPa, megapascals) ': 'concrete compressive strength (MPa)'}, inplace = True)
concrete_data.head()

concrete_data.columns

#checking for missing values in concrete dataset 
concrete_data.isnull().sum()

#shape of concrete dataframe 
concrete_data.shape
#handling duplicates 
concrete_data.duplicated().sum()

#duplicates in the concrete_data 
concrete_data.loc[concrete_data.duplicated(), :]

#dropping duplicates in dataset 
concrete_data.drop_duplicates(inplace = True, keep = 'first')

#check to see if the duplicates were handled in the dataset 
concrete_data.duplicated().sum()

#handling null values 
concrete_data.isnull().sum()

concrete_data.info()

##outliers analysis##

#untouched concrete data
concrete_df = concrete_data[['cement (kg/m^3)', 'blast furnace (kg/m^3)', 'fly ash (kg/m^3)',
       'water (kg/m^3)', 'superplasticizer (kg/m^3)',
       'coarse aggregate (kg/m^3)', 'fine aggregate', 'Age (day)',
       'concrete compressive strength (MPa)']]
concrete_untouched = sns.boxplot(data = concrete_df, orient ="h", palette = 'Set2')
plt.show()

#caluclate z-score of column 'concrete compressive strength (MPa)'
z_score_c = stats.zscore(concrete_data['concrete compressive strength (MPa)'])
#identify outliers with a z-score greater than 3 or less then -3
outliers_c = concrete_data[(z_score_c > 3) | (z_score_c < -3)]
outliers_c

#outliers based out 'concrete compressive strength (MPa)'
fig, concrete_untouched = plt.subplots(figsize=(10,10))
sns.boxplot(x=concrete_data['concrete compressive strength (MPa)'], ax = concrete_untouched)
concrete_untouched.set_title('concrete compressive strength (MPa)', fontsize = 15)
plt.show()

#understanding boxplot with statistical summary 
concrete_data['concrete compressive strength (MPa)'].describe()

#filtering the dataframe to only include outlier with a concrete compressive strength (MPa) over 78
outliers_c_ccs = concrete_data[concrete_data['concrete compressive strength (MPa)'] > 78]

#calculating the percentage of outliers_c_ccs
per_out_c_ccs = (len(outliers_c_ccs)/len(concrete_data))*100
per_out_c_ccs

#handling the outliers in the concrete_data 
concrete_data['concrete compressive strength (MPa)'] = mstats.winsorize(concrete_data['concrete compressive strength (MPa)'], limits = [0.01,0.1])

concrete_data['concrete compressive strength (MPa)'].sort_values(ascending = False).head(10)

#winsorize outliers in 'concrete compressive strength (MPa)'
fig, concrete_winsorize = plt.subplots(figsize=(10,10))
sns.boxplot(x=concrete_data['concrete compressive strength (MPa)'], ax=concrete_winsorize)
concrete_winsorize.set_title('concrete compressive strength (MPa)')
plt.show()

concrete_data['concrete compressive strength (MPa)'].describe()

#normalize concrete_data using StandardScaler 
scaler_c = StandardScaler()
scaler_c.fit_transform(concrete_data)

#splitting independent variables and dependent variable 
features_c = concrete_data.drop('concrete compressive strength (MPa)', axis = 1)
ccs = concrete_data['concrete compressive strength (MPa)']

#standardization 
scale_c = scaler_c.fit_transform(features_c)
scale_c

#feature selection, filter method 
X_c = concrete_data.drop(columns = ['concrete compressive strength (MPa)'])
X_c

y_c = concrete_data['concrete compressive strength (MPa)']
y_c

X_y_c = X_c.copy()
X_y_c['concrete compressive strength (MPa)'] = y_c
X_y_c

corr_matrix_c = X_y_c.corr()

#isolate the column corresponding to 'concrete compressive strength (MPa)'
corr_tar_c = corr_matrix_c[['concrete compressive strength (MPa)']].drop(labels = ['concrete compressive strength (MPa)'])

sns.heatmap(corr_tar_c, annot = True, fmt = '3', cmap = 'RdBu_r')
plt.show()
