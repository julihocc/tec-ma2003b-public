# Kuiper Belt Objects PCA Example

## Overview

This example demonstrates Principal Component Analysis (PCA) applied to orbital parameters of Kuiper Belt objects and trans-Neptunian objects in the outer solar system. It analyzes synthetic astronomical data for 98 objects across 5 orbital elements to understand the main modes of orbital variation.

## Files

- `fetch_kuiper.py` - Generates synthetic Kuiper Belt object orbital data
- `kuiper_example.py` - Main PCA analysis script with astronomical interpretation  
- `kuiper.csv` - Generated dataset (98 objects × 5 orbital parameters)
- `kuiper_scree.png` - Scree plot for component selection
- `kuiper_biplot.png` - Biplot visualization of objects and orbital parameters
- `KUIPER_BELT_DATA_DICTIONARY.md` - Detailed variable definitions and astronomical context

## Orbital Parameters

The dataset includes 5 key orbital elements:

1. **designation** - Object identifier (Minor Planet Center numbering)
2. **a** (AU) - Semi-major axis (average distance from Sun)
3. **e** - Eccentricity (orbital shape, 0=circle to 1=parabola) 
4. **i** (degrees) - Inclination (tilt relative to solar system plane)
5. **H** (magnitude) - Absolute magnitude (brightness/size indicator)

## Usage

```bash
# Generate the synthetic Kuiper Belt data
python fetch_kuiper.py

# Run the PCA analysis
python kuiper_example.py
```

## Key Findings

The PCA analysis reveals:

- **PC1 (39.8% variance)**: Orbital excitation dimension
  - Correlates semi-major axis, eccentricity, and inclination
  - Separates dynamically "hot" (excited) from "cold" (pristine) populations
  
- **PC2 (21.4% variance)**: Size-distance relationship
  - May reflect observational bias or physical size distribution

## Educational Value

This example illustrates:
- **Astronomical data analysis**: Working with real-world space science datasets
- **Orbital dynamics**: How gravitational perturbations create correlated orbital families
- **Population structure**: Identifying distinct dynamical groups (classical, scattered, resonant)
- **Physical interpretation**: Connecting statistical patterns to astrophysical processes

See `KUIPER_BELT_DATA_DICTIONARY.md` for detailed explanations of each orbital parameter and their physical significance in planetary science.
