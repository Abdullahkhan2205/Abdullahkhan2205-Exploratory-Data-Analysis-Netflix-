#!/usr/bin/env python
# coding: utf-8

# # EXPLORATORY DATA ANALYSIS ON NETFLIX

# About the Netflix data: Netflix is one of the most popular media and video streaming platforms. They have over 8000 movies or tv shows available on their platform, as of mid-2021, they have over 200M Subscribers globally. This tabular dataset consists of listings of all the movies and tv shows available on Netflix, along with details such as - cast, directors, ratings, release year, duration, etc.
# 
# This data set consist of 10 columns and 8790 rows. which contains of information about the different Netflix Tv shows and Movies released in different countries.
# 
# The columns consist of id, type, title, director, country, date_added, release year,	rating and	duration.

# # Data Preparation and Cleaning

# In[1]:


import pandas as pd
import numpy as np


# ### Loading Data

# In[2]:


data_netflix = pd.read_csv(r'raw netflix.csv')


# In[3]:


data_netflix


# ### Information about data

# In[4]:


data_netflix.info()


# ### Identify the shape of the data set

# In[5]:


data_netflix.shape


# In[6]:


data_netflix.columns


# #### Show_id :
# This column shows the id of Netflix Tv shows and Movies.

# In[7]:


data_netflix.show_id.head(6)


# #### Type:
# This column show the type of the content wether it is a Tv show or a movie.

# In[8]:


data_netflix.type.head(6)


# #### Title:
# This shows the title of a Movie or Tv show.

# In[9]:


data_netflix.title.head(6)


# #### Director:
# This show the name of a director who directes the movie or a show.

# In[10]:


data_netflix.director.head(6)


# #### Country:
# This column shows the country of origin of a Tv shows and movies.

# In[11]:


data_netflix.country.head(6)


# #### Date Added:
# This column show the date on which the show is released.

# In[12]:


data_netflix.date_added.head(6)


# #### Release year:
# This column show the Year on which the show is released.

# In[13]:


data_netflix.release_year.head(6)


# #### Rating:
# This column show the rating of the show released on Netflix.

# In[14]:


data_netflix.rating.head(6)


# #### Duration:
# This column show the duration of the shows available in data.

# In[15]:


data_netflix.duration.head(6)


# #### Listed in:
# This column show the genre of the shows available in data. 

# In[16]:


data_netflix.listed_in.head(6)


# ### Description of dataset

# In[17]:


data_netflix.describe()


# ### Droping the duplicates

# In[18]:


data_netflix.drop_duplicates()


# ### Handling the Missing values

# In[19]:


Null_data= ['Not Given',np.nan]
dg=pd.read_csv(r'raw netflix.csv',na_values=Null_data)


# In[20]:


missing_data = data_netflix[data_netflix.isna()==True]
missing_data[missing_data==True].count()


# In[21]:


dg


# In[22]:


dg.dropna()


# # Visualization Analysis

# In[23]:


import matplotlib.pyplot as plt
import seaborn as sns


# In[24]:


plt.figure(figsize=(10,5))
plt.pie(dg['type'].value_counts().sort_values(),labels=dg['type'].value_counts().index,explode=[0.05,0],
        autopct='%1.2f%%',colors=['Green','grey'])
plt.title('Percentage of types')
plt.show()


# **Observation**: In this we observe that the percantage of Tv-shows is more than Movies.

# In[25]:


sns.heatmap(dg.isnull(),cmap = 'viridis')
plt.title('Missing values HeatMap',
          pad=20)


# **Observation:** In this chart we observe that there are null or not given values in director and country in our data.

# In[26]:


sns.countplot(x='type',data = dg)
plt.title('Number of Movies and Tv Shows',pad=10)
plt.xlabel=('Type')
plt.ylabel=('Count')
plt.show()


# **Observation**: In this we observe that there are more numbers of Movies than Tv shows.

# In[27]:


plt.figure(figsize = (12,8))
sns.countplot(x='rating',data = dg)
plt.title('Rating Counts',pad=10)
plt.xlabel=('Rating')
plt.ylabel=('Count')
plt.show()


# **Observation**: In this chart we observe the Rating counts of Tv shows and Movies.

# In[28]:


plt.figure(figsize = (35,6))
sns.countplot(x='release_year', data = dg)
plt.title('Number of movies and shows release in a year',pad=20)
plt.xlabel=('Release Year')
plt.ylabel=('Count')
plt.show()


# **Observation**:In this chart we observe the number of movies release per year.

# In[29]:


plt.figure(figsize = (12,8))
sns.countplot(x='rating',data = dg,hue='type')
plt.title('Ratings of movies and shows',pad=10)
plt.xlabel=('Ratings')
plt.ylabel=('Count')
plt.show()


# **Observation**: In this we observe the count of ratings of both movies and tv shows.

# In[30]:


get_ipython().system('pip install plotly')


# In[31]:


import plotly.express as px 
top_rated=dg[0:10]
fig =px.sunburst(
    top_rated,
    path=['country'],title='Distribution According Countries')
fig.show()


# **Observation**: In this we observe Country wise count of top rated Movies.

# In[32]:


plt.figure(figsize=(12,6))
dg[dg["type"]=="Movie"]["release_year"].value_counts()[:20].plot(kind="bar",color="Red")
plt.title("Frequency of Movies which were released in different years and are available on Netflix")
plt.xlabel=('release_Year')
plt.ylabel=('counts of Movies')


# **Observation**: In this we observe Country wise count of Movies on Netflix.

# # Question and Answers

# ### 1- What is The Moves and TV Shows Number In Each Year

# In[33]:


q1 = dg.groupby(['release_year','type'],as_index = False)['title'].count()

px.line(q1, x = 'release_year',y='title',color='type',labels={'title':'Number ','release_year':'release Year'},title='Moves and TV Shows Each Year').show()


# ### 2- What is the Frecuency Of Directors In Movies and TV Shows

# In[34]:


q2 = dg.groupby(['release_year','type'],as_index = False)['title'].count()
px.histogram(dg, x = 'director',color='type',title='Frecuency Of Directors In Movies and TV Shows').show()


# ### 3- Variety Of Rating In Movies and TV Shows

# In[35]:


px.histogram(dg, x = 'rating',color='type',barmode='group',title='Variety Of Rating In Movies and TV Shows')


# ### 4- Top 6 Country in Production in Movies And TV Shows

# In[36]:


q4 = dg.groupby(['country','type'],as_index=False)['title'].count()
px.bar(q4.sort_values('title')[-10:], x = 'country',color='type',y='title',barmode='group',title='Top 6 Country in Production in Movies And TV Shows')


# # Refrences and Future work

# Refrence Link: https://www.kaggle.com/datasets/ariyoomotade/netflix-data-cleaning-analysis-and-visualization
# 
# Future work: This dataset can further used to analyse the type of movies and tv shows country-wise for better results. 
# 

# # Inferences and Conclusion
# 
#    We explore the Netflix dataset and saw how to clean the data and then jump into how to visualize the data. We saw some basic and advanced level charts of Plotly like Heatmap, barchart, etc.
#    Through this we are able to analyse the top rated movies and tv shows available on Netflix
#    we are also able to find out the number of shows release according to countries
#    we also analyse the percentage of movies released on Netflix
#    we also fin out the top countries in production of the Movies and Tv shows.
