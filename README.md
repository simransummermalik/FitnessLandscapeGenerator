# FitnessLandscapeGenerator
A Fitness Landscape Generator

# Fitness Landscape Generator  
## Population Genetics Simulation  

Author: Summer Malik
Date: April 2025  

## Background Information  

In population genetics, a fitness landscape is a way of visualizing how different combinations of alleles (gene variants) influence the survival and reproduction of a population.

- Alleles that increase fitness (better survival & reproduction) are represented as "peaks" in the landscape.
- Alleles with lower fitness are in the "valleys."
- Natural selection tends to push populations towards the peaks.
- Mutation introduces random variation, sometimes allowing escape from local traps.

Fitness landscapes help scientists understand how populations evolve over time under different evolutionary pressures like selection, mutation, and genetic drift.

## How It Works (Simple Breakdown)

This simulation models a population evolving across a 3D fitness landscape over several generations.

| Axis | What it Represents |
|------|-------------------|
| X-axis | Frequency of Allele A |
| Y-axis | Frequency of Allele B |
| Z-axis | Fitness (higher = better survival & reproduction) |


### Simulation Logic:

- The population starts at a random (or user-defined) point in allele frequency space.
- Natural selection moves the population uphill toward higher fitness regions.
- Mutation adds randomness, so the path is not perfectly straight.
- The red line in the plot shows the evolutionary path of the population over time.

## Where to Input Your Own Data  

### Set Your Own Starting Allele Frequencies:

In `project_1.py`, find this section:

```python
# Random starting allele frequencies
freqA = np.random.rand()
freqB = np.random.rand()

#Customize the Fitness Landscape:
In main.py, find the fitness() function:
def fitness(alleleA, alleleB):
return np.exp(-((alleleA - 0.5) ** 2 + (alleleB - 0.5) ** 2) * selection_strength)

Modify it to change the location of fitness peaks.

Example: Disruptive selection with two peaks:
def fitness(alleleA, alleleB):
    peak1 = np.exp(-((alleleA - 0.2) ** 2 + (alleleB - 0.8) ** 2) * selection_strength)
    peak2 = np.exp(-((alleleA - 0.8) ** 2 + (alleleB - 0.2) ** 2) * selection_strength)
    return np.maximum(peak1, peak2)

Running the Simulation:
1. Install all required Libraries
pip install numpy plotly
2.Run it!
python project_1.py (or how you saved the file)





