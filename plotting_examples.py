# This code gives some examples for plotting of data

# Getting data using .loc[] and .iloc[]
pandas.DataFrame.iloc[i,j] # where i is the row and j the column

df.iloc[0:3, 1]

# Other option with .loc[]
pandas.DataFrame.loc["name in index", "name in columns"]
df.loc["Aruba", "1960"]
df.loc["Aruba", ["1960", "1980"]]
df.loc["Aruba", "1960": "1960"]

# Subsetting using a boolean
rows_of_interest = d2["Inidcator"]== "urban population (% of total)"

# Using the variable "rows_of_interest" to subset d2
d_subset = d2.loc[rows_of_interest]


# We have used a series of plotting commands from the matplotlib.pyplot library. The start for plotting was always to create our figure and axes objects with the .subplots() command, e.g.:

fig, ax = plt.subplots(nrows=1, ncols=1)

# ax.plot()
# ax.pie()
# ax.scatter()
# ax.bar()

# Below, a plain plot is plotted

import matplotlib.pyplot as plt
fig, ax = plt.subplots(nrows=1, ncols=1)

x = d_s1x   # the years
y1 = d_s1y1 # United States
y2 = d_s1y2 # China

ax.plot(x,y1, label = country1)
ax.plot(x,y2, label = country2)

# making the plot pretty
ax.set_title(descriptor1+' for '+ country1 + ' and ' + country2)
ax.set_xlabel('year')
ax.set_ylabel(descriptor1)
ax.legend()


