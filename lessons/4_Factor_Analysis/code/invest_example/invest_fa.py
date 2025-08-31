# %% [markdown]
# # Factor Analysis of European Stock Markets
#
# This script applies Factor Analysis to European stock market data to identify
# common market factors and understand the latent structure of financial market
# integration. Unlike PCA which focuses on variance maximization, Factor Analysis
# seeks to model the shared comovement among European markets.
#
# ## Financial Factor Analysis Applications:
# - **Market Integration**: Common factors representing systematic market risks
# - **Contagion Analysis**: How shocks spread through interconnected markets
# - **Portfolio Construction**: Risk factor identification for diversification
# - **Asset Pricing**: Multi-factor models (Fama-French, APT theory)
#
# ## Expected Factor Structure:
# - **Common European Factor**: Shared economic/political influences
# - **Regional Factors**: Country-specific or sector-specific factors
# - **Idiosyncratic Components**: Market-specific movements

# %%
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from pathlib import Path
from factor_analyzer import FactorAnalyzer
from factor_analyzer.factor_analyzer import calculate_bartlett_sphericity, calculate_kmo
import seaborn as sns
from utils import setup_logger

# %%
# Setup logging and paths
script_dir = Path(__file__).resolve().parent
logger = setup_logger("invest_fa")

logger.info("Starting European Stock Markets Factor Analysis")
print("European Stock Markets - Factor Analysis")
print("=" * 50)

# %% [markdown]
# ## Load and Examine Financial Data
#
# We use the same European stock market data (DAX, SMI, CAC, FTSE) to enable
# direct comparison with the PCA analysis. This dataset represents 1,860 trading
# days of market index returns, providing a rich basis for factor analysis.

# %%
# Load the investment data
data_file = script_dir / "invest.csv"
if not data_file.exists():
    print(f"Data file not found: {data_file}")
    print(
        "Please run: .venv/bin/python lessons/4_Factor_Analysis/code/invest_example/fetch_invest.py"
    )
    exit(1)

# Load data
df = pd.read_csv(data_file, index_col=0)
print(f"Data loaded: {df.shape[0]} trading days × {df.shape[1]} market indices")
print(f"Trading day range: Day {df.index.min()} to Day {df.index.max()}")
print("\nMarket indices:", list(df.columns))

# Convert prices to returns for financial analysis
print("\nConverting price levels to daily returns...")
returns_df = df.pct_change().dropna()  # Daily percentage returns
print(f"Returns data: {returns_df.shape[0]} observations after conversion")

# Show basic statistics
print(f"\nMarket Statistics (Daily Returns):")
print(f"{'Market':<8} {'Mean':<8} {'Std':<8} {'Min':<8} {'Max':<8}")
print("-" * 44)
for col in returns_df.columns:
    returns_data = returns_df[col].dropna()
    mean_ret = returns_data.mean()  # Daily return
    volatility = returns_data.std()  # Daily volatility
    print(
        f"{col:<8} {mean_ret:<8.1%} {volatility:<8.1%} {returns_data.min():<8.1%} {returns_data.max():<8.1%}"
    )

# Update df to use returns for factor analysis
df = returns_df

# %% [markdown]
# ## Data Preprocessing and Factor Analysis Assumptions
#
# Financial returns often require careful preprocessing:
# - **Stationarity**: Returns are typically stationary (prices are not)
# - **Standardization**: Equal weight to different volatility markets
# - **Missing values**: Handle non-synchronous trading days
# - **Outliers**: Consider impact of market crashes/rallies

# %%
# Handle missing values and prepare data for analysis
X = df.values
X_clean = X[~np.isnan(X).any(axis=1)]  # Remove rows with any NaN
print(f"Data after cleaning: {X_clean.shape[0]} complete observations")

# Standardize the data
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X_clean)

# Check Factor Analysis assumptions
chi_square_value, p_value = calculate_bartlett_sphericity(X_scaled)
kmo_all, kmo_model = calculate_kmo(X_scaled)

print("\n" + "=" * 50)
print("FACTOR ANALYSIS ASSUMPTIONS")
print("=" * 50)
print(f"Bartlett's Test of Sphericity:")
print(f"  Chi-square: {chi_square_value:.2f}")
print(f"  p-value: {p_value:.2e}")
print(
    f"  Result: {'✓ Suitable for FA' if p_value < 0.05 else '✗ May not be suitable for FA'}"
)

