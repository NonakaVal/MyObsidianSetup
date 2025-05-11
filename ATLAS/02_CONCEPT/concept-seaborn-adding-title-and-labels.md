---
tags:
  - learning/review
HUB:
  - "[[hub-python]]"
  - "[[hub-data-visualization]]"
---
```python
# Create scatter plot
g = sns.relplot(x="weight", y="horsepower", data=mpg, kind="scatter")

# Add a title "Car Weight vs. Horsepower"
g.fig.suptitle("Car Weight vs. Horsepower")

# Show the plot
plt.show()

```

# Adding titles and labels: Part 2

```python
# Create point plot
sns.catplot(
    x="origin",
    y="acceleration",
    data=mpg,
    kind="point",
    join=False,
    capsize=0.1
)

# Rotate x-tick labels
plt.xticks(rotation=90)

# Show the plot
plt.show()

```


```python
#Setpaletteto"Blues"

sns.set_palette('Blues')  

#Adjusttoaddsubgroupsbasedon"InterestedinPets"
g=sns.catplot(x="Gender",
y="Age",data=survey_data,
kind="box",hue="InterestedinPets")

#Settitleto"AgeofThoseInterestedinPetsvs.Not"
g.fig.suptitle('AgeofThoseInterestedinPetsvs.Not')


#Showplot
plt.show()
```


```python
#Setthefigurestyleto"dark"

sns.set_style('dark')

#Adjusttoaddsubplotspergender
g=sns.catplot(x="Village-town",y="LikesTechno",
data=survey_data,kind="bar",
col='Gender')

#Addtitleandaxislabels
g.fig.suptitle("PercentageofYoungPeopleWhoLikeTechno",y=1.02)
g.set(xlabel="LocationofResidence",
ylabel="%WhoLikeTechno")

#Showplot
plt.show()
```