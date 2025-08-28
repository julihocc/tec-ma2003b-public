# European Stock Markets Data Dictionary

## Dataset Overview
This dataset contains synthetic daily closing prices for four major European stock market indices over a period of 1860 trading days (approximately 7.5 years). The data is designed to reflect realistic stock market behavior with high correlations between regional markets.

## Variables

### `rownames` (integer)
- **Description**: Sequential row identifier for each trading day
- **Format**: Integer (1, 2, 3, ..., 1860)
- **Range**: 1-1860
- **Purpose**: Simple time index for the observations

### `DAX` (float)
- **Description**: German stock market index (Deutscher Aktienindex)
- **Units**: Index points
- **Range**: ~2,000-4,500 points (typical for this time period)
- **Market**: Frankfurt Stock Exchange, Germany
- **Composition**: 30 largest German companies by market capitalization
- **Economic significance**: Represents German economic performance and European continental markets

### `SMI` (float)
- **Description**: Swiss stock market index (Swiss Market Index)
- **Units**: Index points  
- **Range**: ~3,000-7,000 points
- **Market**: SIX Swiss Exchange
- **Composition**: 20 largest Swiss companies
- **Economic significance**: Represents Swiss market, known for stability and multinational corporations

### `CAC` (float)
- **Description**: French stock market index (CAC 40)
- **Units**: Index points
- **Range**: ~1,800-4,400 points
- **Market**: Euronext Paris
- **Composition**: 40 largest French companies
- **Economic significance**: Represents French economic performance and Eurozone integration

### `FTSE` (float)  
- **Description**: UK stock market index (Financial Times Stock Exchange 100)
- **Units**: Index points
- **Range**: ~2,900-6,500 points
- **Market**: London Stock Exchange
- **Composition**: 100 largest UK companies by market capitalization
- **Economic significance**: Represents UK economy, historically less correlated with EU markets

## Correlation Structure

The synthetic data exhibits realistic correlations found in European stock markets:

1. **High inter-market correlations (0.99+)**:
   - Markets move together due to shared economic factors
   - Global financial integration creates synchronized movements
   - Similar business cycles across European economies

2. **DAX-SMI correlation (~0.993)**:
   - Geographic proximity and strong trade relationships
   - Similar economic structures (manufacturing, exports)

3. **FTSE correlations (~0.994-0.996)**:
   - Despite Brexit, UK markets remain highly correlated with Europe
   - Multinational companies listed across exchanges

## Market Dynamics Represented

### Common Market Factor (75% weight)
- **Description**: Shared movements across all European markets
- **Drivers**: 
  - European Central Bank monetary policy
  - Global economic conditions
  - Major political events (elections, Brexit, etc.)
  - Currency fluctuations (EUR/USD, GBP/USD)

### Regional Factors (20% weight)
- **European Factor**: Affects continental markets (DAX, SMI, CAC)
  - Eurozone-specific news and policies
  - EU regulations and trade agreements
- **UK Factor**: Affects FTSE specifically
  - Bank of England policy
  - UK-specific political developments

### Individual Market Noise (5-25% weight)
- **Company-specific news**: Earnings announcements, mergers
- **Sector rotation**: Different weightings across markets
- **Technical trading**: Market-specific momentum and volatility

## Financial Context

### Time Period Characteristics
- **Bull/bear cycles**: Natural market fluctuations over 7+ years
- **Volatility clustering**: Periods of high and low volatility
- **Mean reversion**: Tendency for extreme values to return toward average
- **Random walk behavior**: Daily returns approximately follow random walk with drift

### Economic Interpretation
- **Market integration**: High correlations reflect globalized financial markets
- **Risk diversification**: Limited benefits from European diversification alone
- **Systematic risk**: Common factors affect all markets simultaneously
- **Portfolio management**: Need for global (not just regional) diversification

## Educational Applications

### Principal Component Analysis
- **PC1 (99.5% variance)**: Common European market factor
  - Represents overall market sentiment and economic conditions
  - Almost perfect correlation suggests markets move as one unit
- **PC2-PC4 (0.5% variance)**: Market-specific factors
  - Subtle differences in national economic performance
  - Currency effects and local political developments

### Financial Modeling Concepts
- **Factor models**: Decomposition into common and specific factors
- **Risk management**: Understanding correlated vs idiosyncratic risk
- **Portfolio optimization**: Efficient frontier with highly correlated assets
- **Market efficiency**: How information flows across integrated markets

### Statistical Learning
- **Multivariate time series**: Multiple correlated financial series
- **Dimensionality reduction**: Summarizing complex market data
- **Correlation vs causation**: High correlation doesn't imply direct causation
- **Out-of-sample performance**: How PCA models generalize to new data

## Data Generation Notes

The synthetic data uses a multi-factor model:
- **Market returns**: Generated using correlated random walks
- **Realistic volatility**: Daily returns approximately 0.5-1.5% standard deviation
- **Price levels**: Converted from return series to maintain realistic index values
- **Correlation preservation**: Factor weightings designed to match empirical correlations

## References for Real Data
- Yahoo Finance: Historical index data
- European Central Bank: Economic statistics
- Bloomberg/Reuters: Professional financial data services
- Academic finance databases: CRSP, Datastream, Thomson Reuters