print(f"\nKaiser-Meyer-Olkin (KMO) Test:")
print(f"  Overall MSA: {kmo_model:.3f}")
interpretation = (
    "✓ Excellent"
    if kmo_model > 0.9
    else (
        "✓ Good"
        if kmo_model > 0.8
        else (
            "✓ Acceptable"
            if kmo_model > 0.6
            else "⚠ Poor" if kmo_model > 0.5 else "✗ Unacceptable"
        )
    )
)
print(f"  Interpretation: {interpretation} sampling adequacy")

print(f"\nIndividual Market MSA Values:")
print(f"{'Market':<8} {'MSA':<8}")
print("-" * 18)
for i, market in enumerate(df.columns):
    print(f"{market:<8} {kmo_all[i]:<8.3f}")

# %% [markdown]
# ## Factor Extraction: Determine Number of Factors
#
# For financial markets, we use multiple criteria to determine factors:
# - **Kaiser Criterion**: Eigenvalues > 1
# - **Scree Plot**: Visual identification of "elbow"
# - **Theoretical Expectation**: 1-2 common market factors expected
# - **Parallel Analysis**: Compare with random data eigenvalues

# %%
# Perform initial factor analysis to examine eigenvalues
fa_explore = FactorAnalyzer(n_factors=df.shape[1], rotation=None, method="principal")
fa_explore.fit(X_scaled)

eigenvalues, _ = fa_explore.get_eigenvalues()

print("\n" + "=" * 50)
print("FACTOR RETENTION ANALYSIS")
print("=" * 50)
print(f"{'Factor':<8} {'Eigenvalue':<12} {'% Variance':<12} {'Cumulative %':<12}")
print("-" * 48)

cumulative_var = 0
n_factors_kaiser = 0
for i, eigenval in enumerate(eigenvalues):
    var_explained = eigenval / len(df.columns) * 100
    cumulative_var += var_explained
    if eigenval > 1.0:
        n_factors_kaiser += 1

    print(
        f"Factor {i+1:<2} {eigenval:<12.3f} {var_explained:<12.1f} {cumulative_var:<12.1f}"
    )

print(f"\nFactor Retention Criteria:")
print(f"  Kaiser criterion (eigenvalue > 1): {n_factors_kaiser} factors")
print(
    f"  70% variance rule: {np.argmax(np.cumsum(eigenvalues)/np.sum(eigenvalues) >= 0.70) + 1} factors"
)
print(f"  Financial theory expectation: 1-2 common market factors")

# %% [markdown]
# ## Factor Analysis: Two-Factor Solution
#
# Based on financial theory and our factor retention analysis, we extract 2 factors:
# - **Factor 1**: Expected to be a general European market factor
# - **Factor 2**: Expected to capture regional/sectoral differences
#
# We compare unrotated and Varimax-rotated solutions.

# %%
# Extract 2-factor solution
n_factors = 2
print(f"\n" + "=" * 50)
print(f"FACTOR ANALYSIS: {n_factors}-FACTOR SOLUTION")
print("=" * 50)

# Unrotated solution
fa_unrotated = FactorAnalyzer(n_factors=n_factors, rotation=None, method="principal")
fa_unrotated.fit(X_scaled)

# Varimax rotated solution
fa_rotated = FactorAnalyzer(n_factors=n_factors, rotation="varimax", method="principal")
fa_rotated.fit(X_scaled)

# Extract results
loadings_unrotated = fa_unrotated.loadings_
loadings_rotated = fa_rotated.loadings_
communalities = fa_rotated.get_communalities()
uniquenesses = 1 - communalities

print(f"Factor Analysis Results:")
print(
    f"{'Market':<8} {'h²':<8} {'u²':<8} {'Unrot-F1':<10} {'Unrot-F2':<10} {'Vmax-F1':<10} {'Vmax-F2':<10}"
)
print("-" * 78)
for i, market in enumerate(df.columns):
    print(
        f"{market:<8} {communalities[i]:<8.3f} {uniquenesses[i]:<8.3f} "
        f"{loadings_unrotated[i,0]:<10.3f} {loadings_unrotated[i,1]:<10.3f} "
        f"{loadings_rotated[i,0]:<10.3f} {loadings_rotated[i,1]:<10.3f}"
    )

