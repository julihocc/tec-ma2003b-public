# 4.1 Objectives of Factor Analysis
# 
# Julia practice script (pseudocode-like): demonstrate the key objectives
# of factor analysis and compare with PCA.
#
# Key concepts:
# - Factor analysis identifies latent variables that explain correlations
# - PCA creates linear combinations that maximize variance
# - FA focuses on common variance, PCA on total variance
# - Different objectives lead to different interpretations

using LinearAlgebra, Statistics, Random

Random.seed!(42)

function generate_psychology_data(n=200, p=6)
    """Generate synthetic psychology test data with underlying factor structure"""
    
    println("Generating Psychology Test Data")
    println("==============================")
    
    # Create latent factors
    intelligence = randn(n)
    verbal_ability = randn(n)
    
    # Create observed variables influenced by factors
    # Intelligence factor → Math, Logic, Spatial
    math_score = 0.8 * intelligence + 0.2 * randn(n)
    logic_score = 0.7 * intelligence + 0.3 * randn(n)
    spatial_score = 0.6 * intelligence + 0.4 * randn(n)
    
    # Verbal factor → Reading, Writing, Vocabulary
    reading_score = 0.8 * verbal_ability + 0.2 * randn(n)
    writing_score = 0.7 * verbal_ability + 0.3 * randn(n)
    vocabulary_score = 0.9 * verbal_ability + 0.1 * randn(n)
    
    # Combine into data matrix X (n × p)
    X = [math_score logic_score spatial_score reading_score writing_score vocabulary_score]
    
    variable_names = ["Math", "Logic", "Spatial", "Reading", "Writing", "Vocabulary"]
    
    println("Created $n observations with $(size(X,2)) variables")
    println("Variables: ", variable_names)
    println("True factors: Intelligence, Verbal Ability")
    
    return X, variable_names
end

function analyze_correlation_structure(X, variable_names)
    """Examine correlation patterns in the data"""
    
    println("\nCorrelation Structure Analysis")
    println("=============================")
    
    # Calculate correlation matrix R = X'X / (n-1)
    R = cor(X)
    
    println("Correlation Matrix:")
    for (i, var1) in enumerate(variable_names)
        print(rpad(var1, 12))
        for j in 1:length(variable_names)
            print(@sprintf("%7.3f", R[i,j]))
        end
        println()
    end
    
    # Identify patterns
    println("\nCorrelation Patterns:")
    println("Math-Logic-Spatial: High intercorrelations (Intelligence factor)")
    println("Reading-Writing-Vocabulary: High intercorrelations (Verbal factor)")
    println("Across factors: Lower correlations")
    
    return R
end

function perform_pca_analysis(X, variable_names)
    """Perform Principal Component Analysis"""
    
    println("\nPrincipal Component Analysis")
    println("===========================")
    
    # Standardize data: Z = (X - μ) / σ
    Z = zscore(X, dims=1)
    
    # Calculate covariance matrix of standardized data (= correlation matrix)
    Σ = cov(Z)
    
    # Eigendecomposition: Σ = VΛVᵀ
    λ, V = eigen(Σ)
    
    # Sort eigenvalues in descending order
    perm = sortperm(λ, rev=true)
    λ = λ[perm]
    V = V[:, perm]
    
    println("PCA Results:")
    println("Eigenvalues (variance explained):")
    for i in 1:length(λ)
        proportion = λ[i] / sum(λ)
        println("  PC$i: $(round(λ[i], digits=3)) ($(round(proportion*100, digits=1))%)")
    end
    
    cumulative = cumsum(λ) / sum(λ)
    println("First 2 PCs explain: $(round(cumulative[2]*100, digits=1))% of total variance")
    
    return λ, V, Z
end

