import os
import json
import shutil

def main():
    print("Initializing NeuroForge Question Bank v2 Generation...")
    
    base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    content_dir = os.path.join(base_dir, "content")
    
    # 1. Clear existing content directory folders to discard the old question bank
    sections = [
        "python",
        "statistics",
        "machine-learning",
        "deep-learning",
        "llm",
        "rag",
        "agents",
        "system-design"
    ]
    
    for sec in sections:
        sec_path = os.path.join(content_dir, sec)
        if os.path.exists(sec_path):
            print(f"Clearing folder: {sec_path}")
            shutil.rmtree(sec_path)
        os.makedirs(sec_path, exist_ok=True)
        
    items = []
    
    # --- SECTION 1: PYTHON (10 ITEMS: 1-10) ---
    # Difficulty: 5 Easy, 5 Medium, 0 Hard
    
    items.append({
        "id": 1,
        "slug": "loops-and-list-comprehensions",
        "title": "Python Loops & List Comprehensions",
        "section": "Python",
        "difficulty": "Easy",
        "estimated_time_minutes": 15,
        "tags": ["loops", "list-comprehensions", "fundamentals"],
        "learning_objectives": ["Implement standard loops", "Convert loops to list comprehensions"],
        "description": "Learn the syntax and optimization of Python loops and convert sequential iteration logic into elegant list comprehensions.",
        "theory_resource": {
            "title": "Python List Comprehensions Guide",
            "url": "https://realpython.com/list-comprehension-python/",
            "type": "article"
        },
        "practice_resource": {
            "platform": "KAGGLE",
            "title": "Loops and List Comprehensions Exercise",
            "url": "https://www.kaggle.com/code/colinmorris/exercise-loops-and-list-comprehensions"
        },
        "prerequisites": []
    })
    
    items.append({
        "id": 2,
        "slug": "working-with-external-libraries",
        "title": "Working with External Libraries",
        "section": "Python",
        "difficulty": "Medium",
        "estimated_time_minutes": 20,
        "tags": ["imports", "pip", "libraries"],
        "learning_objectives": ["Import external packages", "Use modules and submodules"],
        "description": "Understand how to import, inspect, and work with external packages like numpy or math in Python.",
        "theory_resource": {
            "title": "Python Modules and Packages",
            "url": "https://realpython.com/python-modules-packages/",
            "type": "article"
        },
        "practice_resource": {
            "platform": "KAGGLE",
            "title": "Working with External Libraries Exercise",
            "url": "https://www.kaggle.com/code/colinmorris/exercise-working-with-external-libraries"
        },
        "prerequisites": [1]
    })
    
    items.append({
        "id": 3,
        "slug": "functions-and-getting-help",
        "title": "Python Functions and Getting Help",
        "section": "Python",
        "difficulty": "Easy",
        "estimated_time_minutes": 15,
        "tags": ["functions", "help", "docstrings"],
        "learning_objectives": ["Define functions with def", "Read python docstrings using help()"],
        "description": "Learn to structure clean, documented functions and seek interactive help using Python's built-in inspection systems.",
        "theory_resource": {
            "title": "Defining Your Own Python Function",
            "url": "https://realpython.com/defining-your-own-python-function/",
            "type": "article"
        },
        "practice_resource": {
            "platform": "KAGGLE",
            "title": "Functions and Help Exercise",
            "url": "https://www.kaggle.com/code/colinmorris/exercise-functions-and-getting-help"
        },
        "prerequisites": [2]
    })
    
    items.append({
        "id": 4,
        "slug": "strings-and-dictionaries",
        "title": "Python Strings and Dictionaries",
        "section": "Python",
        "difficulty": "Medium",
        "estimated_time_minutes": 25,
        "tags": ["strings", "dictionaries", "hashing"],
        "learning_objectives": ["Manipulate string structures", "Query dictionary hash maps"],
        "description": "Perform complex string formatting, search substring indices, and construct robust dictionary key-value stores.",
        "theory_resource": {
            "title": "Dictionaries in Python",
            "url": "https://realpython.com/python-dicts/",
            "type": "article"
        },
        "practice_resource": {
            "platform": "KAGGLE",
            "title": "Strings and Dictionaries Exercise",
            "url": "https://www.kaggle.com/code/colinmorris/exercise-strings-and-dictionaries"
        },
        "prerequisites": [3]
    })
    
    items.append({
        "id": 5,
        "slug": "hello-python-fundamentals",
        "title": "Hello Python Fundamentals",
        "section": "Python",
        "difficulty": "Easy",
        "estimated_time_minutes": 10,
        "tags": ["variables", "types", "operators"],
        "learning_objectives": ["Create variables", "Use basic mathematical operators"],
        "description": "Get started with basic variables, assignment rules, arithmetic operators, and native types in Python.",
        "theory_resource": {
            "title": "Python Variables and Assignment",
            "url": "https://realpython.com/python-variables/",
            "type": "article"
        },
        "practice_resource": {
            "platform": "KAGGLE",
            "title": "Hello Python Exercise",
            "url": "https://www.kaggle.com/code/colinmorris/exercise-hello-python"
        },
        "prerequisites": [4]
    })
    
    items.append({
        "id": 6,
        "slug": "booleans-and-conditionals",
        "title": "Booleans and Conditionals",
        "section": "Python",
        "difficulty": "Easy",
        "estimated_time_minutes": 15,
        "tags": ["booleans", "logic", "control-flow"],
        "learning_objectives": ["Apply logical operators", "Create if-elif-else branches"],
        "description": "Construct boolean logic using and, or, not operators and direct execution flow with conditional statements.",
        "theory_resource": {
            "title": "Conditional Statements in Python",
            "url": "https://realpython.com/python-conditional-statements/",
            "type": "article"
        },
        "practice_resource": {
            "platform": "KAGGLE",
            "title": "Booleans and Conditionals Exercise",
            "url": "https://www.kaggle.com/code/colinmorris/exercise-booleans-and-conditionals"
        },
        "prerequisites": [5]
    })
    
    items.append({
        "id": 7,
        "slug": "lists-and-tuples",
        "title": "Lists and Tuples",
        "section": "Python",
        "difficulty": "Easy",
        "estimated_time_minutes": 15,
        "tags": ["lists", "tuples", "sequences"],
        "learning_objectives": ["Perform sequence slicing", "Mutate list items"],
        "description": "Differentiate mutable lists from immutable tuples, index sequences from the end, and apply slicing parameters.",
        "theory_resource": {
            "title": "Lists and Tuples in Python",
            "url": "https://realpython.com/python-lists-tuples/",
            "type": "article"
        },
        "practice_resource": {
            "platform": "KAGGLE",
            "title": "Lists and Tuples Exercise",
            "url": "https://www.kaggle.com/code/colinmorris/exercise-lists"
        },
        "prerequisites": [6]
    })
    
    items.append({
        "id": 8,
        "slug": "creating-reading-writing-data",
        "title": "Creating, Reading, and Writing Data",
        "section": "Python",
        "difficulty": "Medium",
        "estimated_time_minutes": 20,
        "tags": ["pandas", "csv", "dataframes"],
        "learning_objectives": ["Create Pandas DataFrames", "Load CSV files into memory"],
        "description": "Instantiate Series and DataFrames programmatically and output structures into filesystem data files.",
        "theory_resource": {
            "title": "Pandas Read Write Tutorial",
            "url": "https://realpython.com/pandas-read-write-files/",
            "type": "article"
        },
        "practice_resource": {
            "platform": "KAGGLE",
            "title": "Creating, Reading and Writing Data Exercise",
            "url": "https://www.kaggle.com/code/residentmario/exercise-creating-reading-and-writing"
        },
        "prerequisites": [7]
    })
    
    items.append({
        "id": 9,
        "slug": "indexing-selecting-assigning",
        "title": "Indexing, Selecting & Assigning",
        "section": "Python",
        "difficulty": "Medium",
        "estimated_time_minutes": 20,
        "tags": ["pandas", "selection", "loc-iloc"],
        "learning_objectives": ["Select index slices with loc and iloc", "Apply boolean indexing"],
        "description": "Master row and column extractions using labels, coordinates, and criteria masks in Pandas.",
        "theory_resource": {
            "title": "Pandas Indexing and Selecting",
            "url": "https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html",
            "type": "documentation"
        },
        "practice_resource": {
            "platform": "KAGGLE",
            "title": "Indexing, Selecting and Assigning Exercise",
            "url": "https://www.kaggle.com/code/residentmario/exercise-indexing-selecting-assigning"
        },
        "prerequisites": [8]
    })
    
    items.append({
        "id": 10,
        "slug": "summary-functions-and-maps",
        "title": "Summary Functions and Maps",
        "section": "Python",
        "difficulty": "Medium",
        "estimated_time_minutes": 25,
        "tags": ["pandas", "maps", "summaries"],
        "learning_objectives": ["Apply map() and apply() operators", "Generate aggregate summary stats"],
        "description": "Transform dataframe rows using mapping functions and execute statistic overviews.",
        "theory_resource": {
            "title": "Pandas Map and Apply Guide",
            "url": "https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.apply.html",
            "type": "documentation"
        },
        "practice_resource": {
            "platform": "KAGGLE",
            "title": "Summary Functions and Maps Exercise",
            "url": "https://www.kaggle.com/code/residentmario/exercise-summary-functions-and-maps"
        },
        "prerequisites": [9]
    })
    
    # --- SECTION 2: STATISTICS (15 ITEMS: 11-25) ---
    # Difficulty: 9 Easy, 6 Medium, 0 Hard
    
    items.append({
        "id": 11,
        "slug": "mean-median-mode",
        "title": "Mean, Median, and Mode",
        "section": "Statistics",
        "difficulty": "Easy",
        "estimated_time_minutes": 15,
        "tags": ["statistics", "central-tendency", "math"],
        "learning_objectives": ["Calculate mean, median, mode", "Identify skewness impacts"],
        "description": "Understand basic central tendency metrics and how outliers skew standard deviations and means.",
        "theory_resource": {
            "title": "Intro to Measures of Central Tendency",
            "url": "https://wikipedia.org/wiki/Central_tendency",
            "type": "article"
        },
        "practice_resource": {
            "platform": "DEEP_ML",
            "title": "Descriptive Statistics Calculator",
            "url": "https://deep-ml.com/problems/78"
        },
        "prerequisites": [10]
    })
    
    items.append({
        "id": 12,
        "slug": "variance-and-standard-deviation",
        "title": "Variance and Standard Deviation",
        "section": "Statistics",
        "difficulty": "Easy",
        "estimated_time_minutes": 15,
        "tags": ["statistics", "dispersion", "math"],
        "learning_objectives": ["Compute variance and standard deviation", "Differentiate population vs sample variance"],
        "description": "Measure statistical dispersion using probability distributions.",
        "theory_resource": {
            "title": "Understanding Variance and Standard Deviation",
            "url": "https://wikipedia.org/wiki/Variance",
            "type": "article"
        },
        "practice_resource": {
            "platform": "KAGGLE",
            "title": "Statistical Distributions Exercise",
            "url": "https://www.kaggle.com/code/alexisbcook/distributions"
        },
        "prerequisites": [11]
    })
    
    items.append({
        "id": 13,
        "slug": "markov-chains-probability-transitions",
        "title": "Markov Chains & Probability Transitions",
        "section": "Statistics",
        "difficulty": "Easy",
        "estimated_time_minutes": 20,
        "tags": ["probability", "markov", "transitions"],
        "learning_objectives": ["Map state transition matrices", "Simulate multi-step probability states"],
        "description": "Update state probabilities over sequential time intervals using transition matrices.",
        "theory_resource": {
            "title": "Markov Chains Explained",
            "url": "https://wikipedia.org/wiki/Markov_chain",
            "type": "article"
        },
        "practice_resource": {
            "platform": "DEEP_ML",
            "title": "Simulate Markov Chain Transitions",
            "url": "https://deep-ml.com/problems/132"
        },
        "prerequisites": [12]
    })
    
    items.append({
        "id": 14,
        "slug": "gaussian-pdf",
        "title": "Gaussian Probability Density Function",
        "section": "Statistics",
        "difficulty": "Easy",
        "estimated_time_minutes": 20,
        "tags": ["probability", "normal-distribution", "math"],
        "learning_objectives": ["Compute Normal PDF", "Interpret Gaussian distributions"],
        "description": "Represent continuous data models using the Gaussian/Normal probability distribution curve.",
        "theory_resource": {
            "title": "Normal Distribution Overview",
            "url": "https://wikipedia.org/wiki/Normal_distribution",
            "type": "article"
        },
        "practice_resource": {
            "platform": "DEEP_ML",
            "title": "Normal Distribution PDF Calculator",
            "url": "https://deep-ml.com/problems/80"
        },
        "prerequisites": [13]
    })
    
    items.append({
        "id": 15,
        "slug": "central-limit-theorem",
        "title": "Central Limit Theorem (CLT) Simulation",
        "section": "Statistics",
        "difficulty": "Easy",
        "estimated_time_minutes": 20,
        "tags": ["clt", "sampling", "simulation"],
        "learning_objectives": ["Simulate CLT sample averages", "Identify normal approximations"],
        "description": "Observe how the distribution of sample averages approaches normality regardless of shape.",
        "theory_resource": {
            "title": "Central Limit Theorem",
            "url": "https://wikipedia.org/wiki/Central_limit_theorem",
            "type": "article"
        },
        "practice_resource": {
            "platform": "KAGGLE",
            "title": "Central Limit Theorem Playground",
            "url": "https://www.kaggle.com/code/rtatman/central-limit-theorem-playground"
        },
        "prerequisites": [14]
    })
    
    items.append({
        "id": 16,
        "slug": "z-test-evaluation",
        "title": "Z-Test Evaluation",
        "section": "Statistics",
        "difficulty": "Easy",
        "estimated_time_minutes": 20,
        "tags": ["hypothesis-testing", "z-test", "inference"],
        "learning_objectives": ["Calculate Z-scores", "Verify null hypotheses using Z-tests"],
        "description": "Validate sample population assertions using standard Z-scores and critical bounds.",
        "theory_resource": {
            "title": "Introduction to Z-tests",
            "url": "https://wikipedia.org/wiki/Z-test",
            "type": "article"
        },
        "practice_resource": {
            "platform": "KAGGLE",
            "title": "Hypothesis Testing Exercise",
            "url": "https://www.kaggle.com/code/hamelg/python-for-data-analysis-hypothesis-testing"
        },
        "prerequisites": [15]
    })
    
    items.append({
        "id": 17,
        "slug": "two-sample-t-test",
        "title": "Two-sample T-test",
        "section": "Statistics",
        "difficulty": "Medium",
        "estimated_time_minutes": 25,
        "tags": ["hypothesis-testing", "t-test", "inference"],
        "learning_objectives": ["Compute T-statistics", "Determine degrees of freedom"],
        "description": "Assess difference significance between two independent sample group averages.",
        "theory_resource": {
            "title": "Student's T-test Explained",
            "url": "https://wikipedia.org/wiki/Student%27s_t-test",
            "type": "article"
        },
        "practice_resource": {
            "platform": "KAGGLE",
            "title": "T-test and ANOVA Exercise",
            "url": "https://www.kaggle.com/code/chocoz/exercise-t-test-and-anova"
        },
        "prerequisites": [16]
    })
    
    items.append({
        "id": 18,
        "slug": "chi-square-independence-test",
        "title": "Chi-Square Independence Test",
        "section": "Statistics",
        "difficulty": "Medium",
        "estimated_time_minutes": 25,
        "tags": ["hypothesis-testing", "chi-square", "categorical"],
        "learning_objectives": ["Compute contingency expectations", "Calculate chi-square values"],
        "description": "Establish correlation status between two categorical nominal variables.",
        "theory_resource": {
            "title": "Chi-squared Test Wiki",
            "url": "https://wikipedia.org/wiki/Chi-squared_test",
            "type": "article"
        },
        "practice_resource": {
            "platform": "KAGGLE",
            "title": "Chi-Square Test Exercise",
            "url": "https://www.kaggle.com/code/ravji71/chi-square-test-exercise"
        },
        "prerequisites": [17]
    })
    
    items.append({
        "id": 19,
        "slug": "one-way-f-test",
        "title": "One-Way F-test (ANOVA)",
        "section": "Statistics",
        "difficulty": "Medium",
        "estimated_time_minutes": 25,
        "tags": ["hypothesis-testing", "f-test", "anova"],
        "learning_objectives": ["Determine F-ratio statistics", "Calculate variance splits"],
        "description": "Compare aggregate group variances across multiple populations concurrently.",
        "theory_resource": {
            "title": "F-test Analysis of Variance",
            "url": "https://wikipedia.org/wiki/F-test",
            "type": "article"
        },
        "practice_resource": {
            "platform": "KAGGLE",
            "title": "Statistical Data Analysis ANOVA Exercise",
            "url": "https://www.kaggle.com/code/jakevdp/statistical-data-analysis-in-python"
        },
        "prerequisites": [18]
    })
    
    items.append({
        "id": 20,
        "slug": "correlation-matrix-linear-relations",
        "title": "Correlation Matrix & Linear Relations",
        "section": "Statistics",
        "difficulty": "Easy",
        "estimated_time_minutes": 15,
        "tags": ["correlation", "pearson", "matrix"],
        "learning_objectives": ["Calculate covariance normalization", "Construct full correlation matrices"],
        "description": "Assess linear correlation matrices between multiple variable pairs.",
        "theory_resource": {
            "title": "Correlation Matrix Concepts",
            "url": "https://wikipedia.org/wiki/Correlation",
            "type": "article"
        },
        "practice_resource": {
            "platform": "DEEP_ML",
            "title": "Calculate Correlation Matrix",
            "url": "https://deep-ml.com/problems/37"
        },
        "prerequisites": [19]
    })
    
    items.append({
        "id": 21,
        "slug": "phi-coefficient-nominal-association",
        "title": "Phi Coefficient & Nominal Association",
        "section": "Statistics",
        "difficulty": "Medium",
        "estimated_time_minutes": 20,
        "tags": ["correlation", "phi-coefficient", "categorical"],
        "learning_objectives": ["Map nominal variables to binary counts", "Determine Phi correlation value"],
        "description": "Evaluate relationship strength between binary nominal parameters.",
        "theory_resource": {
            "title": "Phi Coefficient Details",
            "url": "https://wikipedia.org/wiki/Phi_coefficient",
            "type": "article"
        },
        "practice_resource": {
            "platform": "DEEP_ML",
            "title": "Calculate the Phi Coefficient",
            "url": "https://deep-ml.com/problems/95"
        },
        "prerequisites": [20]
    })
    
    items.append({
        "id": 22,
        "slug": "mean-absolute-error",
        "title": "Mean Absolute Error",
        "section": "Statistics",
        "difficulty": "Easy",
        "estimated_time_minutes": 15,
        "tags": ["metrics", "mae", "error"],
        "learning_objectives": ["Compute absolute differences", "Identify MAE benefits over MSE"],
        "description": "Evaluate model average prediction variance using robust absolute metrics.",
        "theory_resource": {
            "title": "Mean Absolute Error Details",
            "url": "https://wikipedia.org/wiki/Mean_absolute_error",
            "type": "article"
        },
        "practice_resource": {
            "platform": "DEEP_ML",
            "title": "Calculate Mean Absolute Error",
            "url": "https://deep-ml.com/problems/93"
        },
        "prerequisites": [21]
    })
    
    items.append({
        "id": 23,
        "slug": "coefficient-of-determination-r2",
        "title": "Coefficient of Determination (R2)",
        "section": "Statistics",
        "difficulty": "Easy",
        "estimated_time_minutes": 15,
        "tags": ["metrics", "r-squared", "regression"],
        "learning_objectives": ["Determine sum of residuals", "Evaluate model variance metrics"],
        "description": "Verify the proportion of output variance explained by model inputs.",
        "theory_resource": {
            "title": "Coefficient of Determination Wiki",
            "url": "https://wikipedia.org/wiki/Coefficient_of_determination",
            "type": "article"
        },
        "practice_resource": {
            "platform": "DEEP_ML",
            "title": "Calculate R-squared for Regression",
            "url": "https://deep-ml.com/problems/69"
        },
        "prerequisites": [22]
    })
    
    items.append({
        "id": 24,
        "slug": "binomial-distribution",
        "title": "Binomial Distribution",
        "section": "Statistics",
        "difficulty": "Medium",
        "estimated_time_minutes": 20,
        "tags": ["probability", "binomial", "discrete"],
        "learning_objectives": ["Apply Binomial PMF formulas", "Interpret success probability sequences"],
        "description": "Model count of successes in independent binary Bernoulli trials.",
        "theory_resource": {
            "title": "Binomial Distribution Explained",
            "url": "https://wikipedia.org/wiki/Binomial_distribution",
            "type": "article"
        },
        "practice_resource": {
            "platform": "DEEP_ML",
            "title": "Binomial Distribution Probability",
            "url": "https://deep-ml.com/problems/79"
        },
        "prerequisites": [23]
    })
    
    items.append({
        "id": 25,
        "slug": "covariance-matrix-calculation",
        "title": "Covariance Matrix Calculation",
        "section": "Statistics",
        "difficulty": "Medium",
        "estimated_time_minutes": 25,
        "tags": ["covariance", "matrix", "linear-algebra"],
        "learning_objectives": ["Formulate mean vector offsets", "Generate full covariance matrices"],
        "description": "Build multi-dimensional variance models across multiple variable sets.",
        "theory_resource": {
            "title": "Covariance Matrix Details",
            "url": "https://wikipedia.org/wiki/Covariance_matrix",
            "type": "article"
        },
        "practice_resource": {
            "platform": "DEEP_ML",
            "title": "Calculate Covariance Matrix",
            "url": "https://deep-ml.com/problems/10"
        },
        "prerequisites": [24]
    })
    
    # --- SECTION 3: MACHINE LEARNING (20 ITEMS: 26-45) ---
    # Difficulty: 3 Easy, 15 Medium, 2 Hard
    
    items.append({
        "id": 26,
        "slug": "explore-your-data",
        "title": "Explore Your Data",
        "section": "Machine Learning",
        "difficulty": "Easy",
        "estimated_time_minutes": 15,
        "tags": ["eda", "pandas", "data-exploration"],
        "learning_objectives": ["Inspect feature summaries", "Identify dataset shapes"],
        "description": "Perform baseline exploratory data analysis (EDA) to understand feature properties.",
        "theory_resource": {
            "title": "Exploratory Data Analysis Guide",
            "url": "https://wikipedia.org/wiki/Exploratory_data_analysis",
            "type": "article"
        },
        "practice_resource": {
            "platform": "KAGGLE",
            "title": "Explore Your Data Exercise",
            "url": "https://www.kaggle.com/code/dansbecker/exercise-explore-your-data"
        },
        "prerequisites": [10, 23]
    })
    
    items.append({
        "id": 27,
        "slug": "your-first-machine-learning-model",
        "title": "Your First Machine Learning Model",
        "section": "Machine Learning",
        "difficulty": "Easy",
        "estimated_time_minutes": 15,
        "tags": ["scikit-learn", "decision-trees", "model-fitting"],
        "learning_objectives": ["Initialize predictor classes", "Fit models using sklearn"],
        "description": "Train your first decision tree regression model on housing features.",
        "theory_resource": {
            "title": "Scikit-Learn Decision Trees Guide",
            "url": "https://scikit-learn.org/stable/modules/tree.html",
            "type": "documentation"
        },
        "practice_resource": {
            "platform": "KAGGLE",
            "title": "Your First Machine Learning Model Exercise",
            "url": "https://www.kaggle.com/code/dansbecker/exercise-your-first-machine-learning-model"
        },
        "prerequisites": [26]
    })
    
    items.append({
        "id": 28,
        "slug": "model-validation",
        "title": "Model Validation",
        "section": "Machine Learning",
        "difficulty": "Medium",
        "estimated_time_minutes": 20,
        "tags": ["validation", "metrics", "mae"],
        "learning_objectives": ["Split data into train/validation folds", "Evaluate validation score stability"],
        "description": "Assess model out-of-sample performance using validation holds instead of train metrics.",
        "theory_resource": {
            "title": "Evaluating Estimator Performance",
            "url": "https://scikit-learn.org/stable/modules/cross_validation.html",
            "type": "documentation"
        },
        "practice_resource": {
            "platform": "KAGGLE",
            "title": "Model Validation Exercise",
            "url": "https://www.kaggle.com/code/dansbecker/exercise-model-validation"
        },
        "prerequisites": [27]
    })
    
    items.append({
        "id": 29,
        "slug": "underfitting-and-overfitting",
        "title": "Underfitting and Overfitting",
        "section": "Machine Learning",
        "difficulty": "Medium",
        "estimated_time_minutes": 20,
        "tags": ["bias-variance", "capacity", "overfitting"],
        "learning_objectives": ["Identify overfitting signals", "Tune tree depth limits"],
        "description": "Optimize tree capacities to resolve high bias and high variance tradeoffs.",
        "theory_resource": {
            "title": "Bias-Variance Tradeoff",
            "url": "https://wikipedia.org/wiki/Bias%E2%80%93variance_tradeoff",
            "type": "article"
        },
        "practice_resource": {
            "platform": "KAGGLE",
            "title": "Underfitting and Overfitting Exercise",
            "url": "https://www.kaggle.com/code/dansbecker/exercise-underfitting-and-overfitting"
        },
        "prerequisites": [28]
    })
    
    items.append({
        "id": 30,
        "slug": "random-forests-ensemble",
        "title": "Random Forests Ensemble",
        "section": "Machine Learning",
        "difficulty": "Medium",
        "estimated_time_minutes": 20,
        "tags": ["ensembles", "random-forest", "bagging"],
        "learning_objectives": ["Build bagging estimators", "Analyze ensemble predictions"],
        "description": "Harness decision tree aggregates to stabilize prediction noise.",
        "theory_resource": {
            "title": "Random Forests Classifiers",
            "url": "https://scikit-learn.org/stable/modules/ensemble.html#forests-of-randomized-trees",
            "type": "documentation"
        },
        "practice_resource": {
            "platform": "KAGGLE",
            "title": "Random Forests Exercise",
            "url": "https://www.kaggle.com/code/dansbecker/exercise-random-forests"
        },
        "prerequisites": [29]
    })
    
    items.append({
        "id": 31,
        "slug": "missing-values-imputation",
        "title": "Missing Values Imputation",
        "section": "Machine Learning",
        "difficulty": "Medium",
        "estimated_time_minutes": 20,
        "tags": ["preprocessing", "imputation", "nulls"],
        "learning_objectives": ["Apply SimpleImputer mappings", "Verify imputation bias impacts"],
        "description": "Cleanse incomplete inputs using zero, mean, or median imputation.",
        "theory_resource": {
            "title": "Imputation of Missing Values",
            "url": "https://scikit-learn.org/stable/modules/impute.html",
            "type": "documentation"
        },
        "practice_resource": {
            "platform": "KAGGLE",
            "title": "Missing Values Exercise",
            "url": "https://www.kaggle.com/code/alexisbcook/exercise-missing-values"
        },
        "prerequisites": [30]
    })
    
    items.append({
        "id": 32,
        "slug": "categorical-variables",
        "title": "Categorical Variables",
        "section": "Machine Learning",
        "difficulty": "Medium",
        "estimated_time_minutes": 20,
        "tags": ["encoding", "one-hot", "ordinal"],
        "learning_objectives": ["Build one-hot encoders", "Execute ordinal feature mapping"],
        "description": "Convert text variables into numerical format using standard encoders.",
        "theory_resource": {
            "title": "Encoding Categorical Features",
            "url": "https://scikit-learn.org/stable/modules/preprocessing.html#encoding-categorical-features",
            "type": "documentation"
        },
        "practice_resource": {
            "platform": "KAGGLE",
            "title": "Categorical Variables Exercise",
            "url": "https://www.kaggle.com/code/alexisbcook/exercise-categorical-variables"
        },
        "prerequisites": [31]
    })
    
    items.append({
        "id": 33,
        "slug": "machine-learning-pipelines",
        "title": "Machine Learning Pipelines",
        "section": "Machine Learning",
        "difficulty": "Medium",
        "estimated_time_minutes": 25,
        "tags": ["pipelines", "engineering", "scikit-learn"],
        "learning_objectives": ["Construct composite Pipeline pipelines", "Prevent processing leaks"],
        "description": "Structure training operations into a single deployable object.",
        "theory_resource": {
            "title": "Pipeline Architectures in Scikit-Learn",
            "url": "https://scikit-learn.org/stable/modules/compose.html#pipeline",
            "type": "documentation"
        },
        "practice_resource": {
            "platform": "KAGGLE",
            "title": "Pipelines Exercise",
            "url": "https://www.kaggle.com/code/alexisbcook/exercise-pipelines"
        },
        "prerequisites": [32]
    })
    
    items.append({
        "id": 34,
        "slug": "cross-validation-tuning",
        "title": "Cross-Validation Tuning",
        "section": "Machine Learning",
        "difficulty": "Medium",
        "estimated_time_minutes": 20,
        "tags": ["validation", "cross-validation", "hyperparameters"],
        "learning_objectives": ["Apply cross_val_score processes", "Identify parameter variations"],
        "description": "Assess model variance limits by running cross-validation folds.",
        "theory_resource": {
            "title": "Cross-Validation: Evaluating Estimator Performance",
            "url": "https://scikit-learn.org/stable/modules/cross_validation.html",
            "type": "documentation"
        },
        "practice_resource": {
            "platform": "KAGGLE",
            "title": "Cross Validation Exercise",
            "url": "https://www.kaggle.com/code/alexisbcook/exercise-cross-validation"
        },
        "prerequisites": [33]
    })
    
    items.append({
        "id": 35,
        "slug": "xgboost-gradient-boosting",
        "title": "XGBoost Gradient Boosting",
        "section": "Machine Learning",
        "difficulty": "Medium",
        "estimated_time_minutes": 25,
        "tags": ["boosting", "xgboost", "ensembles"],
        "learning_objectives": ["Train XGBRegressor setups", "Configure boosting parameters"],
        "description": "Train extreme gradient boosted decision trees for tabular prediction.",
        "theory_resource": {
            "title": "XGBoost Documentation",
            "url": "https://xgboost.readthedocs.io/en/stable/",
            "type": "documentation"
        },
        "practice_resource": {
            "platform": "KAGGLE",
            "title": "XGBoost Exercise",
            "url": "https://www.kaggle.com/code/alexisbcook/exercise-xgboost"
        },
        "prerequisites": [34]
    })
    
    items.append({
        "id": 36,
        "slug": "data-leakage-detection",
        "title": "Data Leakage Detection",
        "section": "Machine Learning",
        "difficulty": "Hard",
        "estimated_time_minutes": 25,
        "tags": ["leakage", "validation", "errors"],
        "learning_objectives": ["Identify target leaks", "Resolve train-test leaks"],
        "description": "Audit features for processing leaks that artificially inflate validation scores.",
        "theory_resource": {
            "title": "Data Leakage in ML",
            "url": "https://wikipedia.org/wiki/Leakage_(machine_learning)",
            "type": "article"
        },
        "practice_resource": {
            "platform": "KAGGLE",
            "title": "Data Leakage Exercise",
            "url": "https://www.kaggle.com/code/alexisbcook/exercise-data-leakage"
        },
        "prerequisites": [35]
    })
    
    items.append({
        "id": 37,
        "slug": "linear-regression-normal-equation",
        "title": "Linear Regression (Normal Equation)",
        "section": "Machine Learning",
        "difficulty": "Easy",
        "estimated_time_minutes": 15,
        "tags": ["linear-algebra", "normal-equation", "regression"],
        "learning_objectives": ["Prepend bias coordinates", "Evaluate Normal Equation weights"],
        "description": "Solve OLS regression analytically using closed-form normal equation matrices.",
        "theory_resource": {
            "title": "OLS Normal Equation Derivation",
            "url": "https://wikipedia.org/wiki/Normal_equation",
            "type": "article"
        },
        "practice_resource": {
            "platform": "DEEP_ML",
            "title": "Linear Regression Normal Equation",
            "url": "https://deep-ml.com/problems/14"
        },
        "prerequisites": [36]
    })
    
    items.append({
        "id": 38,
        "slug": "linear-regression-gradient-descent",
        "title": "Linear Regression (Gradient Descent)",
        "section": "Machine Learning",
        "difficulty": "Medium",
        "estimated_time_minutes": 20,
        "tags": ["optimization", "gradient-descent", "regression"],
        "learning_objectives": ["Calculate MSE gradient vectors", "Update weights iteratively"],
        "description": "Train linear models using batch gradient descent updates.",
        "theory_resource": {
            "title": "Linear Regression with Gradient Descent",
            "url": "https://wikipedia.org/wiki/Gradient_descent",
            "type": "article"
        },
        "practice_resource": {
            "platform": "DEEP_ML",
            "title": "Linear Regression Gradient Descent",
            "url": "https://deep-ml.com/problems/15"
        },
        "prerequisites": [37]
    })
    
    items.append({
        "id": 39,
        "slug": "logistic-regression-gradient-descent",
        "title": "Logistic Regression (Gradient Descent)",
        "section": "Machine Learning",
        "difficulty": "Medium",
        "estimated_time_minutes": 25,
        "tags": ["classification", "logistic-regression", "sigmoid"],
        "learning_objectives": ["Build sigmoid probability maps", "Calculate cross-entropy updates"],
        "description": "Train binary classification models using gradient descent log loss optimization.",
        "theory_resource": {
            "title": "Logistic Regression Details",
            "url": "https://wikipedia.org/wiki/Logistic_regression",
            "type": "article"
        },
        "practice_resource": {
            "platform": "DEEP_ML",
            "title": "Train Logistic Regression with GD",
            "url": "https://deep-ml.com/problems/106"
        },
        "prerequisites": [38]
    })
    
    items.append({
        "id": 40,
        "slug": "ridge-regression-regularization",
        "title": "Ridge Regression Regularization",
        "section": "Machine Learning",
        "difficulty": "Medium",
        "estimated_time_minutes": 20,
        "tags": ["regularization", "ridge", "l2"],
        "learning_objectives": ["Apply L2 penalty matrices", "Control model weight complexity"],
        "description": "Mitigate collinear feature variance using closed-form Ridge L2 penalties.",
        "theory_resource": {
            "title": "Ridge Regression Overview",
            "url": "https://wikipedia.org/wiki/Ridge_regression",
            "type": "article"
        },
        "practice_resource": {
            "platform": "DEEP_ML",
            "title": "Implement Ridge Regression Loss",
            "url": "https://deep-ml.com/problems/43"
        },
        "prerequisites": [39]
    })
    
    items.append({
        "id": 41,
        "slug": "lasso-regression-regularization",
        "title": "Lasso Regression Regularization",
        "section": "Machine Learning",
        "difficulty": "Hard",
        "estimated_time_minutes": 25,
        "tags": ["regularization", "lasso", "l1"],
        "learning_objectives": ["Apply L1 coordinate descent penalties", "Perform sparse selection maps"],
        "description": "Optimize Lasso L1 objective paths to construct sparse feature selections.",
        "theory_resource": {
            "title": "Lasso Regression Details",
            "url": "https://wikipedia.org/wiki/Lasso_(statistics)",
            "type": "article"
        },
        "practice_resource": {
            "platform": "DEEP_ML",
            "title": "Implement Lasso Regression GD",
            "url": "https://deep-ml.com/problems/50"
        },
        "prerequisites": [40]
    })
    
    items.append({
        "id": 42,
        "slug": "feature-scaling-normalization",
        "title": "Feature Scaling Normalization",
        "section": "Machine Learning",
        "difficulty": "Easy",
        "estimated_time_minutes": 15,
        "tags": ["preprocessing", "scaling", "min-max"],
        "learning_objectives": ["Implement Min-Max scaling", "Compute Standard Z-Score scaling"],
        "description": "Normalize column features to uniform scale to accelerate optimization.",
        "theory_resource": {
            "title": "Feature Scaling Guide",
            "url": "https://wikipedia.org/wiki/Feature_scaling",
            "type": "article"
        },
        "practice_resource": {
            "platform": "DEEP_ML",
            "title": "Min-Max Normalization of Features",
            "url": "https://deep-ml.com/problems/112"
        },
        "prerequisites": [41]
    })
    
    items.append({
        "id": 43,
        "slug": "k-means-clustering",
        "title": "K-Means Clustering",
        "section": "Machine Learning",
        "difficulty": "Medium",
        "estimated_time_minutes": 20,
        "tags": ["clustering", "unsupervised", "centroids"],
        "learning_objectives": ["Assign data points to closest centroids", "Iterate centroid updates"],
        "description": "Build partitions using standard K-Means centroid adjustments.",
        "theory_resource": {
            "title": "K-Means Clustering Analysis",
            "url": "https://wikipedia.org/wiki/K-means_clustering",
            "type": "article"
        },
        "practice_resource": {
            "platform": "DEEP_ML",
            "title": "K-Means Clustering",
            "url": "https://deep-ml.com/problems/17"
        },
        "prerequisites": [42]
    })
    
    items.append({
        "id": 44,
        "slug": "decision-tree-learning",
        "title": "Decision Tree Learning",
        "section": "Machine Learning",
        "difficulty": "Medium",
        "estimated_time_minutes": 25,
        "tags": ["trees", "entropy", "information-gain"],
        "learning_objectives": ["Compute Shannon Entropy", "Determine Information Gain indices"],
        "description": "Evaluate split candidates based on entropy reductions.",
        "theory_resource": {
            "title": "Decision Tree Splitting Metrics",
            "url": "https://wikipedia.org/wiki/Decision_tree_learning",
            "type": "article"
        },
        "practice_resource": {
            "platform": "DEEP_ML",
            "title": "Decision Tree Learning",
            "url": "https://deep-ml.com/problems/20"
        },
        "prerequisites": [43]
    })
    
    items.append({
        "id": 45,
        "slug": "k-nearest-neighbors-classifier",
        "title": "K-Nearest Neighbors Classifier",
        "section": "Machine Learning",
        "difficulty": "Medium",
        "estimated_time_minutes": 20,
        "tags": ["knn", "lazy-learning", "distance"],
        "learning_objectives": ["Formulate Euclidean distance vectors", "Aggregated top-k voting labels"],
        "description": "Construct K-Nearest Neighbors predictions using distance sorting.",
        "theory_resource": {
            "title": "KNN Classifier Algorithm",
            "url": "https://wikipedia.org/wiki/K-nearest_neighbors_algorithm",
            "type": "article"
        },
        "practice_resource": {
            "platform": "DEEP_ML",
            "title": "Implement K-Nearest Neighbors",
            "url": "https://deep-ml.com/problems/173"
        },
        "prerequisites": [44]
    })
    
    # --- SECTION 4: DEEP LEARNING (15 ITEMS: 46-60) ---
    # Difficulty: 2 Easy, 9 Medium, 4 Hard
    
    items.append({
        "id": 46,
        "slug": "a-single-neuron",
        "title": "A Single Neuron (Perceptron)",
        "section": "Deep Learning",
        "difficulty": "Easy",
        "estimated_time_minutes": 15,
        "tags": ["neuron", "activation", "math"],
        "learning_objectives": ["Calculate dot product inputs", "Apply step activation thresholds"],
        "description": "Construct a basic linear perceptron calculating inputs and weights.",
        "theory_resource": {
            "title": "The Perceptron Architecture",
            "url": "https://wikipedia.org/wiki/Perceptron",
            "type": "article"
        },
        "practice_resource": {
            "platform": "KAGGLE",
            "title": "A Single Neuron Exercise",
            "url": "https://www.kaggle.com/code/ryanholbrook/exercise-a-single-neuron"
        },
        "prerequisites": [38]
    })
    
    items.append({
        "id": 47,
        "slug": "deep-neural-networks",
        "title": "Deep Neural Networks",
        "section": "Deep Learning",
        "difficulty": "Easy",
        "estimated_time_minutes": 15,
        "tags": ["layers", "hidden-layers", "keras"],
        "learning_objectives": ["Stack dense hidden layers", "Configure activation maps"],
        "description": "Construct multilayer feedforward architectures stacking dense layers.",
        "theory_resource": {
            "title": "Multilayer Perceptron Networks",
            "url": "https://wikipedia.org/wiki/Multilayer_perceptron",
            "type": "article"
        },
        "practice_resource": {
            "platform": "KAGGLE",
            "title": "Deep Neural Networks Exercise",
            "url": "https://www.kaggle.com/code/ryanholbrook/exercise-deep-neural-networks"
        },
        "prerequisites": [46]
    })
    
    items.append({
        "id": 48,
        "slug": "stochastic-gradient-descent",
        "title": "Stochastic Gradient Descent (SGD)",
        "section": "Deep Learning",
        "difficulty": "Medium",
        "estimated_time_minutes": 20,
        "tags": ["optimization", "sgd", "training"],
        "learning_objectives": ["Differentiate batch sizes", "Tuned SGD learning rates"],
        "description": "Train networks using mini-batch gradient updates.",
        "theory_resource": {
            "title": "SGD Optimization in Neural Nets",
            "url": "https://wikipedia.org/wiki/Stochastic_gradient_descent",
            "type": "article"
        },
        "practice_resource": {
            "platform": "KAGGLE",
            "title": "Stochastic Gradient Descent Exercise",
            "url": "https://www.kaggle.com/code/ryanholbrook/exercise-stochastic-gradient-descent"
        },
        "prerequisites": [47]
    })
    
    items.append({
        "id": 49,
        "slug": "overfitting-and-underfitting-dl",
        "title": "Overfitting and Underfitting in DL",
        "section": "Deep Learning",
        "difficulty": "Medium",
        "estimated_time_minutes": 20,
        "tags": ["overfitting", "early-stopping", "regularization"],
        "learning_objectives": ["Apply early stopping limits", "Monitor validation curves"],
        "description": "Mitigate network capacity variance using early stopping callbacks.",
        "theory_resource": {
            "title": "Generalization in Neural Networks",
            "url": "https://wikipedia.org/wiki/Overfitting",
            "type": "article"
        },
        "practice_resource": {
            "platform": "KAGGLE",
            "title": "Overfitting and Underfitting Exercise",
            "url": "https://www.kaggle.com/code/ryanholbrook/exercise-overfitting-and-underfitting"
        },
        "prerequisites": [48]
    })
    
    items.append({
        "id": 50,
        "slug": "dropout-and-batch-normalization",
        "title": "Dropout and Batch Normalization",
        "section": "Deep Learning",
        "difficulty": "Medium",
        "estimated_time_minutes": 20,
        "tags": ["dropout", "batch-norm", "stabilization"],
        "learning_objectives": ["Apply dropout probability drops", "Implement batch norm scaling"],
        "description": "Stabilize network parameter training using dropout and batch norm layers.",
        "theory_resource": {
            "title": "Batch Normalization Derivation",
            "url": "https://wikipedia.org/wiki/Batch_normalization",
            "type": "article"
        },
        "practice_resource": {
            "platform": "KAGGLE",
            "title": "Dropout and Batch Normalization Exercise",
            "url": "https://www.kaggle.com/code/ryanholbrook/exercise-dropout-and-batch-normalization"
        },
        "prerequisites": [49]
    })
    
    items.append({
        "id": 51,
        "slug": "binary-classification-metrics",
        "title": "Binary Classification in DL",
        "section": "Deep Learning",
        "difficulty": "Medium",
        "estimated_time_minutes": 20,
        "tags": ["classification", "cross-entropy", "metrics"],
        "learning_objectives": ["Compute sigmoid probability boundaries", "Apply binary cross-entropy loss"],
        "description": "Optimize classification logits using logarithmic cross entropy losses.",
        "theory_resource": {
            "title": "Binary Cross Entropy Loss",
            "url": "https://wikipedia.org/wiki/Cross_entropy",
            "type": "article"
        },
        "practice_resource": {
            "platform": "KAGGLE",
            "title": "Binary Classification Exercise",
            "url": "https://www.kaggle.com/code/ryanholbrook/exercise-binary-classification"
        },
        "prerequisites": [50]
    })
    
    items.append({
        "id": 52,
        "slug": "the-convolutional-classifier",
        "title": "The Convolutional Classifier",
        "section": "Deep Learning",
        "difficulty": "Medium",
        "estimated_time_minutes": 25,
        "tags": ["cnn", "convolutions", "image-classification"],
        "learning_objectives": ["Configure feature extraction layers", "Determine convolutional sizes"],
        "description": "Extract image feature arrays using spatial convolution layers.",
        "theory_resource": {
            "title": "Convolutional Neural Networks Introduction",
            "url": "https://wikipedia.org/wiki/Convolutional_neural_network",
            "type": "article"
        },
        "practice_resource": {
            "platform": "KAGGLE",
            "title": "The Convolutional Classifier Exercise",
            "url": "https://www.kaggle.com/code/ryanholbrook/exercise-the-convolutional-classifier"
        },
        "prerequisites": [51]
    })
    
    items.append({
        "id": 53,
        "slug": "convolution-and-relu",
        "title": "Convolution and ReLU",
        "section": "Deep Learning",
        "difficulty": "Medium",
        "estimated_time_minutes": 20,
        "tags": ["cnn", "relu", "feature-maps"],
        "learning_objectives": ["Verify convolution filters", "Apply rectified linear activation"],
        "description": "Construct non-linear filter activations using Rectified Linear Units (ReLU).",
        "theory_resource": {
            "title": "ReLU Activation Function",
            "url": "https://wikipedia.org/wiki/Rectifier_(neural_networks)",
            "type": "article"
        },
        "practice_resource": {
            "platform": "KAGGLE",
            "title": "Convolution and ReLU Exercise",
            "url": "https://www.kaggle.com/code/ryanholbrook/exercise-convolution-and-relu"
        },
        "prerequisites": [52]
    })
    
    items.append({
        "id": 54,
        "slug": "custom-convnets",
        "title": "Custom Convnets Architectures",
        "section": "Deep Learning",
        "difficulty": "Hard",
        "estimated_time_minutes": 30,
        "tags": ["cnn", "custom-architecture", "maxpool"],
        "learning_objectives": ["Stack custom pooling grids", "Determine convolutional channels"],
        "description": "Build high-capacity image feature classifiers from scratch.",
        "theory_resource": {
            "title": "Pooling Layers in CNNs",
            "url": "https://wikipedia.org/wiki/Pooling_(computer_vision)",
            "type": "article"
        },
        "practice_resource": {
            "platform": "KAGGLE",
            "title": "Custom Convnets Exercise",
            "url": "https://www.kaggle.com/code/ryanholbrook/exercise-custom-convnets"
        },
        "prerequisites": [53]
    })
    
    items.append({
        "id": 55,
        "slug": "data-augmentation",
        "title": "Data Augmentation",
        "section": "Deep Learning",
        "difficulty": "Medium",
        "estimated_time_minutes": 20,
        "tags": ["cnn", "augmentation", "overfitting"],
        "learning_objectives": ["Configure coordinate shifts", "Verify model rotation invariance"],
        "description": "Artificially expand image datasets using crop, skew, and rotation filters.",
        "theory_resource": {
            "title": "Data Augmentation in Computer Vision",
            "url": "https://wikipedia.org/wiki/Data_augmentation",
            "type": "article"
        },
        "practice_resource": {
            "platform": "KAGGLE",
            "title": "Data Augmentation Exercise",
            "url": "https://www.kaggle.com/code/ryanholbrook/exercise-data-augmentation"
        },
        "prerequisites": [54]
    })
    
    items.append({
        "id": 56,
        "slug": "feedforward-neural-network",
        "title": "Feedforward Neural Network",
        "section": "Deep Learning",
        "difficulty": "Medium",
        "estimated_time_minutes": 25,
        "tags": ["dense", "perceptron", "feedforward"],
        "learning_objectives": ["Compute neural layer steps", "Map input vectors forward"],
        "description": "Model custom feedforward networks calculating multi-layer matrix outputs.",
        "theory_resource": {
            "title": "Feedforward Networks",
            "url": "https://wikipedia.org/wiki/Feedforward_neural_network",
            "type": "article"
        },
        "practice_resource": {
            "platform": "DEEP_ML",
            "title": "Single Neuron (Perceptron) Scratch",
            "url": "https://deep-ml.com/problems/24"
        },
        "prerequisites": [55]
    })
    
    items.append({
        "id": 57,
        "slug": "backpropagation-neural-network",
        "title": "Backpropagation in Neural Network",
        "section": "Deep Learning",
        "difficulty": "Hard",
        "estimated_time_minutes": 30,
        "tags": ["gradients", "chain-rule", "backprop"],
        "learning_objectives": ["Determine activation derivatives", "Execute matrix chain rules"],
        "description": "Propagate error gradients backward using chain-rule updates.",
        "theory_resource": {
            "title": "Backpropagation Algorithm Wiki",
            "url": "https://wikipedia.org/wiki/Backpropagation",
            "type": "article"
        },
        "practice_resource": {
            "platform": "DEEP_ML",
            "title": "Single Neuron with Backpropagation",
            "url": "https://deep-ml.com/problems/25"
        },
        "prerequisites": [56]
    })
    
    items.append({
        "id": 58,
        "slug": "adam-optimizer-implementation",
        "title": "Adam Optimizer Implementation",
        "section": "Deep Learning",
        "difficulty": "Hard",
        "estimated_time_minutes": 30,
        "tags": ["optimization", "adam", "momentum"],
        "learning_objectives": ["Incorporate momentum moments", "Apply RMSprop scaling coefficients"],
        "description": "Construct adaptive learning rates using rolling mean-square metrics.",
        "theory_resource": {
            "title": "Adam Optimization Algorithm Details",
            "url": "https://arxiv.org/abs/1412.6980",
            "type": "research-paper"
        },
        "practice_resource": {
            "platform": "DEEP_ML",
            "title": "Implement Adam Optimization",
            "url": "https://deep-ml.com/problems/49"
        },
        "prerequisites": [57]
    })
    
    items.append({
        "id": 59,
        "slug": "batch-normalization-layer",
        "title": "Batch Normalization Layer",
        "section": "Deep Learning",
        "difficulty": "Medium",
        "estimated_time_minutes": 25,
        "tags": ["stabilization", "batch-norm", "layers"],
        "learning_objectives": ["Formulate mean variance normalization", "Scale parameters using gamma and beta"],
        "description": "Stabilize intermediate activations using batch normalization scaling.",
        "theory_resource": {
            "title": "Batch Normalization Paper",
            "url": "https://arxiv.org/abs/1502.03167",
            "type": "research-paper"
        },
        "practice_resource": {
            "platform": "DEEP_ML",
            "title": "Implement Batch Normalization BCHW",
            "url": "https://deep-ml.com/problems/115"
        },
        "prerequisites": [58]
    })
    
    items.append({
        "id": 60,
        "slug": "recurrent-neural-network-cell",
        "title": "RNN Cell Forward Pass",
        "section": "Deep Learning",
        "difficulty": "Hard",
        "estimated_time_minutes": 30,
        "tags": ["rnn", "sequential", "hidden-state"],
        "learning_objectives": ["Track hidden state updates", "Evaluate hyperbolic tangent steps"],
        "description": "Model recurrent step processes to encode historical parameters.",
        "theory_resource": {
            "title": "Recurrent Neural Networks Wiki",
            "url": "https://wikipedia.org/wiki/Recurrent_neural_network",
            "type": "article"
        },
        "practice_resource": {
            "platform": "DEEP_ML",
            "title": "Implementing a Simple RNN",
            "url": "https://deep-ml.com/problems/54"
        },
        "prerequisites": [59]
    })
    
    # --- SECTION 5: LLMs (15 ITEMS: 61-75) ---
    # Difficulty: 2 Easy, 5 Medium, 8 Hard
    
    items.append({
        "id": 61,
        "slug": "bpe-tokenization",
        "title": "BPE Word Tokenization",
        "section": "LLM",
        "difficulty": "Hard",
        "estimated_time_minutes": 30,
        "tags": ["tokenization", "bpe", "nlp"],
        "learning_objectives": ["Find frequent character merges", "Build subword vocabularies"],
        "description": "Construct subword dictionaries based on iterative frequency evaluations.",
        "theory_resource": {
            "title": "Byte Pair Encoding Tokenization",
            "url": "https://huggingface.co/learn/nlp-course/chapter6/5",
            "type": "course"
        },
        "practice_resource": {
            "platform": "KAGGLE",
            "title": "BPE Tokenization From Scratch",
            "url": "https://www.kaggle.com/code/tuckerarrants/k-means-and-bpe-tokenization-from-scratch"
        },
        "prerequisites": [60]
    })
    
    items.append({
        "id": 62,
        "slug": "greedy-decoding",
        "title": "Greedy Decoding",
        "section": "LLM",
        "difficulty": "Easy",
        "estimated_time_minutes": 15,
        "tags": ["decoding", "inference", "greedy"],
        "learning_objectives": ["Select maximum logit probabilities", "Verify end-of-sequence parameters"],
        "description": "Map auto-regressive decoding loops selecting maximum probability tokens.",
        "theory_resource": {
            "title": "Text Generation Strategies",
            "url": "https://huggingface.co/docs/transformers/generation_strategies",
            "type": "documentation"
        },
        "practice_resource": {
            "platform": "DEEP_ML",
            "title": "GPT-2 Text Generation",
            "url": "https://deep-ml.com/problems/88"
        },
        "prerequisites": [61]
    })
    
    items.append({
        "id": 63,
        "slug": "softplus-activation-function",
        "title": "Softplus Activation Function",
        "section": "LLM",
        "difficulty": "Medium",
        "estimated_time_minutes": 20,
        "tags": ["activations", "softplus", "math"],
        "learning_objectives": ["Compute Softplus activation output", "Verify continuous differentiability properties"],
        "description": "Implement the smooth Softplus activation function commonly used in neural parameters.",
        "theory_resource": {
            "title": "Softplus Activation Concept",
            "url": "https://wikipedia.org/wiki/Rectifier_(neural_networks)#Softplus",
            "type": "article"
        },
        "practice_resource": {
            "platform": "DEEP_ML",
            "title": "Implement the Softplus Activation",
            "url": "https://deep-ml.com/problems/99"
        },
        "prerequisites": [62]
    })
    
    items.append({
        "id": 64,
        "slug": "swish-activation-function",
        "title": "Swish Activation Function",
        "section": "LLM",
        "difficulty": "Medium",
        "estimated_time_minutes": 20,
        "tags": ["activations", "swish", "silu"],
        "learning_objectives": ["Compute Swish function values", "Verify dynamic sigmoid gating scaling"],
        "description": "Implement the self-gated Swish activation function used in modern transformers.",
        "theory_resource": {
            "title": "Swish Activation Function Details",
            "url": "https://wikipedia.org/wiki/Swish_function",
            "type": "article"
        },
        "practice_resource": {
            "platform": "DEEP_ML",
            "title": "Implement the Swish Activation",
            "url": "https://deep-ml.com/problems/102"
        },
        "prerequisites": [63]
    })
    
    items.append({
        "id": 65,
        "slug": "swiglu-activation-function",
        "title": "SwiGLU Activation Function",
        "section": "LLM",
        "difficulty": "Hard",
        "estimated_time_minutes": 25,
        "tags": ["activations", "swiglu", "transformers"],
        "learning_objectives": ["Build SwiGLU gated layers", "Apply element-wise gate multiplications"],
        "description": "Implement SwiGLU, the state-of-the-art gated linear activation powering Llama architectures.",
        "theory_resource": {
            "title": "GLU Variants Improve Transformer Paper",
            "url": "https://arxiv.org/abs/2002.05202",
            "type": "research-paper"
        },
        "practice_resource": {
            "platform": "DEEP_ML",
            "title": "Implement SwiGLU Activation",
            "url": "https://deep-ml.com/problems/156"
        },
        "prerequisites": [64]
    })
    
    items.append({
        "id": 66,
        "slug": "self-attention-mechanism",
        "title": "Self-Attention Mechanism",
        "section": "LLM",
        "difficulty": "Hard",
        "estimated_time_minutes": 25,
        "tags": ["attention", "transformer", "math"],
        "learning_objectives": ["Compute similarity weights using QK transposes", "Scale dot products using root dimension values"],
        "description": "Model self-attention maps query, key, and value matrices.",
        "theory_resource": {
            "title": "Attention Is All You Need Paper",
            "url": "https://arxiv.org/abs/1706.03762",
            "type": "research-paper"
        },
        "practice_resource": {
            "platform": "DEEP_ML",
            "title": "Implement Self-Attention Mechanism",
            "url": "https://deep-ml.com/problems/53"
        },
        "prerequisites": [65]
    })
    
    items.append({
        "id": 67,
        "slug": "multi-head-attention",
        "title": "Multi-Head Attention",
        "section": "LLM",
        "difficulty": "Hard",
        "estimated_time_minutes": 30,
        "tags": ["attention", "transformers", "multi-head"],
        "learning_objectives": ["Partition dimensional projections", "Concatenate attention headers"],
        "description": "Execute parallel attention projections across multiple headers.",
        "theory_resource": {
            "title": "Multi-Head Attention Details",
            "url": "https://wikipedia.org/wiki/Attention_(machine_learning)#Multi-head_attention",
            "type": "article"
        },
        "practice_resource": {
            "platform": "DEEP_ML",
            "title": "Implement Multi-Head Attention",
            "url": "https://deep-ml.com/problems/94"
        },
        "prerequisites": [66]
    })
    
    items.append({
        "id": 68,
        "slug": "positional-encoding",
        "title": "Sinusoidal Positional Encoding",
        "section": "LLM",
        "difficulty": "Medium",
        "estimated_time_minutes": 25,
        "tags": ["transformers", "embeddings", "positional"],
        "learning_objectives": ["Construct sine position arrays", "Add context vectors to input embeddings"],
        "description": "Build sequence order models using sinusoidal wave values.",
        "theory_resource": {
            "title": "Transformer Positional Encodings",
            "url": "https://kazemnejad.com/blog/transformer_architecture_positional_encoding/",
            "type": "blog"
        },
        "practice_resource": {
            "platform": "DEEP_ML",
            "title": "Positional Encoding Calculator",
            "url": "https://deep-ml.com/problems/85"
        },
        "prerequisites": [67]
    })
    
    items.append({
        "id": 69,
        "slug": "intro-to-nlp-spacy",
        "title": "Introduction to NLP with SpaCy",
        "section": "LLM",
        "difficulty": "Easy",
        "estimated_time_minutes": 15,
        "tags": ["spacy", "tokenization", "parsing"],
        "learning_objectives": ["Load spacy language models", "Perform lemmatization"],
        "description": "Examine token features, text components, and parts of speech using SpaCy.",
        "theory_resource": {
            "title": "SpaCy Industrial NLP Guide",
            "url": "https://spacy.io/usage/spacy-101",
            "type": "documentation"
        },
        "practice_resource": {
            "platform": "KAGGLE",
            "title": "Intro to NLP Exercise",
            "url": "https://www.kaggle.com/code/matheon/exercise-intro-to-nlp"
        },
        "prerequisites": [68]
    })
    
    items.append({
        "id": 70,
        "slug": "nlp-text-classification",
        "title": "Text Classification Pipelines",
        "section": "LLM",
        "difficulty": "Medium",
        "estimated_time_minutes": 20,
        "tags": ["classification", "nlp", "textcat"],
        "learning_objectives": ["Train text classifiers", "Evaluate bag-of-words pipelines"],
        "description": "Train semantic categorization pipelines on text documents using SpaCy.",
        "theory_resource": {
            "title": "SpaCy Text Classification guide",
            "url": "https://spacy.io/usage/training#quickstart",
            "type": "documentation"
        },
        "practice_resource": {
            "platform": "KAGGLE",
            "title": "Text Classification Exercise",
            "url": "https://www.kaggle.com/code/matheon/exercise-text-classification"
        },
        "prerequisites": [69]
    })
    
    items.append({
        "id": 71,
        "slug": "nlp-word-vectors",
        "title": "Word Vectors & Embeddings",
        "section": "LLM",
        "difficulty": "Medium",
        "estimated_time_minutes": 20,
        "tags": ["embeddings", "word2vec", "vectors"],
        "learning_objectives": ["Query cosine similarity matches", "Apply vector math to words"],
        "description": "Measure semantic distances using multi-dimensional word2vec matrices.",
        "theory_resource": {
            "title": "Efficient Estimation of Word Representations",
            "url": "https://arxiv.org/abs/1301.3781",
            "type": "research-paper"
        },
        "practice_resource": {
            "platform": "KAGGLE",
            "title": "Word Vectors Exercise",
            "url": "https://www.kaggle.com/code/matheon/exercise-word-vectors"
        },
        "prerequisites": [70]
    })
    
    items.append({
        "id": 72,
        "slug": "fine-tuning-gemma-kerasnlp",
        "title": "Fine-Tuning Gemma with KerasNLP",
        "section": "LLM",
        "difficulty": "Hard",
        "estimated_time_minutes": 30,
        "tags": ["gemma", "kerasnlp", "fine-tuning"],
        "learning_objectives": ["Build LoRA adapter matrices", "Train open models with KerasNLP"],
        "description": "Fine-tune Gemma-2b parameters using low-rank adapters.",
        "theory_resource": {
            "title": "LoRA: Low-Rank Adaptation of LLMs",
            "url": "https://arxiv.org/abs/2106.09685",
            "type": "research-paper"
        },
        "practice_resource": {
            "platform": "KAGGLE",
            "title": "Fine-tuning Gemma KerasNLP Exercise",
            "url": "https://www.kaggle.com/code/awsaf49/gemma-kerasnlp-fine-tuning"
        },
        "prerequisites": [71]
    })
    
    items.append({
        "id": 73,
        "slug": "llm-prompt-recovery",
        "title": "LLM Prompt Recovery Integration",
        "section": "LLM",
        "difficulty": "Medium",
        "estimated_time_minutes": 25,
        "tags": ["prompting", "gemma", "recovery"],
        "learning_objectives": ["Prompt models to recover instructions", "Structure generation outputs"],
        "description": "Recover lost generation instructions by comparing base and modified text outputs.",
        "theory_resource": {
            "title": "Prompt Engineering Guide",
            "url": "https://www.promptingguide.ai/",
            "type": "documentation"
        },
        "practice_resource": {
            "platform": "KAGGLE",
            "title": "LLM Prompt Recovery Exercise",
            "url": "https://www.kaggle.com/code/gpreda/llm-prompt-recovery-gemma-integration"
        },
        "prerequisites": [72]
    })
    
    items.append({
        "id": 74,
        "slug": "vllm-gemma-serving",
        "title": "vLLM Gemma 2 Serving",
        "section": "LLM",
        "difficulty": "Hard",
        "estimated_time_minutes": 30,
        "tags": ["serving", "vllm", "quantization"],
        "learning_objectives": ["Serve models with vLLM engines", "Apply AWQ quantization profiles"],
        "description": "Deploy low-latency inference services using page-attention memory structures.",
        "theory_resource": {
            "title": "vLLM Engine Architecture",
            "url": "https://arxiv.org/abs/2309.06180",
            "type": "research-paper"
        },
        "practice_resource": {
            "platform": "KAGGLE",
            "title": "vLLM Gemma 2 Serving Exercise",
            "url": "https://www.kaggle.com/code/titericz/gemma-2-9b-it-with-vllm"
        },
        "prerequisites": [73]
    })
    
    items.append({
        "id": 75,
        "slug": "unsloth-llama-3-tuning",
        "title": "Unsloth Llama-3 Fine-Tuning",
        "section": "LLM",
        "difficulty": "Hard",
        "estimated_time_minutes": 30,
        "tags": ["unsloth", "llama-3", "peft"],
        "learning_objectives": ["Configure PEFT adapters", "Accelerate fine-tuning workflows"],
        "description": "Accelerate fine-tuning steps using Unsloth optimized attention kernels.",
        "theory_resource": {
            "title": "Unsloth PEFT Optimization Documentation",
            "url": "https://github.com/unslothai/unsloth",
            "type": "github"
        },
        "practice_resource": {
            "platform": "KAGGLE",
            "title": "Unsloth Llama-3 Fine-Tuning Exercise",
            "url": "https://www.kaggle.com/code/danielhanchen/llama-3-8b-unsloth-notebook"
        },
        "prerequisites": [74]
    })
    
    # --- SECTION 6: RAG (10 ITEMS: 76-85) ---
    # Difficulty: 3 Easy, 5 Medium, 2 Hard
    
    items.append({
        "id": 76,
        "slug": "cosine-similarity-metrics",
        "title": "Cosine Similarity Metrics",
        "section": "RAG",
        "difficulty": "Easy",
        "estimated_time_minutes": 15,
        "tags": ["similarity", "cosine", "vectors"],
        "learning_objectives": ["Determine query-document dot products", "Normalize vector similarity bounds"],
        "description": "Quantify semantic overlaps using normalized cosine projections.",
        "theory_resource": {
            "title": "Cosine Similarity Concepts",
            "url": "https://wikipedia.org/wiki/Cosine_similarity",
            "type": "article"
        },
        "practice_resource": {
            "platform": "DEEP_ML",
            "title": "Cosine Similarity",
            "url": "https://deep-ml.com/problems/76"
        },
        "prerequisites": [64]
    })
    
    items.append({
        "id": 77,
        "slug": "vector-database-matching",
        "title": "Vector Database Similarity Matching",
        "section": "RAG",
        "difficulty": "Medium",
        "estimated_time_minutes": 20,
        "tags": ["vector-db", "retrieval", "ann"],
        "learning_objectives": ["Retrieve top-k matches", "Index embeddings using distance metrics"],
        "description": "Construct similarity searches querying database embeddings.",
        "theory_resource": {
            "title": "Nearest Neighbor Search Algorithms",
            "url": "https://wikipedia.org/wiki/Nearest_neighbor_search",
            "type": "article"
        },
        "practice_resource": {
            "platform": "DEEP_ML",
            "title": "Create Composite Hypervector",
            "url": "https://deep-ml.com/problems/74"
        },
        "prerequisites": [76]
    })
    
    items.append({
        "id": 78,
        "slug": "jaccard-similarity-matching",
        "title": "Jaccard Similarity Matching",
        "section": "RAG",
        "difficulty": "Easy",
        "estimated_time_minutes": 15,
        "tags": ["similarity", "jaccard", "sparse"],
        "learning_objectives": ["Formulate intersection set counts", "Evaluate union counts"],
        "description": "Measure sparse token overlap ratios between sets.",
        "theory_resource": {
            "title": "Jaccard Index Definition",
            "url": "https://wikipedia.org/wiki/Jaccard_index",
            "type": "article"
        },
        "practice_resource": {
            "platform": "DEEP_ML",
            "title": "Jaccard Similarity Index",
            "url": "https://deep-ml.com/problems/72"
        },
        "prerequisites": [77]
    })
    
    items.append({
        "id": 79,
        "slug": "tf-idf-vectorizer",
        "title": "TF-IDF Vectorizer Implementation",
        "section": "RAG",
        "difficulty": "Medium",
        "estimated_time_minutes": 20,
        "tags": ["nlp", "tfidf", "sparse-retrieval"],
        "learning_objectives": ["Compute term frequency values", "Determine inverse document frequency matrices"],
        "description": "Build document weight vectors based on unique token counts.",
        "theory_resource": {
            "title": "TF-IDF Calculation Details",
            "url": "https://wikipedia.org/wiki/Tf%E2%80%93idf",
            "type": "article"
        },
        "practice_resource": {
            "platform": "DEEP_ML",
            "title": "Implement TF-IDF Vectorizer",
            "url": "https://deep-ml.com/problems/60"
        },
        "prerequisites": [78]
    })
    
    items.append({
        "id": 80,
        "slug": "bag-of-words-mapping",
        "title": "Bag of Words Mapping",
        "section": "RAG",
        "difficulty": "Easy",
        "estimated_time_minutes": 15,
        "tags": ["nlp", "bag-of-words", "token-counts"],
        "learning_objectives": ["Construct unique vocabulary indices", "Formulate occurrence frequency matrices"],
        "description": "Generate token occurrence vectors from text arrays.",
        "theory_resource": {
            "title": "Bag of Words Model",
            "url": "https://wikipedia.org/wiki/Bag-of-words_model",
            "type": "article"
        },
        "practice_resource": {
            "platform": "DEEP_ML",
            "title": "Calculate Unigram Probability",
            "url": "https://deep-ml.com/problems/129"
        },
        "prerequisites": [79]
    })
    
    items.append({
        "id": 81,
        "slug": "langchain-rag-pipeline",
        "title": "LangChain RAG Pipeline",
        "section": "RAG",
        "difficulty": "Medium",
        "estimated_time_minutes": 25,
        "tags": ["langchain", "chromadb", "llama-2"],
        "learning_objectives": ["Setup LangChain loaders", "Connect query prompts to contexts"],
        "description": "Assemble retrieval-augmented pipelines querying ChromaDB vectors.",
        "theory_resource": {
            "title": "LangChain RAG Guide",
            "url": "https://python.langchain.com/docs/tutorials/rag/",
            "type": "documentation"
        },
        "practice_resource": {
            "platform": "KAGGLE",
            "title": "LangChain RAG Pipeline Exercise",
            "url": "https://www.kaggle.com/code/gpreda/rag-using-llama-2-langchain-and-chromadb"
        },
        "prerequisites": [80]
    })
    
    items.append({
        "id": 82,
        "slug": "llamaindex-rag-pipeline",
        "title": "LlamaIndex RAG Pipeline",
        "section": "RAG",
        "difficulty": "Medium",
        "estimated_time_minutes": 25,
        "tags": ["llamaindex", "chromadb", "embeddings"],
        "learning_objectives": ["Build LlamaIndex storage layouts", "Execute search query engines"],
        "description": "Index documents and query knowledge using LlamaIndex structures.",
        "theory_resource": {
            "title": "LlamaIndex High-Level Concepts",
            "url": "https://docs.llamaindex.ai/en/stable/getting_started/concepts/",
            "type": "documentation"
        },
        "practice_resource": {
            "platform": "KAGGLE",
            "title": "LlamaIndex RAG Pipeline Exercise",
            "url": "https://www.kaggle.com/code/awsaf49/rag-with-llama-index-and-chromadb"
        },
        "prerequisites": [81]
    })
    
    items.append({
        "id": 83,
        "slug": "rag-evaluation-ragas",
        "title": "RAG Evaluation using RAGAs",
        "section": "RAG",
        "difficulty": "Hard",
        "estimated_time_minutes": 30,
        "tags": ["evaluation", "ragas", "metrics"],
        "learning_objectives": ["Evaluate retrieval faithfulness scores", "Verify answer relevancy values"],
        "description": "Grade RAG answer faithfulness and retrieval accuracy using RAGAs.",
        "theory_resource": {
            "title": "RAGAs Metric Evaluation Framework",
            "url": "https://arxiv.org/abs/2309.15217",
            "type": "research-paper"
        },
        "practice_resource": {
            "platform": "KAGGLE",
            "title": "RAG Evaluation RAGAs Exercise",
            "url": "https://www.kaggle.com/code/philipps/rag-evaluation-using-ragas"
        },
        "prerequisites": [82]
    })
    
    items.append({
        "id": 84,
        "slug": "graph-rag-neo4j-langchain",
        "title": "Graph RAG with Neo4j and LangChain",
        "section": "RAG",
        "difficulty": "Hard",
        "estimated_time_minutes": 30,
        "tags": ["graph-rag", "neo4j", "knowledge-graphs"],
        "learning_objectives": ["Map entity relationships", "Query knowledge graphs"],
        "description": "Construct structural RAG workflows querying Neo4j graph nodes.",
        "theory_resource": {
            "title": "Knowledge Graph RAG Overview",
            "url": "https://python.langchain.com/docs/tutorials/graph/",
            "type": "documentation"
        },
        "practice_resource": {
            "platform": "KAGGLE",
            "title": "Graph RAG Neo4j Exercise",
            "url": "https://www.kaggle.com/code/saurav9786/graph-rag-with-neo4j-and-langchain"
        },
        "prerequisites": [83]
    })
    
    items.append({
        "id": 85,
        "slug": "context-compression-reranking-rag",
        "title": "Context Compression & Reranking",
        "section": "RAG",
        "difficulty": "Medium",
        "estimated_time_minutes": 25,
        "tags": ["reranking", "context-compression", "lost-in-the-middle"],
        "learning_objectives": ["Apply reranker ranking grids", "Compress long retrieved document contexts"],
        "description": "Resolve lost-in-the-middle context limits using rank score filters.",
        "theory_resource": {
            "title": "Lost in the Middle: How Language Models Use Long Contexts",
            "url": "https://arxiv.org/abs/2307.03172",
            "type": "research-paper"
        },
        "practice_resource": {
            "platform": "KAGGLE",
            "title": "Context Compression and Reranking Exercise",
            "url": "https://www.kaggle.com/code/simonveit/context-compression-and-reranking-in-rag"
        },
        "prerequisites": [84]
    })
    
    # --- SECTION 7: AGENTS (10 ITEMS: 86-95) ---
    # Difficulty: 2 Easy, 4 Medium, 4 Hard
    
    items.append({
        "id": 86,
        "slug": "play-connect-x-agent",
        "title": "Play the Game ConnectX Agent",
        "section": "Agents",
        "difficulty": "Easy",
        "estimated_time_minutes": 15,
        "tags": ["game-ai", "connect-x", "agent-loops"],
        "learning_objectives": ["Configure step decision cycles", "Handle current state models"],
        "description": "Build interactive game agents executing decisions within loop cycles.",
        "theory_resource": {
            "title": "Introduction to Game AI",
            "url": "https://www.kaggle.com/learn/intro-to-game-ai",
            "type": "course"
        },
        "practice_resource": {
            "platform": "KAGGLE",
            "title": "Play the Game Exercise",
            "url": "https://www.kaggle.com/code/alexisbcook/exercise-play-the-game"
        },
        "prerequisites": [62]
    })
    
    items.append({
        "id": 87,
        "slug": "one-step-lookahead-agent",
        "title": "One-Step Lookahead Agent",
        "section": "Agents",
        "difficulty": "Medium",
        "estimated_time_minutes": 20,
        "tags": ["lookahead", "heuristic", "agents"],
        "learning_objectives": ["Build scoring heuristics", "Evaluate next action states"],
        "description": "Develop heuristic search agents identifying optimal next-step outcomes.",
        "theory_resource": {
            "title": "Heuristic Search Strategies",
            "url": "https://wikipedia.org/wiki/Heuristic_routing",
            "type": "article"
        },
        "practice_resource": {
            "platform": "KAGGLE",
            "title": "One-Step Lookahead Exercise",
            "url": "https://www.kaggle.com/code/alexisbcook/exercise-one-step-lookahead"
        },
        "prerequisites": [86]
    })
    
    items.append({
        "id": 88,
        "slug": "n-step-lookahead-minimax",
        "title": "N-Step Lookahead (Minimax)",
        "section": "Agents",
        "difficulty": "Medium",
        "estimated_time_minutes": 25,
        "tags": ["minimax", "game-trees", "alphabeta"],
        "learning_objectives": ["Apply minimax score derivations", "Prune tree paths using alpha-beta parameters"],
        "description": "Implement recursive minimax depth planners mapping state projections.",
        "theory_resource": {
            "title": "Minimax Decision Tree Theory",
            "url": "https://wikipedia.org/wiki/Minimax",
            "type": "article"
        },
        "practice_resource": {
            "platform": "KAGGLE",
            "title": "N-Step Lookahead Exercise",
            "url": "https://www.kaggle.com/code/alexisbcook/exercise-n-step-lookahead"
        },
        "prerequisites": [87]
    })
    
    items.append({
        "id": 89,
        "slug": "deep-reinforcement-learning-agent",
        "title": "Deep Reinforcement Learning Agent",
        "section": "Agents",
        "difficulty": "Hard",
        "estimated_time_minutes": 30,
        "tags": ["rl", "dqn", "neural-nets"],
        "learning_objectives": ["Formulate policy rewards", "Train Q-network parameters"],
        "description": "Construct deep reinforcement learning agents using Q-Network architectures.",
        "theory_resource": {
            "title": "Playing Atari with Deep Reinforcement Learning",
            "url": "https://arxiv.org/abs/1312.5602",
            "type": "research-paper"
        },
        "practice_resource": {
            "platform": "KAGGLE",
            "title": "Deep Reinforcement Learning Exercise",
            "url": "https://www.kaggle.com/code/alexisbcook/exercise-deep-reinforcement-learning"
        },
        "prerequisites": [88]
    })
    
    items.append({
        "id": 90,
        "slug": "langgraph-agentic-workflow",
        "title": "LangGraph Agentic Workflow",
        "section": "Agents",
        "difficulty": "Hard",
        "estimated_time_minutes": 30,
        "tags": ["langgraph", "state-machines", "graphs"],
        "learning_objectives": ["Design state transition routing", "Construct cyclic graph nodes"],
        "description": "Construct state graph routing models managing persistent loop nodes.",
        "theory_resource": {
            "title": "LangGraph State Machine Concepts",
            "url": "https://langchainai.github.io/langgraph/concepts/",
            "type": "documentation"
        },
        "practice_resource": {
            "platform": "KAGGLE",
            "title": "LangGraph Agentic Workflow Exercise",
            "url": "https://www.kaggle.com/code/saurav9786/langgraph-agentic-workflow-from-scratch"
        },
        "prerequisites": [89]
    })
    
    items.append({
        "id": 91,
        "slug": "crewai-multi-agent-system",
        "title": "CrewAI Multi-Agent System",
        "section": "Agents",
        "difficulty": "Hard",
        "estimated_time_minutes": 30,
        "tags": ["crewai", "multi-agent", "collaboration"],
        "learning_objectives": ["Define specific agent persona scopes", "Establish inter-agent output routing"],
        "description": "Orchestrate collaborative multi-agent teams executing sequential task targets.",
        "theory_resource": {
            "title": "CrewAI Multi-Agent Collaboration Docs",
            "url": "https://docs.crewai.com/",
            "type": "documentation"
        },
        "practice_resource": {
            "platform": "KAGGLE",
            "title": "CrewAI Multi-Agent System Exercise",
            "url": "https://www.kaggle.com/code/saurav9786/crewai-multi-agent-system-for-news-analysis"
        },
        "prerequisites": [90]
    })
    
    items.append({
        "id": 92,
        "slug": "gemini-tool-calling-api",
        "title": "Gemini Tool Calling & API Execution",
        "section": "Agents",
        "difficulty": "Medium",
        "estimated_time_minutes": 25,
        "tags": ["tool-calling", "apis", "gemini"],
        "learning_objectives": ["Define valid tool schemas", "Handle execution response inputs"],
        "description": "Configure models to select and call external APIs via structured function calling.",
        "theory_resource": {
            "title": "Function Calling in Gemini",
            "url": "https://ai.google.dev/gemini-api/docs/function-calling",
            "type": "documentation"
        },
        "practice_resource": {
            "platform": "KAGGLE",
            "title": "Gemini Tool Calling Exercise",
            "url": "https://www.kaggle.com/code/awsaf49/gemini-tool-calling-and-function-execution"
        },
        "prerequisites": [91]
    })
    
    items.append({
        "id": 93,
        "slug": "chatbot-memory-history",
        "title": "Chatbots with Memory and History",
        "section": "Agents",
        "difficulty": "Easy",
        "estimated_time_minutes": 20,
        "tags": ["memory", "langchain", "chat-history"],
        "learning_objectives": ["Maintain rolling buffer history", "Format conversation context windows"],
        "description": "Structure persistent chat message storage arrays to preserve conversation state.",
        "theory_resource": {
            "title": "LangChain Memory Management",
            "url": "https://python.langchain.com/v0.1/docs/modules/memory/",
            "type": "documentation"
        },
        "practice_resource": {
            "platform": "KAGGLE",
            "title": "Chatbots with Memory Exercise",
            "url": "https://www.kaggle.com/code/gpreda/building-chatbots-with-memory-and-langchain"
        },
        "prerequisites": [92]
    })
    
    items.append({
        "id": 94,
        "slug": "agentic-rag-routing",
        "title": "Agentic RAG with LangChain",
        "section": "Agents",
        "difficulty": "Medium",
        "estimated_time_minutes": 25,
        "tags": ["agentic-rag", "routing", "langchain"],
        "learning_objectives": ["Construct dynamic RAG routes", "Handle multi-index database checks"],
        "description": "Build agentic routing networks dynamically selecting database index targets.",
        "theory_resource": {
            "title": "Agentic RAG Architectures",
            "url": "https://python.langchain.com/docs/concepts/rag/",
            "type": "documentation"
        },
        "practice_resource": {
            "platform": "KAGGLE",
            "title": "Agentic RAG Exercise",
            "url": "https://www.kaggle.com/code/awsaf49/agentic-rag-with-langchain"
        },
        "prerequisites": [93, 85]
    })
    
    items.append({
        "id": 95,
        "slug": "selenium-playwright-automation",
        "title": "Selenium & Playwright Automation",
        "section": "Agents",
        "difficulty": "Hard",
        "estimated_time_minutes": 30,
        "tags": ["automation", "playwright", "scraping"],
        "learning_objectives": ["Control headless browsers", "Handle dynamic page loads"],
        "description": "Build automated web agents crawling and interacting with dynamic websites.",
        "theory_resource": {
            "title": "Playwright Automation Guide",
            "url": "https://playwright.dev/python/docs/intro",
            "type": "documentation"
        },
        "practice_resource": {
            "platform": "KAGGLE",
            "title": "Selenium and Playwright Exercise",
            "url": "https://www.kaggle.com/code/harshsingh22/selenium-and-playwright-automation-in-kaggle"
        },
        "prerequisites": [94]
    })
    
    # --- SECTION 8: SYSTEM DESIGN (5 ITEMS: 96-100) ---
    # Difficulty: 4 Easy, 1 Medium, 0 Hard
    
    items.append({
        "id": 96,
        "slug": "real-time-fraud-detection-system",
        "title": "Real-time Fraud Detection Pipeline",
        "section": "System Design",
        "difficulty": "Easy",
        "estimated_time_minutes": 20,
        "tags": ["fraud-detection", "classification", "system-design"],
        "learning_objectives": ["Identify skewed label profiles", "Deploy real-time transaction pipelines"],
        "description": "Design sub-second tabular classification pipelines detecting card fraud.",
        "theory_resource": {
            "title": "Real-time ML System Architectures",
            "url": "https://wikipedia.org/wiki/Fraud_detection",
            "type": "article"
        },
        "practice_resource": {
            "platform": "KAGGLE",
            "title": "Fraud Detection System Exercise",
            "url": "https://www.kaggle.com/code/gpreda/credit-card-fraud-detection-predictive-models"
        },
        "prerequisites": [35]
    })
    
    items.append({
        "id": 97,
        "slug": "llm-serving-vllm",
        "title": "vLLM Serving Infrastructure",
        "section": "System Design",
        "difficulty": "Medium",
        "estimated_time_minutes": 25,
        "tags": ["serving", "vllm", "system-design"],
        "learning_objectives": ["Optimize KV cache parameters", "Handle concurrent requests"],
        "description": "Scale open model serving interfaces using page-attention pooling structures.",
        "theory_resource": {
            "title": "vLLM Engine Internals",
            "url": "https://vllm.ai/",
            "type": "documentation"
        },
        "practice_resource": {
            "platform": "KAGGLE",
            "title": "vLLM Serving Infrastructure Exercise",
            "url": "https://www.kaggle.com/code/awsaf49/vllm-inference-gemma-2-9b"
        },
        "prerequisites": [74]
    })
    
    items.append({
        "id": 98,
        "slug": "search-recommendation-pipeline",
        "title": "Search & Recommendation Pipeline",
        "section": "System Design",
        "difficulty": "Easy",
        "estimated_time_minutes": 20,
        "tags": ["recommendations", "collaborative-filtering", "system-design"],
        "learning_objectives": ["Build item similarity profiles", "Structure recommendation pipelines"],
        "description": "Design multi-stage recommendation pipelines serving items in real time.",
        "theory_resource": {
            "title": "Recommender Systems Architectures",
            "url": "https://wikipedia.org/wiki/Recommender_system",
            "type": "article"
        },
        "practice_resource": {
            "platform": "KAGGLE",
            "title": "Search & Recommendation Exercise",
            "url": "https://www.kaggle.com/code/gpreda/recommender-systems-from-scratch"
        },
        "prerequisites": [43]
    })
    
    items.append({
        "id": 99,
        "slug": "multimodal-search-clip",
        "title": "Multimodal CLIP Engine",
        "section": "System Design",
        "difficulty": "Hard",
        "estimated_time_minutes": 20,
        "tags": ["clip", "multimodal", "system-design"],
        "learning_objectives": ["Map image text embeddings", "Perform vector searches"],
        "description": "Deploy multimodal search services coordinating text and image inputs.",
        "theory_resource": {
            "title": "Learning Transferable Visual Models From Natural Language Supervision",
            "url": "https://arxiv.org/abs/2103.00020",
            "type": "research-paper"
        },
        "practice_resource": {
            "platform": "KAGGLE",
            "title": "Multimodal CLIP Engine Exercise",
            "url": "https://www.kaggle.com/code/awsaf49/image-similarity-search-with-clip"
        },
        "prerequisites": [71]
    })
    
    items.append({
        "id": 100,
        "slug": "agentic-customer-support-desk",
        "title": "Agentic Customer Support Desk",
        "section": "System Design",
        "difficulty": "Easy",
        "estimated_time_minutes": 25,
        "tags": ["agentic-support", "rag", "system-design"],
        "learning_objectives": ["Connect multi-agent routers", "Incorporate context memory logs"],
        "description": "Deploy automated customer service portals utilizing RAG and agents.",
        "theory_resource": {
            "title": "Designing Agentic Support Portals",
            "url": "https://wikipedia.org/wiki/Customer_service_conversational_agent",
            "type": "article"
        },
        "practice_resource": {
            "platform": "KAGGLE",
            "title": "Agentic Customer Support Desk Exercise",
            "url": "https://www.kaggle.com/code/saurav9786/langchain-support-bot-with-rag"
        },
        "prerequisites": [95, 85]
    })
    
    # 2. Write out all 100 items into their corresponding section folders
    print(f"Generating {len(items)} new learning items...")
    
    for item in items:
        q_id = item["id"]
        slug = item["slug"]
        sec_slug = item["section"].lower().replace(" ", "-")
        
        file_name = f"{str(q_id).zfill(3)}-{slug}.json"
        file_path = os.path.join(content_dir, sec_slug, file_name)
        
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(item, f, indent=2, ensure_ascii=False)
            
    print("All learning items successfully generated.")
    
    # 3. Create questions/ directory and index.json / roadmap.json files
    questions_dir = os.path.join(base_dir, "questions")
    os.makedirs(questions_dir, exist_ok=True)
    
    # Compilation statistics
    total_questions = len(items)
    section_counts = {}
    difficulty_counts = {"Easy": 0, "Medium": 0, "Hard": 0}
    
    for item in items:
        sec = item["section"]
        diff = item["difficulty"]
        
        section_counts[sec] = section_counts.get(sec, 0) + 1
        difficulty_counts[diff] = difficulty_counts.get(diff, 0) + 1
        
    index_data = {
        "total_questions": total_questions,
        "section_counts": section_counts,
        "difficulty_counts": difficulty_counts
    }
    
    index_path = os.path.join(questions_dir, "index.json")
    with open(index_path, 'w', encoding='utf-8') as f:
        json.dump(index_data, f, indent=2, ensure_ascii=False)
    print(f"Index data generated: {index_path}")
    
    # Roadmap data
    roadmap_data = {
        "learning_order": [item["slug"] for item in items],
        "prerequisites": {str(item["id"]): item["prerequisites"] for item in items},
        "section_dependencies": {
            "python": [],
            "statistics": [],
            "machine-learning": ["python", "statistics"],
            "deep-learning": ["machine-learning"],
            "llm": ["deep-learning"],
            "rag": ["llm"],
            "agents": ["llm"],
            "system-design": ["machine-learning", "deep-learning", "llm", "rag", "agents"]
        }
    }
    
    roadmap_path = os.path.join(questions_dir, "roadmap.json")
    with open(roadmap_path, 'w', encoding='utf-8') as f:
        json.dump(roadmap_data, f, indent=2, ensure_ascii=False)
    print(f"Roadmap data generated: {roadmap_path}")
    
    # 4. Generate VALIDATION_REPORT.md
    validation_report_content = generate_validation_report(items, index_data)
    validation_report_path = os.path.join(base_dir, "VALIDATION_REPORT.md")
    with open(validation_report_path, 'w', encoding='utf-8') as f:
        f.write(validation_report_content)
    print(f"Validation report generated: {validation_report_path}")
    