# Calculate variance explained by factors
total_communality = np.sum(communalities)
proportion_common_variance = total_communality / len(df.columns)
print(f"\nVariance Analysis:")
print(f"  Total communality (sum of h²): {total_communality:.3f}")
print(
    f"  Proportion of variance explained by factors: {proportion_common_variance:.1%}"
)
print(f"  Average communality per market: {np.mean(communalities):.3f}")

# %% [markdown]
# ## Factor Interpretation and Financial Insights
#
# Let's interpret what each factor represents in financial terms:

# %%
print(f"\n" + "=" * 50)
print("FACTOR INTERPRETATION")
print("=" * 50)

# Identify factor characteristics based on loadings
loading_threshold = 0.4
print(f"Factor loadings above {loading_threshold} threshold:")

for factor_idx in range(n_factors):
    factor_name = f"Factor {factor_idx + 1}"
    high_loading_markets = []

    print(f"\n{factor_name}:")
    for market_idx, market in enumerate(df.columns):
        loading = loadings_rotated[market_idx, factor_idx]
        if abs(loading) > loading_threshold:
            sign = "+" if loading > 0 else "-"
            high_loading_markets.append(f"{sign}{market}({abs(loading):.2f})")

        print(f"  {market:<8}: {loading:>6.3f}")

    if high_loading_markets:
        print(f"  High loadings: {', '.join(high_loading_markets)}")

    # Financial interpretation
    if factor_idx == 0:
        print(f"  → Likely represents: Common European market factor")
        print(f"    (Systematic risk affecting all markets)")
    elif factor_idx == 1:
        print(f"  → Likely represents: Regional/sectoral differentiation")
        print(f"    (Idiosyncratic movements between markets)")

# Market integration analysis
print(f"\nMarket Integration Analysis:")
well_explained = [
    market
    for i, market in enumerate(df.columns)
    if communalities[i] > np.mean(communalities)
]
poorly_explained = [
    market
    for i, market in enumerate(df.columns)
    if communalities[i] <= np.mean(communalities)
]

print(f"  Highly integrated markets (h² > average): {', '.join(well_explained)}")
print(f"  More idiosyncratic markets (h² ≤ average): {', '.join(poorly_explained)}")

# %% [markdown]
# ## Visualization: Factor Structure

# %%
# Create comprehensive factor analysis visualizations
fig = plt.figure(figsize=(15, 10))

# 1. Factor loadings heatmap comparison
ax1 = plt.subplot(2, 3, 1)
sns.heatmap(
    loadings_unrotated.T,
    annot=True,
    fmt=".2f",
    xticklabels=df.columns,
    yticklabels=[f"Factor {i+1}" for i in range(n_factors)],
    cmap="RdBu_r",
    center=0,
    cbar_kws={"shrink": 0.8},
)
ax1.set_title("Unrotated Factor Loadings")

ax2 = plt.subplot(2, 3, 2)
sns.heatmap(
    loadings_rotated.T,
    annot=True,
    fmt=".2f",
    xticklabels=df.columns,
    yticklabels=[f"Factor {i+1}" for i in range(n_factors)],
    cmap="RdBu_r",
    center=0,
    cbar_kws={"shrink": 0.8},
)
ax2.set_title("Varimax Rotated Loadings")

# 2. Communalities bar chart
ax3 = plt.subplot(2, 3, 3)
bars = ax3.bar(df.columns, communalities, color="steelblue", alpha=0.7)
ax3.set_title("Communalities by Market")
ax3.set_ylabel("h² (Proportion of Variance Explained)")
ax3.tick_params(axis="x", rotation=45)
ax3.axhline(
    y=np.mean(communalities),
    color="red",
    linestyle="--",
    label=f"Average = {np.mean(communalities):.3f}",
)
ax3.legend()
ax3.grid(True, alpha=0.3)

