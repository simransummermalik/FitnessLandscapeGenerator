import numpy as np
import plotly.graph_objects as go
import plotly.express as px
import time

# Parameters
generations = 50
pop_size = 100
mutation_rate = 0.01  # Optional mutation
selection_strength = 20  # How steep the fitness peak is

# Allele frequency grid
x = np.linspace(0, 1, 50)  # Allele A frequency
y = np.linspace(0, 1, 50)  # Allele B frequency

#Fitness Landscape Function
def fitness(alleleA, alleleB):
    # Peak at-
    return np.exp(-((alleleA - 0.5) ** 2 + (alleleB - 0.5) ** 2) * selection_strength)

# Landscape Grid
X, Y = np.meshgrid(x, y)
Z = fitness(X, Y)

#random allele frequencies
freqA = np.random.rand()
freqB = np.random.rand()

#allele frequencies over time
historyA = [freqA]
historyB = [freqB]

for gen in range(generations):
    fit = fitness(freqA, freqB)
    
   
    freqA += (0.5 - freqA) * fit * 0.1
    freqB += (0.5 - freqB) * fit * 0.1
    
    #  randomness
    freqA += np.random.uniform(-mutation_rate, mutation_rate)
    freqB += np.random.uniform(-mutation_rate, mutation_rate)
    
    
    freqA = np.clip(freqA, 0, 1)
    freqB = np.clip(freqB, 0, 1)
    
    historyA.append(freqA)
    historyB.append(freqB)

# fitness Landscape Plot
fig = go.Figure()


fig.add_trace(go.Surface(z=Z, x=x, y=y, colorscale='Viridis', opacity=0.7))


fig.add_trace(go.Scatter3d(
    x=historyA,
    y=historyB,
    z=[fitness(a, b) for a, b in zip(historyA, historyB)],
    mode='lines+markers',
    line=dict(color='red', width=5),
    marker=dict(size=5, color='red')
))

fig.update_layout(
    title="Fitness Landscape Generator",
    scene=dict(
        xaxis_title='Allele A Frequency',
        yaxis_title='Allele B Frequency',
        zaxis_title='Fitness'
    )
)

fig.show()
