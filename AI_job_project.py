#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[2]:


job = pd.read_csv("ai_job_impact.csv")
job.head()


# In[3]:


job.tail()


# In[4]:


job.info()


# In[5]:


job.columns


# In[6]:


job.shape


# In[45]:


job.isnull().any()
# No Null values


# In[8]:


job.isnull().sum().any()
# No Null values


# In[9]:


print(job.describe())
# Statistical summary for all columns


# In[10]:


print(job.describe(include='object'))
# Statistical summary for only non-numerical columns


# In[11]:


print("Duplicate Rows :", job.duplicated().sum())


# In[12]:


# Meadian of salary after AI
print("Median of salary:",np.median(job['Salary_After_AI']))

# Standard Daviation of salary after AI
print("Standard Daviation of Salary:",np.std(job['Salary_After_AI']))

print("Maximum salary:",np.max(job['Salary_After_AI']))

print("Minimun salary:",np.min(job['Salary_After_AI']))

print("Average salary:",np.mean(job['Salary_After_AI']))


# In[13]:


# Average Salary after AI
job['Salary_After_AI'].mean()


# In[31]:


# Salary Difference
job['Salary_Difference'] = job['Salary_After_AI'] - job['Salary_Before_AI']
job[['Industry','Salary_Before_AI','Salary_After_AI','Salary_Difference']].head()


# In[32]:


# Average Salary after AI Grouped by Industry

job.groupby('Industry')[['Salary_After_AI']].mean().sort_values(by= 'Salary_After_AI', ascending=False)


# In[17]:


# Average Salary after AI Grouped by Education Level

job.groupby('Education_Level')['Salary_After_AI'].mean().sort_values(ascending=False)


# In[40]:


# Average Salary after AI grouped by Industry and AI Adoption level of thoes industries

job.groupby(['Industry', 'AI_Adoption_Level'])[['Salary_After_AI']].mean().round(2)


# In[19]:


# People working in office are more than remote working people
job['Remote_Work'].value_counts()


# In[41]:


# The average productivity % is approx same with AI adoption but is increased with High AI Adoption level

job.groupby('AI_Adoption_Level')[['Productivity_Change_%']].mean().round(2)


# In[21]:


# Job satisfaction remains fairly consistent across industries, with only small variations

job.groupby('Industry')['Job_Satisfaction'].mean().sort_values(ascending=False)


# In[22]:


# Most employee's job status are unchanged even after AI adoption 
# some employees has modified there jobs and only 106 were replaced

job['Job_Status'].value_counts()


# In[23]:


# Automation risk differs across industries, with each industry showing a different distribution of risk levels.
job.groupby('Industry')['Automation_Risk'].value_counts()


# In[37]:


job.groupby('Gender')[['Salary_After_AI']].mean()


# In[25]:


job.groupby('Job_Role')[['Salary_Before_AI','Salary_After_AI']].mean().sort_values(by= ['Salary_Before_AI','Salary_After_AI'], ascending=False)


# In[35]:


industry = job['Industry'].value_counts()

plt.figure(figsize=(10,7))
c = ['skyblue', 'lightgreen', 'salmon', 'gold','plum', 'orange', 'turquoise', 'pink']
bars = plt.bar(industry.index, industry.values, color = c, label='Number of Employees')
plt.bar_label(bars)

plt.title("Employees by Industry")
plt.xlabel("Industry")
plt.ylabel("Count")

plt.legend()

plt.show()

# The chart shows the distribution of employees across different industries.


# In[46]:


salary = job[['Salary_Before_AI','Salary_After_AI']].mean()

plt.figure(figsize=(6,6))
c=['lightblue','orange']
bars = plt.bar(salary.index, salary.values, color=c)
plt.bar_label(bars)
plt.title("Average Salary Before vs After AI")
plt.xlabel("Salary")
plt.ylabel("Average Salary")
plt.show()

# Chart shows Average Salary after AI is more than before AI


# In[28]:


status = job['Job_Status'].value_counts()

plt.figure(figsize=(5,5))
plt.pie(status.values, labels=status.index, autopct = "%0.1f%%", shadow =True, textprops = {"fontsize":12, "color": "black"})

plt.title("Distribution of Job Status")
plt.show()


# In[33]:


sns.histplot(job['Salary_Difference'], kde=True)


# In[ ]:





# Analysis :: 
# Conclusion: The analysis indicates that AI has primarily transformed jobs rather than replacing them, with most employees retaining their positions and many experiencing modified responsibilities. Industries with higher AI adoption generally demonstrated better salary outcomes, while technical and customer-facing job roles showed notable benefits after AI implementation. Productivity also improved with higher levels of AI adoption, highlighting AI's positive impact on workplace efficiency. Additionally, automation risk varied across industries, reflecting that the impact of AI differs depending on the nature of the work. 
# 
# Recommendation: AI has improved productivity and contributed to salary growth. Organizations should use AI as a tool to assist employees rather than replace human expertise.

# In[ ]:




