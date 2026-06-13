def get_questions():
    questions = []
    
    # Q11: Mean, Median, Mode
    questions.append({
        "id": 11,
        "slug": "mean-median-mode",
        "title": "Build a Central Tendency Outlier Tester",
        "section": "Statistics",
        "difficulty": "Easy",
        "question_type": "coding",
        "neuroforge_skill": "Mathematical Statistics",
        "estimated_time_minutes": 10,
        "tags": ["descriptive-statistics", "metrics", "data-analysis"],
        "learning_objectives": [
            "Build functions to measure outlier sensitivity on mean, median, and mode",
            "Choose correct central tendency metrics based on skewness"
        ],
        "problem_statement": "Build a python function `calculate_central_tendencies(data)` that computes the mean, median, and mode of a list. Then, write code that programmatically appends a massive outlier to the dataset and calculates the exact percentage shift for all three metrics to verify their sensitivity to noise.",
        "real_world_context": "When evaluating model response latencies, using average latency can be misleading due to cold starts or network timeouts. Median latency (p50) and p99 are more representative of the user experience.",
        "hints": [
            "Mean is the sum divided by the count; it is highly affected by large numbers.",
            "Median is the middle value of sorted data; it is resistant to extreme values.",
            "Use `statistics.mean`, `statistics.median`, and `statistics.mode` or build them from scratch."
        ],
        "solution": {
            "explanation": "The mean aggregates all data points, so a single outlier shifts it proportional to the outlier magnitude. The median is position-based; adding one outlier shifts it at most by one position in the sorted list, meaning the change is negligible. The mode is frequency-based and remains unchanged unless the outlier creates a new highest-frequency bucket.",
            "key_takeaways": [
                "Mean is sensitive to outliers and skewness.",
                "Median is a robust estimator of central tendency for skewed distributions.",
                "Mode is useful for categorical data but can be unstable for continuous datasets."
            ]
        },
        "starter_code": {
            "python": "import statistics\n\ndef calculate_central_tendencies(data):\n    # TODO: Calculate mean, median, mode, append an outlier (1000 * max(data)),\n    # and return a dict of percentage shifts: {'mean_shift': ..., 'median_shift': ..., 'mode_shift': ...}\n    pass"
        },
        "expected_output": "A dictionary showing the calculated percentage shifts.",
        "follow_up_questions": [
            "Under what distribution shape will the mean, median, and mode be exactly equal?",
            "For a right-skewed distribution, what is the typical inequality relationship between mean, median, and mode?"
        ],
        "references": [
            {
                "title": "Descriptive Statistics Guide",
                "url": "https://openstax.org/books/introductory-statistics/pages/2-5-skewness-and-the-mean-median-and-mode"
            }
        ]
    })
    
    # Q12: Probability Rules
    questions.append({
        "id": 12,
        "slug": "probability-rules",
        "title": "Build a Variable Independence Verifier",
        "section": "Statistics",
        "difficulty": "Easy",
        "question_type": "coding",
        "neuroforge_skill": "Mathematical Statistics",
        "estimated_time_minutes": 10,
        "tags": ["probability", "conditional-probability", "foundations"],
        "learning_objectives": [
            "Compute joint and conditional probabilities from contingency parameters",
            "Verify mathematical independence of random events"
        ],
        "problem_statement": "Build a python function `verify_independence(p_mobile, p_purchase, p_joint)` that computes the conditional probability `P(Purchase | Mobile)` and determines mathematically whether visiting from a mobile device and making a purchase are independent events.",
        "real_world_context": "A/B testing and user segmentation models rely on joint and conditional probabilities to evaluate whether specific cohorts are more likely to perform conversion actions.",
        "hints": [
            "The formula for conditional probability is P(A|B) = P(A and B) / P(B).",
            "Two events are independent if and only if P(A and B) = P(A) * P(B) or equivalently P(A|B) = P(A)."
        ],
        "solution": {
            "explanation": "Using the conditional probability formula, we get P(Purchase | Mobile) = P(Mobile and Purchase) / P(Mobile) = 0.09 / 0.60 = 0.15. To check for independence: P(Mobile) * P(Purchase) = 0.60 * 0.15 = 0.09. Since P(Mobile and Purchase) = P(Mobile) * P(Purchase) = 0.09, the events are independent.",
            "key_takeaways": [
                "Conditional probability measures the probability of an event given another event occurred.",
                "Independence requires the joint probability to be the product of marginal probabilities."
            ]
        },
        "starter_code": {
            "python": "def verify_independence(p_mobile, p_purchase, p_joint):\n    # TODO: Calculate P(Purchase | Mobile) and check if events are independent\n    p_cond = 0.0\n    is_independent = False\n    return p_cond, is_independent"
        },
        "expected_output": "(0.15, True)",
        "follow_up_questions": [
            "If P(A and B) = 0, does that mean A and B are independent? What is the correct term for this relationship?",
            "How does conditional probability relate to the joint probability distribution?"
        ],
        "references": [
            {
                "title": "Introduction to Probability (MIT)",
                "url": "https://ocw.mit.edu/courses/6-041-probabilistic-systems-analysis-and-applied-probability-fall-2010/"
            }
        ]
    })

    # Q13: Bayes Theorem
    questions.append({
        "id": 13,
        "slug": "bayes-theorem",
        "title": "Build a Bayesian Diagnostic Classifier",
        "section": "Statistics",
        "difficulty": "Easy",
        "question_type": "coding",
        "neuroforge_skill": "Mathematical Statistics",
        "estimated_time_minutes": 15,
        "tags": ["bayes-theorem", "probability", "conditional-probability"],
        "learning_objectives": [
            "Apply Bayes' Theorem to calculate posterior probabilities",
            "Identify the base rate fallacy in diagnostic systems"
        ],
        "problem_statement": "Build a python function `calculate_posterior_clean(sensitivity, specificity, prior_malware)` that applies Bayes' Theorem to calculate the posterior probability that a file flagged as malware by an AI classifier is actually clean. Use this to prove the base rate fallacy.",
        "real_world_context": "In spam filters or intrusion detection systems, even a highly accurate model can produce a large volume of false alarms if the event being flagged is extremely rare (low prior probability).",
        "hints": [
            "Sensitivity = P(Flagged | Malware) = 0.99. Specificity = P(Not Flagged | Clean) = 0.98.",
            "Prior P(Malware) = 0.005. P(Clean) = 0.995.",
            "Bayes' Theorem: P(Malware | Flagged) = [P(Flagged | Malware) * P(Malware)] / [P(Flagged | Malware) * P(Malware) + P(Flagged | Clean) * P(Clean)]."
        ],
        "solution": {
            "explanation": "P(Flagged | Clean) = 1 - Specificity = 1 - 0.98 = 0.02. The total probability of a file being flagged is P(Flagged) = P(Flagged|Malware)*P(Malware) + P(Flagged|Clean)*P(Clean) = (0.99 * 0.005) + (0.02 * 0.995) = 0.02485. Thus, P(Malware | Flagged) = 0.00495 / 0.02485 = 0.1992 (approx 19.9%). The probability that a flagged file is actually clean is P(Clean | Flagged) = 1 - 0.1992 = 0.8008 (approx 80.1%). This is due to the base rate fallacy: because clean files are so abundant, even a low 2% false positive rate yields more false alarms than true detections.",
            "key_takeaways": [
                "Bayes' Theorem updates prior beliefs with new evidence.",
                "Low prior probability (base rate) heavily dominates posterior results, leading to high false-alarm rates."
            ]
        },
        "starter_code": {
            "python": "def calculate_posterior_clean(sensitivity, specificity, prior_malware):\n    # TODO: Apply Bayes' Theorem to find P(Clean | Flagged)\n    pass"
        },
        "expected_output": "0.8008048289738431",
        "follow_up_questions": [
            "How does increasing the prior probability of malware affect the false alarm rate?",
            "What parameter (sensitivity or specificity) must you optimize to reduce false alarms?"
        ],
        "references": [
            {
                "title": "Bayes' Theorem and Base Rate Fallacy",
                "url": "https://wikipedia.org/wiki/Base_rate_fallacy"
            }
        ]
    })

    # Q14: Discrete vs Continuous Distributions
    questions.append({
        "id": 14,
        "slug": "discrete-vs-continuous-distributions",
        "title": "Build a Numerical PDF Integrator",
        "section": "Statistics",
        "difficulty": "Easy",
        "question_type": "coding",
        "neuroforge_skill": "Mathematical Statistics",
        "estimated_time_minutes": 10,
        "tags": ["probability-distributions", "binomial", "normal"],
        "learning_objectives": [
            "Build a trapezoidal integration solver for continuous density functions",
            "Explain why the probability of a continuous variable taking a specific single value is zero"
        ],
        "problem_statement": "Build a python function `integrate_normal_pdf(lower, upper, steps)` that performs numerical integration of the standard normal PDF using the trapezoidal rule. Verify that the integral of the PDF over a wide range converges to approximately 1.0.",
        "real_world_context": "We model LLM output token counts (integers) using discrete distributions (like Poisson/Binomial), but we model token generation latencies (floats) using continuous distributions (like Gamma/Normal).",
        "hints": [
            "For continuous variables, the probability of any single exact value (like 1.0000000...) is zero because there are infinite possible values.",
            "The probability for continuous distributions is represented by the area under the PDF curve (integration).",
            "Trapezoidal rule formula: `area = dx * (0.5 * f(x0) + f(x1) + ... + f(xn-1) + 0.5 * f(xn))` where `dx = (upper - lower) / steps`."
        ],
        "solution": {
            "explanation": "Discrete distributions map values directly to probabilities using a PMF (e.g. P(X=k)). Continuous distributions map values to densities using a PDF. Because the sample space is uncountably infinite, the probability of hitting a exact single point is 0. Instead, probability is computed as the integral of the PDF over an interval. Integrating the standard normal PDF `1 / sqrt(2*pi) * exp(-x^2 / 2)` from -5 to 5 yields approximately 1.0.",
            "key_takeaways": [
                "PMF values are probabilities; PDF values are probability densities.",
                "Continuous probability is calculated over intervals, not single points."
            ]
        },
        "starter_code": {
            "python": "import math\n\ndef normal_pdf(x):\n    return (1 / math.sqrt(2 * math.pi)) * math.exp(-0.5 * x**2)\n\ndef integrate_normal_pdf(lower, upper, steps=1000):\n    # TODO: Build trapezoidal numerical integration of normal_pdf\n    pass"
        },
        "expected_output": "Approximately 1.0 (e.g., 0.9999...) when integrated between -5 and 5.",
        "follow_up_questions": [
            "What is the Cumulative Distribution Function (CDF) and how does it relate to PMFs and PDFs?",
            "What distribution would you use to model the number of queries arriving at a server per second?"
        ],
        "references": [
            {
                "title": "Continuous Probability Distributions (MIT)",
                "url": "https://ocw.mit.edu/courses/18-05-introduction-to-probability-and-statistics-spring-2014/"
            }
        ]
    })

    # Q15: Central Limit Theorem
    questions.append({
        "id": 15,
        "slug": "central-limit-theorem",
        "title": "Build a CLT Simulation Engine",
        "section": "Statistics",
        "difficulty": "Easy",
        "question_type": "coding",
        "neuroforge_skill": "Mathematical Statistics",
        "estimated_time_minutes": 15,
        "tags": ["sampling-distributions", "clt", "simulation"],
        "learning_objectives": [
            "Build a CLT simulation that samples non-normal distributions",
            "Verify standard error scaling mathematically against theoretical values"
        ],
        "problem_statement": "Build a python function `simulate_clt(population, sample_size, num_samples)` that takes a non-normal population, draws random samples of size `sample_size`, and computes their means. Return the standard deviation of these sample means and prove it matches the theoretical Standard Error: `sigma / sqrt(n)`.",
        "real_world_context": "The CLT is the reason why we can construct confidence intervals and run hypothesis tests on user conversion rates, even though individual conversion outcomes are binary (Bernoulli) rather than normally distributed.",
        "hints": [
            "Compute the population standard deviation `sigma`.",
            "The standard deviation of the sample means is the empirical Standard Error.",
            "As `sample_size` (n) increases, the Standard Error decreases, meaning the sample means cluster closer to the true population mean."
        ],
        "solution": {
            "explanation": "The Central Limit Theorem (CLT) states that the distribution of sample means will approximate a normal distribution as the sample size becomes large (typically n >= 30), regardless of the shape of the parent population. The mean of this sampling distribution equals the population mean, and its standard deviation (Standard Error) is equal to `sigma / sqrt(n)`, illustrating that larger sample sizes yield more precise estimates.",
            "key_takeaways": [
                "The distribution of sample means converges to normality as sample size increases.",
                "Standard Error decreases with the square root of the sample size."
            ]
        },
        "starter_code": {
            "python": "import random\nimport math\n\ndef simulate_clt(population, sample_size, num_samples):\n    # population: list of floats representing the parent population\n    # TODO: Draw samples with replacement, compute means, and return (empirical_se, theoretical_se)\n    pass"
        },
        "expected_output": "A tuple of floats representing (empirical_se, theoretical_se).",
        "follow_up_questions": [
            "Does the CLT apply to the distribution of sample medians? Why or why not?",
            "What sample size is commonly recommended as a minimum threshold for the CLT to take effect?"
        ],
        "references": [
            {
                "title": "Central Limit Theorem Visualized",
                "url": "https://wikipedia.org/wiki/Central_limit_theorem"
            }
        ]
    })

    # Q16: Hypothesis Testing & P-Values
    questions.append({
        "id": 16,
        "slug": "hypothesis-testing-p-values",
        "title": "Build a Two-Proportion Z-Test Evaluator",
        "section": "Statistics",
        "difficulty": "Medium",
        "question_type": "coding",
        "neuroforge_skill": "Mathematical Statistics",
        "estimated_time_minutes": 15,
        "tags": ["hypothesis-testing", "p-values", "a-b-testing"],
        "learning_objectives": [
            "Build a two-proportion z-test calculator from scratch",
            "Define and calculate p-values under the null hypothesis"
        ],
        "problem_statement": "Build a python function `two_proportion_z_test(successes_a, trials_a, successes_b, trials_b)` that computes the pooled proportion, the z-statistic, and the corresponding two-tailed p-value for an A/B testing conversion layout comparison.",
        "real_world_context": "A/B testing is the standard way tech companies release updates. Misinterpreting p-values can lead to rolling out features that don't actually improve metrics, wasting engineering resources.",
        "hints": [
            "The null hypothesis (H0) assumes there is no difference between group A and group B.",
            "Formula for z-statistic in two-proportion test: z = (p1 - p2) / sqrt(p_pool * (1 - p_pool) * (1/n1 + 1/n2)), where p_pool is total successes divided by total trials.",
            "Use `scipy.stats.norm.cdf` to find the two-tailed probability: `2 * (1 - norm.cdf(abs(z)))`."
        ],
        "solution": {
            "explanation": "The null hypothesis H0 is that the prompt layouts A and B produce identical conversion rates. A p-value of 0.03 means there is a 3% chance of observing a conversion difference at least as large as the one measured if there was actually no real difference between the layouts. It does NOT mean there is a 97% chance that B is better than A. The proportions are pooled to calculate the standard error of the null distribution, and a z-score is calculated and mapped to a standard normal CDF to find the two-tailed probability.",
            "key_takeaways": [
                "Null hypothesis assumes zero effect or difference.",
                "P-value is a conditional probability: P(Data or more extreme | H0 is true). It is not the probability that the hypothesis is true."
            ]
        },
        "starter_code": {
            "python": "import math\nfrom scipy.stats import norm\n\ndef two_proportion_z_test(successes_a, trials_a, successes_b, trials_b):\n    # TODO: Calculate pooled proportion, z-statistic, and two-tailed p-value\n    p_value = 0.0\n    return p_value"
        },
        "expected_output": "The calculated two-tailed p-value.",
        "follow_up_questions": [
            "If you run an A/B test with alpha=0.05 and the p-value is 0.06, can you conclude the layouts are identical?",
            "How does sample size affect the likelihood of getting a statistically significant p-value?"
        ],
        "references": [
            {
                "title": "ASA Statement on P-Values",
                "url": "https://www.tandfonline.com/doi/full/10.1080/00031305.2016.1154108"
            }
        ]
    })

    # Q17: Type I and Type II Errors
    questions.append({
        "id": 17,
        "slug": "type-i-and-type-ii-errors",
        "title": "Build a Statistical Power Calculator",
        "section": "Statistics",
        "difficulty": "Medium",
        "question_type": "coding",
        "neuroforge_skill": "Mathematical Statistics",
        "estimated_time_minutes": 15,
        "tags": ["hypothesis-testing", "power-analysis", "a-b-testing"],
        "learning_objectives": [
            "Build a function that calculates Type II error (beta)",
            "Identify the relationship between statistical power, sample size, and effect size"
        ],
        "problem_statement": "Build a python function `calculate_type_ii_error(mean_a, mean_b, std_dev, n, alpha)` that computes the Type II error rate (beta) for a one-tailed z-test comparing two means, and explain how to increase the power of the test.",
        "real_world_context": "If your A/B test is underpowered (low sample size), you will fail to detect small but highly profitable conversion improvements (a false negative / Type II error).",
        "hints": [
            "Type I error (alpha) is rejecting H0 when H0 is true (False Positive).",
            "Type II error (beta) is failing to reject H0 when H0 is false (False Negative).",
            "To calculate beta: Find the critical value threshold under the null distribution, then calculate the probability of falling below this threshold under the alternative distribution."
        ],
        "solution": {
            "explanation": "To find the Type II error rate (beta), we first locate the critical value on the null distribution: `crit = mean_a + z_crit * (std_dev / sqrt(n))` where `z_crit` corresponds to `1 - alpha`. Then, we determine the probability of obtaining a sample mean below this critical value under the alternative distribution centered at `mean_b`. This probability is `beta = P(X < crit | Mean = mean_b)`. The power of the test is `1 - beta`. Power increases with larger sample sizes, larger expected effect sizes (difference in means), or by accepting a higher Type I error rate (larger alpha).",
            "key_takeaways": [
                "Type I error is a False Positive; Type II error is a False Negative.",
                "Power (1 - beta) is the ability of a test to detect an actual effect when it exists."
            ]
        },
        "starter_code": {
            "python": "import math\nfrom scipy.stats import norm\n\ndef calculate_type_ii_error(mean_a, mean_b, std_dev, n, alpha=0.05):\n    # Assumes mean_b > mean_a, one-tailed test\n    # TODO: Calculate beta (probability of committing a Type II error)\n    beta = 0.0\n    return beta"
        },
        "expected_output": "The computed value of beta (e.g. between 0 and 1).",
        "follow_up_questions": [
            "What is the industry standard target value for statistical power in A/B testing?",
            "Why is it bad practice to continuously check p-values and stop an A/B test early?"
        ],
        "references": [
            {
                "title": "Understanding Statistical Power",
                "url": "https://wikipedia.org/wiki/Power_of_a_test"
            }
        ]
    })

    # Q18: Z-Score vs T-Score
    questions.append({
        "id": 18,
        "slug": "z-score-vs-t-score",
        "title": "Build a Critical Value Lookup Engine",
        "section": "Statistics",
        "difficulty": "Medium",
        "question_type": "coding",
        "neuroforge_skill": "Mathematical Statistics",
        "estimated_time_minutes": 15,
        "tags": ["z-score", "t-distribution", "inference"],
        "learning_objectives": [
            "Build functions to fetch critical values for Z and T distributions",
            "Contrast Z and T confidence interval boundaries at various sample sizes"
        ],
        "problem_statement": "Build a python function `compute_critical_values(n, confidence_level)` that returns the two-tailed critical values for both a Z-test and a T-test at degrees of freedom `df = n - 1`. Compare these values at `n = 5` and `n = 500`.",
        "real_world_context": "In user testing or pilot runs, we often have very small sample sizes (e.g. n=10). Using a standard Z-score instead of a T-score would lead to overly narrow confidence intervals and inflated False Positive rates.",
        "hints": [
            "Use a Z-test when the population standard deviation is known and the sample size is large.",
            "Use a T-test when the population standard deviation is unknown and estimated using the sample standard deviation.",
            "Use `scipy.stats.norm.ppf` for Z and `scipy.stats.t.ppf` with `df = n - 1` for T."
        ],
        "solution": {
            "explanation": "Student's T-distribution has heavier tails than the normal (Z) distribution. This accounts for the extra uncertainty in estimating the population variance from a small sample. As the degrees of freedom `df = n - 1` increase, the T-distribution converges to the normal distribution. For small samples (like n=5), the critical value of T is much larger than Z, requiring stronger evidence to reject the null hypothesis.",
            "key_takeaways": [
                "T-distributions feature thicker tails to account for small sample variance estimation errors.",
                "As sample size n increases, t-scores converge to z-scores."
            ]
        },
        "starter_code": {
            "python": "from scipy.stats import norm, t\n\ndef compute_critical_values(n, confidence_level=0.95):\n    # TODO: Calculate two-tailed z_crit and t_crit\n    z_crit = 0.0\n    t_crit = 0.0\n    return z_crit, t_crit"
        },
        "expected_output": "A tuple of floats representing (z_crit, t_crit).",
        "follow_up_questions": [
            "Why does the T-distribution have thicker tails than the Z-distribution?",
            "If the population variance is known but n=5, should you use Z or T?"
        ],
        "references": [
            {
                "title": "Student's t-Distribution Details",
                "url": "https://wikipedia.org/wiki/Student%27s_t-distribution"
            }
        ]
    })

    # Q19: ANOVA
    questions.append({
        "id": 19,
        "slug": "anova-group-comparison",
        "title": "Build a One-Way ANOVA Calculator",
        "section": "Statistics",
        "difficulty": "Medium",
        "question_type": "coding",
        "neuroforge_skill": "Mathematical Statistics",
        "estimated_time_minutes": 20,
        "tags": ["anova", "hypothesis-testing", "variance"],
        "learning_objectives": [
            "Build a one-way ANOVA variance partitioner from scratch",
            "Calculate Sum of Squares Between (SSB) and Sum of Squares Within (SSW)"
        ],
        "problem_statement": "Build a python function `one_way_anova(*groups)` that accepts multiple lists representing groups, calculates the Sum of Squares Between (SSB), Sum of Squares Within (SSW), degrees of freedom, Mean Squares, and returns the final F-statistic.",
        "real_world_context": "When testing three different LLM prompts (A, B, and C) to see which yields the highest user feedback score, running multiple t-tests increases the family-wise error rate. ANOVA allows comparing all three prompts simultaneously.",
        "hints": [
            "Overall mean (Grand Mean) is the average of all data points combined.",
            "SSB measures distance from each group mean to the grand mean, weighted by group size.",
            "SSW measures distance from individual data points to their respective group mean.",
            "F-statistic = (SSB / df_between) / (SSW / df_within)."
        ],
        "solution": {
            "explanation": "ANOVA compares the variance between groups to the variance within groups. If the variation between groups (SSB/df_b) is significantly larger than the variation within groups (SSW/df_w), the F-statistic is large, suggesting that at least one group mean is different from the others. Running a single ANOVA test controls the Type I error rate across multiple group comparisons.",
            "key_takeaways": [
                "ANOVA splits total variance into between-group and within-group components.",
                "F-statistic is the ratio of explained variance (between groups) to unexplained variance (within groups)."
            ]
        },
        "starter_code": {
            "python": "def one_way_anova(*groups):\n    # groups: tuple of lists, e.g. ([1, 2, 3], [4, 5], [2, 6, 7])\n    # TODO: Calculate F-statistic manually\n    f_stat = 0.0\n    return f_stat"
        },
        "expected_output": "The computed F-statistic as a float.",
        "follow_up_questions": [
            "If the ANOVA F-test yields a significant result (p < 0.05), how do you determine which specific group means differ?",
            "What assumptions must be met to trust ANOVA results?"
        ],
        "references": [
            {
                "title": "One-Way ANOVA Formulation",
                "url": "https://wikipedia.org/wiki/One-way_analysis_of_variance"
            }
        ]
    })

    # Q20: Correlation vs Causation
    questions.append({
        "id": 20,
        "slug": "correlation-vs-causation",
        "title": "Build a Pearson and Spearman Correlation Estimator",
        "section": "Statistics",
        "difficulty": "Medium",
        "question_type": "coding",
        "neuroforge_skill": "Mathematical Statistics",
        "estimated_time_minutes": 15,
        "tags": ["correlation", "spearman", "pearson", "confounders"],
        "learning_objectives": [
            "Build functions to calculate both linear and rank correlations",
            "Contrast Pearson and Spearman values on monotonic non-linear datasets"
        ],
        "problem_statement": "Build a python function `compare_correlations(x, y)` that calculates both the Pearson and Spearman correlation coefficients. Generate a sample dataset where Pearson is low (<0.5) but Spearman is exactly 1.0.",
        "real_world_context": "In user recommendation engines, the relationship between user age and click-through-rate might be monotonic but non-linear. Relying strictly on Pearson correlation would miss this correlation, whereas Spearman would detect it.",
        "hints": [
            "Pearson correlation measures the linear relationship between continuous variables.",
            "Spearman correlation converts values to ranks and measures the monotonic relationship.",
            "A dataset following `y = x^3` is perfectly monotonic but non-linear."
        ],
        "solution": {
            "explanation": "Pearson correlation coefficient (`r`) measures linear relationships. If the relationship is non-linear but strictly increasing (monotonic), Pearson will be less than 1.0. Spearman correlation coefficient (`rho`) applies Pearson correlation to the ranked values of the variables. Because ranking transforms any monotonic relationship into a straight line, Spearman will be exactly 1.0. Confounding variables are third-party factors related to both the independent and dependent variables, creating a false correlation if not controlled.",
            "key_takeaways": [
                "Pearson measures linear trends; Spearman measures monotonic trends.",
                "Spearman is robust to outliers because it operates on ranks rather than raw values."
            ]
        },
        "starter_code": {
            "python": "import scipy.stats as stats\n\ndef compare_correlations(x, y):\n    # TODO: Compute Pearson and Spearman correlations\n    pearson_r = 0.0\n    spearman_rho = 0.0\n    return pearson_r, spearman_rho"
        },
        "expected_output": "A tuple of floats representing (pearson_r, spearman_rho).",
        "follow_up_questions": [
            "How does Simpson's Paradox demonstrate the danger of ignoring confounding variables in aggregated data?",
            "What statistical technique is used to measure the correlation between two variables while controlling for a third variable?"
        ],
        "references": [
            {
                "title": "Correlation Coefficients Comparison",
                "url": "https://wikipedia.org/wiki/Spearman%27s_rank_correlation_coefficient"
            }
        ]
    })

    # Q21: Maximum Likelihood Estimation
    questions.append({
        "id": 21,
        "slug": "maximum-likelihood-estimation",
        "title": "Build a Bernoulli MLE Parameter Solver",
        "section": "Statistics",
        "difficulty": "Medium",
        "question_type": "coding",
        "neuroforge_skill": "Mathematical Statistics",
        "estimated_time_minutes": 20,
        "tags": ["parameter-estimation", "mle", "math"],
        "learning_objectives": [
            "Build an estimator that solves for model parameters maximizing likelihood",
            "Derive the log-likelihood mathematical formulas for Bernoulli experiments"
        ],
        "problem_statement": "Build a python function `find_mle_bernoulli(observations)` that returns the probability parameter `p` maximizing the log-likelihood of a list of Bernoulli outcomes, and explain the derivation mathematically.",
        "real_world_context": "Training machine learning models like logistic regression involves finding weight parameters that maximize the likelihood of the training labels, which is equivalent to minimizing binary cross-entropy loss.",
        "hints": [
            "The likelihood function is the product of individual probabilities: L(p) = prod(p^xi * (1-p)^(1-xi)).",
            "Taking the log converts the product to a sum: log L(p) = sum(xi * log(p) + (1-xi) * log(1-p)).",
            "Take the derivative with respect to p, set it to zero, and solve for p. You will find that the MLE is the sample mean."
        ],
        "solution": {
            "explanation": "To find the MLE, we maximize the log-likelihood function. For a Bernoulli sample, this function is `ln L(p) = k * ln(p) + (n - k) * ln(1 - p)`, where `k` is the sum of successes and `n` is the sample size. Differentiating with respect to `p` yields `d/dp [ln L(p)] = k/p - (n-k)/(1-p)`. Setting this derivative to zero gives `k(1-p) = (n-k)p`, which simplifies to `k = np`, meaning `p_mle = k/n` (the sample proportion).",
            "key_takeaways": [
                "Likelihood is the probability of the observed data as a function of the model parameters.",
                "Maximizing log-likelihood simplifies calculation by turning products into sums."
            ]
        },
        "starter_code": {
            "python": "def find_mle_bernoulli(observations):\n    # observations: list of 0s and 1s\n    # TODO: Calculate the MLE of parameter p\n    pass"
        },
        "expected_output": "The sample mean of the observations.",
        "follow_up_questions": [
            "Why do we maximize log-likelihood instead of the raw likelihood function?",
            "Is the MLE parameter estimate always unbiased? What about the MLE estimator for the variance of a normal distribution?"
        ],
        "references": [
            {
                "title": "MLE Derivations (Penn State)",
                "url": "https://online.stat.psu.edu/stat415/lesson/1/1.2"
            }
        ]
    })

    # Q22: Confidence Intervals
    questions.append({
        "id": 22,
        "slug": "confidence-intervals",
        "title": "Build a Confidence Interval Estimator",
        "section": "Statistics",
        "difficulty": "Medium",
        "question_type": "coding",
        "neuroforge_skill": "Mathematical Statistics",
        "estimated_time_minutes": 15,
        "tags": ["confidence-intervals", "estimation", "inference"],
        "learning_objectives": [
            "Build a confidence interval generator for sample means",
            "Interpret frequentist confidence bounds accurately"
        ],
        "problem_statement": "Build a python function `calculate_confidence_interval(data, confidence_level)` that constructs confidence boundaries for a population mean (assuming population variance is unknown) using the T-distribution.",
        "real_world_context": "If a latency model predicts response time is 120ms with a 95% CI of [115ms, 125ms], it informs system designers about the precision of the metric, indicating if the sample size is sufficient.",
        "hints": [
            "Use the sample standard deviation and a T-distribution critical value.",
            "Standard Error of mean = s / sqrt(n).",
            "Frequentist interpretation: 95% of such intervals constructed from repeated random samples will contain the true population mean. Once an interval is calculated, the true mean is either in it or it is not (the probability is 0 or 1)."
        ],
        "solution": {
            "explanation": "A confidence interval is calculated as `mean +/- t_crit * (s / sqrt(n))`. In frequentist statistics, the population mean is a fixed, constant value, not a random variable. Therefore, the interval is what is random. A 95% confidence level means that if we repeat the sampling process infinitely, 95% of the calculated intervals will contain the true population mean. It is incorrect to say there is a 95% probability that the true mean lies within a specific calculated interval.",
            "key_takeaways": [
                "Confidence intervals represent the reliability of the estimation procedure over repeated sampling.",
                "In frequentist stats, parameters are fixed; the intervals are the random variables."
            ]
        },
        "starter_code": {
            "python": "import math\nfrom scipy.stats import t\n\ndef calculate_confidence_interval(data, confidence_level=0.95):\n    # TODO: Calculate mean, sample std, standard error, and interval bounds using T-distribution\n    lower_bound = 0.0\n    upper_bound = 0.0\n    return lower_bound, upper_bound"
        },
        "expected_output": "A tuple of floats representing the lower and upper bounds.",
        "follow_up_questions": [
            "How does increasing the sample size affect the width of a confidence interval?",
            "What is the Bayesian equivalent of a confidence interval, and how does its interpretation differ?"
        ],
        "references": [
            {
                "title": "Frequentist Confidence Intervals",
                "url": "https://wikipedia.org/wiki/Confidence_interval"
            }
        ]
    })

    # Q23: Bias-Variance Decomposition Derivation
    questions.append({
        "id": 23,
        "slug": "bias-variance-tradeoff-math",
        "title": "Build a Bias-Variance Simulation Engine",
        "section": "Statistics",
        "difficulty": "Hard",
        "question_type": "coding",
        "neuroforge_skill": "Mathematical Statistics",
        "estimated_time_minutes": 25,
        "tags": ["bias-variance", "mathematics", "machine-learning-theory"],
        "learning_objectives": [
            "Build an empirical simulator measuring bias squared and variance",
            "Derive the algebraic decomposition of Mean Squared Error"
        ],
        "problem_statement": "Build a python function `simulate_bias_variance(true_function, num_runs, sample_size)` that empirically estimates and returns the bias squared, variance, and irreducible error components of MSE for a model fitting noisy data. Outline the mathematical proof.",
        "real_world_context": "Understanding this decomposition is crucial when debugging underfitting vs overfitting. Underfitting is caused by high bias (model is too simple), while overfitting is caused by high variance (model is overly sensitive to the training set).",
        "hints": [
            "Start with the definition of MSE: E[(y - f_hat(x))^2], where y = f(x) + epsilon, and E[epsilon] = 0, Var(epsilon) = sigma^2.",
            "Use the algebraic trick of adding and subtracting E[f_hat(x)] inside the expectation: E[(f_hat(x) - E[f_hat(x)] + E[f_hat(x)] - f(x) - epsilon)^2].",
            "Expand the square and use the independence of epsilon to cancel out the cross-product terms."
        ],
        "solution": {
            "explanation": "Expected MSE = E[(y - f_hat)^2] = E[((f + epsilon) - f_hat)^2] = E[(f - f_hat + epsilon)^2]. Since epsilon is independent of f_hat and has mean 0, the cross terms cancel, leaving E[(f - f_hat)^2] + E[epsilon^2]. Adding and subtracting E[f_hat] inside the first term: E[((f - E[f_hat]) + (E[f_hat] - f_hat))^2] = (f - E[f_hat])^2 + E[(E[f_hat] - f_hat)^2] + 2*E[(f - E[f_hat])*(E[f_hat] - f_hat)]. The third term evaluates to 0 because E[E[f_hat] - f_hat] = E[f_hat] - E[f_hat] = 0. We are left with (f - E[f_hat])^2 (which is Bias^2) + E[(f_hat - E[f_hat])^2] (which is Var(f_hat)) + sigma^2 (irreducible error).",
            "key_takeaways": [
                "Expected MSE = Bias^2 + Variance + Irreducible Error.",
                "Irreducible error represents noise in the data generating process that cannot be modeled."
            ]
        },
        "starter_code": {
            "python": "import numpy as np\n\ndef simulate_bias_variance(true_func, num_runs=100, sample_size=30):\n    # TODO: Generate multiple training sets, fit a simple model, evaluate on a fixed point x_test\n    # Compute bias squared, variance, and comparison to total MSE\n    pass"
        },
        "expected_output": "Estimated bias squared, variance, and irreducible error summing close to target MSE.",
        "follow_up_questions": [
            "Why is the irreducible error term constant and unaffected by model choice?",
            "How does regularization affect the bias and variance of a model?"
        ],
        "references": [
            {
                "title": "Bias-Variance Tradeoff (Stanford)",
                "url": "https://web.stanford.edu/~hastie/ElemStatLearn/"
            }
        ]
    })

    # Q24: Multiple Testing & FDR
    questions.append({
        "id": 24,
        "slug": "p-hacking-multiple-testing",
        "title": "Build a Multiple-Testing P-Value Adjuster",
        "section": "Statistics",
        "difficulty": "Hard",
        "question_type": "coding",
        "neuroforge_skill": "Mathematical Statistics",
        "estimated_time_minutes": 20,
        "tags": ["multiple-testing", "bonferroni", "fdr", "inference"],
        "learning_objectives": [
            "Build Bonferroni and Benjamini-Hochberg FDR correction filters",
            "Explain Family-Wise Error Rate inflation during multiple comparisons"
        ],
        "problem_statement": "Build a python function `adjust_p_values(p_values, method)` that implements the Bonferroni correction and the Benjamini-Hochberg False Discovery Rate (FDR) procedure, returning adjusted p-values.",
        "real_world_context": "If a marketing team tests 50 different color layouts on a website simultaneously, at least a few will appear to yield a significant conversion improvement purely by chance. Without multiple testing corrections, you will deploy features that are actually useless.",
        "hints": [
            "Probability of no Type I errors in 100 independent tests is (1 - 0.05)^100. The probability of at least one error is 1 - (1 - alpha)^N.",
            "Bonferroni controls the Family-Wise Error Rate (FWER) by dividing alpha by the number of tests (N). Equivalently, multiply each p-value by N (capped at 1.0).",
            "Benjamini-Hochberg controls the False Discovery Rate (FDR) by sorting p-values: find the largest index k such that p_(k) <= (k/N) * alpha, and reject all hypotheses up to k."
        ],
        "solution": {
            "explanation": "With 100 tests, the probability of at least one false positive is `1 - (1 - 0.05)^100 = 0.994` (99.4%), showing that Type I error rates inflate rapidly. The Bonferroni correction is highly conservative because it guards against *any* false positive (FWER). The Benjamini-Hochberg method is more powerful because it controls the *proportion* of false positives among the rejected tests (FDR). It sorts p-values in ascending order and compares them to `(i/N) * alpha`.",
            "key_takeaways": [
                "Multiple testing inflation makes random noise look statistically significant.",
                "Bonferroni controls the chance of *any* false positive; FDR controls the *percentage* of false positives."
            ]
        },
        "starter_code": {
            "python": "def adjust_p_values(p_values, method='bonferroni', alpha=0.05):\n    # p_values: list of float p-values\n    # TODO: Implement corrections and return adjusted p-values list\n    pass"
        },
        "expected_output": "Adjusted p-values list after correction.",
        "follow_up_questions": [
            "Why is the Bonferroni correction considered too conservative for highly correlated tests?",
            "What is the mathematical definition of False Discovery Rate?"
        ],
        "references": [
            {
                "title": "Benjamini-Hochberg FDR Paper",
                "url": "https://www.jstor.org/stable/2346101"
            }
        ]
    })

    # Q25: Bayesian Inference & MCMC
    questions.append({
        "id": 25,
        "slug": "bayesian-inference-mcmc",
        "title": "Build a Metropolis-Hastings MCMC Sampler",
        "section": "Statistics",
        "difficulty": "Hard",
        "question_type": "coding",
        "neuroforge_skill": "Mathematical Statistics",
        "estimated_time_minutes": 25,
        "tags": ["bayesian-inference", "mcmc", "sampling"],
        "learning_objectives": [
            "Build a 1D Metropolis-Hastings MCMC algorithm from scratch",
            "Contrast MCMC posterior sampling with analytical conjugate prior updates"
        ],
        "problem_statement": "Build a python function `metropolis_hastings(target_density, num_samples, proposal_width)` that implements a 1D Metropolis-Hastings sampler to draw samples from a given unnormalized target probability density.",
        "real_world_context": "Bayesian neural networks use MCMC or variational inference to estimate weight distributions rather than single-point weights. This allows the model to output a formal estimate of its own uncertainty when making predictions.",
        "hints": [
            "Frequentist inference assumes parameter theta is fixed but unknown. Bayesian inference treats theta as a random variable with a probability distribution.",
            "Conjugate priors yield posterior distributions of the same algebraic family, avoiding integration.",
            "In Metropolis-Hastings, propose a new state `x_new ~ N(x_current, proposal_width)`. Accept `x_new` with probability `min(1, target_density(x_new) / target_density(x_current))`."
        ],
        "solution": {
            "explanation": "Bayesian inference updates parameter distributions using the relation `Posterior = (Likelihood * Prior) / Evidence`. The denominator (Evidence) requires integrating over all possible parameters. For high-dimensional or non-standard distributions, this integral is analytically intractable. MCMC methods like Metropolis-Hastings bypass calculating this denominator by simulating a Markov Chain whose stationary distribution matches the target posterior. The algorithm compares the ratio of the target density at a proposed point to the current point, accepting or rejecting the proposal based on a random draw.",
            "key_takeaways": [
                "Bayesian inference yields parameter distributions (posteriors) rather than single-point estimates (MLE).",
                "MCMC algorithms draw samples from complex posteriors by avoiding calculation of the normalization constant."
            ]
        },
        "starter_code": {
            "python": "import random\nimport math\n\ndef metropolis_hastings(target_density, num_samples=1000, proposal_width=0.5):\n    # TODO: Build Metropolis-Hastings algorithm loop and return a list of samples\n    samples = []\n    return samples"
        },
        "expected_output": "A list of sampled floats whose histogram approximates the shape of the target density.",
        "follow_up_questions": [
            "What is the 'burn-in' period in MCMC sampling, and why is it necessary?",
            "What is autocorrelation in MCMC chains, and how can you reduce it?"
        ],
        "references": [
            {
                "title": "Bayesian Methods for Hackers",
                "url": "https://github.com/CamDavidsonPilon/Probabilistic-Programming-and-Bayesian-Methods-for-Hackers"
            }
        ]
    })
    
    return questions
