# 🏙️ Project 02 – Empire State Building Random Walk (Hacker Statistics)

## 📌 Overview  
This project simulates 500 random walks of 100 steps each, following special dice rules to model a “climb” up the Empire State Building. The goal is to estimate the probability of ending at **≥ 60 steps** using Monte Carlo simulation.  

## 📂 Files  
- `Project_02_empire_random_walk.ipynb` → Jupyter Notebook with simulation and analysis  

## 🛠️ Tools & Skills  
- Python (NumPy, Matplotlib)  
- Random process simulation (Monte Carlo)  
- Data visualization (histograms, sample paths)  
- Probability estimation  

## 🔍 Key Questions  
1. What does the distribution of final steps look like after 100 moves?  
2. What is the estimated probability of ending at step **≥ 60**?  
3. How does clumsiness (0.1% fall chance) affect outcomes?  

## 📊 Insights  
- Most walks cluster below the 60-step mark, but a portion exceed it.  
- The simulation provides a reproducible way to approximate the winning chance without complex equations.  
- Histogram visualization highlights the spread of ending positions across 500 simulations.  

## ✅ Result  
The probability of reaching at least **60 steps** is estimated by:  
```python
np.mean(ends >= 60) * 100

This returns the percentage of simulations where the final step was ≥ 60. For example, a sample run might output:

Estimated chance of reaching ≥ 60 steps: 77.60% (n=500)
