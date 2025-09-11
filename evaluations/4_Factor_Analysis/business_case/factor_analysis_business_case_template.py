#!/usr/bin/env python3
"""
factor_analysis_business_case_template.py

Template for Business Case: Customer Satisfaction Intelligence
TechnoServe Solutions - Advanced Factor Analysis

Teams must complete TODOs and implement rigorous factor analysis
following statistical methodology and business interpretation.

Authors: [Team names]
Date: [Start date]
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from factor_analyzer import FactorAnalyzer
from factor_analyzer.factor_analyzer import calculate_kmo, calculate_bartlett_sphericity
from scipy import stats
import warnings

warnings.filterwarnings("ignore")

# Professional graphics configuration
plt.style.use("seaborn-v0_8")
sns.set_palette("husl")


def load_customer_data():
    """
    Loads and prepares the customer satisfaction dataset.

    Returns:
        tuple: (satisfaction_data, outcome_variables, metadata)
    """
    # TODO: Load customer_satisfaction_data.csv
    # TODO: Separate satisfaction variables (23 items) from outcome variables (5 items)
    # TODO: Create metadata dictionary for dataset

    pass


# %% [markdown]
# # Business Case: Customer Satisfaction Intelligence
# ## TechnoServe Solutions - Factor Analysis
#
# **Team:** [Team name]
# **Members:**
# - [Name 1] - [ID] - Expertise: Factorability and Extraction
# - [Name 2] - [ID] - Expertise: Interpretation and Scoring
# - [Name 3] - [ID] - Expertise: Application and Communication
#
# **Objective:** Transform customer satisfaction data into strategic intelligence
# through rigorous Factor Analysis and actionable business recommendations.


# %%
def exploratory_data_analysis(satisfaction_data):
    """
    Exploratory Data Analysis for satisfaction variables.

    Args:
        satisfaction_data: DataFrame with satisfaction variables (1-7 scale)

    Returns:
        dict: Results of exploratory analysis
    """
    print("=== EXPLORATORY DATA ANALYSIS ===")

    # TODO: Complete descriptive statistics
    # - Central tendency and dispersion measures per variable
    # - Outlier identification using IQR or Z-score
    # - Distribution analysis (histograms, Q-Q plots)

    # TODO: Análisis de correlaciones
    # - Matriz de correlación con visualización heatmap
    # - Identificación de clusters de variables correlacionadas
    # - Distribución de correlaciones (histograma de valores r)

    # TODO: Manejo de datos faltantes
    # - Análisis de patrón de missingness (MCAR, MAR, MNAR)
    # - Visualización de patrones de datos faltantes
    # - Estrategia de imputación o eliminación

    pass


# %% [markdown]
# ### Reflection Question 1
# **What patterns do you observe in the correlation matrix? How do these patterns
# suggest the presence of underlying latent factors?**
#
# [Team response - 4-6 lines]
# %%
def evaluate_factorability(clean_data):
    """
    Evaluates factorability using rigorous statistical tests.

    Args:
        clean_data: DataFrame without missing data

    Returns:
        dict: Factorability test results with interpretation
    """
    print("=== FACTORABILITY ASSESSMENT ===")

    results = {}

    # TODO: Kaiser-Meyer-Olkin (KMO) Test
    # - Global KMO (should be > 0.6, preferably > 0.8)
    # - Individual variable KMO
    # - Interpretation of MSA (Measure of Sampling Adequacy) values

    # TODO: Bartlett's Sphericity Test
    # - H₀: Correlation matrix is identity matrix
    # - Chi-square statistic and p-value
    # - Statistical interpretation (reject H₀ if p < 0.05)

    # TODO: Anti-image Matrix
    # - Partial correlations (should be small)
    # - Diagonal MSA values (> 0.5 acceptable)
    # - Identify problematic variables

    # TODO: Correlation Matrix Determinant
    # - Verify non-singularity (det ≠ 0)
    # - Evaluate extreme multicollinearity

    return results


# %% [markdown]
# ### Reflection Question 2
# **Why is it crucial to evaluate factorability before proceeding with factor
# extraction? What implications would ignoring these tests have?**
#
# [Team response - 4-6 lines]
# %%
def determine_optimal_factors(correlation_matrix, data):
    """
    Determines optimal number of factors using multiple criteria.

    Args:
        correlation_matrix: Correlation matrix
        data: DataFrame of clean data

    Returns:
        dict: Dimensionality analysis results
    """
    print("=== OPTIMAL NUMBER OF FACTORS DETERMINATION ===")

    # TODO: Kaiser Criterion (Eigenvalues > 1)
    # - Calculate correlation matrix eigenvalues
    # - Count eigenvalues > 1.0
    # - Plot eigenvalues in descending order

    # TODO: Scree Plot
    # - Visualize eigenvalues vs. factor number
    # - Identify "elbow" or inflection point
    # - Visual interpretation of cutoff point

    # TODO: Parallel Analysis (Horn, 1965)
    # - Generate random data with same dimensions
    # - Compare real vs. random eigenvalues
    # - Retain factors where real > random

    # TODO: Explained Variance
    # - % cumulative variance by number of factors
    # - Criterion of 60-80% explained variance
    # - Trade-off parsimony vs. explanation

    pass


# %% [markdown]
# ### Reflection Question 3
# **What advantages and limitations does each method have for determining the optimal
# number of factors? How do you reconcile contradictory results between methods?**
#
# [Team response - 4-6 lines]
# %%
def compare_extraction_methods(data, n_factors):
    """
    Compares factor extraction methods: PCA, PAF, ML.

    Args:
        data: Standardized DataFrame
        n_factors: Number of factors to extract

    Returns:
        dict: Comparative results by method
    """
    print("=== EXTRACTION METHODS COMPARISON ===")

    results = {}

    # TODO: Principal Component Analysis (PCA)
    # - Use sklearn.decomposition.PCA
    # - Calculate % explained variance per component
    # - Obtain component loadings matrix

    # TODO: Principal Axis Factoring (PAF)
    # - Use FactorAnalyzer with method='principal'
    # - Estimate communalities iteratively
    # - Compare communalities vs. PCA

    # TODO: Maximum Likelihood (ML)
    # - Use FactorAnalyzer with method='ml'
    # - Evaluate convergence and fit statistics
    # - Chi-square goodness of fit test

    # TODO: Comparative Analysis
    # - Eigenvalues and % variance by method
    # - Estimated communalities (h²)
    # - Residuals and goodness of fit
    # - Selected method justification

    return results


# %% [markdown]
# ### Reflection Question 4
# **When is it appropriate to use PCA vs. Factor Analysis? What fundamental
# assumptions differentiate these approaches and how do they affect business interpretation?**
#
# [Team response - 4-6 lines]
# %%
def apply_factor_rotations(factor_loadings, method="ml"):
    """
    Aplica y compara diferentes estrategias de rotación factorial.

    Args:
        factor_loadings: Matriz de cargas factoriales pre-rotación
        method: Método de extracción usado ('pca', 'paf', 'ml')

    Returns:
        dict: Resultados de rotaciones con métricas de calidad
    """
    print("=== ANÁLISIS DE ROTACIONES FACTORIALES ===")

    rotaciones = {}

    # TODO: Rotación Varimax (Ortogonal)
    # - Maximizar varianza de cargas al cuadrado
    # - Mantener factores independientes (correlación = 0)
    # - Evaluar estructura simple achieved

    # TODO: Rotación Promax (Oblicua)
    # - Permitir correlaciones entre factores
    # - Calcular correlaciones interfactoriales
    # - Evaluar si correlaciones son sustantivas (> 0.3)

    # TODO: Rotación Oblimin (Oblicua alternativa)
    # - Método directo oblicuo
    # - Comparar con Promax
    # - Evaluar estabilidad de solución

    # TODO: Evaluación de Calidad de Rotación
    # - Simplicidad de estructura (loading > |0.4| en un factor)
    # - Interpretabilidad conceptual
    # - % varianza preservada post-rotación
    # - Selección de rotación óptima con justificación

    return rotaciones


# %% [markdown]
# ### Pregunta de Reflexión 5
# **¿Por qué las correlaciones entre factores pueden ser teóricamente
# justificables en el contexto de satisfacción del cliente? ¿Qué implicaciones
# tiene esto para la selección de rotación?**
#
# [Respuesta del equipo - 4-6 líneas]


# %%
def interpret_and_label_factors(rotated_loadings, variable_names):
    """
    Interpreta factores y desarrolla etiquetas conceptuales empresariales.

    Args:
        rotated_loadings: Matriz de cargas post-rotación
        variable_names: Lista de nombres de variables

    Returns:
        dict: Interpretación factorial con etiquetas empresariales
    """
    print("=== INTERPRETACIÓN Y ETIQUETADO FACTORIAL ===")

    # TODO: Análisis de Cargas Factoriales
    # - Identificar variables con |loading| > 0.4 por factor
    # - Analizar variables con cargas cruzadas significativas
    # - Examinar coherencia teórica de agrupaciones

    # TODO: Desarrollo de Etiquetas Conceptuales
    # - Etiquetar factores basado en variables dominantes
    # - Conectar con dimensiones empresariales (ej: "Excelencia Técnica")
    # - Validar coherencia con framework teórico inicial

    # TODO: Validación de Estructura
    # - Alpha de Cronbach por factor (consistencia interna)
    # - Comunalidades para identificar variables mal representadas
    # - Análisis de variables residuales (sin carga clara)

    pass


# %% [markdown]
# ### Pregunta de Reflexión 6
# **¿Cómo balanceas la parsimonia estadística con la riqueza interpretativa
# al etiquetar factores? ¿Qué hacer con variables que no cargan claramente en ningún factor?**
#
# [Respuesta del equipo - 4-6 líneas]


# %%
def calculate_factor_scores_and_predict(factor_model, datos, outcomes):
    """
    Calcula factor scores y desarrolla modelos predictivos empresariales.

    Args:
        factor_model: Modelo factorial ajustado final
        datos: DataFrame de variables de satisfacción
        outcomes: DataFrame de variables de resultado

    Returns:
        dict: Factor scores y análisis predictivo
    """
    print("=== CÁLCULO DE FACTOR SCORES Y MODELADO PREDICTIVO ===")

    # TODO: Métodos de Factor Scoring
    # - Regression method (correlaciones óptimas)
    # - Bartlett method (varianza mínima, insesgado)
    # - Comparar propiedades estadísticas entre métodos

    # TODO: Validación de Factor Scores
    # - Verificar propiedades estadísticas esperadas
    # - Analizar distribuciones de scores
    # - Detectar outliers en espacio factorial

    # TODO: Modelos Predictivos por Outcome
    # - NPS Score ~ Factor1 + Factor2 + ... + FactorN
    # - Renewal Likelihood ~ Factor scores
    # - Revenue Growth ~ Factor scores
    # - Evaluar R², significancia, coeficientes

    # TODO: Matriz de Impacto Empresarial
    # - Factor × Outcome impact matrix
    # - Identificar factores más predictivos por outcome
    # - Desarrollar insights para priorización estratégica

    pass


# %% [markdown]
# ### Pregunta de Reflexión 7
# **¿Cómo interpretas la capacidad predictiva diferencial de los factores?
# ¿Qué factores son más críticos para outcomes específicos y por qué?**
#
# [Respuesta del equipo - 4-6 líneas]


# %%
def create_executive_visualizations(factor_results, outcomes_analysis):
    """
    Genera visualizaciones profesionales para audiencia ejecutiva.

    Args:
        factor_results: Resultados del análisis factorial
        outcomes_analysis: Análisis de variables de resultado

    Returns:
        dict: Gráficos ejecutivos y métricas clave
    """
    print("=== VISUALIZACIÓN EJECUTIVA AVANZADA ===")

    # TODO: Loading Plot (Factor Loadings Visualization)
    # - Scatter plot bidimensional de dos factores principales
    # - Variables como puntos con etiquetas claras
    # - Círculos de referencia para |loading| = 0.4, 0.7

    # TODO: Customer Score Plot
    # - Distribución de clientes en espacio factorial
    # - Identificar segmentos naturales
    # - Colorear por outcome performance (ej: NPS alto/bajo)

    # TODO: Factor Importance Heatmap
    # - Matriz Factor × Outcome con coeficientes predictivos
    # - Color coding por magnitud de impacto
    # - Anotaciones con R² y significancia

    # TODO: Strategic Priority Matrix
    # - Factores vs. Facilidad de mejora vs. Impacto empresarial
    # - Cuadrantes estratégicos para priorización
    # - Recomendaciones visuales claras

    pass


# %% [markdown]
# ### Pregunta de Reflexión 8
# **¿Qué historia cuenta cada visualización sobre la estructura subyacente
# de satisfacción del cliente? ¿Cómo usarías estos gráficos para convencer a un CEO escéptico?**
#
# [Respuesta del equipo - 4-6 líneas]


# %%
def generate_executive_recommendations(factor_insights, predictive_models):
    """
    Desarrolla recomendaciones estratégicas ejecutivas basadas en análisis factorial.

    Args:
        factor_insights: Interpretaciones factoriales
        predictive_models: Modelos predictivos factor → outcomes

    Returns:
        dict: Recomendaciones accionables con ROI estimado
    """
    print("=== RECOMENDACIONES ESTRATÉGICAS EJECUTIVAS ===")

    # TODO: Identificación de Factores Críticos
    # - Top 3 factores por impacto en retención/NPS
    # - Análisis de gaps en performance actual
    # - Benchmarking contra competencia (si disponible)

    # TODO: Matriz de Priorización
    # - Impacto empresarial vs. Dificultad de implementación
    # - Clasificación en Quick Wins vs. Strategic Initiatives
    # - Timeline de implementación sugerido

    # TODO: ROI y Business Case
    # - Estimación de mejora en NPS/retention por factor
    # - Traducción a impacto financiero ($)
    # - Inversión requerida vs. retorno esperado

    # TODO: Roadmap de Implementación
    # - Iniciativas específicas por factor crítico
    # - KPIs de seguimiento y métricas de éxito
    # - Plan de comunicación para stakeholders

    pass


# %%
def main_analysis_workflow():
    """
    Flujo principal de análisis factorial para el caso empresarial.
    Orquesta todas las etapas del análisis de manera sistemática.
    """
    print("INICIANDO ANÁLISIS FACTORIAL: CUSTOMER SATISFACTION INTELLIGENCE")
    print("=" * 70)

    # Stage 1: Data loading and preparation
    print("\n1. DATA LOADING AND PREPARATION")
    satisfaction_data, outcomes, metadata = load_customer_data()

    # Stage 2: Exploratory analysis
    print("\n2. EXPLORATORY DATA ANALYSIS")
    eda_results = exploratory_data_analysis(satisfaction_data)

    # Stage 3: Factorability assessment
    print("\n3. FACTORABILITY ASSESSMENT")
    factorability = evaluate_factorability(satisfaction_data.dropna())

    # Stage 4: Dimensionality determination
    print("\n4. OPTIMAL NUMBER OF FACTORS DETERMINATION")
    optimal_factors = determine_optimal_factors(
        satisfaction_data.corr(), satisfaction_data
    )

    # Stage 5: Extraction and method comparison
    print("\n5. COMPARATIVE FACTOR EXTRACTION")
    extraction_results = compare_extraction_methods(
        satisfaction_data, n_factors=5  # Adjust according to previous analysis
    )

    # Stage 6: Factor rotation
    print("\n6. FACTOR ROTATION ANALYSIS")
    rotation_results = apply_factor_rotations(extraction_results["best_loadings"])

    # Stage 7: Business interpretation
    print("\n7. FACTOR INTERPRETATION AND LABELING")
    factor_interpretation = interpret_and_label_factors(
        rotation_results["final_loadings"], satisfaction_data.columns
    )

    # Stage 8: Scoring and prediction
    print("\n8. FACTOR SCORING AND PREDICTIVE MODELING")
    predictive_analysis = calculate_factor_scores_and_predict(
        rotation_results["final_model"], satisfaction_data, outcomes
    )

    # Etapa 9: Visualización ejecutiva
    print("\n9. VISUALIZACIÓN EJECUTIVA")
    executive_viz = create_executive_visualizations(
        factor_interpretation, predictive_analysis
    )

    # Etapa 10: Recomendaciones estratégicas
    print("\n10. RECOMENDACIONES ESTRATÉGICAS")
    recommendations = generate_executive_recommendations(
        factor_interpretation, predictive_analysis
    )

    print("\n" + "=" * 70)
    print("ANÁLISIS FACTORIAL COMPLETADO")
    print("Revisar todos los resultados y preparar deliverables finales:")
    print("1. Notebook técnico completo")
    print("2. Reporte ejecutivo (PDF)")
    print("3. Video de presentación (YouTube)")

    return {
        "eda": eda_results,
        "factorability": factorability,
        "dimensionality": optimal_factors,
        "extraction": extraction_results,
        "rotation": rotation_results,
        "interpretation": factor_interpretation,
        "prediction": predictive_analysis,
        "visualization": executive_viz,
        "recommendations": recommendations,
    }


# %% [markdown]
# ## Reflexión Final del Equipo
#
# **Responder a 3 de las siguientes 5 preguntas (4-6 líneas cada una):**
#
# ### 1. Validez Metodológica
# **¿Cómo evaluarías la robustez de tu solución factorial? ¿Qué análisis
# adicionales realizarías para fortalecer las conclusiones?**
#
# [Respuesta del equipo]
#
# ### 2. Interpretación Empresarial
# **¿Qué factor representa la mayor oportunidad estratégica para TechnoServe
# Solutions y por qué? ¿Cómo justificas esta priorización?**
#
# [Respuesta del equipo]
#
# ### 3. Limitaciones Analíticas
# **¿Qué limitaciones fundamentales tiene el enfoque de Factor Analysis para
# este problema empresarial? ¿Qué métodos complementarios considerarías?**
#
# [Respuesta del equipo]
#
# ### 4. Escalabilidad e Implementación
# **¿Cómo adaptarías tu análisis si TechnoServe tuviera 10,000 clientes y 50
# variables de satisfacción? ¿Qué desafíos metodológicos emergerían?**
#
# [Respuesta del equipo]
#
# ### 5. Desarrollo Profesional
# **¿Qué aspecto del análisis factorial encontraste más desafiante y cómo
# desarrollaste competencia en esa área? ¿Qué harías diferente en un proyecto similar?**
#
# [Respuesta del equipo]

# %% [markdown]
# ## Información del Equipo y Entregables
#
# **Equipo:** [Nombre del equipo]
#
# **Integrantes:**
# - [Nombre Completo 1] ([Matrícula]) - Expertise: [Factorizabilidad y Extracción]
# - [Nombre Completo 2] ([Matrícula]) - Expertise: [Interpretación y Scoring]
# - [Nombre Completo 3] ([Matrícula]) - Expertise: [Aplicación y Comunicación]
#
# **Enlaces de Entregables:**
# - **Video Presentación:** [TÍTULO](URL_YOUTUBE)
# - **Reporte Ejecutivo:** [Disponible en Canvas]
# - **Dataset:** `customer_satisfaction_data.csv`
#
# **Fechas:**
# - Analysis completed: [DD/MM/YYYY]
# - Recording made: [DD/MM/YYYY]
# - Final submission: [DD/MM/YYYY]

# %%
if __name__ == "__main__":
    # Execute complete analysis
    results = main_analysis_workflow()

    print("\n🎉 Template completed!")
    print("📋 Next step: Complete all TODOs")
    print("📊 Generate executive visualizations")
    print("📝 Write report and record video")
    print("🚀 Good luck team!")