# 3. Scree plot
ax4 = plt.subplot(2, 3, 4)
factors = np.arange(1, len(eigenvalues) + 1)
ax4.plot(factors, eigenvalues, "o-", color="steelblue", markersize=8, linewidth=2)
ax4.axhline(y=1.0, color="red", linestyle="--", alpha=0.7, label="Kaiser criterion")
ax4.set_xlabel("Factor Number")
ax4.set_ylabel("Eigenvalue")
ax4.set_title("Scree Plot")
ax4.grid(True, alpha=0.3)
ax4.legend()
ax4.set_xticks(factors)

# 4. Factor scores scatter plot (first 100 observations)
ax5 = plt.subplot(2, 3, 5)
factor_scores = fa_rotated.transform(X_scaled)
scatter = ax5.scatter(
    factor_scores[:100, 0],
    factor_scores[:100, 1],
    c=np.arange(100),
    cmap="viridis",
    alpha=0.6,
)
ax5.set_xlabel("Factor 1 (Common Market)")
ax5.set_ylabel("Factor 2 (Regional Differences)")
ax5.set_title("Factor Scores (First 100 Days)")
ax5.grid(True, alpha=0.3)
plt.colorbar(scatter, ax=ax5, label="Trading Day")

# 5. Uniquenesses vs Communalities
ax6 = plt.subplot(2, 3, 6)
x = np.arange(len(df.columns))
width = 0.35
ax6.bar(
    x - width / 2,
    communalities,
    width,
    label="Communalities (h²)",
    color="steelblue",
    alpha=0.7,
)
ax6.bar(
    x + width / 2,
    uniquenesses,
    width,
    label="Uniquenesses (u²)",
    color="lightcoral",
    alpha=0.7,
)
ax6.set_xlabel("Markets")
ax6.set_ylabel("Proportion of Variance")
ax6.set_title("Variance Decomposition")
ax6.set_xticks(x)
ax6.set_xticklabels(df.columns, rotation=45)
ax6.legend()
ax6.grid(True, alpha=0.3)

plt.tight_layout()
loadings_out = script_dir / "invest_fa_loadings.png"
plt.savefig(loadings_out, dpi=150, bbox_inches="tight")
print(f"\nSaved comprehensive factor analysis plots: {loadings_out}")
logger.info(f"Saved factor analysis visualization: {loadings_out}")

# %% [markdown]
# ## Financial Risk and Portfolio Implications
#
# Factor Analysis results have direct applications in finance:

# %%
print(f"\n" + "=" * 50)
print("FINANCIAL APPLICATIONS")
print("=" * 50)

# 1. Systematic vs Idiosyncratic Risk
systematic_risk = np.mean(communalities)  # Average explained by common factors
idiosyncratic_risk = np.mean(uniquenesses)  # Average unexplained (market-specific)

print(f"Risk Decomposition (Average across markets):")
print(f"  Systematic risk (common factors): {systematic_risk:.1%}")
print(f"  Idiosyncratic risk (market-specific): {idiosyncratic_risk:.1%}")

# 2. Market Factor Sensitivities
print(f"\nMarket Factor Sensitivities:")
print(f"{'Market':<8} {'Factor 1':<10} {'Factor 2':<10} {'Interpretation'}")
print("-" * 60)

for i, market in enumerate(df.columns):
    f1_loading = loadings_rotated[i, 0]
    f2_loading = loadings_rotated[i, 1]

    # Interpret factor sensitivity
    if abs(f1_loading) > abs(f2_loading):
        interpretation = "Common factor driven"
    else:
        interpretation = "Regional factor driven"

    print(f"{market:<8} {f1_loading:<10.3f} {f2_loading:<10.3f} {interpretation}")

# 3. Portfolio Diversification Insights
print(f"\nPortfolio Diversification Insights:")
high_common = [
    market for i, market in enumerate(df.columns) if abs(loadings_rotated[i, 0]) > 0.8
]
differentiated = [
    market
    for i, market in enumerate(df.columns)
    if abs(loadings_rotated[i, 1]) > abs(loadings_rotated[i, 0])
]

if high_common:
    print(f"  Markets with high common factor exposure: {', '.join(high_common)}")
    print(f"  → These markets move together; limited diversification benefit")

if differentiated:
    print(f"  Markets with differentiated patterns: {', '.join(differentiated)}")
    print(f"  → These markets may provide diversification opportunities")

# %% [markdown]
# ## Model Validation and Goodness of Fit
#
# Assess how well our 2-factor model reproduces the observed correlations:

