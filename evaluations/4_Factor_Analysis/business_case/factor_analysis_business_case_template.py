#!/usr/bin/env python3
"""
factor_analysis_business_case_template.py

Template para el Caso Práctico: Customer Satisfaction Intelligence
TechnoServe Solutions - Análisis Factorial Avanzado

Equipos deben completar TODOs y implementar análisis factorial riguroso
siguiendo metodología estadística y interpretación empresarial.

Autores: [Nombres del equipo]
Fecha: [Fecha de inicio]
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

# Configuración para gráficos profesionales
plt.style.use("seaborn-v0_8")
sns.set_palette("husl")


def load_customer_data():
    """
    Carga y prepara el dataset de satisfacción del cliente.

    Returns:
        tuple: (datos_satisfaccion, variables_resultado, metadata)
    """
    # TODO: Cargar customer_satisfaction_data.csv
    # TODO: Separar variables de satisfacción (23 items) de variables de resultado (5 items)
    # TODO: Crear diccionario con metadatos del dataset

    pass


# %% [markdown]
# # Caso Práctico: Customer Satisfaction Intelligence
# ## TechnoServe Solutions - Análisis Factorial
#
# **Equipo:** [Nombre del equipo]
# **Integrantes:**
# - [Nombre 1] - [Matrícula] - Expertise: Factorizabilidad y Extracción
# - [Nombre 2] - [Matrícula] - Expertise: Interpretación y Scoring
# - [Nombre 3] - [Matrícula] - Expertise: Aplicación y Comunicación
#
# **Objetivo:** Transformar datos de satisfacción del cliente en inteligencia estratégica
# mediante Análisis Factorial riguroso y recomendaciones empresariales accionables.


# %%
def exploratory_data_analysis(datos_satisfaccion):
    """
    Análisis Exploratorio de Datos para variables de satisfacción.

    Args:
        datos_satisfaccion: DataFrame con variables de satisfacción (escala 1-7)

    Returns:
        dict: Resultados del análisis exploratorio
    """
    print("=== ANÁLISIS EXPLORATORIO DE DATOS ===")

    # TODO: Estadísticas descriptivas completas
    # - Medidas de tendencia central y dispersión por variable
    # - Identificación de outliers usando IQR o Z-score
    # - Análisis de distribuciones (histogramas, Q-Q plots)

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
# ### Pregunta de Reflexión 1
# **¿Qué patrones observas en la matriz de correlaciones? ¿Cómo estos patrones
# sugieren la presencia de factores latentes subyacentes?**
#
# [Respuesta del equipo - 4-6 líneas]


# %%
def evaluate_factorability(datos_limpios):
    """
    Evalúa factorizabilidad usando tests estadísticos rigurosos.

    Args:
        datos_limpios: DataFrame sin datos faltantes

    Returns:
        dict: Resultados de tests de factorizabilidad con interpretación
    """
    print("=== EVALUACIÓN DE FACTORIZABILIDAD ===")

    resultados = {}

    # TODO: Test Kaiser-Meyer-Olkin (KMO)
    # - KMO global (debe ser > 0.6, preferiblemente > 0.8)
    # - KMO por variable individual
    # - Interpretación de MSA (Measure of Sampling Adequacy) values

    # TODO: Test de Esfericidad de Bartlett
    # - H₀: Matriz de correlación es matriz identidad
    # - Chi-cuadrado estadístico y p-value
    # - Interpretación estadística (rechazar H₀ si p < 0.05)

    # TODO: Matriz Anti-imagen
    # - Correlaciones parciales (deben ser pequeñas)
    # - Valores MSA en diagonal (> 0.5 aceptable)
    # - Identificar variables problemáticas

    # TODO: Determinante de matriz de correlación
    # - Verificar no singularidad (det ≠ 0)
    # - Evaluar multicolinealidad extrema

    return resultados


# %% [markdown]
# ### Pregunta de Reflexión 2
# **¿Por qué es crucial evaluar factorizabilidad antes de proceder con extracción
# factorial? ¿Qué implicaciones tendría ignorar estos tests?**
#
# [Respuesta del equipo - 4-6 líneas]


# %%
def determine_optimal_factors(correlation_matrix, datos):
    """
    Determina número óptimo de factores usando múltiples criterios.

    Args:
        correlation_matrix: Matriz de correlaciones
        datos: DataFrame de datos limpios

    Returns:
        dict: Resultados de análisis de dimensionalidad
    """
    print("=== DETERMINACIÓN DE NÚMERO ÓPTIMO DE FACTORES ===")

    # TODO: Criterio de Kaiser (Eigenvalues > 1)
    # - Calcular eigenvalues de matriz de correlación
    # - Contar eigenvalues > 1.0
    # - Graficar eigenvalues en orden descendente

    # TODO: Scree Plot
    # - Visualizar eigenvalues vs. número de factor
    # - Identificar "codo" o punto de inflexión
    # - Interpretación visual del punto de corte

    # TODO: Análisis Paralelo (Horn, 1965)
    # - Generar datos aleatorios con mismas dimensiones
    # - Comparar eigenvalues reales vs. aleatorios
    # - Retener factores donde real > aleatorio

    # TODO: Varianza Explicada
    # - % varianza acumulada por número de factores
    # - Criterio de 60-80% varianza explicada
    # - Trade-off parsimonia vs. explicación

    pass


# %% [markdown]
# ### Pregunta de Reflexión 3
# **¿Qué ventajas y limitaciones tiene cada método para determinar el número
# óptimo de factores? ¿Cómo reconcilias resultados contradictorios entre métodos?**
#
# [Respuesta del equipo - 4-6 líneas]


# %%
def compare_extraction_methods(datos, n_factors):
    """
    Compara métodos de extracción factorial: PCA, PAF, ML.

    Args:
        datos: DataFrame estandarizado
        n_factors: Número de factores a extraer

    Returns:
        dict: Resultados comparativos por método
    """
    print("=== COMPARACIÓN DE MÉTODOS DE EXTRACCIÓN ===")

    resultados = {}

    # TODO: Principal Component Analysis (PCA)
    # - Usar sklearn.decomposition.PCA
    # - Calcular % varianza explicada por componente
    # - Obtener component loadings matrix

    # TODO: Principal Axis Factoring (PAF)
    # - Usar FactorAnalyzer con method='principal'
    # - Estimar comunalidades iterativamente
    # - Comparar comunalidades vs. PCA

    # TODO: Maximum Likelihood (ML)
    # - Usar FactorAnalyzer con method='ml'
    # - Evaluar convergencia y fit statistics
    # - Chi-cuadrado goodness of fit test

    # TODO: Análisis Comparativo
    # - Eigenvalues y % varianza por método
    # - Comunalidades estimadas (h²)
    # - Residuales y bondad de ajuste
    # - Justificación de método seleccionado

    return resultados


# %% [markdown]
# ### Pregunta de Reflexión 4
# **¿Cuándo es apropiado usar PCA vs. Factor Analysis? ¿Qué asunciones
# fundamentales diferencian estos enfoques y cómo afectan la interpretación empresarial?**
#
# [Respuesta del equipo - 4-6 líneas]


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

    # Etapa 1: Carga y preparación de datos
    print("\n1. CARGA Y PREPARACIÓN DE DATOS")
    datos_satisfaccion, outcomes, metadata = load_customer_data()

    # Etapa 2: Análisis exploratorio
    print("\n2. ANÁLISIS EXPLORATORIO DE DATOS")
    eda_results = exploratory_data_analysis(datos_satisfaccion)

    # Etapa 3: Evaluación de factorizabilidad
    print("\n3. EVALUACIÓN DE FACTORIZABILIDAD")
    factorability = evaluate_factorability(datos_satisfaccion.dropna())

    # Etapa 4: Determinación de dimensionalidad
    print("\n4. DETERMINACIÓN DE NÚMERO ÓPTIMO DE FACTORES")
    optimal_factors = determine_optimal_factors(
        datos_satisfaccion.corr(), datos_satisfaccion
    )

    # Etapa 5: Extracción y comparación de métodos
    print("\n5. EXTRACCIÓN FACTORIAL COMPARATIVA")
    extraction_results = compare_extraction_methods(
        datos_satisfaccion, n_factors=5  # Ajustar según análisis anterior
    )

    # Etapa 6: Rotación factorial
    print("\n6. ANÁLISIS DE ROTACIONES FACTORIALES")
    rotation_results = apply_factor_rotations(extraction_results["best_loadings"])

    # Etapa 7: Interpretación empresarial
    print("\n7. INTERPRETACIÓN Y ETIQUETADO FACTORIAL")
    factor_interpretation = interpret_and_label_factors(
        rotation_results["final_loadings"], datos_satisfaccion.columns
    )

    # Etapa 8: Scoring y predicción
    print("\n8. FACTOR SCORING Y MODELADO PREDICTIVO")
    predictive_analysis = calculate_factor_scores_and_predict(
        rotation_results["final_model"], datos_satisfaccion, outcomes
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
# - Análisis completado: [DD/MM/AAAA]
# - Grabación realizada: [DD/MM/AAAA]
# - Entrega final: [DD/MM/AAAA]

# %%
if __name__ == "__main__":
    # Ejecutar análisis completo
    results = main_analysis_workflow()

    print("\n🎉 Template completado!")
    print("📋 Siguiente paso: Completar todos los TODOs")
    print("📊 Generar visualizaciones ejecutivas")
    print("📝 Escribir reporte y grabar video")
    print("🚀 ¡Buena suerte equipo!")