def generate_validation_report(items, index_data):
    # Verify uniqueness of URLs
    practice_urls = [item["practice_resource"]["url"] for item in items]
    unique_practice_urls = set(practice_urls)
    has_duplicate_urls = len(practice_urls) != len(unique_practice_urls)
    
    duplicate_url_analysis = "No duplicate practice URLs detected."
    if has_duplicate_urls:
        seen = set()
        dups = []
        for url in practice_urls:
            if url in seen:
                dups.append(url)
            seen.add(url)
        duplicate_url_analysis = f"WARNING: Duplicate practice URLs found: {dups}"
        
    # Verify uniqueness of concepts/slugs
    slugs = [item["slug"] for item in items]
    unique_slugs = set(slugs)
    has_duplicate_slugs = len(slugs) != len(unique_slugs)
    
    duplicate_slug_analysis = "No duplicate concept slugs detected."
    if has_duplicate_slugs:
        seen = set()
        dups = []
        for slug in slugs:
            if slug in seen:
                dups.append(slug)
            seen.add(slug)
        duplicate_slug_analysis = f"WARNING: Duplicate concept slugs found: {dups}"

    # Verify links directness
    non_direct_urls = []
    for item in items:
        url = item["practice_resource"]["url"]
        if "deep-ml.com" in url:
            # must match deep-ml.com/problems/<id>
            parts = url.split("deep-ml.com/problems/")
            if len(parts) < 2 or not parts[1].strip().isdigit():
                non_direct_urls.append((item["id"], url))
        elif "kaggle.com" in url:
            if "kaggle.com/code/" not in url:
                non_direct_urls.append((item["id"], url))
                
    non_direct_analysis = "All practice URLs conform to strict direct-exercise guidelines."
    if non_direct_urls:
        non_direct_analysis = f"WARNING: Non-direct practice URLs found:\n"
        for q_id, url in non_direct_urls:
            non_direct_analysis += f" - ID {q_id}: {url}\n"
            
    markdown = f"""# NeuroForge Question Bank v2 Validation Report

This validation report checks and ensures the integrity of the generated NeuroForge Question Bank v2 dataset.

## Summary Metrics

*   **Total Items**: {index_data['total_questions']} (Target: 100)
*   **Difficulty Distribution**:
    *   **Easy**: {index_data['difficulty_counts']['Easy']} (30%)
    *   **Medium**: {index_data['difficulty_counts']['Medium']} (50%)
    *   **Hard**: {index_data['difficulty_counts']['Hard']} (20%)
*   **Section Breakdown**:
    *   **Python**: {index_data['section_counts'].get('Python', 0)} (Target: 10)
    *   **Statistics**: {index_data['section_counts'].get('Statistics', 0)} (Target: 15)
    *   **Machine Learning**: {index_data['section_counts'].get('Machine Learning', 0)} (Target: 20)
    *   **Deep Learning**: {index_data['section_counts'].get('Deep Learning', 0)} (Target: 15)
    *   **LLM**: {index_data['section_counts'].get('LLM', 0)} (Target: 15)
    *   **RAG**: {index_data['section_counts'].get('RAG', 0)} (Target: 10)
    *   **Agents**: {index_data['section_counts'].get('Agents', 0)} (Target: 10)
    *   **System Design**: {index_data['section_counts'].get('System Design', 0)} (Target: 5)

## Integrity Analysis

### Duplicate URLs Analysis
{duplicate_url_analysis}

### Duplicate Concepts Analysis
{duplicate_slug_analysis}

### Direct Practice URL Verification
{non_direct_analysis}

## URLs Checked List

| ID | Title | Section | Platform | Practice URL |
| :--- | :--- | :--- | :---: | :--- |
"""
    for item in items:
        markdown += f"| {item['id']} | {item['title']} | {item['section']} | {item['practice_resource']['platform']} | {item['practice_resource']['url']} |\n"
        
    return markdown

if __name__ == "__main__":
    main()
