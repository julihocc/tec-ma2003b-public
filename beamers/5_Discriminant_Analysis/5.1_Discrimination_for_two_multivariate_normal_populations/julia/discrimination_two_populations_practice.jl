# 5.1 Discrimination for Two Multivariate Normal Populations
# 
# Julia practice script (pseudocode-like): demonstrate Linear Discriminant Analysis
# for two populations with equal covariance matrices.
#
# Key concepts:
# - Two populations π₀ and π₁ with equal covariance Σ
# - Linear discriminant function: w'x + b > 0 → classify as π₁
# - Pooled covariance estimation
# - Bayes optimal classification

using LinearAlgebra, Statistics, Random

Random.seed!(42)

function simulate_populations(n=300, p=3)
    """Simulate two multivariate normal populations"""
    
    # Population parameters
    μ₀ = zeros(p)
    μ₁ = 1.5 * ones(p)
    Σ = I(p)  # Identity covariance matrix
    
    println("Two-Population Discriminant Analysis")
    println("===================================")
    println("Population π₀: μ₀ = ", μ₀)
    println("Population π₁: μ₁ = ", μ₁)
    println("Common covariance: Σ = I")
    
    # Generate samples from each population
    n₀ = n ÷ 2
    n₁ = n - n₀
    
    # X₀ ~ N(μ₀, Σ) and X₁ ~ N(μ₁, Σ)
    X₀ = randn(n₀, p) * sqrt(Σ) .+ μ₀'
    X₁ = randn(n₁, p) * sqrt(Σ) .+ μ₁'
    
    # Combine data
    X = [X₀; X₁]
    y = [zeros(Int, n₀); ones(Int, n₁)]
    
    println("Generated $n₀ samples from π₀ and $n₁ samples from π₁")
    return X, y
end

function estimate_parameters(X, y)
    """Estimate population parameters from data"""
    
    println("\nParameter Estimation:")
    println("====================")
    
    # Sample means
    μ̂₀ = mean(X[y .== 0, :], dims=1)[1, :]
    μ̂₁ = mean(X[y .== 1, :], dims=1)[1, :]
    
    println("Sample mean μ̂₀ = ", μ̂₀)
    println("Sample mean μ̂₁ = ", μ̂₁)
    
    # Sample covariances
    X₀ = X[y .== 0, :]
    X₁ = X[y .== 1, :]
    
    S₀ = cov(X₀)
    S₁ = cov(X₁)
    
    n₀, n₁ = sum(y .== 0), sum(y .== 1)
    
    # Pooled covariance: Σ̂ = [(n₀-1)S₀ + (n₁-1)S₁] / (n₀+n₁-2)
    Σ̂ = ((n₀ - 1) * S₀ + (n₁ - 1) * S₁) / (n₀ + n₁ - 2)
    
    println("Pooled covariance Σ̂:")
    display(Σ̂)
    
    return μ̂₀, μ̂₁, Σ̂
end

function compute_discriminant_function(μ₀, μ₁, Σ)
    """Compute linear discriminant coefficients"""
    
    println("\nLinear Discriminant Function:")
    println("============================")
    
    # Linear discriminant coefficients from Bayes rule:
    # w = Σ⁻¹(μ₁ - μ₀)
    # b = -½(μ₁'Σ⁻¹μ₁ - μ₀'Σ⁻¹μ₀)
    
    Σ⁻¹ = inv(Σ)
    w = Σ⁻¹ * (μ₁ - μ₀)
    b = -0.5 * (μ₁' * Σ⁻¹ * μ₁ - μ₀' * Σ⁻¹ * μ₀)
    
    println("Classification rule: assign to π₁ if w'x + b > 0")
    println("Coefficient vector w = ", w)
    println("Intercept b = ", round(b, digits=4))
    
    return w, b
end

function classify(X, w, b)
    """Classify observations using linear discriminant"""
    
    # Discriminant scores: g(x) = w'x + b
    scores = X * w .+ b
    
    # Predictions: ŷ = 1 if g(x) > 0, else 0
    ŷ = (scores .> 0) .|> Int
    
    return ŷ, scores
end

function evaluate_performance(y_true, ŷ)
    """Evaluate classification performance"""
    
    println("\nClassification Results:")
    println("======================")
    
    # Accuracy
    accuracy = mean(ŷ .== y_true)
    println("Accuracy: ", round(accuracy, digits=4))
    
    # Confusion matrix elements
    tp = sum((y_true .== 1) .& (ŷ .== 1))  # True positives
    tn = sum((y_true .== 0) .& (ŷ .== 0))  # True negatives  
    fp = sum((y_true .== 0) .& (ŷ .== 1))  # False positives
    fn = sum((y_true .== 1) .& (ŷ .== 0))  # False negatives
    
    println("Confusion Matrix:")
    println("           Predicted")
    println("         π₀    π₁")
    println("Actual π₀ ", lpad(tn, 3), "  ", lpad(fp, 3))
    println("       π₁ ", lpad(fn, 3), "  ", lpad(tp, 3))
    
    error_rate = 1 - accuracy
    println("Error rate: ", round(error_rate, digits=4))
    
    return accuracy
end

function main()
    """Main demonstration of two-population discriminant analysis"""
    
    # Algorithm steps:
    
    # Step 1: Generate data from two populations
    X, y = simulate_populations(300, 3)
    
    # Step 2: Estimate population parameters  
    μ̂₀, μ̂₁, Σ̂ = estimate_parameters(X, y)
    
    # Step 3: Compute linear discriminant function
    w, b = compute_discriminant_function(μ̂₀, μ̂₁, Σ̂)
    
    # Step 4: Classify observations and evaluate
    ŷ, scores = classify(X, w, b)
    accuracy = evaluate_performance(y, ŷ)
    
    # Summary
    println("\nSummary:")
    println("========")
    println("✓ Simulated two multivariate normal populations")
    println("✓ Estimated parameters using pooled covariance")
    println("✓ Computed linear discriminant function")
    println("✓ Classified observations and evaluated accuracy")
    println("Final accuracy: ", round(accuracy, digits=4))
end

# Run the demonstration
main()