# European Stock Markets PCA Example

## Overview

This example demonstrates Principal Component Analysis (PCA) applied to European stock market indices. It analyzes synthetic financial data for 4 major European stock markets over 1,860 trading days to understand market integration and correlation structure.

## Files

- `fetch_invest.py` - Generates synthetic European stock market index data
- `invest_example.py` - Main PCA analysis script with financial interpretation
- `invest.csv` - Generated dataset (1,860 days × 4 market indices)  
- `invest_scree.png` - Scree plot for component selection
- `invest_biplot.png` - Biplot visualization of time series and market loadings
- `EUROPEAN_STOCKS_DATA_DICTIONARY.md` - Detailed variable definitions and financial context

## Market Indices

The dataset includes 4 major European stock indices:

1. **DAX** - German stock market (Frankfurt)
2. **SMI** - Swiss stock market (Zurich)
3. **CAC** - French stock market (Paris) 
4. **FTSE** - UK stock market (London)

## Usage

```bash
# Generate the synthetic stock market data
python fetch_invest.py

# Run the PCA analysis  
python invest_example.py
```

## Key Findings

The PCA analysis reveals:

- **PC1 (99.5% variance)**: Common European market factor
  - Represents shared movements across all markets
  - Reflects global economic conditions and European integration
  - Demonstrates high correlation between regional markets

- **PC2-PC4 (0.5% variance)**: Market-specific factors
  - Capture subtle differences in national economic performance
  - Currency effects and country-specific political developments

## Educational Value

This example illustrates:

- **Financial market analysis**: Understanding correlation structure in asset returns
- **Factor models**: Decomposition into systematic and idiosyncratic risk components  
- **Market integration**: How globalization creates highly correlated financial markets
- **Portfolio diversification**: Limited benefits from regional diversification alone
- **Risk management**: Identifying common factors that drive multiple assets

See `EUROPEAN_STOCKS_DATA_DICTIONARY.md` for detailed explanations of each market index and their economic significance in European finance.
