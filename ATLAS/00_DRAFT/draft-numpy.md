---
tags:
  - learning
HUB:
  - "[[hub-python]]"
---
 [[numpy-transformacao-logaritima-method]]

>[!Calcula a soma cumulativa]
```python
import numpy as np 
data = [1, 2, 3, 4, 5] 
cumulative_sum = np.cumsum(data) print(cumulative_sum)
```

>[!Calcula o máximo cumulativo]
```python
data = [3, 1, 4, 1, 5, 9, 2, 6] 
cumulative_max = np.maximum.accumulate(data) 
print(cumulative_max)
```

```python
import numpy as np

# Create list baseball
baseball = [180, 215, 210, 210, 188, 176, 209, 200]

# Create a numpy array from baseball: np_baseball
np_baseball = np.array(baseball)

```

>[! Baseball players' height]
```python
# Create a numpy array from height_in: np_height_in

np_height_in = np.array(height_in)

# Print out np_height_in
print(np_height_in)

# Convert np_height_in to m: np_height_m
np_height_m = np_height_in * 0.0254
```

>[! Baseball player's BMI]
``` python
# Create array from height_in with metric units: np_height_m
np_height_m = np.array(height_in) * 0.0254

# Create array from weight_lb with metric units: np_weight_kg
np_weight_kg = np.array(weight_lb) * 0.453592

# Calculate the BMI: bmi
bmi = np_weight_kg / np_height_m  **2
```


>[! Lightweight baseball players]
```python
# Calculate the BMI: bmi
np_height_m = np.array(height_in) * 0.0254
np_weight_kg = np.array(weight_lb) * 0.453592
bmi = np_weight_kg / np_height_m ** 2

# Create the light array
light = bmi < 21

# Print out ligh
print(light)

# Print out BMIs of all baseball players whose BMI is below 21
print(bmi[bmi< 21])
```


>[! Subsetting NumPy Arrays]
```python
# Store weight and height lists as numpy arrays

np_weight_lb = np.array(weight_lb)
np_height_in = np.array(height_in)

  

# Print out the weight at index 50
print(np_weight_lb[50])

# Print out sub-array of np_height_in: index 100 up to and including index 110
print(np_height_in[100:111])
```

>[!Subsetting 2D NumPy Arrays]
```python
# Create np_baseball (2 cols)
np_baseball = np.array(baseball)

# Print out the 50th row of np_baseball
print(np_baseball[49,:])

# Select the entire second column of np_baseball: np_weight_lb
np_weight_lb = np_baseball[:,1]
  
# Print out height of 124th player
print(np_baseball[123,0])
```

>[!aritmetic]
```python
# Convert positions and heights to numpy arrays: np_positions, np_heights

np_positions = np.array(positions)
np_heights = np.array(heights)

# Heights of the goalkeepers: gk_heights

gk_heights = np_heights[np_positions == 'GK'] 

  

# Heights of the other players: other_heights
other_heights = np_heights[np_positions != 'GK'] 
 
# Print out the median height of goalkeepers. Replace 'None'
print("Median height of goalkeepers: " + str(np.median(gk_heights)))

  

# Print out the median height of other players. Replace 'None'
print("Median height of other players: " + str(np.median(other_heights)))
```