# %%
print(f"\n" + "=" * 50)
print("MODEL VALIDATION")
print("=" * 50)

# Calculate observed correlation matrix
observed_corr = np.corrcoef(X_scaled.T)

# Calculate reproduced correlation matrix from factor model
# R̂ = ΛΛ' + Ψ (where Ψ is diagonal uniquenesses matrix)
reproduced_corr = loadings_rotated @ loadings_rotated.T + np.diag(uniquenesses)

# Calculate residual correlation matrix
residual_corr = observed_corr - reproduced_corr

# Model fit statistics
total_corr_sum_sq = np.sum(observed_corr**2)
residual_sum_sq = np.sum(residual_corr**2)
fit_index = 1 - (residual_sum_sq / total_corr_sum_sq)

print(f"Model Fit Assessment:")
print(f"  Correlation fit index: {fit_index:.3f}")
print(f"  Interpretation: {fit_index:.1%} of correlations explained by factor model")

# Root mean squared residual
rmsr = np.sqrt(np.mean(residual_corr[np.triu_indices_from(residual_corr, k=1)] ** 2))
print(f"  Root Mean Square Residual (RMSR): {rmsr:.4f}")
print(
    f"  Interpretation: {'Good fit' if rmsr < 0.05 else 'Acceptable fit' if rmsr < 0.10 else 'Poor fit'}"
)

# Show largest residuals
residual_triu = residual_corr[np.triu_indices_from(residual_corr, k=1)]
large_residuals = np.abs(residual_triu) > 0.1

if np.any(large_residuals):
    print(f"\n  Large residual correlations (>0.1) detected:")
    triu_indices = list(zip(*np.triu_indices_from(residual_corr, k=1)))
    for i, is_large in enumerate(large_residuals):
        if is_large:
            row, col = triu_indices[i]
            market1, market2 = df.columns[row], df.columns[col]
            print(f"    {market1}-{market2}: {residual_triu[i]:.3f}")
    print(f"  → Consider additional factors or model modifications")
else:
    print(f"  ✓ All residual correlations < 0.1 - Good model fit")

# %% [markdown]
# ## Summary and Conclusions
#
# This Factor Analysis of European stock markets reveals:

# %%
print(f"\n" + "=" * 50)
print("SUMMARY AND CONCLUSIONS")
print("=" * 50)

print(f"Factor Structure Identified:")
print(
    f"  • {n_factors} common factors explain {proportion_common_variance:.1%} of market covariance"
)
print(f"  • Factor 1: Common European market factor (systematic risk)")
print(f"  • Factor 2: Regional differentiation factor (idiosyncratic patterns)")

print(f"\nKey Financial Insights:")
print(f"  • Average systematic risk: {systematic_risk:.1%}")
print(f"  • Average idiosyncratic risk: {idiosyncratic_risk:.1%}")
print(f"  • Model explains {fit_index:.1%} of observed correlations")

print(f"\nMarket Integration:")
most_integrated = df.columns[np.argmax(communalities)]
least_integrated = df.columns[np.argmin(communalities)]
print(
    f"  • Most integrated market: {most_integrated} (h² = {np.max(communalities):.3f})"
)
print(
    f"  • Least integrated market: {least_integrated} (h² = {np.min(communalities):.3f})"
)

print(f"\nPractical Applications:")
print(f"  • Portfolio risk management: Identify common risk factors")
print(f"  • Diversification strategy: Focus on markets with low communalities")
print(f"  • Risk modeling: Use factor loadings for multi-factor risk models")
print(f"  • Market timing: Monitor common factor vs idiosyncratic movements")

logger.info("European Stock Markets Factor Analysis completed successfully")
print(f"\nFactor analysis completed. Results saved to: {script_dir}")

# %% [markdown]
# ## Next Steps for Advanced Applications
#
# This analysis provides foundation for:
# - **Dynamic Factor Analysis**: Time-varying factor loadings
# - **Regime-Switching Models**: Different factors in different market states
# - **Higher-Frequency Analysis**: Intraday factor structures
# - **Cross-Asset Applications**: Bonds, currencies, commodities factor analysis
# - **Risk Attribution**: Performance attribution to systematic vs idiosyncratic sources