function perform_factor_analysis(R, variable_names, k=2)
    """Perform Factor Analysis using eigendecomposition approach"""
    
    println("\nFactor Analysis (k=$k factors)")
    println("=============================")
    
    # Eigendecomposition of correlation matrix R
    λ, V = eigen(R)
    
    # Sort eigenvalues in descending order
    perm = sortperm(λ, rev=true)
    λ = λ[perm]
    V = V[:, perm]
    
    # Factor loadings: Λ = V_k √Λ_k (first k eigenvectors scaled by √eigenvalues)
    Λ = V[:, 1:k] * diagm(sqrt.(λ[1:k]))
    
    println("Factor Loadings Matrix:")
    println("Variable      Factor 1  Factor 2")
    println("-" * 35)
    for (i, var) in enumerate(variable_names)
        println(@sprintf("%-12s  %8.3f  %8.3f", var, Λ[i,1], Λ[i,2]))
    end
    
    # Communalities: h² = Σⱼ λᵢⱼ² (sum of squared loadings)
    h² = sum(Λ.^2, dims=2)[:, 1]
    
    println("\nCommunalities (proportion of variance explained by factors):")
    for (i, var) in enumerate(variable_names)
        println(@sprintf("%-12s: %.3f", var, h²[i]))
    end
    
    # Factor interpretation
    println("\nFactor Interpretation:")
    println("Factor 1: High loadings on Math, Logic, Spatial → Intelligence")
    println("Factor 2: High loadings on Reading, Writing, Vocabulary → Verbal Ability")
    
    return Λ, h²
end

function compare_objectives(λ_pca, Λ_fa)
    """Compare objectives of PCA vs Factor Analysis"""
    
    println("\nComparison: PCA vs Factor Analysis Objectives")
    println("============================================")
    
    println("PCA Objectives:")
    println("• Maximize total variance explained by components")
    println("• Create orthogonal linear combinations: Y = VᵀX")
    println("• Dimensionality reduction with minimal information loss")
    println("• All variance (common + unique) considered")
    
    println("\nFactor Analysis Objectives:")
    println("• Identify latent factors that cause observed correlations")
    println("• Model: X = ΛF + ε (common factors + unique factors)")
    println("• Focus on common variance only")
    println("• Explain covariance structure, not just variance")
    
    println("\nKey Differences:")
    println("• PCA: Data-driven dimensionality reduction")
    println("• FA: Theory-driven latent variable modeling")
    println("• PCA components are linear combinations of variables")
    println("• FA factors are hypothetical constructs causing correlations")
end

function demonstrate_applications()
    """Show practical applications of factor analysis objectives"""
    
    println("\nFactor Analysis Applications")
    println("===========================")
    
    applications = Dict(
        "Psychology & Education" => [
            "Intelligence research (g-factor identification)",
            "Personality assessment (Big Five factors)",
            "Attitude and satisfaction measurement",
            "Test validation and scale development"
        ],
        "Business & Marketing" => [
            "Customer segmentation and profiling",
            "Brand perception measurement",
            "Product attribute analysis",
            "Market research data reduction"
        ],
        "Finance & Economics" => [
            "Risk factor identification",
            "Economic indicator clustering",
            "Portfolio factor analysis",
            "Credit risk modeling"
        ]
    )
    
    for (field, apps) in applications
        println("\n$field:")
        for app in apps
            println("  • $app")
        end
    end
end

function main()
    """Main demonstration of factor analysis objectives"""
    
    println("MA2003B - Objectives of Factor Analysis")
    println("Julia pseudocode demonstration")
    
    # Algorithm steps:
    
    # Step 1: Generate data with known factor structure
    X, variable_names = generate_psychology_data(200, 6)
    
    # Step 2: Analyze correlation patterns
    R = analyze_correlation_structure(X, variable_names)
    
    # Step 3: Perform PCA for comparison
    λ_pca, V_pca, Z = perform_pca_analysis(X, variable_names)
    
    # Step 4: Perform Factor Analysis
    Λ_fa, h² = perform_factor_analysis(R, variable_names, 2)
    
    # Step 5: Compare objectives and methods
    compare_objectives(λ_pca, Λ_fa)
    
    # Step 6: Show practical applications
    demonstrate_applications()
    
    # Summary
    println("\nSummary")
    println("=======")
    println("✓ Generated data with 2 latent factors")
    println("✓ Analyzed correlation structure")
    println("✓ Performed PCA and Factor Analysis")
    println("✓ Compared objectives and interpretations")
    println("✓ Demonstrated practical applications")
    
    println("\nKey Learning Points:")
    println("• FA seeks latent variables that explain correlations")
    println("• PCA seeks dimensions that maximize variance")
    println("• Choose method based on research objectives")
    println("• FA better for theory testing, PCA for data reduction")
end

# Run the demonstration
main()