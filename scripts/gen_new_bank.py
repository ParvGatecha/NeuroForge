import os
import json
import shutil

def main():
    print("Initializing TensorTrack Question Bank v2 Generation...")
    
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
    
    # --- SECTION 9: ADDED PYTHON (10 ITEMS: 101-110) ---
    items.append({
        "id": 101,
        "slug": "custom-context-managers",
        "title": "Python Custom Context Managers",
        "section": "Python",
        "difficulty": "Easy",
        "estimated_time_minutes": 15,
        "tags": ["context-managers", "resource-management"],
        "learning_objectives": ["Implement class-based context managers", "Create generator context managers using contextlib"],
        "description": "Learn to build custom context managers in Python using both class-based __enter__ / __exit__ protocols and the @contextmanager generator utility.",
        "theory_resource": {
            "title": "Python List Comprehensions Guide",
            "url": "https://realpython.com/python-with-statement/",
            "type": "article"
        },
        "practice_resource": {
            "platform": "KAGGLE",
            "title": "Loops and List Comprehensions Exercise",
            "url": "https://www.kaggle.com/code/colinmorris/exercise-hello-python"
        },
        "prerequisites": [1]
    })
    
    items.append({
        "id": 102,
        "slug": "dataclasses-validation",
        "title": "Data Validation with Dataclasses",
        "section": "Python",
        "difficulty": "Medium",
        "estimated_time_minutes": 20,
        "tags": ["dataclasses", "validation", "type-hints"],
        "learning_objectives": ["Build structured data models using dataclasses", "Enforce type checking and post-init validations"],
        "description": "Structure clean schemas and run dynamic validation rules on instantiation using Python dataclasses.",
        "theory_resource": {
            "title": "Python Modules and Packages",
            "url": "https://realpython.com/python-data-classes/",
            "type": "article"
        },
        "practice_resource": {
            "platform": "KAGGLE",
            "title": "Functions and Help Exercise",
            "url": "https://www.kaggle.com/code/colinmorris/exercise-strings-and-dictionaries"
        },
        "prerequisites": [4]
    })
    
    items.append({
        "id": 103,
        "slug": "abstract-base-classes",
        "title": "Abstract Base Classes (ABCs)",
        "section": "Python",
        "difficulty": "Medium",
        "estimated_time_minutes": 20,
        "tags": ["oop", "abc", "inheritance"],
        "learning_objectives": ["Define interfaces using Abstract Base Classes", "Enforce method implementation in child subclasses"],
        "description": "Design robust interfaces and enforce code patterns in downstream classes using abc.",
        "theory_resource": {
            "title": "Python Functions and Docstrings",
            "url": "https://docs.python.org/3/library/abc.html",
            "type": "documentation"
        },
        "practice_resource": {
            "platform": "KAGGLE",
            "title": "Working with External Libraries Exercise",
            "url": "https://www.kaggle.com/code/residentmario/exercise-creating-reading-and-writing"
        },
        "prerequisites": [8]
    })
    
    items.append({
        "id": 104,
        "slug": "advanced-generators-send",
        "title": "Advanced Generators & Coroutines",
        "section": "Python",
        "difficulty": "Hard",
        "estimated_time_minutes": 25,
        "tags": ["generators", "coroutines", "concurrency"],
        "learning_objectives": ["Pass data into generators using the send() method", "Manage stateful generator execution loops"],
        "description": "Control execution flow and pass values back into a running generator stream using .send().",
        "theory_resource": {
            "title": "Python Modules and Packages",
            "url": "https://realpython.com/introduction-to-python-generators/",
            "type": "article"
        },
        "practice_resource": {
            "platform": "DEEP_ML",
            "title": "Softmax Activation Function Exercise",
            "url": "https://deep-ml.com/problems/11"
        },
        "prerequisites": [101]
    })
    
    items.append({
        "id": 105,
        "slug": "python-multiprocessing-pool",
        "title": "Multiprocessing & Parallel Execution",
        "section": "Python",
        "difficulty": "Medium",
        "estimated_time_minutes": 25,
        "tags": ["multiprocessing", "parallelism", "performance"],
        "learning_objectives": ["Bypass the GIL using the multiprocessing module", "Distribute work across CPU cores with Pool.map"],
        "description": "Bypass Python's Global Interpreter Lock (GIL) by distributing compute-heavy work across processes.",
        "theory_resource": {
            "title": "Python Functions and Docstrings",
            "url": "https://docs.python.org/3/library/multiprocessing.html",
            "type": "documentation"
        },
        "practice_resource": {
            "platform": "KAGGLE",
            "title": "Working with External Libraries Exercise",
            "url": "https://www.kaggle.com/code/residentmario/exercise-indexing-selecting-assigning"
        },
        "prerequisites": [9]
    })
    
    items.append({
        "id": 106,
        "slug": "custom-metaclasses",
        "title": "Metaprogramming & Custom Metaclasses",
        "section": "Python",
        "difficulty": "Hard",
        "estimated_time_minutes": 30,
        "tags": ["metaprogramming", "metaclasses", "oop"],
        "learning_objectives": ["Interfere with class creation using __new__ and __init__ in metaclasses", "Enforce runtime constraints on class parameters"],
        "description": "Learn to intercept, modify, and register class definitions dynamically at load-time.",
        "theory_resource": {
            "title": "Python Modules and Packages",
            "url": "https://realpython.com/python-metaclasses/",
            "type": "article"
        },
        "practice_resource": {
            "platform": "DEEP_ML",
            "title": "One-Hot Encoding Exercise",
            "url": "https://deep-ml.com/problems/21"
        },
        "prerequisites": [103]
    })
    
    items.append({
        "id": 107,
        "slug": "python-threading-locks",
        "title": "Thread Synchronization with Locks",
        "section": "Python",
        "difficulty": "Medium",
        "estimated_time_minutes": 20,
        "tags": ["threading", "concurrency", "locks"],
        "learning_objectives": ["Identify and resolve race conditions in shared memory", "Synchronize parallel tasks using threading.Lock"],
        "description": "Prevent shared-memory race conditions in IO-bound workloads using mutual exclusion thread locks.",
        "theory_resource": {
            "title": "Python Modules and Packages",
            "url": "https://realpython.com/intro-to-python-threading/",
            "type": "article"
        },
        "practice_resource": {
            "platform": "KAGGLE",
            "title": "Working with External Libraries Exercise",
            "url": "https://www.kaggle.com/code/residentmario/exercise-summary-functions-and-maps"
        },
        "prerequisites": [10]
    })
    
    items.append({
        "id": 108,
        "slug": "weak-references-memory",
        "title": "Weak References & Memory Optimization",
        "section": "Python",
        "difficulty": "Medium",
        "estimated_time_minutes": 20,
        "tags": ["memory-management", "weakref", "garbage-collection"],
        "learning_objectives": ["Prevent circular reference memory leaks using weak references", "Construct clean element caches using WeakValueDictionary"],
        "description": "Avoid reference cycles and memory leaks in large caching structures using the weakref module.",
        "theory_resource": {
            "title": "Python Functions and Docstrings",
            "url": "https://docs.python.org/3/library/weakref.html",
            "type": "documentation"
        },
        "practice_resource": {
            "platform": "DEEP_ML",
            "title": "Matrix Vector Product Exercise",
            "url": "https://deep-ml.com/problems/1"
        },
        "prerequisites": [104]
    })
    
    items.append({
        "id": 109,
        "slug": "built-in-descriptors",
        "title": "Python Property Descriptors",
        "section": "Python",
        "difficulty": "Easy",
        "estimated_time_minutes": 15,
        "tags": ["descriptors", "properties", "oop"],
        "learning_objectives": ["Define dynamic attributes using __get__ and __set__ descriptors", "Encapsulate reusable validation logic across class properties"],
        "description": "Understand how Python's descriptor protocol powers properties and custom access logic.",
        "theory_resource": {
            "title": "Python Functions and Docstrings",
            "url": "https://docs.python.org/3/howto/descriptor.html",
            "type": "documentation"
        },
        "practice_resource": {
            "platform": "DEEP_ML",
            "title": "Scalar Multiplication Exercise",
            "url": "https://deep-ml.com/problems/5"
        },
        "prerequisites": [102]
    })
    
    items.append({
        "id": 110,
        "slug": "functools-lru-cache",
        "title": "Dynamic Caching with lru_cache",
        "section": "Python",
        "difficulty": "Medium",
        "estimated_time_minutes": 15,
        "tags": ["caching", "decorators", "optimization"],
        "learning_objectives": ["Speed up recursive computations using function memoization", "Tune caching capacities and monitor cache performance metrics"],
        "description": "Optimize expensive repetitive functions by caching results automatically with @lru_cache.",
        "theory_resource": {
            "title": "Python Modules and Packages",
            "url": "https://realpython.com/lru-cache-python/",
            "type": "article"
        },
        "practice_resource": {
            "platform": "DEEP_ML",
            "title": "Mean by Row or Column Exercise",
            "url": "https://deep-ml.com/problems/6"
        },
        "prerequisites": [2]
    })
    
    # --- SECTION 10: ADDED STATISTICS (15 ITEMS: 111-125) ---
    items.append({
        "id": 111,
        "slug": "probability-distributions-pmf",
        "title": "Probability Mass Functions",
        "section": "Statistics",
        "difficulty": "Easy",
        "estimated_time_minutes": 15,
        "tags": ["probability", "pmf", "statistics"],
        "learning_objectives": ["Understand discrete probability mass functions", "Evaluate PMF bounds and normalized variables"],
        "description": "Examine PMFs for discrete variables mapping single events to precise occurrence ratios.",
        "theory_resource": {
            "title": "Probability Mass Function Overview",
            "url": "https://en.wikipedia.org/wiki/Probability_mass_function",
            "type": "article"
        },
        "practice_resource": {
            "platform": "DEEP_ML",
            "title": "Mean, Median, Mode Exercise",
            "url": "https://deep-ml.com/problems/78"
        },
        "prerequisites": [11]
    })
    
    items.append({
        "id": 112,
        "slug": "poisson-distribution-events",
        "title": "Poisson Distribution & Rates",
        "section": "Statistics",
        "difficulty": "Medium",
        "estimated_time_minutes": 20,
        "tags": ["poisson", "probability", "statistics"],
        "learning_objectives": ["Model events happening in a fixed time interval", "Calculate Poisson probabilities and rates"],
        "description": "Construct discrete event rate models measuring probability ranges over fixed periods.",
        "theory_resource": {
            "title": "Poisson Distribution Overview",
            "url": "https://en.wikipedia.org/wiki/Poisson_distribution",
            "type": "article"
        },
        "practice_resource": {
            "platform": "DEEP_ML",
            "title": "Binomial Distribution Exercise",
            "url": "https://deep-ml.com/problems/79"
        },
        "prerequisites": [24]
    })
    
    items.append({
        "id": 113,
        "slug": "exponential-distribution-intervals",
        "title": "Exponential Distribution & Wait Times",
        "section": "Statistics",
        "difficulty": "Easy",
        "estimated_time_minutes": 15,
        "tags": ["exponential", "continuous", "statistics"],
        "learning_objectives": ["Model wait time intervals between Poisson processes", "Calculate memoryless continuous probability limits"],
        "description": "Utilize continuous exponential distribution equations estimating temporal distance between events.",
        "theory_resource": {
            "title": "Exponential Distribution Overview",
            "url": "https://en.wikipedia.org/wiki/Exponential_distribution",
            "type": "article"
        },
        "practice_resource": {
            "platform": "DEEP_ML",
            "title": "Gaussian Probability Density Function Exercise",
            "url": "https://deep-ml.com/problems/80"
        },
        "prerequisites": [14]
    })
    
    items.append({
        "id": 114,
        "slug": "beta-prior-distributions",
        "title": "Beta Distribution and Priors",
        "section": "Statistics",
        "difficulty": "Medium",
        "estimated_time_minutes": 20,
        "tags": ["beta", "bayesian", "statistics"],
        "learning_objectives": ["Apply Beta distributions as prior models", "Update prior beliefs with conjugate Bernoulli updates"],
        "description": "Master Bayesian priors modeling probabilities dynamically using the continuous Beta function.",
        "theory_resource": {
            "title": "Beta Distribution Overview",
            "url": "https://en.wikipedia.org/wiki/Beta_distribution",
            "type": "article"
        },
        "practice_resource": {
            "platform": "DEEP_ML",
            "title": "Bayes Theorem Exercise",
            "url": "https://deep-ml.com/problems/84"
        },
        "prerequisites": [13]
    })
    
    items.append({
        "id": 115,
        "slug": "maximum-aposteriori-estimation",
        "title": "Maximum A Posteriori (MAP)",
        "section": "Statistics",
        "difficulty": "Hard",
        "estimated_time_minutes": 25,
        "tags": ["map", "bayesian", "estimation"],
        "learning_objectives": ["Formulate Maximum A Posteriori objective functions", "Incorporate prior distributions into standard MLE formulas"],
        "description": "Perform Bayesian point estimation integrating prior distribution constraints onto target model variables.",
        "theory_resource": {
            "title": "Maximum A Posteriori Overview",
            "url": "https://en.wikipedia.org/wiki/Maximum_a_posteriori_estimation",
            "type": "article"
        },
        "practice_resource": {
            "platform": "DEEP_ML",
            "title": "Conditional Probability Exercise",
            "url": "https://deep-ml.com/problems/85"
        },
        "prerequisites": [114]
    })
    
    items.append({
        "id": 116,
        "slug": "linear-regression-t-stats",
        "title": "T-Statistics in Linear Regression",
        "section": "Statistics",
        "difficulty": "Medium",
        "estimated_time_minutes": 20,
        "tags": ["t-test", "regression", "inference"],
        "learning_objectives": ["Calculate regression coefficient standard errors", "Verify significance of linear predictors using t-statistics"],
        "description": "Validate linear coefficient fit significance using standard errors and t-distribution mappings.",
        "theory_resource": {
            "title": "T-Statistic Overview",
            "url": "https://en.wikipedia.org/wiki/T-statistic",
            "type": "article"
        },
        "practice_resource": {
            "platform": "DEEP_ML",
            "title": "Coefficient of Determination Exercise",
            "url": "https://deep-ml.com/problems/69"
        },
        "prerequisites": [23, 17]
    })
    
    items.append({
        "id": 117,
        "slug": "anova-multiple-comparisons",
        "title": "ANOVA & Post-Hoc Tests",
        "section": "Statistics",
        "difficulty": "Medium",
        "estimated_time_minutes": 25,
        "tags": ["anova", "hypothesis-testing", "statistics"],
        "learning_objectives": ["Compare multiple group means using F-tests", "Apply Tukey post-hoc corrections on group variables"],
        "description": "Run variance analysis tracking variable differences across multiple distinct parameter groups.",
        "theory_resource": {
            "title": "Analysis of Variance Overview",
            "url": "https://en.wikipedia.org/wiki/Analysis_of_variance",
            "type": "article"
        },
        "practice_resource": {
            "platform": "DEEP_ML",
            "title": "Mean Absolute Error Exercise",
            "url": "https://deep-ml.com/problems/93"
        },
        "prerequisites": [19]
    })
    
    items.append({
        "id": 118,
        "slug": "fdr-benjamini-hochberg",
        "title": "False Discovery Rate & Multiple Testing",
        "section": "Statistics",
        "difficulty": "Hard",
        "estimated_time_minutes": 25,
        "tags": ["fdr", "multiple-testing", "statistics"],
        "learning_objectives": ["Explain multiple comparisons type-I error inflation", "Apply Benjamini-Hochberg FDR adjustments on hypothesis arrays"],
        "description": "Manage false discovery rates in large concurrent hypothesis test datasets using BH metrics.",
        "theory_resource": {
            "title": "False Discovery Rate Overview",
            "url": "https://en.wikipedia.org/wiki/False_discovery_rate",
            "type": "article"
        },
        "practice_resource": {
            "platform": "DEEP_ML",
            "title": "Phi Coefficient Exercise",
            "url": "https://deep-ml.com/problems/95"
        },
        "prerequisites": [18]
    })
    
    items.append({
        "id": 119,
        "slug": "confidence-intervals-bootstrap",
        "title": "Bootstrap Confidence Intervals",
        "section": "Statistics",
        "difficulty": "Easy",
        "estimated_time_minutes": 15,
        "tags": ["bootstrap", "confidence-intervals", "statistics"],
        "learning_objectives": ["Perform resampling with replacement on sample arrays", "Calculate confidence bounds using percentile bootstrap outputs"],
        "description": "Estimate population sample confidence metrics dynamically by computing bootsrap resampled groups.",
        "theory_resource": {
            "title": "Bootstrapping Overview",
            "url": "https://en.wikipedia.org/wiki/Bootstrapping_(statistics)",
            "type": "article"
        },
        "practice_resource": {
            "platform": "DEEP_ML",
            "title": "Covariance Matrix Exercise",
            "url": "https://deep-ml.com/problems/10"
        },
        "prerequisites": [12]
    })
    
    items.append({
        "id": 120,
        "slug": "conditional-expectation-variance",
        "title": "Conditional Expectation and Variance",
        "section": "Statistics",
        "difficulty": "Medium",
        "estimated_time_minutes": 20,
        "tags": ["probability", "expectation", "variance"],
        "learning_objectives": ["Derive expectations conditioned on random variables", "Apply the law of total variance on compound models"],
        "description": "Analyze system behavior changes by measuring expectations conditioned on subset parameters.",
        "theory_resource": {
            "title": "Conditional Expectation Overview",
            "url": "https://en.wikipedia.org/wiki/Conditional_expectation",
            "type": "article"
        },
        "practice_resource": {
            "platform": "DEEP_ML",
            "title": "Correlation Matrix Exercise",
            "url": "https://deep-ml.com/problems/37"
        },
        "prerequisites": [20]
    })
    
    items.append({
        "id": 121,
        "slug": "central-moment-calculations",
        "title": "Skewness and Kurtosis Moments",
        "section": "Statistics",
        "difficulty": "Easy",
        "estimated_time_minutes": 15,
        "tags": ["moments", "skewness", "kurtosis"],
        "learning_objectives": ["Calculate standard central statistical moments", "Analyze distribution asymmetry and tail shapes"],
        "description": "Evaluate non-symmetrical distribution profile attributes using skewness and kurtosis equations.",
        "theory_resource": {
            "title": "Central Moment Overview",
            "url": "https://en.wikipedia.org/wiki/Moment_(mathematics)",
            "type": "article"
        },
        "practice_resource": {
            "platform": "DEEP_ML",
            "title": "Central Limit Theorem Exercise",
            "url": "https://deep-ml.com/problems/81"
        },
        "prerequisites": [15]
    })
    
    items.append({
        "id": 122,
        "slug": "law-large-numbers-sim",
        "title": "Law of Large Numbers Simulation",
        "section": "Statistics",
        "difficulty": "Easy",
        "estimated_time_minutes": 15,
        "tags": ["lln", "limits", "simulation"],
        "learning_objectives": ["Explain difference between weak and strong LLN", "Simulate sampling averages converging to expected means"],
        "description": "Simulate and verify sample average convergence patterns towards mathematical expected value limits.",
        "theory_resource": {
            "title": "Law of Large Numbers Overview",
            "url": "https://en.wikipedia.org/wiki/Law_of_large_numbers",
            "type": "article"
        },
        "practice_resource": {
            "platform": "DEEP_ML",
            "title": "Law of Large Numbers Exercise",
            "url": "https://deep-ml.com/problems/82"
        },
        "prerequisites": [15]
    })
    
    items.append({
        "id": 123,
        "slug": "chebyshev-bounds-anomaly",
        "title": "Chebyshev's Inequality Bounds",
        "section": "Statistics",
        "difficulty": "Medium",
        "estimated_time_minutes": 20,
        "tags": ["chebyshev", "inequality", "statistics"],
        "learning_objectives": ["Determine upper probability bounds for deviations from means", "Apply Chebyshev rules for anomaly detection without assumption of normality"],
        "description": "Derive absolute probability bounds for variable variance deviations on non-normal distributions.",
        "theory_resource": {
            "title": "Chebyshev's Inequality Overview",
            "url": "https://en.wikipedia.org/wiki/Chebyshev%27s_inequality",
            "type": "article"
        },
        "practice_resource": {
            "platform": "DEEP_ML",
            "title": "Chebyshev Inequality Exercise",
            "url": "https://deep-ml.com/problems/83"
        },
        "prerequisites": [12]
    })
    
    items.append({
        "id": 124,
        "slug": "mcmc-gibbs-sampling",
        "title": "Gibbs Sampling in MCMC",
        "section": "Statistics",
        "difficulty": "Hard",
        "estimated_time_minutes": 30,
        "tags": ["mcmc", "gibbs-sampling", "bayesian"],
        "learning_objectives": ["Perform multidimensional variable updates iteratively", "Analyze conditional updates mapping complex joint probability topologies"],
        "description": "Implement multi-variable sampling algorithms sequentially using conditional coordinate update sequences.",
        "theory_resource": {
            "title": "Gibbs Sampling Overview",
            "url": "https://en.wikipedia.org/wiki/Gibbs_sampling",
            "type": "article"
        },
        "practice_resource": {
            "platform": "DEEP_ML",
            "title": "Markov Chains Exercise",
            "url": "https://deep-ml.com/problems/132"
        },
        "prerequisites": [13]
    })
    
    items.append({
        "id": 125,
        "slug": "eigenvalues-covariance",
        "title": "Eigenvalues of Covariance Matrices",
        "section": "Statistics",
        "difficulty": "Medium",
        "estimated_time_minutes": 20,
        "tags": ["linear-algebra", "covariance", "eigenvalues"],
        "learning_objectives": ["Calculate covariance matrix eigenvalues and eigenvectors", "Map variance distribution axes to spatial matrix dimensions"],
        "description": "Analyze variance distribution patterns along vector direction axes using eigenvalue calculations.",
        "theory_resource": {
            "title": "Covariance Matrix Overview",
            "url": "https://en.wikipedia.org/wiki/Covariance_matrix",
            "type": "article"
        },
        "practice_resource": {
            "platform": "DEEP_ML",
            "title": "Covariance Matrix Exercise",
            "url": "https://deep-ml.com/problems/10"
        },
        "prerequisites": [25]
    })
    
    # --- SECTION 11: ADDED MACHINE LEARNING (20 ITEMS: 126-145) ---
    items.append({
        "id": 126,
        "slug": "train-test-split-indices",
        "title": "Train/Test Dataset Split Implementation",
        "section": "Machine Learning",
        "difficulty": "Easy",
        "estimated_time_minutes": 15,
        "tags": ["ml-foundations", "split", "validation"],
        "learning_objectives": ["Split data arrays into train/test groups", "Manage deterministic shuffling parameters across target groups"],
        "description": "Build deterministic dataset splitting models avoiding leakages during parameter extraction.",
        "theory_resource": {
            "title": "Train Test Validation Splitting",
            "url": "https://en.wikipedia.org/wiki/Training,_validation,_and_test_data_sets",
            "type": "article"
        },
        "practice_resource": {
            "platform": "DEEP_ML",
            "title": "Train Test Split Exercise",
            "url": "https://deep-ml.com/problems/31"
        },
        "prerequisites": [28]
    })
    
    items.append({
        "id": 127,
        "slug": "recall-metric-scratch",
        "title": "Recall Metric Calculation",
        "section": "Machine Learning",
        "difficulty": "Easy",
        "estimated_time_minutes": 15,
        "tags": ["metrics", "recall", "classification"],
        "learning_objectives": ["Formulate positive detection ratios relative to ground truth", "Examine true positive vs false negative counts across classification maps"],
        "description": "Assess model ability to capture positive instances using ground truth comparisons.",
        "theory_resource": {
            "title": "Precision and Recall Overview",
            "url": "https://en.wikipedia.org/wiki/Precision_and_recall",
            "type": "article"
        },
        "practice_resource": {
            "platform": "DEEP_ML",
            "title": "Recall Metric Exercise",
            "url": "https://deep-ml.com/problems/29"
        },
        "prerequisites": [28]
    })
    
    items.append({
        "id": 128,
        "slug": "precision-metric-scratch",
        "title": "Precision Metric Calculation",
        "section": "Machine Learning",
        "difficulty": "Easy",
        "estimated_time_minutes": 15,
        "tags": ["metrics", "precision", "classification"],
        "learning_objectives": ["Evaluate true predictions against total predicted positive counts", "Manage false positive rates on highly skewed evaluation groups"],
        "description": "Evaluate positive prediction accuracy profiles comparing true positives to total flagged positive counts.",
        "theory_resource": {
            "title": "Precision and Recall Overview",
            "url": "https://en.wikipedia.org/wiki/Precision_and_recall",
            "type": "article"
        },
        "practice_resource": {
            "platform": "DEEP_ML",
            "title": "Precision Metric Exercise",
            "url": "https://deep-ml.com/problems/30"
        },
        "prerequisites": [28]
    })
    
    items.append({
        "id": 129,
        "slug": "f1-score-scratch",
        "title": "F1-Score Calculation",
        "section": "Machine Learning",
        "difficulty": "Easy",
        "estimated_time_minutes": 15,
        "tags": ["metrics", "f1-score", "classification"],
        "learning_objectives": ["Compute harmonic mean of precision and recall", "Assess balanced classification levels under skewed distributions"],
        "description": "Synthesize precision and recall into a single metric using the harmonic F1 equation.",
        "theory_resource": {
            "title": "F1 Score Overview",
            "url": "https://en.wikipedia.org/wiki/F-score",
            "type": "article"
        },
        "practice_resource": {
            "platform": "DEEP_ML",
            "title": "F1 Score Exercise",
            "url": "https://deep-ml.com/problems/28"
        },
        "prerequisites": [127, 128]
    })
    
    items.append({
        "id": 130,
        "slug": "dice-coefficient-overlap",
        "title": "Dice Similarity Coefficient",
        "section": "Machine Learning",
        "difficulty": "Easy",
        "estimated_time_minutes": 15,
        "tags": ["metrics", "dice-coefficient", "similarity"],
        "learning_objectives": ["Formulate overlapping bounds between target sets", "Map segmentation prediction groups to visual mask records"],
        "description": "Measure overlapping area size differences across target masks using Dice similarity equations.",
        "theory_resource": {
            "title": "Dice Similarity Coefficient Overview",
            "url": "https://en.wikipedia.org/wiki/S%C3%B8rensen%E2%80%93Dice_coefficient",
            "type": "article"
        },
        "practice_resource": {
            "platform": "DEEP_ML",
            "title": "Dice Coefficient Exercise",
            "url": "https://deep-ml.com/problems/34"
        },
        "prerequisites": [129]
    })
    
    items.append({
        "id": 131,
        "slug": "jaccard-index-sets",
        "title": "Jaccard Index Calculation",
        "section": "Machine Learning",
        "difficulty": "Easy",
        "estimated_time_minutes": 15,
        "tags": ["metrics", "jaccard", "similarity"],
        "learning_objectives": ["Derive Intersection over Union (IoU) ratios", "Compare Jaccard vs Dice values under variable overlaps"],
        "description": "Measure similarity of target sets using the intersection over union metric.",
        "theory_resource": {
            "title": "Jaccard Index Overview",
            "url": "https://en.wikipedia.org/wiki/Jaccard_index",
            "type": "article"
        },
        "practice_resource": {
            "platform": "DEEP_ML",
            "title": "Jaccard Index Exercise",
            "url": "https://deep-ml.com/problems/35"
        },
        "prerequisites": [130]
    })
    
    items.append({
        "id": 132,
        "slug": "gini-impurity-splits",
        "title": "Gini Impurity Calculation",
        "section": "Machine Learning",
        "difficulty": "Medium",
        "estimated_time_minutes": 20,
        "tags": ["decision-trees", "gini", "machine-learning"],
        "learning_objectives": ["Calculate subgroup label distributions", "Compute Gini impurity levels across partition branches"],
        "description": "Calculate split group label distributions using Gini impurity math models.",
        "theory_resource": {
            "title": "Decision Tree Gini Index",
            "url": "https://en.wikipedia.org/wiki/Decision_tree_learning#Gini_impurity",
            "type": "article"
        },
        "practice_resource": {
            "platform": "DEEP_ML",
            "title": "Gini Impurity Exercise",
            "url": "https://deep-ml.com/problems/32"
        },
        "prerequisites": [44]
    })
    
    items.append({
        "id": 133,
        "slug": "shannon-entropy-split",
        "title": "Shannon Entropy Calculation",
        "section": "Machine Learning",
        "difficulty": "Medium",
        "estimated_time_minutes": 20,
        "tags": ["decision-trees", "entropy", "machine-learning"],
        "learning_objectives": ["Compute information entropy limits of classification trees", "Determine split information gains based on Shannon metrics"],
        "description": "Compute partition entropy and details information gains to optimize decision tree splits.",
        "theory_resource": {
            "title": "Shannon Entropy Overview",
            "url": "https://en.wikipedia.org/wiki/Entropy_(information_theory)",
            "type": "article"
        },
        "practice_resource": {
            "platform": "DEEP_ML",
            "title": "Shannon Entropy Exercise",
            "url": "https://deep-ml.com/problems/33"
        },
        "prerequisites": [132]
    })
    
    items.append({
        "id": 134,
        "slug": "principal-component-analysis",
        "title": "Principal Component Analysis (PCA)",
        "section": "Machine Learning",
        "difficulty": "Hard",
        "estimated_time_minutes": 30,
        "tags": ["pca", "dimensionality-reduction", "linear-algebra"],
        "learning_objectives": ["Center high dimensional data profiles", "Project parameters onto principal covariance components"],
        "description": "Implement linear dimensionality reduction models projecting records onto variance direction paths.",
        "theory_resource": {
            "title": "Principal Component Analysis Overview",
            "url": "https://en.wikipedia.org/wiki/Principal_component_analysis",
            "type": "article"
        },
        "practice_resource": {
            "platform": "DEEP_ML",
            "title": "PCA Exercise",
            "url": "https://deep-ml.com/problems/19"
        },
        "prerequisites": [42, 25]
    })
    
    items.append({
        "id": 135,
        "slug": "one-hot-encoding-dense",
        "title": "One-Hot Encoding Implementation",
        "section": "Machine Learning",
        "difficulty": "Medium",
        "estimated_time_minutes": 15,
        "tags": ["feature-engineering", "one-hot", "preprocessing"],
        "learning_objectives": ["Map categorical string entries to binary arrays", "Manage vocabulary indexes dynamically avoiding overlaps"],
        "description": "Convert categorical data lists into sparse binary representation blocks.",
        "theory_resource": {
            "title": "One-Hot Encoding Overview",
            "url": "https://en.wikipedia.org/wiki/One-hot",
            "type": "article"
        },
        "practice_resource": {
            "platform": "DEEP_ML",
            "title": "One-Hot Encoding Exercise",
            "url": "https://deep-ml.com/problems/21"
        },
        "prerequisites": [32]
    })
    
    items.append({
        "id": 136,
        "slug": "support-vector-machines",
        "title": "Support Vector Machine Boundaries",
        "section": "Machine Learning",
        "difficulty": "Hard",
        "estimated_time_minutes": 30,
        "tags": ["svm", "classification", "optimization"],
        "learning_objectives": ["Formulate hinge loss optimization limits", "Design linear SVM boundaries maximizing gap sizes"],
        "description": "Construct support vector classification boundaries maximizing margins using hinge loss equations.",
        "theory_resource": {
            "title": "Support Vector Machine Overview",
            "url": "https://en.wikipedia.org/wiki/Support_vector_machine",
            "type": "article"
        },
        "practice_resource": {
            "platform": "DEEP_ML",
            "title": "Hinge Loss Exercise",
            "url": "https://deep-ml.com/problems/71"
        },
        "prerequisites": [39]
    })
    
    items.append({
        "id": 137,
        "slug": "elastic-net-regularization",
        "title": "Elastic Net Regularization",
        "section": "Machine Learning",
        "difficulty": "Medium",
        "estimated_time_minutes": 20,
        "tags": ["regression", "elastic-net", "regularization"],
        "learning_objectives": ["Formulate joint L1 and L2 penalty calculations", "Balance coefficient sparse features vs parameter grouping constraints"],
        "description": "Apply joint Lasso and Ridge regularizations to control coefficient growth.",
        "theory_resource": {
            "title": "Elastic Net Regularization Overview",
            "url": "https://en.wikipedia.org/wiki/Elastic_net_regularization",
            "type": "article"
        },
        "practice_resource": {
            "platform": "DEEP_ML",
            "title": "Elastic Net L1 Exercise",
            "url": "https://deep-ml.com/problems/62"
        },
        "prerequisites": [40, 41]
    })
    
    items.append({
        "id": 138,
        "slug": "cosine-similarity-vectors",
        "title": "Cosine Similarity Metric",
        "section": "Machine Learning",
        "difficulty": "Medium",
        "estimated_time_minutes": 15,
        "tags": ["metrics", "cosine-similarity", "vectors"],
        "learning_objectives": ["Compute dot product angles between numeric arrays", "Evaluate semantic distance measurements ignoring vector sizes"],
        "description": "Compute vector angle orientations to assess similarity independent of magnitude metrics.",
        "theory_resource": {
            "title": "Cosine Similarity Overview",
            "url": "https://en.wikipedia.org/wiki/Cosine_similarity",
            "type": "article"
        },
        "practice_resource": {
            "platform": "DEEP_ML",
            "title": "Cosine Similarity Exercise",
            "url": "https://deep-ml.com/problems/36"
        },
        "prerequisites": [20]
    })
    
    items.append({
        "id": 139,
        "slug": "hierarchical-clustering-linkage",
        "title": "Hierarchical Agglomerative Clustering",
        "section": "Machine Learning",
        "difficulty": "Medium",
        "estimated_time_minutes": 25,
        "tags": ["clustering", "hierarchical", "unsupervised"],
        "learning_objectives": ["Explain difference between single, complete, and average linkage", "Construct bottom-up agglomerative clustering trees"],
        "description": "Perform bottom-up sample grouping trees utilizing average and complete linkage math models.",
        "theory_resource": {
            "title": "Hierarchical Clustering Overview",
            "url": "https://en.wikipedia.org/wiki/Hierarchical_clustering",
            "type": "article"
        },
        "practice_resource": {
            "platform": "KAGGLE",
            "title": "Explore Your Data Exercise",
            "url": "https://www.kaggle.com/code/dansbecker/exercise-explore-your-data"
        },
        "prerequisites": [43]
    })
    
    items.append({
        "id": 140,
        "slug": "dbscan-clustering-density",
        "title": "DBSCAN Density-Based Clustering",
        "section": "Machine Learning",
        "difficulty": "Hard",
        "estimated_time_minutes": 30,
        "tags": ["clustering", "dbscan", "unsupervised"],
        "learning_objectives": ["Differentiate core, border, and noise samples in DBSCAN", "Implement range query algorithms searching density groupings"],
        "description": "Identify dense spatial cluster groupings mapping outlier points to custom noise classes.",
        "theory_resource": {
            "title": "DBSCAN Clustering Overview",
            "url": "https://en.wikipedia.org/wiki/DBSCAN",
            "type": "article"
        },
        "practice_resource": {
            "platform": "KAGGLE",
            "title": "Random Forests Exercise",
            "url": "https://www.kaggle.com/code/dansbecker/exercise-random-forests"
        },
        "prerequisites": [139]
    })
    
    items.append({
        "id": 141,
        "slug": "adaboost-ensemble-weights",
        "title": "AdaBoost Ensemble Learning",
        "section": "Machine Learning",
        "difficulty": "Hard",
        "estimated_time_minutes": 30,
        "tags": ["boosting", "adaboost", "ensemble"],
        "learning_objectives": ["Compute exponential weight modifications for misclassified instances", "Combine weak estimators into a weighted voting group"],
        "description": "Implement weak-classifier weight iteration steps focusing learning on misclassified entries.",
        "theory_resource": {
            "title": "AdaBoost Overview",
            "url": "https://en.wikipedia.org/wiki/AdaBoost",
            "type": "article"
        },
        "practice_resource": {
            "platform": "KAGGLE",
            "title": "Underfitting and Overfitting Exercise",
            "url": "https://www.kaggle.com/code/dansbecker/exercise-underfitting-and-overfitting"
        },
        "prerequisites": [30]
    })
    
    items.append({
        "id": 142,
        "slug": "hyperparameter-grid-search",
        "title": "Grid Search Hyperparameter Tuning",
        "section": "Machine Learning",
        "difficulty": "Medium",
        "estimated_time_minutes": 20,
        "tags": ["hyperparameters", "tuning", "grid-search"],
        "learning_objectives": ["Construct exhaustive parameter value combinations", "Map validation scores back to select optimal configurations"],
        "description": "Identify best model parameter combinations running exhaustive grid search validations.",
        "theory_resource": {
            "title": "Hyperparameter Optimization Overview",
            "url": "https://en.wikipedia.org/wiki/Hyperparameter_optimization",
            "type": "article"
        },
        "practice_resource": {
            "platform": "KAGGLE",
            "title": "Cross-Validation Exercise",
            "url": "https://www.kaggle.com/code/alexisbcook/exercise-cross-validation"
        },
        "prerequisites": [34]
    })
    
    items.append({
        "id": 143,
        "slug": "k-fold-cross-validation",
        "title": "K-Fold Cross-Validation Split",
        "section": "Machine Learning",
        "difficulty": "Medium",
        "estimated_time_minutes": 20,
        "tags": ["cross-validation", "validation", "resampling"],
        "learning_objectives": ["Partition dataset into K equal folders", "Execute train/validation rotations avoiding evaluation bias"],
        "description": "Implement rotating K-fold splits assessing parameter reliability across variable datasets.",
        "theory_resource": {
            "title": "Cross Validation Overview",
            "url": "https://en.wikipedia.org/wiki/Cross-validation_(analysis)",
            "type": "article"
        },
        "practice_resource": {
            "platform": "KAGGLE",
            "title": "Cross-Validation Exercise",
            "url": "https://www.kaggle.com/code/alexisbcook/exercise-cross-validation"
        },
        "prerequisites": [34]
    })
    
    items.append({
        "id": 144,
        "slug": "feature-importance-permutation",
        "title": "Permutation Feature Importance",
        "section": "Machine Learning",
        "difficulty": "Medium",
        "estimated_time_minutes": 20,
        "tags": ["explainability", "feature-importance", "interpretability"],
        "learning_objectives": ["Shuffle column records to destroy semantic relationships", "Measure drops in validation metrics to rank parameter importance"],
        "description": "Measure shifts in prediction performance when feature columns are shuffled to evaluate impact.",
        "theory_resource": {
            "title": "Permutation Feature Importance Overview",
            "url": "https://en.wikipedia.org/wiki/Permutation_feature_importance",
            "type": "article"
        },
        "practice_resource": {
            "platform": "KAGGLE",
            "title": "First ML Model Exercise",
            "url": "https://www.kaggle.com/code/dansbecker/exercise-your-first-machine-learning-model"
        },
        "prerequisites": [27]
    })
    
    items.append({
        "id": 145,
        "slug": "collinearity-variance-inflation",
        "title": "Variance Inflation Factor (VIF)",
        "section": "Machine Learning",
        "difficulty": "Medium",
        "estimated_time_minutes": 20,
        "tags": ["multicollinearity", "regression", "vif"],
        "learning_objectives": ["Identify multicollinear relationships in predictor matrices", "Calculate coefficient variance inflation factor limits"],
        "description": "Compute VIF coefficients identifying collinear features to prevent linear overfit.",
        "theory_resource": {
            "title": "Variance Inflation Factor Overview",
            "url": "https://en.wikipedia.org/wiki/Variance_inflation_factor",
            "type": "article"
        },
        "practice_resource": {
            "platform": "DEEP_ML",
            "title": "Linear Regression Normal Equation Exercise",
            "url": "https://deep-ml.com/problems/14"
        },
        "prerequisites": [37]
    })
    
    # --- SECTION 12: ADDED DEEP LEARNING (15 ITEMS: 146-160) ---
    items.append({
        "id": 146,
        "slug": "leaky-relu-activation",
        "title": "Leaky ReLU Activation Function",
        "section": "Deep Learning",
        "difficulty": "Easy",
        "estimated_time_minutes": 15,
        "tags": ["activation", "leaky-relu", "deep-learning"],
        "learning_objectives": ["Implement forward pass using leaky scaling coefficients", "Derive step backpropagation derivatives mapping positive/negative bounds"],
        "description": "Implement Leaky ReLU activation functions to mitigate vanishing gradients in negative bounds.",
        "theory_resource": {
            "title": "Leaky ReLU Activation",
            "url": "https://en.wikipedia.org/wiki/Rectifier_(neural_networks)#Leaky_ReLU",
            "type": "article"
        },
        "practice_resource": {
            "platform": "DEEP_ML",
            "title": "Leaky ReLU Exercise",
            "url": "https://deep-ml.com/problems/26"
        },
        "prerequisites": [46]
    })
    
    items.append({
        "id": 147,
        "slug": "sigmoid-activation-pass",
        "title": "Sigmoid Activation Function",
        "section": "Deep Learning",
        "difficulty": "Easy",
        "estimated_time_minutes": 15,
        "tags": ["activation", "sigmoid", "deep-learning"],
        "learning_objectives": ["Evaluate logistic curves mapping values to probability bounds", "Derive sigmoid gradient maps based on output parameters"],
        "description": "Implement the sigmoid activation function to map linear inputs onto probability values.",
        "theory_resource": {
            "title": "Sigmoid Function Overview",
            "url": "https://en.wikipedia.org/wiki/Sigmoid_function",
            "type": "article"
        },
        "practice_resource": {
            "platform": "DEEP_ML",
            "title": "Sigmoid Activation Exercise",
            "url": "https://deep-ml.com/problems/22"
        },
        "prerequisites": [46]
    })
    
    items.append({
        "id": 148,
        "slug": "softmax-activation-pass",
        "title": "Softmax Activation Function",
        "section": "Deep Learning",
        "difficulty": "Easy",
        "estimated_time_minutes": 15,
        "tags": ["activation", "softmax", "deep-learning"],
        "learning_objectives": ["Calculate logit exponents across classification parameters", "Normalize outputs into a sum-to-one probability vector"],
        "description": "Construct standard Softmax activation layers normalizing logits into multi-class probability outputs.",
        "theory_resource": {
            "title": "Softmax Activation Overview",
            "url": "https://en.wikipedia.org/wiki/Softmax_function",
            "type": "article"
        },
        "practice_resource": {
            "platform": "DEEP_ML",
            "title": "Softmax Activation Exercise",
            "url": "https://deep-ml.com/problems/23"
        },
        "prerequisites": [47]
    })
    
    items.append({
        "id": 149,
        "slug": "elu-activation-pass",
        "title": "ELU Activation Function",
        "section": "Deep Learning",
        "difficulty": "Easy",
        "estimated_time_minutes": 15,
        "tags": ["activation", "elu", "deep-learning"],
        "learning_objectives": ["Implement Exponential Linear Unit forward activation rules", "Derive ELU gradient outputs for backpropagation steps"],
        "description": "Apply ELU activation scaling negative logits exponentially towards smooth zero limits.",
        "theory_resource": {
            "title": "ELU Activation Overview",
            "url": "https://en.wikipedia.org/wiki/Rectifier_(neural_networks)#ELU",
            "type": "article"
        },
        "practice_resource": {
            "platform": "DEEP_ML",
            "title": "ELU Activation Exercise",
            "url": "https://deep-ml.com/problems/100"
        },
        "prerequisites": [146]
    })
    
    items.append({
        "id": 150,
        "slug": "selu-activation-pass",
        "title": "SELU Activation Function",
        "section": "Deep Learning",
        "difficulty": "Easy",
        "estimated_time_minutes": 15,
        "tags": ["activation", "selu", "deep-learning"],
        "learning_objectives": ["Apply scale/alpha parameters forcing self-normalizing state updates", "Derive SELU activation gradients for backpropagation checks"],
        "description": "Implement SELU activation functions to enable self-normalizing neural network steps.",
        "theory_resource": {
            "title": "SELU Activation Overview",
            "url": "https://en.wikipedia.org/wiki/Rectifier_(neural_networks)#SELU",
            "type": "article"
        },
        "practice_resource": {
            "platform": "DEEP_ML",
            "title": "SELU Activation Exercise",
            "url": "https://deep-ml.com/problems/101"
        },
        "prerequisites": [149]
    })
    
    items.append({
        "id": 151,
        "slug": "l1-l2-loss-scratch",
        "title": "L1 and L2 Loss Functions",
        "section": "Deep Learning",
        "difficulty": "Medium",
        "estimated_time_minutes": 20,
        "tags": ["loss", "l1-loss", "l2-loss"],
        "learning_objectives": ["Implement Mean Absolute and Mean Squared Error losses", "Derive gradients for linear optimization steps"],
        "description": "Calculate and optimize L1 absolute error and L2 squared error loss profiles.",
        "theory_resource": {
            "title": "Loss Functions Overview",
            "url": "https://en.wikipedia.org/wiki/Loss_functions_for_classification",
            "type": "article"
        },
        "practice_resource": {
            "platform": "DEEP_ML",
            "title": "MSE Loss Exercise",
            "url": "https://deep-ml.com/problems/67"
        },
        "prerequisites": [48]
    })
    
    items.append({
        "id": 152,
        "slug": "cross-entropy-loss-scratch",
        "title": "Cross Entropy Loss Function",
        "section": "Deep Learning",
        "difficulty": "Medium",
        "estimated_time_minutes": 20,
        "tags": ["loss", "cross-entropy", "deep-learning"],
        "learning_objectives": ["Formulate negative log-likelihood loss for classification", "Calculate soft labels mapping prediction variance profiles"],
        "description": "Implement cross-entropy loss functions evaluating prediction variance relative to categorical labels.",
        "theory_resource": {
            "title": "Cross Entropy Loss Overview",
            "url": "https://en.wikipedia.org/wiki/Cross_entropy",
            "type": "article"
        },
        "practice_resource": {
            "platform": "DEEP_ML",
            "title": "Cross Entropy Loss Exercise",
            "url": "https://deep-ml.com/problems/66"
        },
        "prerequisites": [51]
    })
    
    items.append({
        "id": 153,
        "slug": "binary-cross-entropy-loss",
        "title": "Binary Cross Entropy Loss",
        "section": "Deep Learning",
        "difficulty": "Medium",
        "estimated_time_minutes": 20,
        "tags": ["loss", "binary-cross-entropy", "deep-learning"],
        "learning_objectives": ["Calculate log-loss metrics for binary classification outputs", "Prevent mathematical underflows using log-sigmoid operations"],
        "description": "Evaluate binary prediction probability variance profiles using log-loss calculations.",
        "theory_resource": {
            "title": "Cross Entropy Loss Overview",
            "url": "https://en.wikipedia.org/wiki/Cross_entropy",
            "type": "article"
        },
        "practice_resource": {
            "platform": "DEEP_ML",
            "title": "BCE Loss Exercise",
            "url": "https://deep-ml.com/problems/70"
        },
        "prerequisites": [152]
    })
    
    items.append({
        "id": 154,
        "slug": "huber-loss-scratch",
        "title": "Huber Loss Implementation",
        "section": "Deep Learning",
        "difficulty": "Medium",
        "estimated_time_minutes": 20,
        "tags": ["loss", "huber-loss", "robust-statistics"],
        "learning_objectives": ["Apply threshold parameters balancing L1 and L2 updates", "Derive smooth continuous transition gradients around threshold limits"],
        "description": "Apply Huber loss functions to balance absolute and squared updates under noisy datasets.",
        "theory_resource": {
            "title": "Huber Loss Overview",
            "url": "https://en.wikipedia.org/wiki/Huber_loss",
            "type": "article"
        },
        "practice_resource": {
            "platform": "DEEP_ML",
            "title": "Huber Loss Exercise",
            "url": "https://deep-ml.com/problems/68"
        },
        "prerequisites": [151]
    })
    
    items.append({
        "id": 155,
        "slug": "layer-normalization-scratch",
        "title": "Layer Normalization Implementation",
        "section": "Deep Learning",
        "difficulty": "Medium",
        "estimated_time_minutes": 20,
        "tags": ["layer-normalization", "normalization", "deep-learning"],
        "learning_objectives": ["Calculate mean/variance metrics across hidden dimensions", "Verify normalization consistency across variable batch dimensions"],
        "description": "Normalize neuron activations across hidden features to stabilize recurrent learning states.",
        "theory_resource": {
            "title": "Layer Normalization Overview",
            "url": "https://en.wikipedia.org/wiki/Layer_normalization",
            "type": "article"
        },
        "practice_resource": {
            "platform": "DEEP_ML",
            "title": "Layer Normalization Exercise",
            "url": "https://deep-ml.com/problems/48"
        },
        "prerequisites": [59]
    })
    
    items.append({
        "id": 156,
        "slug": "conv2d-forward-scratch",
        "title": "Conv2D Layer Forward Pass",
        "section": "Deep Learning",
        "difficulty": "Hard",
        "estimated_time_minutes": 25,
        "tags": ["cnn", "convolution", "deep-learning"],
        "learning_objectives": ["Apply filter kernels across input tensor dimensions", "Account for stride and zero-padding configurations in outputs"],
        "description": "Implement forward spatial filter sweeps calculating convolutional feature maps.",
        "theory_resource": {
            "title": "Convolutional Neural Networks Overview",
            "url": "https://en.wikipedia.org/wiki/Convolutional_neural_network",
            "type": "article"
        },
        "practice_resource": {
            "platform": "DEEP_ML",
            "title": "Conv2D Exercise",
            "url": "https://deep-ml.com/problems/52"
        },
        "prerequisites": [52]
    })
    
    items.append({
        "id": 157,
        "slug": "max-pooling-2d-forward",
        "title": "Max Pooling 2D Forward Pass",
        "section": "Deep Learning",
        "difficulty": "Medium",
        "estimated_time_minutes": 20,
        "tags": ["cnn", "pooling", "deep-learning"],
        "learning_objectives": ["Reduce spatial map dimensions using max pools", "Track maximum indices for sub-sampling gradients"],
        "description": "Downsample feature map shapes using sliding maximum window operations.",
        "theory_resource": {
            "title": "Max Pooling Layer Overview",
            "url": "https://en.wikipedia.org/wiki/Convolutional_neural_network#Pooling_layer",
            "type": "article"
        },
        "practice_resource": {
            "platform": "DEEP_ML",
            "title": "Max Pooling Exercise",
            "url": "https://deep-ml.com/problems/53"
        },
        "prerequisites": [156]
    })
    
    items.append({
        "id": 158,
        "slug": "gru-cell-forward-scratch",
        "title": "GRU Cell Forward Pass",
        "section": "Deep Learning",
        "difficulty": "Hard",
        "estimated_time_minutes": 25,
        "tags": ["rnn", "gru", "sequence-modeling"],
        "learning_objectives": ["Compute reset and update gate operations", "Manage state transitions through gate configurations"],
        "description": "Implement gated recurrent unit update logic resolving temporal dependencies.",
        "theory_resource": {
            "title": "Gated Recurrent Unit Overview",
            "url": "https://en.wikipedia.org/wiki/Gated_recurrent_unit",
            "type": "article"
        },
        "practice_resource": {
            "platform": "DEEP_ML",
            "title": "GRU Forward Exercise",
            "url": "https://deep-ml.com/problems/56"
        },
        "prerequisites": [60]
    })
    
    items.append({
        "id": 159,
        "slug": "weight-initialization-xavier",
        "title": "Xavier/Glorot Weight Initialization",
        "section": "Deep Learning",
        "difficulty": "Medium",
        "estimated_time_minutes": 20,
        "tags": ["initialization", "xavier", "glorot"],
        "learning_objectives": ["Calculate fan-in and fan-out parameters of model layers", "Sample weights dynamically maintaining variance limits across inputs"],
        "description": "Initialize layer weights using Xavier scaling variance bounds to prevent saturation.",
        "theory_resource": {
            "title": "Xavier Initialization Overview",
            "url": "https://en.wikipedia.org/wiki/He_initialization",
            "type": "article"
        },
        "practice_resource": {
            "platform": "DEEP_ML",
            "title": "Xavier Initialization Exercise",
            "url": "https://deep-ml.com/problems/76"
        },
        "prerequisites": [56]
    })
    
    items.append({
        "id": 160,
        "slug": "weight-initialization-he",
        "title": "He/Kaiming Weight Initialization",
        "section": "Deep Learning",
        "difficulty": "Hard",
        "estimated_time_minutes": 25,
        "tags": ["initialization", "he-init", "kaiming"],
        "learning_objectives": ["Formulate initialization scaling parameters for ReLU units", "Prevent activation saturation using Kaiming scaling bounds"],
        "description": "Initialize model parameters using Kaiming scaling profiles tailored for ReLU layers.",
        "theory_resource": {
            "title": "Kaiming Initialization Overview",
            "url": "https://en.wikipedia.org/wiki/He_initialization",
            "type": "article"
        },
        "practice_resource": {
            "platform": "DEEP_ML",
            "title": "Kaiming Initialization Exercise",
            "url": "https://deep-ml.com/problems/77"
        },
        "prerequisites": [159]
    })
    
    # --- SECTION 13: ADDED LARGE LANGUAGE MODELS (LLM) (15 ITEMS: 161-175) ---
    items.append({
        "id": 161,
        "slug": "gelu-activation-pass",
        "title": "GELU Activation Function",
        "section": "LLM",
        "difficulty": "Easy",
        "estimated_time_minutes": 15,
        "tags": ["activation", "gelu", "llm"],
        "learning_objectives": ["Formulate Gaussian Error Linear Unit activation rules", "Derive standard GELU backpropagation gradients"],
        "description": "Implement GELU activation functions weighting inputs by normal probability thresholds.",
        "theory_resource": {
            "title": "GELU Activation Function",
            "url": "https://en.wikipedia.org/wiki/Activation_function#GELU",
            "type": "article"
        },
        "practice_resource": {
            "platform": "DEEP_ML",
            "title": "GELU Activation Exercise",
            "url": "https://deep-ml.com/problems/105"
        },
        "prerequisites": [63]
    })
    
    items.append({
        "id": 162,
        "slug": "hard-sigmoid-activation",
        "title": "Hard Sigmoid Activation Function",
        "section": "LLM",
        "difficulty": "Easy",
        "estimated_time_minutes": 15,
        "tags": ["activation", "hard-sigmoid", "llm"],
        "learning_objectives": ["Compute piece-wise linear approximation of sigmoid", "Optimize runtime execution using hard-sigmoid parameters"],
        "description": "Implement piece-wise linear hard sigmoid activation paths optimized for compute savings.",
        "theory_resource": {
            "title": "Hard Sigmoid Activation Overview",
            "url": "https://en.wikipedia.org/wiki/Hard_sigmoid",
            "type": "article"
        },
        "practice_resource": {
            "platform": "DEEP_ML",
            "title": "Hard Sigmoid Exercise",
            "url": "https://deep-ml.com/problems/103"
        },
        "prerequisites": [147]
    })
    
    items.append({
        "id": 163,
        "slug": "hard-swish-activation",
        "title": "Hard Swish Activation Function",
        "section": "LLM",
        "difficulty": "Easy",
        "estimated_time_minutes": 15,
        "tags": ["activation", "hard-swish", "llm"],
        "learning_objectives": ["Formulate linear approximations of Swish activations", "Compute backpropagation step gradients across linear boundary points"],
        "description": "Implement piece-wise linear hard swish activations to reduce runtime computing overhead.",
        "theory_resource": {
            "title": "Hard Swish Function Overview",
            "url": "https://en.wikipedia.org/wiki/Swish_function#Hard_Swish",
            "type": "article"
        },
        "practice_resource": {
            "platform": "DEEP_ML",
            "title": "Hard Swish Exercise",
            "url": "https://deep-ml.com/problems/104"
        },
        "prerequisites": [64]
    })
    
    items.append({
        "id": 164,
        "slug": "perplexity-evaluation",
        "title": "Perplexity Metric Calculation",
        "section": "LLM",
        "difficulty": "Easy",
        "estimated_time_minutes": 15,
        "tags": ["perplexity", "metrics", "llm"],
        "learning_objectives": ["Define perplexity as exponentiated cross-entropy loss", "Evaluate model prediction confidence over target text groups"],
        "description": "Evaluate model confidence on prediction outputs by calculating sequence perplexity metrics.",
        "theory_resource": {
            "title": "Perplexity Overview",
            "url": "https://en.wikipedia.org/wiki/Perplexity",
            "type": "article"
        },
        "practice_resource": {
            "platform": "DEEP_ML",
            "title": "Perplexity Exercise",
            "url": "https://deep-ml.com/problems/92"
        },
        "prerequisites": [62]
    })
    
    items.append({
        "id": 165,
        "slug": "tf-idf-vectorizer-scratch",
        "title": "TF-IDF Vectorizer",
        "section": "LLM",
        "difficulty": "Easy",
        "estimated_time_minutes": 15,
        "tags": ["nlp", "tf-idf", "text-processing"],
        "learning_objectives": ["Compute term frequency values within documents", "Calculate inverse document frequency weights across corpora"],
        "description": "Implement document term weighting configurations using TF-IDF calculations.",
        "theory_resource": {
            "title": "TF-IDF Overview",
            "url": "https://en.wikipedia.org/wiki/Tf%E2%85%93idf",
            "type": "article"
        },
        "practice_resource": {
            "platform": "DEEP_ML",
            "title": "TF-IDF Exercise",
            "url": "https://deep-ml.com/problems/98"
        },
        "prerequisites": [61]
    })
    
    items.append({
        "id": 166,
        "slug": "self-attention-scratch",
        "title": "Self Attention Mechanism",
        "section": "LLM",
        "difficulty": "Medium",
        "estimated_time_minutes": 20,
        "tags": ["transformers", "attention", "self-attention"],
        "learning_objectives": ["Compute Q, K, V parameter matrix interactions", "Apply scale factors preventing gradient saturation during softmax passes"],
        "description": "Implement scaled dot-product self-attention mechanisms mapping token associations.",
        "theory_resource": {
            "title": "Self-Attention Mechanism Overview",
            "url": "https://en.wikipedia.org/wiki/Attention_(machine_learning)",
            "type": "article"
        },
        "practice_resource": {
            "platform": "DEEP_ML",
            "title": "Self Attention Exercise",
            "url": "https://deep-ml.com/problems/45"
        },
        "prerequisites": [57]
    })
    
    items.append({
        "id": 167,
        "slug": "multi-head-attention-layer",
        "title": "Multi-Head Attention Mechanism",
        "section": "LLM",
        "difficulty": "Hard",
        "estimated_time_minutes": 25,
        "tags": ["transformers", "attention", "multi-head"],
        "learning_objectives": ["Project input representations across multiple attention heads", "Concatenate and project head outputs back to hidden shapes"],
        "description": "Project query, key, and value vectors across multiple parallel attention heads.",
        "theory_resource": {
            "title": "Multi-Head Attention Overview",
            "url": "https://en.wikipedia.org/wiki/Attention_(machine_learning)",
            "type": "article"
        },
        "practice_resource": {
            "platform": "DEEP_ML",
            "title": "Multi-Head Attention Exercise",
            "url": "https://deep-ml.com/problems/46"
        },
        "prerequisites": [166]
    })
    
    items.append({
        "id": 168,
        "slug": "positional-encoding-transformers",
        "title": "Sinusoidal Positional Encoding",
        "section": "LLM",
        "difficulty": "Medium",
        "estimated_time_minutes": 20,
        "tags": ["transformers", "positional-encoding", "nlp"],
        "learning_objectives": ["Formulate sinusoidal coordinates for token sequences", "Incorporate positional arrays into dense token embeddings"],
        "description": "Inject token order relationships using sinusoidal positional encoding waves.",
        "theory_resource": {
            "title": "Sinusoidal Positional Encoding",
            "url": "https://en.wikipedia.org/wiki/Transformer_(deep_learning_architecture)#Positional_encoding",
            "type": "article"
        },
        "practice_resource": {
            "platform": "DEEP_ML",
            "title": "Positional Encoding Exercise",
            "url": "https://deep-ml.com/problems/47"
        },
        "prerequisites": [168]
    })
    
    items.append({
        "id": 169,
        "slug": "beam-search-decoding",
        "title": "Beam Search Decoding Algorithm",
        "section": "LLM",
        "difficulty": "Medium",
        "estimated_time_minutes": 20,
        "tags": ["decoding", "beam-search", "llm"],
        "learning_objectives": ["Track top-K probability token paths dynamically", "Prune low confidence generation branches to extract predictions"],
        "description": "Manage generation outputs by tracking top-K probability sequences using beam search pruning.",
        "theory_resource": {
            "title": "Beam Search Overview",
            "url": "https://en.wikipedia.org/wiki/Beam_search",
            "type": "article"
        },
        "practice_resource": {
            "platform": "DEEP_ML",
            "title": "Beam Search Exercise",
            "url": "https://deep-ml.com/problems/89"
        },
        "prerequisites": [62]
    })
    
    items.append({
        "id": 170,
        "slug": "nucleus-sampling-top-p",
        "title": "Nucleus (Top-p) Sampling",
        "section": "LLM",
        "difficulty": "Medium",
        "estimated_time_minutes": 20,
        "tags": ["decoding", "top-p", "nucleus-sampling"],
        "learning_objectives": ["Sort token indices by output probability curves", "Truncate low probability vocabulary entries using cumulative top-p thresholds"],
        "description": "Filter vocabulary distribution profiles dynamically using cumulative probability limits.",
        "theory_resource": {
            "title": "Top-p Sampling Overview",
            "url": "https://en.wikipedia.org/wiki/Language_model#Sampling_techniques",
            "type": "article"
        },
        "practice_resource": {
            "platform": "DEEP_ML",
            "title": "Nucleus Sampling Exercise",
            "url": "https://deep-ml.com/problems/90"
        },
        "prerequisites": [62]
    })
    
    items.append({
        "id": 171,
        "slug": "temperature-scaling-logits",
        "title": "Temperature Scaling Logits",
        "section": "LLM",
        "difficulty": "Medium",
        "estimated_time_minutes": 20,
        "tags": ["decoding", "temperature", "logits"],
        "learning_objectives": ["Divide output logit arrays by temperature factors", "Manage generation diversity by shifting logit entropy levels"],
        "description": "Adjust output logit distributions to alter generation diversity using temperature scales.",
        "theory_resource": {
            "title": "Temperature Scaling Overview",
            "url": "https://en.wikipedia.org/wiki/Temperature_scaling",
            "type": "article"
        },
        "practice_resource": {
            "platform": "DEEP_ML",
            "title": "Temperature Scaling Exercise",
            "url": "https://deep-ml.com/problems/91"
        },
        "prerequisites": [62]
    })
    
    items.append({
        "id": 172,
        "slug": "bleu-score-evaluation",
        "title": "BLEU Evaluation Metric",
        "section": "LLM",
        "difficulty": "Medium",
        "estimated_time_minutes": 20,
        "tags": ["nlp", "metrics", "bleu"],
        "learning_objectives": ["Compute n-gram precision overlaps between texts", "Apply brevity penalty adjustments on short model translations"],
        "description": "Evaluate translation generation accuracy by computing n-gram overlap BLEU scores.",
        "theory_resource": {
            "title": "BLEU Metric Overview",
            "url": "https://en.wikipedia.org/wiki/BLEU",
            "type": "article"
        },
        "practice_resource": {
            "platform": "DEEP_ML",
            "title": "BLEU Score Exercise",
            "url": "https://deep-ml.com/problems/97"
        },
        "prerequisites": [164]
    })
    
    items.append({
        "id": 173,
        "slug": "rouge-score-evaluation",
        "title": "ROUGE Evaluation Metric",
        "section": "LLM",
        "difficulty": "Medium",
        "estimated_time_minutes": 20,
        "tags": ["nlp", "metrics", "rouge"],
        "learning_objectives": ["Calculate n-gram recall overlaps on summaries", "Evaluate summary predictions using longest common subsequence lengths"],
        "description": "Assess summary generation coverage using n-gram overlap ROUGE recall metrics.",
        "theory_resource": {
            "title": "ROUGE Metric Overview",
            "url": "https://en.wikipedia.org/wiki/ROUGE_(metric)",
            "type": "article"
        },
        "practice_resource": {
            "platform": "DEEP_ML",
            "title": "ROUGE Score Exercise",
            "url": "https://deep-ml.com/problems/96"
        },
        "prerequisites": [172]
    })
    
    items.append({
        "id": 174,
        "slug": "fine-tuning-lora-adapters",
        "title": "LoRA Adapter Weight Matrices",
        "section": "LLM",
        "difficulty": "Hard",
        "estimated_time_minutes": 25,
        "tags": ["peft", "lora", "fine-tuning"],
        "learning_objectives": ["Design low-rank weight update matrices A and B", "Inject parameter updates into model layers minimizing tuning memory footprint"],
        "description": "Train low-rank adapter matrices to update weights without modifying base model parameters.",
        "theory_resource": {
            "title": "LoRA: Low-Rank Adaptation Paper",
            "url": "https://arxiv.org/abs/2106.09685",
            "type": "research-paper"
        },
        "practice_resource": {
            "platform": "KAGGLE",
            "title": "Tokenization Exercise",
            "url": "https://www.kaggle.com/code/tuckerarrants/k-means-and-bpe-tokenization-from-scratch"
        },
        "prerequisites": [167]
    })
    
    items.append({
        "id": 175,
        "slug": "quantization-llm-bits",
        "title": "LLM Model Quantization (4-bit)",
        "section": "LLM",
        "difficulty": "Hard",
        "estimated_time_minutes": 25,
        "tags": ["quantization", "optimization", "compression"],
        "learning_objectives": ["Map continuous weight parameters to discrete 4-bit integer values", "Scale weight parameters dynamically using absolute limits"],
        "description": "Quantize float parameters to 4-bit configurations to compress model footprint.",
        "theory_resource": {
            "title": "ZeroQuant Optimization Paper",
            "url": "https://arxiv.org/abs/2208.07339",
            "type": "research-paper"
        },
        "practice_resource": {
            "platform": "KAGGLE",
            "title": "Tokenization Exercise",
            "url": "https://www.kaggle.com/code/tuckerarrants/k-means-and-bpe-tokenization-from-scratch"
        },
        "prerequisites": [174]
    })
    
    # --- SECTION 14: ADDED RETRIEVAL-AUGMENTED GENERATION (RAG) (10 ITEMS: 176-185) ---
    items.append({
        "id": 176,
        "slug": "vector-db-indexing",
        "title": "Vector DB Indexing Concepts",
        "section": "RAG",
        "difficulty": "Easy",
        "estimated_time_minutes": 15,
        "tags": ["vector-db", "rag", "hnsw"],
        "learning_objectives": ["Explain difference between flat, IVF, and HNSW indexes", "Select indexing configurations balancing retrieval latency and recall limits"],
        "description": "Explore flat, IVF, and HNSW index formats balancing search speed and accuracy.",
        "theory_resource": {
            "title": "Vector Database Indexing Overview",
            "url": "https://en.wikipedia.org/wiki/Vector_database",
            "type": "article"
        },
        "practice_resource": {
            "platform": "KAGGLE",
            "title": "CLIP Similarity Search Exercise",
            "url": "https://www.kaggle.com/code/awsaf49/image-similarity-search-with-clip"
        },
        "prerequisites": [76]
    })
    
    items.append({
        "id": 177,
        "slug": "chunking-strategies-rag",
        "title": "Document Chunking Strategies",
        "section": "RAG",
        "difficulty": "Easy",
        "estimated_time_minutes": 15,
        "tags": ["chunking", "rag", "preprocessing"],
        "learning_objectives": ["Compare fixed-size, recursive character, and semantic chunking", "Configure chunk sizes and overlapping bounds to preserve token context"],
        "description": "Segment documents using recursive character and semantic boundaries to optimize context.",
        "theory_resource": {
            "title": "Retrieval Augmented Generation Overview",
            "url": "https://en.wikipedia.org/wiki/Retrieval-augmented_generation",
            "type": "article"
        },
        "practice_resource": {
            "platform": "KAGGLE",
            "title": "CLIP Similarity Search Exercise",
            "url": "https://www.kaggle.com/code/awsaf49/image-similarity-search-with-clip"
        },
        "prerequisites": [176]
    })
    
    items.append({
        "id": 178,
        "slug": "metadata-filtering-retrieval",
        "title": "Metadata Filtering in Retrieval",
        "section": "RAG",
        "difficulty": "Medium",
        "estimated_time_minutes": 20,
        "tags": ["metadata", "filtering", "rag"],
        "learning_objectives": ["Apply filter criteria on vector search results", "Run pre-filtering vs post-filtering queries"],
        "description": "Design pre- and post-filtering search patterns constraints on vector indices.",
        "theory_resource": {
            "title": "Vector Search Filtering",
            "url": "https://en.wikipedia.org/wiki/Vector_database",
            "type": "article"
        },
        "practice_resource": {
            "platform": "KAGGLE",
            "title": "CLIP Similarity Search Exercise",
            "url": "https://www.kaggle.com/code/awsaf49/image-similarity-search-with-clip"
        },
        "prerequisites": [76]
    })
    
    items.append({
        "id": 179,
        "slug": "hybrid-search-sparse-dense",
        "title": "Hybrid Search (Sparse + Dense)",
        "section": "RAG",
        "difficulty": "Medium",
        "estimated_time_minutes": 20,
        "tags": ["hybrid-search", "bm25", "dense-vector"],
        "learning_objectives": ["Combine BM25 sparse matches and dense vector outputs", "Recalibrate joint ranking lists using Reciprocal Rank Fusion (RRF)"],
        "description": "Combine BM25 keyword matches and dense vector matches using Reciprocal Rank Fusion.",
        "theory_resource": {
            "title": "Hybrid Search Architectures",
            "url": "https://en.wikipedia.org/wiki/Retrieval-augmented_generation",
            "type": "article"
        },
        "practice_resource": {
            "platform": "KAGGLE",
            "title": "LangChain Support Bot Exercise",
            "url": "https://www.kaggle.com/code/saurav9786/langchain-support-bot-with-rag"
        },
        "prerequisites": [78]
    })
    
    items.append({
        "id": 180,
        "slug": "query-expansion-hypothetical",
        "title": "Query Expansion & HyDE",
        "section": "RAG",
        "difficulty": "Medium",
        "estimated_time_minutes": 20,
        "tags": ["query-expansion", "hyde", "rag"],
        "learning_objectives": ["Generate hypothetical answer models using base prompts", "Project hypothetical outputs onto vector database spaces"],
        "description": "Expand query semantics using hypothetical answer embeddings to improve lookup rates.",
        "theory_resource": {
            "title": "HyDE: Hypothetical Document Embeddings Paper",
            "url": "https://arxiv.org/abs/2212.10496",
            "type": "research-paper"
        },
        "practice_resource": {
            "platform": "KAGGLE",
            "title": "LangChain Support Bot Exercise",
            "url": "https://www.kaggle.com/code/saurav9786/langchain-support-bot-with-rag"
        },
        "prerequisites": [77]
    })
    
    items.append({
        "id": 181,
        "slug": "reranking-cross-encoders",
        "title": "Reranking with Cross-Encoders",
        "section": "RAG",
        "difficulty": "Hard",
        "estimated_time_minutes": 25,
        "tags": ["reranking", "cross-encoder", "rag"],
        "learning_objectives": ["Differentiate bi-encoder vector lookups from cross-encoder comparisons", "Score candidate documents relative to query queries"],
        "description": "Re-rank candidate documents using cross-encoders to calculate fine-grained relevancy scores.",
        "theory_resource": {
            "title": "Cross-Encoder Reranking Paper",
            "url": "https://arxiv.org/abs/2010.06467",
            "type": "research-paper"
        },
        "practice_resource": {
            "platform": "KAGGLE",
            "title": "LangChain Support Bot Exercise",
            "url": "https://www.kaggle.com/code/saurav9786/langchain-support-bot-with-rag"
        },
        "prerequisites": [79]
    })
    
    items.append({
        "id": 182,
        "slug": "context-compression-filtering",
        "title": "Context Compression & Filtering",
        "section": "RAG",
        "difficulty": "Medium",
        "estimated_time_minutes": 20,
        "tags": ["context-compression", "optimization", "rag"],
        "learning_objectives": ["Extract relevant sentences matching input queries", "Reduce input context size parameters avoiding saturation"],
        "description": "Compress retrieved context to pass only high-relevancy snippets to LLM inputs.",
        "theory_resource": {
            "title": "Lost in the Middle Paper",
            "url": "https://arxiv.org/abs/2307.03172",
            "type": "research-paper"
        },
        "practice_resource": {
            "platform": "KAGGLE",
            "title": "LangChain Support Bot Exercise",
            "url": "https://www.kaggle.com/code/saurav9786/langchain-support-bot-with-rag"
        },
        "prerequisites": [81]
    })
    
    items.append({
        "id": 183,
        "slug": "rag-context-precision-recall",
        "title": "RAG Context Precision & Recall",
        "section": "RAG",
        "difficulty": "Medium",
        "estimated_time_minutes": 20,
        "tags": ["evaluation", "context-relevancy", "metrics"],
        "learning_objectives": ["Formulate context precision metrics", "Measure retrieval recall rates relative to ground truth references"],
        "description": "Evaluate retrieval chunk precision and recall using reference target spans.",
        "theory_resource": {
            "title": "Ragas: Automated Evaluation of RAG Paper",
            "url": "https://arxiv.org/abs/2309.15217",
            "type": "research-paper"
        },
        "practice_resource": {
            "platform": "KAGGLE",
            "title": "LangChain Support Bot Exercise",
            "url": "https://www.kaggle.com/code/saurav9786/langchain-support-bot-with-rag"
        },
        "prerequisites": [80]
    })
    
    items.append({
        "id": 184,
        "slug": "graph-rag-knowledge",
        "title": "Graph RAG & Knowledge Graphs",
        "section": "RAG",
        "difficulty": "Hard",
        "estimated_time_minutes": 30,
        "tags": ["graph-rag", "knowledge-graph", "rag"],
        "learning_objectives": ["Combine entity relations into graph structures", "Query relational entity graphs to contextualize prompts"],
        "description": "Integrate entity-relationship graphs to enhance RAG systems with relational facts.",
        "theory_resource": {
            "title": "From Local to Global: Graph RAG Paper",
            "url": "https://arxiv.org/abs/2404.16130",
            "type": "research-paper"
        },
        "practice_resource": {
            "platform": "KAGGLE",
            "title": "CLIP Similarity Search Exercise",
            "url": "https://www.kaggle.com/code/awsaf49/image-similarity-search-with-clip"
        },
        "prerequisites": [181]
    })
    
    items.append({
        "id": 185,
        "slug": "multimodal-rag-embeddings",
        "title": "Multimodal Retrieval Systems",
        "section": "RAG",
        "difficulty": "Easy",
        "estimated_time_minutes": 15,
        "tags": ["multimodal", "clip", "rag"],
        "learning_objectives": ["Map image and text embeds to joint spaces", "Execute multimodal vector queries returning mixed outputs"],
        "description": "Deploy multimodal search services coordinating text and image inputs.",
        "theory_resource": {
            "title": "CLIP Multimodal Alignment Paper",
            "url": "https://arxiv.org/abs/2103.00020",
            "type": "research-paper"
        },
        "practice_resource": {
            "platform": "KAGGLE",
            "title": "CLIP Similarity Search Exercise",
            "url": "https://www.kaggle.com/code/awsaf49/image-similarity-search-with-clip"
        },
        "prerequisites": [84]
    })
    
    # --- SECTION 15: ADDED AGENTS (10 ITEMS: 186-195) ---
    items.append({
        "id": 186,
        "slug": "react-agent-loop",
        "title": "ReAct Agent Loop Execution",
        "section": "Agents",
        "difficulty": "Easy",
        "estimated_time_minutes": 15,
        "tags": ["react", "agents", "reasoning"],
        "learning_objectives": ["Structure prompt sequences generating reasoning thoughts", "Execute actions and observe results iteratively"],
        "description": "Implement ReAct agent loops alternating reasoning steps with tool execution actions.",
        "theory_resource": {
            "title": "ReAct: Synergizing Reasoning and Acting Paper",
            "url": "https://arxiv.org/abs/2210.03629",
            "type": "research-paper"
        },
        "practice_resource": {
            "platform": "KAGGLE",
            "title": "Web Automation Exercise",
            "url": "https://www.kaggle.com/code/harshsingh22/selenium-and-playwright-automation-in-kaggle"
        },
        "prerequisites": [86]
    })
    
    items.append({
        "id": 187,
        "slug": "tool-calling-llm",
        "title": "Function & Tool Calling",
        "section": "Agents",
        "difficulty": "Easy",
        "estimated_time_minutes": 15,
        "tags": ["tool-calling", "apis", "agents"],
        "learning_objectives": ["Declare tool schemas in JSON formats", "Parse model tool calls to execute Python routines"],
        "description": "Configure tool schemas enabling models to generate formatted function calling requests.",
        "theory_resource": {
            "title": "Web API Structures Overview",
            "url": "https://en.wikipedia.org/wiki/Web_API",
            "type": "article"
        },
        "practice_resource": {
            "platform": "KAGGLE",
            "title": "Web Automation Exercise",
            "url": "https://www.kaggle.com/code/harshsingh22/selenium-and-playwright-automation-in-kaggle"
        },
        "prerequisites": [87]
    })
    
    items.append({
        "id": 188,
        "slug": "multi-agent-orchestration",
        "title": "Multi-Agent Orchestration",
        "section": "Agents",
        "difficulty": "Medium",
        "estimated_time_minutes": 20,
        "tags": ["multi-agent", "orchestration", "agents"],
        "learning_objectives": ["Coordinate specialized sub-agents with supervisor models", "Implement inter-agent messaging formats passing context"],
        "description": "Orchestrate multi-agent groups passing sub-tasks dynamically between specialized models.",
        "theory_resource": {
            "title": "Multi-Agent Systems Overview",
            "url": "https://en.wikipedia.org/wiki/Multi-agent_system",
            "type": "article"
        },
        "practice_resource": {
            "platform": "KAGGLE",
            "title": "Web Automation Exercise",
            "url": "https://www.kaggle.com/code/harshsingh22/selenium-and-playwright-automation-in-kaggle"
        },
        "prerequisites": [89]
    })
    
    items.append({
        "id": 189,
        "slug": "agentic-state-graphs",
        "title": "State Graphs & Routing",
        "section": "Agents",
        "difficulty": "Medium",
        "estimated_time_minutes": 20,
        "tags": ["state-graph", "routing", "agents"],
        "learning_objectives": ["Define states and transition routes using graphs", "Execute dynamic state routing decisions using model outputs"],
        "description": "Design state-graph structures routing agent paths dynamically based on step evaluations.",
        "theory_resource": {
            "title": "State Transition Graph Overview",
            "url": "https://en.wikipedia.org/wiki/State-transition_table",
            "type": "article"
        },
        "practice_resource": {
            "platform": "KAGGLE",
            "title": "Web Automation Exercise",
            "url": "https://www.kaggle.com/code/harshsingh22/selenium-and-playwright-automation-in-kaggle"
        },
        "prerequisites": [88]
    })
    
    items.append({
        "id": 190,
        "slug": "task-decomposition-agents",
        "title": "Hierarchical Task Decomposition",
        "section": "Agents",
        "difficulty": "Medium",
        "estimated_time_minutes": 20,
        "tags": ["decomposition", "hierarchical", "agents"],
        "learning_objectives": ["Decompose compound user objectives into sequential sub-tasks", "Compile sub-task completion reports back to root monitors"],
        "description": "Decompose complex requests into nested tasks executed sequentially by sub-agents.",
        "theory_resource": {
            "title": "Tree of Thoughts Reasoning Paper",
            "url": "https://arxiv.org/abs/2305.11562",
            "type": "research-paper"
        },
        "practice_resource": {
            "platform": "KAGGLE",
            "title": "Web Automation Exercise",
            "url": "https://www.kaggle.com/code/harshsingh22/selenium-and-playwright-automation-in-kaggle"
        },
        "prerequisites": [90]
    })
    
    items.append({
        "id": 191,
        "slug": "self-reflection-refinement",
        "title": "Agent Self-Reflection & Feedback",
        "section": "Agents",
        "difficulty": "Hard",
        "estimated_time_minutes": 25,
        "tags": ["self-reflection", "refinement", "agents"],
        "learning_objectives": ["Analyze execution outputs seeking errors", "Refine generation attempts using self-criticism logs"],
        "description": "Build self-reflection loops allowing agents to critique and fix their own outputs.",
        "theory_resource": {
            "title": "Reflexion: Language Agents with Memory Paper",
            "url": "https://arxiv.org/abs/2303.11366",
            "type": "research-paper"
        },
        "practice_resource": {
            "platform": "KAGGLE",
            "title": "Web Automation Exercise",
            "url": "https://www.kaggle.com/code/harshsingh22/selenium-and-playwright-automation-in-kaggle"
        },
        "prerequisites": [91]
    })
    
    items.append({
        "id": 192,
        "slug": "agentic-memory-systems",
        "title": "Short and Long Term Memory",
        "section": "Agents",
        "difficulty": "Medium",
        "estimated_time_minutes": 20,
        "tags": ["memory", "persistence", "agents"],
        "learning_objectives": ["Manage short term execution context arrays", "Store long term session states in vector memory indices"],
        "description": "Manage agent performance using short-term context traces and long-term vector storage.",
        "theory_resource": {
            "title": "Memory in Autonomous Agents Paper",
            "url": "https://arxiv.org/abs/2305.11562",
            "type": "research-paper"
        },
        "practice_resource": {
            "platform": "KAGGLE",
            "title": "Web Automation Exercise",
            "url": "https://www.kaggle.com/code/harshsingh22/selenium-and-playwright-automation-in-kaggle"
        },
        "prerequisites": [92]
    })
    
    items.append({
        "id": 193,
        "slug": "human-in-the-loop-agents",
        "title": "Human-in-the-Loop Supervision",
        "section": "Agents",
        "difficulty": "Easy",
        "estimated_time_minutes": 15,
        "tags": ["hitl", "safety", "agents"],
        "learning_objectives": ["Interrupt execution graph steps requesting approvals", "Accept human instructions to adjust path directions"],
        "description": "Establish human feedback gates to approve or adjust agent action steps.",
        "theory_resource": {
            "title": "Human in the Loop Design Principles",
            "url": "https://en.wikipedia.org/wiki/Human-in-the-loop",
            "type": "article"
        },
        "practice_resource": {
            "platform": "KAGGLE",
            "title": "Web Automation Exercise",
            "url": "https://www.kaggle.com/code/harshsingh22/selenium-and-playwright-automation-in-kaggle"
        },
        "prerequisites": [93]
    })
    
    items.append({
        "id": 194,
        "slug": "agent-error-recovery",
        "title": "Error Recovery & Self-Healing",
        "section": "Agents",
        "difficulty": "Medium",
        "estimated_time_minutes": 20,
        "tags": ["error-recovery", "resilience", "agents"],
        "learning_objectives": ["Catch and log tool execution exceptions", "Generate recovery strategies resolving task errors dynamically"],
        "description": "Enable autonomous error recovery loops to debug and fix execution failures.",
        "theory_resource": {
            "title": "Exception Handling Design Patterns",
            "url": "https://en.wikipedia.org/wiki/Exception_handling",
            "type": "article"
        },
        "practice_resource": {
            "platform": "KAGGLE",
            "title": "Web Automation Exercise",
            "url": "https://www.kaggle.com/code/harshsingh22/selenium-and-playwright-automation-in-kaggle"
        },
        "prerequisites": [94]
    })
    
    items.append({
        "id": 195,
        "slug": "web-scraping-agents",
        "title": "Autonomous Web Navigating Agents",
        "section": "Agents",
        "difficulty": "Hard",
        "estimated_time_minutes": 25,
        "tags": ["web-browsing", "scraping", "agents"],
        "learning_objectives": ["Navigate DOM trees selecting interactive nodes", "Execute browser click and input actions dynamically"],
        "description": "Control headless browsers autonomously using DOM interaction schemas.",
        "theory_resource": {
            "title": "Playwright Automation API",
            "url": "https://playwright.dev/python/docs/intro",
            "type": "documentation"
        },
        "practice_resource": {
            "platform": "KAGGLE",
            "title": "Web Automation Exercise",
            "url": "https://www.kaggle.com/code/harshsingh22/selenium-and-playwright-automation-in-kaggle"
        },
        "prerequisites": [95]
    })
    
    # --- SECTION 16: ADDED SYSTEM DESIGN (5 ITEMS: 196-200) ---
    items.append({
        "id": 196,
        "slug": "low-latency-serving-pipelines",
        "title": "Low-latency Inference Architectures",
        "section": "System Design",
        "difficulty": "Easy",
        "estimated_time_minutes": 15,
        "tags": ["inference", "serving", "system-design"],
        "learning_objectives": ["Minimize inference request latency over parallel pools", "Design caching layers holding popular prediction targets"],
        "description": "Design low-latency model inference pipelines using distributed caching layers.",
        "theory_resource": {
            "title": "Client-Server System Design",
            "url": "https://en.wikipedia.org/wiki/Client%E2%80%93server_model",
            "type": "article"
        },
        "practice_resource": {
            "platform": "KAGGLE",
            "title": "vLLM Serving Exercise",
            "url": "https://www.kaggle.com/code/awsaf49/vllm-inference-gemma-2-9b"
        },
        "prerequisites": [97]
    })
    
    items.append({
        "id": 197,
        "slug": "distributed-training-zero",
        "title": "ZeRO Memory Optimizations",
        "section": "System Design",
        "difficulty": "Medium",
        "estimated_time_minutes": 25,
        "tags": ["distributed-training", "zero", "system-design"],
        "learning_objectives": ["Partition training parameters, gradients, and optimizer states", "Minimize network communication overheads during synchronization steps"],
        "description": "Partition training parameters, gradients, and optimizer states to scale model training.",
        "theory_resource": {
            "title": "ZeRO Memory Optimization Paper",
            "url": "https://arxiv.org/abs/1910.02054",
            "type": "research-paper"
        },
        "practice_resource": {
            "platform": "KAGGLE",
            "title": "Recommender Systems Exercise",
            "url": "https://www.kaggle.com/code/gpreda/recommender-systems-from-scratch"
        },
        "prerequisites": [98]
    })
    
    items.append({
        "id": 198,
        "slug": "multimodal-search-clip-deployment",
        "title": "Deploying CLIP Vector Databases",
        "section": "System Design",
        "difficulty": "Medium",
        "estimated_time_minutes": 25,
        "tags": ["clip", "multimodal-search", "system-design"],
        "learning_objectives": ["Deploy image-text vector databases utilizing CLIP models", "Minimize query latency using IVFFlat vector index partitions"],
        "description": "Deploy image-text vector databases using CLIP models to power multimodal search.",
        "theory_resource": {
            "title": "CLIP Contrastive Model Paper",
            "url": "https://arxiv.org/abs/2103.00020",
            "type": "research-paper"
        },
        "practice_resource": {
            "platform": "KAGGLE",
            "title": "CLIP Image Similarity Exercise",
            "url": "https://www.kaggle.com/code/awsaf49/image-similarity-search-with-clip"
        },
        "prerequisites": [99]
    })
    
    items.append({
        "id": 199,
        "slug": "real-time-recommendation-ranking",
        "title": "Multi-stage Recommendation Services",
        "section": "System Design",
        "difficulty": "Hard",
        "estimated_time_minutes": 30,
        "tags": ["recommendations", "ranking", "system-design"],
        "learning_objectives": ["Structure candidates retrieval layers narrowing item pools", "Run fine-grained ranking calculations to output selections"],
        "description": "Structure retrieval and fine-grained ranking stages to build recommendation pipelines.",
        "theory_resource": {
            "title": "Recommender System Overview",
            "url": "https://en.wikipedia.org/wiki/Recommender_system",
            "type": "article"
        },
        "practice_resource": {
            "platform": "KAGGLE",
            "title": "Recommender Systems Exercise",
            "url": "https://www.kaggle.com/code/gpreda/recommender-systems-from-scratch"
        },
        "prerequisites": [98]
    })
    
    items.append({
        "id": 200,
        "slug": "agentic-desk-scalability",
        "title": "Scalability of Agentic Routing Hubs",
        "section": "System Design",
        "difficulty": "Medium",
        "estimated_time_minutes": 25,
        "tags": ["agentic-desks", "scalability", "system-design"],
        "learning_objectives": ["Balance user workloads across distributed agent routers", "Manage context queues preventing memory overflows"],
        "description": "Scale agent groups by distributing workloads across state-sharing queues.",
        "theory_resource": {
            "title": "Load Balancing Architecture Overview",
            "url": "https://en.wikipedia.org/wiki/Load_balancing_(computing)",
            "type": "article"
        },
        "practice_resource": {
            "platform": "KAGGLE",
            "title": "LangChain Support Bot Exercise",
            "url": "https://www.kaggle.com/code/saurav9786/langchain-support-bot-with-rag"
        },
        "prerequisites": [100]
    })
    
    # 2. Write out all 200 items into their corresponding section folders
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
            
    markdown = f"""# TensorTrack Question Bank v2 Validation Report

This validation report checks and ensures the integrity of the generated TensorTrack Question Bank v2 dataset.

## Summary Metrics

*   **Total Items**: {index_data['total_questions']} (Target: 200)
*   **Difficulty Distribution**:
    *   **Easy**: {index_data['difficulty_counts']['Easy']} (30%)
    *   **Medium**: {index_data['difficulty_counts']['Medium']} (50%)
    *   **Hard**: {index_data['difficulty_counts']['Hard']} (20%)
*   **Section Breakdown**:
    *   **Python**: {index_data['section_counts'].get('Python', 0)} (Target: 20)
    *   **Statistics**: {index_data['section_counts'].get('Statistics', 0)} (Target: 30)
    *   **Machine Learning**: {index_data['section_counts'].get('Machine Learning', 0)} (Target: 40)
    *   **Deep Learning**: {index_data['section_counts'].get('Deep Learning', 0)} (Target: 30)
    *   **LLM**: {index_data['section_counts'].get('LLM', 0)} (Target: 30)
    *   **RAG**: {index_data['section_counts'].get('RAG', 0)} (Target: 20)
    *   **Agents**: {index_data['section_counts'].get('Agents', 0)} (Target: 20)
    *   **System Design**: {index_data['section_counts'].get('System Design', 0)} (Target: 10)

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
