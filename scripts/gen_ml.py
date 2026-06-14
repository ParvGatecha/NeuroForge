def get_questions():
    questions = []
    
    # Q26: Linear Regression
    questions.append({
        "id": 26,
        "slug": "linear-regression",
        "title": "Build a Linear Regression Model via the Normal Equation",
        "section": "Machine Learning",
        "difficulty": "Easy",
        "question_type": "coding",
        "tensortrack_skill": "Classical Machine Learning",
        "estimated_time_minutes": 10,
        "tags": ["regression", "supervised-learning", "linear-algebra"],
        "learning_objectives": [
            "Build a closed-form OLS linear regression optimizer using the Normal Equation",
            "Identify the computational complexity of closed-form regression solutions"
        ],
        "problem_statement": "Build a python function `fit_linear_regression(X, y)` that computes the weights of a linear regression model using the closed-form Normal Equation: `theta = (X^T * X)^(-1) * X^T * y`. Make sure to prepend a bias column of 1s to the feature matrix `X`.",
        "real_world_context": "Linear regression is the foundation of house price forecasting, user lifetime value estimation, and baseline forecasting models.",
        "hints": [
            "Use `np.hstack` or `np.column_stack` to add a column of ones to X.",
            "Use `np.linalg.inv` for matrix inversion and `X.T` for transpose.",
            "Matrix multiplication in numpy is done with the `@` operator or `np.dot()`."
        ],
        "solution": {
            "explanation": "The Ordinary Least Squares (OLS) objective is to minimize the sum of squared residuals. The closed-form solution to this optimization problem is the Normal Equation: `theta = (X^T * X)^(-1) * X^T * y`. Computing this requires inverting a matrix of size (D x D), where D is the number of features, leading to a computational complexity of O(D^3). This is computationally expensive when the number of features is large, in which case gradient descent is preferred.",
            "key_takeaways": [
                "The Normal Equation provides the exact analytical solution to OLS regression.",
                "Inverting X^T * X takes O(D^3) time, making it scale poorly with many features."
            ]
        },
        "starter_code": {
            "python": "import numpy as np\n\ndef fit_linear_regression(X, y):\n    # X: numpy array of shape (N, D)\n    # y: numpy array of shape (N,)\n    # TODO: Add bias column, calculate weights via Normal Equation\n    theta = None\n    return theta"
        },
        "expected_output": "A numpy array of shape (D + 1,) containing the weights.",
        "follow_up_questions": [
            "What happens to the Normal Equation if the features are highly collinear (perfect multicollinearity)?",
            "Under what conditions is gradient descent preferred over the Normal Equation?"
        ],
        "references": [
            {
                "title": "Stanford CS229 Linear Regression Notes",
                "url": "https://cs229.stanford.edu/notes2021fall/cs229-notes1.pdf"
            }
        ]
    })
    
    # Q27: Gradient Descent
    questions.append({
        "id": 27,
        "slug": "gradient-descent",
        "title": "Build a Gradient Descent Optimizer Step",
        "section": "Machine Learning",
        "difficulty": "Easy",
        "question_type": "coding",
        "tensortrack_skill": "Classical Machine Learning",
        "estimated_time_minutes": 10,
        "tags": ["optimization", "gradient-descent", "math"],
        "learning_objectives": [
            "Build a single gradient descent update step for Mean Squared Error",
            "Differentiate between Batch SGD and Mini-batch SGD"
        ],
        "problem_statement": "Build a python function `gradient_descent_step(X, y, theta, learning_rate)` that computes the gradient of the Mean Squared Error loss and updates the weight vector `theta` for a single iteration. Return the updated `theta` and the loss value before the update.",
        "real_world_context": "Gradient descent is the core optimizer behind almost all machine learning and deep learning algorithms, including training deep neural networks and support vector machines.",
        "hints": [
            "The prediction is `y_pred = X @ theta`.",
            "The gradient of MSE with respect to theta is `(2/N) * X.T @ (y_pred - y)` or `(1/N) * X.T @ (y_pred - y)` depending on scaling conventions.",
            "Update formula: `theta = theta - learning_rate * gradient`."
        ],
        "solution": {
            "explanation": "Gradient descent computes the derivative of the loss function with respect to the weights, representing the direction of steepest increase. By subtracting the gradient scaled by the learning rate, we step in the direction of steepest decrease. Batch gradient descent uses all samples to compute the gradient, Stochastic Gradient Descent (SGD) uses one sample, and Mini-batch SGD uses a small random subset, trading off computation time for update stability.",
            "key_takeaways": [
                "Gradient descent updates weights iteratively in the direction of negative gradient.",
                "Selecting an appropriate learning rate is crucial: too large causes divergence, too small slows convergence."
            ]
        },
        "starter_code": {
            "python": "import numpy as np\n\ndef gradient_descent_step(X, y, theta, learning_rate):\n    # X: (N, D), y: (N,), theta: (D,)\n    # TODO: Calculate predictions, loss, gradient, and update theta\n    loss = 0.0\n    updated_theta = theta\n    return updated_theta, loss"
        },
        "expected_output": "A tuple of (updated weights array, pre-update MSE float value).",
        "follow_up_questions": [
            "How does feature scaling (normalization/standardization) help gradient descent converge faster?",
            "What is the mathematical effect of adding a momentum term to the gradient descent update?"
        ],
        "references": [
            {
                "title": "An Overview of Gradient Descent Optimization Algorithms",
                "url": "https://arxiv.org/abs/1609.04747"
            }
        ]
    })

    # Q28: Logistic Regression
    questions.append({
        "id": 28,
        "slug": "logistic-regression",
        "title": "Build a Logistic Regression Classifier",
        "section": "Machine Learning",
        "difficulty": "Easy",
        "question_type": "coding",
        "tensortrack_skill": "Classical Machine Learning",
        "estimated_time_minutes": 15,
        "tags": ["logistic-regression", "classification", "sigmoid"],
        "learning_objectives": [
            "Build the sigmoid function and predict classification probabilities",
            "Build the binary cross-entropy loss function with numeric clipping"
        ],
        "problem_statement": "Build two python functions: `predict_probability(X, theta)` that returns the sigmoid probability of classification, and `binary_cross_entropy(y_true, y_pred)` that calculates the cross-entropy loss incorporating value clipping to avoid log(0) errors.",
        "real_world_context": "Logistic regression is widely used for binary classification tasks like email spam classification, ad click prediction, and credit default scoring.",
        "hints": [
            "The sigmoid function is `1 / (1 + exp(-z))` where `z = X @ theta`.",
            "Binary cross-entropy loss formula is `-1/N * sum(y * log(p) + (1 - y) * log(1 - p))`.",
            "Avoid numerical underflow/overflow by clipping prediction values between a tiny epsilon and `1 - epsilon` before calculating logs."
        ],
        "solution": {
            "explanation": "Logistic regression maps linear model predictions to probabilities in the range [0, 1] using the sigmoid function. The decision boundary is the line where the predicted probability is exactly 0.5, corresponding to `X @ theta = 0`. Since this equation is linear, logistic regression is classified as a linear classifier. The model parameters are optimized by minimizing the binary cross-entropy loss.",
            "key_takeaways": [
                "Sigmoid maps continuous input numbers to [0, 1] probability outputs.",
                "Logistic regression has a linear decision boundary in the input feature space."
            ]
        },
        "starter_code": {
            "python": "import numpy as np\n\ndef sigmoid(z):\n    return 1 / (1 + np.exp(-z))\n\ndef predict_probability(X, theta):\n    # TODO: Build sigmoid probability predictor\n    pass\n\ndef binary_cross_entropy(y_true, y_pred):\n    # TODO: Build loss calculator with numeric clipping\n    pass"
        },
        "expected_output": "Probability arrays and float cross-entropy values.",
        "follow_up_questions": [
            "Why is MSE not used as a loss function in logistic regression models?",
            "How does L1 vs L2 regularization affect the coefficients of a logistic regression model?"
        ],
        "references": [
            {
                "title": "Stanford CS229 Logistic Regression Notes",
                "url": "https://cs229.stanford.edu/notes2021fall/cs229-notes1.pdf"
            }
        ]
    })

    # Q29: K-Nearest Neighbors
    questions.append({
        "id": 29,
        "slug": "k-nearest-neighbors",
        "title": "Build a K-Nearest Neighbors Classifier",
        "section": "Machine Learning",
        "difficulty": "Easy",
        "question_type": "coding",
        "tensortrack_skill": "Classical Machine Learning",
        "estimated_time_minutes": 10,
        "tags": ["knn", "lazy-learning", "distance-metrics"],
        "learning_objectives": [
            "Build a vector-distance sorter using Euclidean distance",
            "Select classifications using voting aggregators on the top K neighbors"
        ],
        "problem_statement": "Build a python function `knn_classify(X_train, y_train, X_test, k)` that implements a complete K-Nearest Neighbors classifier using Euclidean distance. Assign classes using a majority vote on the top K neighbors.",
        "real_world_context": "KNN is a simple, intuitive baseline model used for anomaly detection, image similarity searches, and item recommendations.",
        "hints": [
            "Euclidean distance between points p and q is `sqrt(sum((pi - qi)^2))`.",
            "Use `np.linalg.norm(X_train - test_point, axis=1)` to compute distance to all points quickly.",
            "Sort the distances and find the most common class label among the top K closest instances."
        ],
        "solution": {
            "explanation": "KNN is a instance-based, non-parametric, lazy learner: it does not train a model but performs calculations during inference. When K=1, the model is highly sensitive to local noise, resulting in high variance (overfitting). When K=N, the model predicts the majority class for all points, resulting in high bias (underfitting). As dimensionality increases, the volume of space grows exponentially, making all points seem far and equidistant, degrading KNN performance (curse of dimensionality).",
            "key_takeaways": [
                "Small K leads to high variance (overfitting); large K leads to high bias (underfitting).",
                "KNN is computationally expensive during inference, scaling as O(N * D) where N is dataset size."
            ]
        },
        "starter_code": {
            "python": "import numpy as np\nfrom collections import Counter\n\ndef knn_classify(X_train, y_train, X_test, k):\n    # TODO: Build KNN classification loop for each test coordinate\n    predictions = []\n    return np.array(predictions)"
        },
        "expected_output": "A numpy array of predicted class labels for the test points.",
        "follow_up_questions": [
            "Why is feature normalization critical before training a KNN classifier?",
            "What data structures can you use to accelerate the nearest-neighbor search phase?"
        ],
        "references": [
            {
                "title": "Introduction to KNN",
                "url": "https://wikipedia.org/wiki/K-nearest_neighbors_algorithm"
            }
        ]
    })

    # Q30: Decision Trees
    questions.append({
        "id": 30,
        "slug": "decision-trees",
        "title": "Build a Decision Tree Split Evaluator",
        "section": "Machine Learning",
        "difficulty": "Easy",
        "question_type": "coding",
        "tensortrack_skill": "Classical Machine Learning",
        "estimated_time_minutes": 15,
        "tags": ["decision-trees", "entropy", "gini"],
        "learning_objectives": [
            "Build functions to calculate Shannon Entropy and Gini Impurity from scratch",
            "Build an Information Gain evaluation function for split features"
        ],
        "problem_statement": "Build a python function `calculate_information_gain(y_parent, y_left, y_right, metric='entropy')` that computes the information gain of splitting a parent node into left and right child nodes. Support both 'entropy' and 'gini' metrics.",
        "real_world_context": "Splitting metrics form the core decision-making logic of tree-based algorithms like CART, ID3, C4.5, and Random Forests when classifying tabular user data.",
        "hints": [
            "Entropy = -sum(pi * log2(pi)), Gini Impurity = 1 - sum(pi^2).",
            "Information Gain is defined as: `Metric(Parent) - (N_left/N_parent * Metric(Left) + N_right/N_parent * Metric(Right))`."
        ],
        "solution": {
            "explanation": "Decision trees build splits by maximizing Information Gain, which measures the reduction in impurity (entropy or Gini) after splitting the data. Gini impurity is computationally faster because it does not require calculating logarithms, which is why it is the default in libraries like scikit-learn. Entropy measures the level of disorder or uncertainty in a system.",
            "key_takeaways": [
                "Gini Impurity is faster to compute; Entropy involves logarithmic scales.",
                "Information Gain evaluates how well a feature splits the classes into distinct child nodes."
            ]
        },
        "starter_code": {
            "python": "import numpy as np\n\ndef calculate_entropy(y):\n    # TODO: Build Shannon Entropy calculator\n    pass\n\ndef calculate_gini(y):\n    # TODO: Build Gini Impurity calculator\n    pass\n\ndef calculate_information_gain(y_parent, y_left, y_right, metric='entropy'):\n    # TODO: Build Information Gain calculation\n    pass"
        },
        "expected_output": "Float values representing the split information gain.",
        "follow_up_questions": [
            "Why do decision trees tend to overfit easily, and how does pruning prevent this?",
            "What splitting metric do regression decision trees use instead of entropy or Gini?"
        ],
        "references": [
            {
                "title": "CART Splitting Criteria Details",
                "url": "https://wikipedia.org/wiki/Decision_tree_learning"
            }
        ]
    })

    # Q31: Train, Validation, Test
    questions.append({
        "id": 31,
        "slug": "train-validation-test",
        "title": "Build a K-Fold Cross-Validation Index Splitter",
        "section": "Machine Learning",
        "difficulty": "Easy",
        "question_type": "coding",
        "tensortrack_skill": "Classical Machine Learning",
        "estimated_time_minutes": 10,
        "tags": ["cross-validation", "data-leakage", "methodology"],
        "learning_objectives": [
            "Build a K-Fold cross-validation splitter from scratch",
            "Avoid common data leakage bugs during preprocessing pipelines"
        ],
        "problem_statement": "Build a python function `k_fold_indices(n_samples, n_splits)` that yields train/validation indices for custom K-Fold Cross Validation without using scikit-learn. Explain how to sequence data transformations to avoid data leakage.",
        "real_world_context": "Data leakage can lead to models performing exceptionally well during development but failing completely when deployed to production on real-world inputs.",
        "hints": [
            "Fit your transformers (scalers, encoders, imputers) ONLY on the training split, and apply the transform to the validation/test splits.",
            "To build K-Fold indices: shuffle indices, split them into K equal parts, and iterate, using part `i` as the validation split and the rest as the training split."
        ],
        "solution": {
            "explanation": "Data leakage occurs when information from outside the training dataset is used to train the model. For example, standardizing the entire dataset before splitting leaks the global mean and variance into the training fold, artificially boosting evaluation performance. The correct workflow is to split the data first, call `.fit()` and `.transform()` on the training set, and use the fitted scaler to `.transform()` the validation/test sets.",
            "key_takeaways": [
                "Fit transformers ONLY on the training fold to avoid data leakage.",
                "Cross-validation provides a robust estimate of model generalization by validating on all data parts."
            ]
        },
        "starter_code": {
            "python": "import numpy as np\n\ndef k_fold_indices(n_samples, n_splits=5):\n    # TODO: Build K-fold partition indices and yield them as (train_idx, val_idx) pairs\n    pass"
        },
        "expected_output": "Generates a list of tuples containing (train_idx, val_idx) arrays.",
        "follow_up_questions": [
            "Why is Stratified K-Fold preferred over standard K-Fold for imbalanced classification tasks?",
            "What is Time Series Split, and why is standard K-Fold inappropriate for sequential temporal data?"
        ],
        "references": [
            {
                "title": "Data Leakage in Machine Learning",
                "url": "https://machinelearningmastery.com/data-leakage-machine-learning/"
            }
        ]
    })

    # Q32: L1 & L2 Regularization
    questions.append({
        "id": 32,
        "slug": "l1-l2-regularization",
        "title": "Build an Elastic Net Loss Function",
        "section": "Machine Learning",
        "difficulty": "Medium",
        "question_type": "coding",
        "tensortrack_skill": "Classical Machine Learning",
        "estimated_time_minutes": 15,
        "tags": ["regularization", "lasso", "ridge"],
        "learning_objectives": [
            "Build loss penalties for L1 (Lasso) and L2 (Ridge) constraints",
            "Identify the geometric characteristics of regularizer constraints"
        ],
        "problem_statement": "Build a python function `regularized_loss(y_true, y_pred, weights, alpha, l1_ratio)` that calculates the Mean Squared Error loss incorporating Elastic Net regularization (combining L1 and L2 penalties). Explain why L1 induces feature sparsity.",
        "real_world_context": "When working with genomic datasets with 50,000 genes but only 200 samples, L1 regularization acts as automated feature selection, identifying the most predictive genes.",
        "hints": [
            "L1 penalty is the sum of absolute weights: `sum(|wi|)`. L2 penalty is the sum of squared weights: `sum(wi^2)`.",
            "Elastic Net loss is: `MSE + alpha * l1_ratio * L1_penalty + alpha * (1 - l1_ratio) * L2_penalty`."
        ],
        "solution": {
            "explanation": "L1 regularization uses the absolute values of the weights as a penalty. Geometrically, the constraint region is a diamond with sharp corners that lie on the coordinate axes. The loss contours are likely to hit these corners, setting some weights to exactly zero, creating sparsity. L2 regularization uses squared weights, forming a spherical constraint region. Loss contours touch the sphere at non-zero points, shrinking weights close to zero but rarely setting them to exactly zero.",
            "key_takeaways": [
                "L1 regularization yields sparse models (feature selection).",
                "L2 regularization shrinks coefficients evenly, preventing extreme weight values."
            ]
        },
        "starter_code": {
            "python": "import numpy as np\n\ndef regularized_loss(y_true, y_pred, weights, alpha, l1_ratio=0.5):\n    # TODO: Build Elastic Net loss calculation\n    loss = 0.0\n    return loss"
        },
        "expected_output": "Elastic Net loss float value.",
        "follow_up_questions": [
            "How does Elastic Net combine the benefits of Lasso and Ridge?",
            "What happens to Lasso coefficients when features are highly correlated?"
        ],
        "references": [
            {
                "title": "Lasso and Ridge Geometric Interpretations",
                "url": "https://wikipedia.org/wiki/Regularization_(mathematics)"
            }
        ]
    })

    # Q33: Support Vector Machines
    questions.append({
        "id": 33,
        "slug": "support-vector-machines",
        "title": "Build an RBF Kernel Matrix Generator",
        "section": "Machine Learning",
        "difficulty": "Medium",
        "question_type": "coding",
        "tensortrack_skill": "Classical Machine Learning",
        "estimated_time_minutes": 20,
        "tags": ["svm", "kernel-trick", "optimization"],
        "learning_objectives": [
            "Build a Radial Basis Function (RBF) kernel matrix",
            "Contrast hard-margin and soft-margin optimization parameters"
        ],
        "problem_statement": "Build a python function `rbf_kernel(X1, X2, gamma)` that computes the Radial Basis Function (RBF) kernel matrix between two sets of vectors. Explain how hyperparameter `C` regulates margins in SVMs.",
        "real_world_context": "SVMs with RBF kernels are used to classify non-linear data structures, such as handwriting digits or protein structures, by implicitly projecting them into high-dimensional space.",
        "hints": [
            "A small `C` value prioritizes a wider margin, allowing more classification errors (underfitting). A large `C` value forces a narrow margin to minimize training errors (overfitting).",
            "The formula for the RBF kernel between vectors x and y is `K(x, y) = exp(-gamma * ||x - y||^2)`."
        ],
        "solution": {
            "explanation": "SVMs find a hyperplane that maximizes the margin between classes. In non-separable data, a soft margin allows training errors using slack variables, controlled by `C`. High `C` penalizes errors heavily, risking overfitting. The kernel trick computes inner products in a high-dimensional feature space without explicitly projecting the data, allowing non-linear decision boundaries to be calculated efficiently. The RBF kernel maps inputs into an infinite-dimensional space.",
            "key_takeaways": [
                "C balances margin size against classification accuracy.",
                "The kernel trick calculates high-dimensional projections implicitly, saving computation."
            ]
        },
        "starter_code": {
            "python": "import numpy as np\n\ndef rbf_kernel(X1, X2, gamma=1.0):\n    # X1: (N, D), X2: (M, D)\n    # TODO: Build pairwise squared Euclidean distances and return the kernel matrix of shape (N, M)\n    kernel_matrix = None\n    return kernel_matrix"
        },
        "expected_output": "A numpy array of shape (N, M) containing kernel values.",
        "follow_up_questions": [
            "What are 'support vectors' in the context of SVMs?",
            "What is Mercer's Theorem, and why is it important for custom SVM kernels?"
        ],
        "references": [
            {
                "title": "Support Vector Machines (Stanford)",
                "url": "https://cs229.stanford.edu/notes2021fall/cs229-notes3.pdf"
            }
        ]
    })

    # Q34: Random Forests
    questions.append({
        "id": 34,
        "slug": "random-forests",
        "title": "Build a Bootstrap Sampler for Random Forests",
        "section": "Machine Learning",
        "difficulty": "Medium",
        "question_type": "coding",
        "tensortrack_skill": "Classical Machine Learning",
        "estimated_time_minutes": 15,
        "tags": ["ensemble", "random-forests", "bagging"],
        "learning_objectives": [
            "Build a bootstrap dataset sampler with replacement",
            "Extract Out-Of-Bag (OOB) indices for built-in model validation"
        ],
        "problem_statement": "Build a python function `bootstrap_sample(X, y)` that generates a bootstrap sample of a dataset with replacement, and identifies the Out-Of-Bag (OOB) indices. Explain why feature randomness is added to Random Forests.",
        "real_world_context": "Random Forests are highly robust models used in credit scoring, churn prediction, and asset pricing due to their stability and resistance to overfitting.",
        "hints": [
            "A bootstrap sample draws N samples from N instances with replacement.",
            "The probability of a specific instance NOT being selected in N draws is `(1 - 1/N)^N`. As N approaches infinity, this limits to `1/e` (approx 36.8%).",
            "Feature randomness forces each node split to consider only a random subset of features, decorrelating the trees."
        ],
        "solution": {
            "explanation": "Random Forests combine Bootstrap Aggregation (bagging) with feature randomness. Bagging trains trees on bootstrap samples, reducing variance by averaging predictions. Out-of-bag (OOB) samples (the ~36.8% left out) are used as a built-in validation set. Standard bagged trees can look very similar if a single dominant feature is always split first. Random Forests solve this by selecting a random subset of features at each split, decorrelating the trees and further reducing variance.",
            "key_takeaways": [
                "Bootstrap samples leave out ~36.8% of data as Out-of-Bag (OOB) validation samples.",
                "Feature randomness decorrelates individual trees, yielding greater ensemble diversity."
            ]
        },
        "starter_code": {
            "python": "import numpy as np\n\ndef bootstrap_sample(X, y):\n    # X: (N, D), y: (N,)\n    # TODO: Build bootstrap sampling, returning (X_sample, y_sample, oob_indices)\n    pass"
        },
        "expected_output": "Bootstrap sample matrices and the array of unselected OOB indices.",
        "follow_up_questions": [
            "Why do Random Forests not need a separate validation set during tuning?",
            "How does the number of trees parameter (n_estimators) affect bias and variance in a Random Forest?"
        ],
        "references": [
            {
                "title": "Breiman's Random Forests Paper",
                "url": "https://link.springer.com/article/10.1023/A:1010933404324"
            }
        ]
    })

    # Q35: Gradient Boosting
    questions.append({
        "id": 35,
        "slug": "gradient-boosting",
        "title": "Build a Gradient Boosting Iteration Step",
        "section": "Machine Learning",
        "difficulty": "Medium",
        "question_type": "coding",
        "tensortrack_skill": "Classical Machine Learning",
        "estimated_time_minutes": 20,
        "tags": ["ensemble", "gradient-boosting", "boosting"],
        "learning_objectives": [
            "Build pseudo-residual estimators for MSE loss",
            "Implement a sequential boosting update iteration"
        ],
        "problem_statement": "Build two python functions: `compute_pseudo_residuals(y_true, y_pred)` that calculates prediction residuals, and `mock_boosting_step(y_pred, weak_learner_preds, learning_rate)` that updates the prediction vector. Explain the difference between boosting sequential updates and bagging parallel training.",
        "real_world_context": "Gradient boosted decision trees (like XGBoost, LightGBM) are the dominant algorithms for competitive machine learning on tabular data (e.g. Kaggle competitions).",
        "hints": [
            "Pseudo-residuals for MSE loss are simply the difference `y_true - y_pred`.",
            "In boosting, the next tree is fit to predict these residuals, not the original target value.",
            "New predictions: `y_pred_new = y_pred + learning_rate * weak_learner_predictions`."
        ],
        "solution": {
            "explanation": "Unlike bagging, where trees are trained independently in parallel, boosting builds trees sequentially. Each new tree corrects the errors (residuals) of the existing ensemble. The pseudo-residuals represent the negative gradient of the loss function with respect to the predictions. By fitting a weak learner to the residuals and adding its scaled predictions, we perform gradient descent in the function space.",
            "key_takeaways": [
                "Boosting is sequential, focusing on correcting previous model mistakes.",
                "Pseudo-residuals represent the negative gradient of the loss function."
            ]
        },
        "starter_code": {
            "python": "import numpy as np\n\ndef compute_pseudo_residuals(y_true, y_pred):\n    # TODO: Build residual calculator for MSE loss\n    pass\n\ndef mock_boosting_step(y_pred, weak_learner_preds, learning_rate):\n    # TODO: Build scaled additive update step\n    pass"
        },
        "expected_output": "Updated prediction vector close to target labels.",
        "follow_up_questions": [
            "What is the difference between AdaBoost and Gradient Boosting?",
            "How does learning rate (shrinkage) act as a regularizer in boosting?"
        ],
        "references": [
            {
                "title": "Greedy Function Approximation: A Gradient Boosting Machine",
                "url": "https://projecteuclid.org/journals/annals-of-statistics/volume-29/issue-5/Greedy-function-approximation-A-gradient-boosting-machine/10.1214/aos/1013203451.full"
            }
        ]
    })

    # Q36: K-Means Clustering
    questions.append({
        "id": 36,
        "slug": "k-means-clustering",
        "title": "Build a K-Means Convergence Step",
        "section": "Machine Learning",
        "difficulty": "Medium",
        "question_type": "coding",
        "tensortrack_skill": "Classical Machine Learning",
        "estimated_time_minutes": 15,
        "tags": ["clustering", "unsupervised-learning", "k-means"],
        "learning_objectives": [
            "Build the assignment and update steps of K-Means clustering",
            "Contrast standard random centroid initialization with K-Means++"
        ],
        "problem_statement": "Build a python function `kmeans_step(X, centroids)` that assigns data points to the closest centroid and recomputes the centroid coordinates as the mean of assigned points. Explain how K-Means++ prevents poor convergence.",
        "real_world_context": "K-Means is used for market segmentation, image compression, and generating initial document cluster labels for unlabeled customer feedback.",
        "hints": [
            "Compute distance from each point to all centroids using `np.linalg.norm(X[:, None] - centroids, axis=2)`.",
            "Find the closest centroid index using `np.argmin()`.",
            "Recompute each centroid as the mean of points assigned to it."
        ],
        "solution": {
            "explanation": "K-Means alternates between two steps: assigning points to the closest centroid (expectation) and updating centroids to the mean of assigned points (maximization). It is guaranteed to converge to a local minimum of the inertia objective (within-cluster sum-of-squares). However, poor initial placement of centroids can lead to suboptimal clustering. K-Means++ improves convergence by selecting initial centroids that are spaced far apart from each other.",
            "key_takeaways": [
                "K-Means is an expectation-maximization algorithm that minimizes inertia.",
                "K-Means++ initialization reduces convergence speed and guards against local minima."
            ]
        },
        "starter_code": {
            "python": "import numpy as np\n\ndef kmeans_step(X, centroids):\n    # X: (N, D), centroids: (K, D)\n    # TODO: Build coordinate assignment and mean update steps\n    pass"
        },
        "expected_output": "Updated centroid coordinates and class assignments array.",
        "follow_up_questions": [
            "Why is K-Means sensitive to scale, and what preprocessing is required?",
            "What is the difference between hard clustering (K-Means) and soft clustering (Gaussian Mixture Models)?"
        ],
        "references": [
            {
                "title": "K-Means++ Initialization Paper",
                "url": "http://ilpubs.stanford.edu:8090/778/1/2006-13.pdf"
            }
        ]
    })

    # Q37: Principal Component Analysis
    questions.append({
        "id": 37,
        "slug": "principal-component-analysis",
        "title": "Build a PCA Projection Engine",
        "section": "Machine Learning",
        "difficulty": "Medium",
        "question_type": "coding",
        "tensortrack_skill": "Classical Machine Learning",
        "estimated_time_minutes": 20,
        "tags": ["pca", "dimensionality-reduction", "linear-algebra"],
        "learning_objectives": [
            "Build a PCA dimension reducer via covariance eigen-decomposition",
            "Calculate explained variance ratio arrays for principal components"
        ],
        "problem_statement": "Build a python function `pca_projection(X, n_components)` that standardizes input data, calculates its covariance matrix, extracts the eigenvectors, and projects the data onto the top `n_components` principal components.",
        "real_world_context": "PCA is used to visualize high-dimensional data, reduce features for downstream models, and compress images or signals by removing redundant correlations.",
        "hints": [
            "Zero-center the data: `X_centered = X - np.mean(X, axis=0)`.",
            "Covariance matrix formula: `Cov = (X_centered.T @ X_centered) / (N - 1)`.",
            "Use `np.linalg.eig` or `np.linalg.eigh` (since Cov is symmetric) to get eigenvalues and eigenvectors. Sort them descending."
        ],
        "solution": {
            "explanation": "PCA projects data onto orthogonal axes that maximize variance. The first principal component is the direction of maximum variance. The eigenvalues of the covariance matrix represent the variance captured by each principal component. Standardizing data is critical because features with larger scales will otherwise dominate the covariance calculations and the resulting components.",
            "key_takeaways": [
                "PCA finds orthogonal directions of maximum variance in the feature space.",
                "Features must be scaled before PCA to prevent variables with large units from dominating."
            ]
        },
        "starter_code": {
            "python": "import numpy as np\n\ndef pca_projection(X, n_components=2):\n    # X: (N, D)\n    # TODO: Build standardizer, covariance math, sort eigenvectors, and project data\n    projected_data = None\n    explained_variance = None\n    return projected_data, explained_variance"
        },
        "expected_output": "A tuple of (projected matrix array of shape (N, n_components), explained variance ratio array).",
        "follow_up_questions": [
            "How does SVD (Singular Value Decomposition) relate to PCA, and why is it preferred numerically?",
            "Can PCA capture non-linear relationships in data? How can this be addressed?"
        ],
        "references": [
            {
                "title": "A Tutorial on Principal Component Analysis",
                "url": "https://arxiv.org/abs/1404.1100"
            }
        ]
    })

    # Q38: Classification Metrics
    questions.append({
        "id": 38,
        "slug": "classification-metrics",
        "title": "Build a Precision, Recall, and F1 Estimator",
        "section": "Machine Learning",
        "difficulty": "Medium",
        "question_type": "coding",
        "tensortrack_skill": "Classical Machine Learning",
        "estimated_time_minutes": 15,
        "tags": ["metrics", "classification", "evaluation"],
        "learning_objectives": [
            "Build basic metrics from raw confusion matrix parameters",
            "Contrast ROC-AUC and Precision-Recall AUC under severe class imbalance"
        ],
        "problem_statement": "Build a python function `compute_precision_recall_f1(y_true, y_pred)` that computes classification metrics from scratch. Explain why ROC-AUC can be misleadingly high on imbalanced datasets compared to PR-AUC.",
        "real_world_context": "In critical applications like cancer diagnosis or credit card fraud, a high accuracy or high ROC-AUC is meaningless if the model's actual precision (positive predictive value) is extremely low.",
        "hints": [
            "Precision = TP / (TP + FP). Recall = TP / (TP + FN).",
            "F1-score is the harmonic mean of precision and recall: `2 * (P * R) / (P + R)`.",
            "ROC-AUC plots True Positive Rate vs False Positive Rate. Under class imbalance, the vast number of True Negatives inflates the denominator of FPR, making it look artificially small."
        ],
        "solution": {
            "explanation": "ROC-AUC plots TPR against FPR. Since FPR = FP / (FP + TN), an enormous number of negative class instances (TN) drives the FPR close to zero, causing the ROC curve to look perfect even if there are many false positives. The Precision-Recall curve plots Precision against Recall. It does not include True Negatives in its calculations, making it much more sensitive to False Positives and a superior metric for highly imbalanced datasets.",
            "key_takeaways": [
                "ROC-AUC is insensitive to class distributions; PR-AUC is highly sensitive to class imbalance.",
                "Precision-Recall focus purely on the positive class performance."
            ]
        },
        "starter_code": {
            "python": "def compute_precision_recall_f1(y_true, y_pred):\n    # TODO: Build TP, FP, FN, TN counters and return precision, recall, f1 dict\n    pass"
        },
        "expected_output": "A dictionary containing the float metric values.",
        "follow_up_questions": [
            "Why do we use the harmonic mean instead of the arithmetic mean for F1-score?",
            "What is Cohen's Kappa, and how does it adjust for chance agreement?"
        ],
        "references": [
            {
                "title": "ROC vs PR Curves Comparison (ICML)",
                "url": "https://dl.acm.org/doi/10.1145/1143844.1143874"
            }
        ]
    })

    # Q39: Imbalanced Data Strategies
    questions.append({
        "id": 39,
        "slug": "imbalanced-data",
        "title": "Build a Weighted Cross-Entropy Loss Function",
        "section": "Machine Learning",
        "difficulty": "Medium",
        "question_type": "coding",
        "tensortrack_skill": "Classical Machine Learning",
        "estimated_time_minutes": 15,
        "tags": ["imbalanced-data", "smote", "class-weights"],
        "learning_objectives": [
            "Build class-weighted binary cross-entropy loss equations",
            "Explain how SMOTE creates synthetic samples"
        ],
        "problem_statement": "Build a python function `weighted_cross_entropy(y_true, y_pred, weight_0, weight_1)` that penalizes minority errors higher during calculation. Explain how SMOTE generates new samples using nearest-neighbor interpolation.",
        "real_world_context": "In content moderation pipelines, toxic posts represent <1% of total comments. Using weighted loss functions ensures the model prioritizes identifying toxic content rather than optimizing overall accuracy.",
        "hints": [
            "Weighted cross-entropy formula: `-1/N * sum(weight_1 * y * log(p) + weight_0 * (1 - y) * log(1 - p))`.",
            "SMOTE selects a minority class sample, finds its k-nearest neighbors, selects one neighbor, and creates a synthetic point along the line segment connecting them."
        ],
        "solution": {
            "explanation": "Weighted loss functions assign higher penalty coefficients to minority class errors during gradient updates, forcing the decision boundary away from the minority class. SMOTE avoids overfitting caused by simple oversampling (duplicating instances, which causes the decision boundary to wrap around specific points) by interpolating between nearest neighbors in the feature space, producing realistic synthetic examples.",
            "key_takeaways": [
                "Class weighting adjusts the loss gradient magnitude to balance class representation.",
                "SMOTE synthetically interpolates between minority class neighbors, avoiding simple duplication overfitting."
            ]
        },
        "starter_code": {
            "python": "import numpy as np\n\ndef weighted_cross_entropy(y_true, y_pred, weight_0, weight_1):\n    # TODO: Build weighted binary cross entropy calculator\n    pass"
        },
        "expected_output": "Float loss value.",
        "follow_up_questions": [
            "Why should you apply SMOTE ONLY to the training set and never to the validation or test sets?",
            "What is Focal Loss, and how does it dynamically scale loss based on prediction confidence?"
        ],
        "references": [
            {
                "title": "SMOTE: Synthetic Minority Over-sampling Technique",
                "url": "https://arxiv.org/abs/1106.1813"
            }
        ]
    })

    # Q40: Hyperparameter Tuning
    questions.append({
        "id": 40,
        "slug": "hyperparameter-tuning",
        "title": "Build a Random Search Parameter Sampler",
        "section": "Machine Learning",
        "difficulty": "Medium",
        "question_type": "coding",
        "tensortrack_skill": "Classical Machine Learning",
        "estimated_time_minutes": 15,
        "tags": ["hyperparameter-tuning", "bayesian-optimization", "random-search"],
        "learning_objectives": [
            "Build a random parameter distribution sampler",
            "Contrast search efficiencies of Grid Search, Random Search, and Bayesian Optimization"
        ],
        "problem_statement": "Build a python function `random_search_sampler(param_grid, n_iter)` that yields random hyperparameter combinations from a dictionary of distributions and lists. Explain why random search is more efficient than grid search.",
        "real_world_context": "Tuning deep neural networks is expensive, with single training runs taking days. Understanding search efficiency saves compute costs and finds better model configurations.",
        "hints": [
            "Use the `random` module to sample from lists or continuous uniform distributions.",
            "Grid search tests all combinations, testing redundant values on unimportant parameters. Random search tests unique values on all dimensions."
        ],
        "solution": {
            "explanation": "In many ML tasks, only a few hyperparameters (e.g. learning rate) have a large impact on performance, while others have minimal impact. Grid search tests redundant values because it fixes parameters on a grid. Random search tests unique values along all parameter dimensions, discovering better configurations in fewer iterations. Bayesian optimization improves on this by modeling the parameter-space performance using a Gaussian Process surrogate model to choose the next parameters strategically.",
            "key_takeaways": [
                "Random search is more efficient than grid search in high-dimensional spaces.",
                "Bayesian optimization utilizes acquisition functions to balance exploration of parameter spaces vs exploitation of known good areas."
            ]
        },
        "starter_code": {
            "python": "import random\n\ndef random_search_sampler(param_grid, n_iter=10):\n    # param_grid: dict where values are list of choices or tuple (min, max) for float uniform\n    # TODO: Build generator yielding random sampled combinations\n    pass"
        },
        "expected_output": "Yields dictionaries of sampled parameter values.",
        "follow_up_questions": [
            "What is the role of an acquisition function (e.g. Expected Improvement) in Bayesian optimization?",
            "How does Hyperband improve hyperparameter search efficiency by using early stopping?"
        ],
        "references": [
            {
                "title": "Random Search for Hyper-Parameter Optimization",
                "url": "https://www.jmlr.org/papers/volume13/bergstra12a/bergstra12a.pdf"
            }
        ]
    })

    # Q41: Feature Engineering
    questions.append({
        "id": 41,
        "slug": "feature-engineering-target-encoding",
        "title": "Build a Smoothed Target Encoder",
        "section": "Machine Learning",
        "difficulty": "Medium",
        "question_type": "coding",
        "tensortrack_skill": "Classical Machine Learning",
        "estimated_time_minutes": 20,
        "tags": ["feature-engineering", "data-preprocessing", "target-encoding"],
        "learning_objectives": [
            "Build a target encoder for high-cardinality categorical variables",
            "Incorporate a smoothing factor using global target statistics"
        ],
        "problem_statement": "Build a python function `target_encode(train_df, val_df, cat_col, target_col, smoothing)` that replaces categories with their expected target means, regularized by the global mean and a smoothing weight.",
        "real_world_context": "When predicting click-through rate, features like `zip_code` or `device_model` can have thousands of distinct values. One-hot encoding would create a massive, sparse matrix, whereas target encoding keeps representation compact.",
        "hints": [
            "Smoothing formula: `S = (n * group_mean + smoothing * global_mean) / (n + smoothing)`.",
            "Map the computed dictionary of smoothed means from the train dataframe onto both train and validation dataframes."
        ],
        "solution": {
            "explanation": "Target encoding replaces categorical values with the expected target value for that category. For high-cardinality variables, this provides a highly informative 1D feature. However, categories with very few samples can lead to extreme estimates and overfitting. Applying smoothing weights the category average with the global average based on the category's sample size, regularizing small groups.",
            "key_takeaways": [
                "Target encoding represents high-cardinality categories efficiently without dimensionality explosion.",
                "Smoothing regularizes encoding for rare classes by shrinking estimates toward the global mean."
            ]
        },
        "starter_code": {
            "python": "import pandas as pd\n\ndef target_encode(train_df, val_df, cat_col, target_col, smoothing=10):\n    # TODO: Build target encoder mapping smoothed statistics onto train and val DFs\n    pass"
        },
        "expected_output": "Encoded versions of the train and validation dataframes.",
        "follow_up_questions": [
            "How does target encoding introduce the risk of data leakage during cross-validation?",
            "What is the difference between target encoding and frequency encoding?"
        ],
        "references": [
            {
                "title": "Target Encoding Smoothing Details",
                "url": "https://maxhalford.github.io/blog/target-encoding/"
            }
        ]
    })

    # Q42: XGBoost Architecture Optimization
    questions.append({
        "id": 42,
        "slug": "xgboost-architecture",
        "title": "Build an XGBoost Split Gain Calculator",
        "section": "Machine Learning",
        "difficulty": "Hard",
        "question_type": "coding",
        "tensortrack_skill": "Classical Machine Learning",
        "estimated_time_minutes": 25,
        "tags": ["xgboost", "tree-boosting", "gradient-boosting-math"],
        "learning_objectives": [
            "Build a split-finding gain evaluator incorporating gradient and hessian parameters",
            "Explain the role of L2 regularization in the XGBoost objective function"
        ],
        "problem_statement": "Build a python function `calculate_xgboost_split_gain(g_left, h_left, g_right, h_right, reg_lambda)` that calculates the split gain using first-order (`g_i`) and second-order (`h_i`) gradients with regularization `lambda`. Outline the mathematical proof.",
        "real_world_context": "XGBoost's custom split-finding math allows it to handle arbitrary loss functions (by approximating them via Taylor expansion) and evaluate splits extremely fast in distributed systems.",
        "hints": [
            "The optimal weight of leaf j is `w_j* = -sum(g_i) / (sum(h_i) + lambda)`.",
            "The optimal objective value of the tree is `Obj = -0.5 * sum((sum(g_i))^2 / (sum(h_i) + lambda)) + gamma * T`.",
            "Split gain formula is: `Gain = 0.5 * [ (G_L^2 / (H_L + lambda)) + (G_R^2 / (H_R + lambda)) - ((G_L + G_R)^2 / (H_L + H_R + lambda)) ] - gamma`."
        ],
        "solution": {
            "explanation": "XGBoost approximates the loss function using a second-order Taylor expansion: `L^t approx sum(l(y_i, y_hat^(t-1)) + g_i * f_t(x_i) + 0.5 * h_i * f_t^2(x_i)) + reg`. By defining the tree structure and minimizing this quadratic formula, it derives the optimal leaf weights and the best split criteria. The split gain compares the objective score of the child nodes against the parent node, incorporating L2 weight regularization (`lambda`).",
            "key_takeaways": [
                "XGBoost uses Taylor expansion to support custom loss functions via gradient and hessian values.",
                "Split evaluations incorporate weight regularization directly in the gain formula."
            ]
        },
        "starter_code": {
            "python": "def calculate_xgboost_split_gain(g_left, h_left, g_right, h_right, reg_lambda=1.0, gamma=0.0):\n    # g_left: sum of gradients in left leaf, h_left: sum of hessians\n    # TODO: Build the split gain evaluator\n    gain = 0.0\n    return gain"
        },
        "expected_output": "Float gain value representing split quality.",
        "follow_up_questions": [
            "How does XGBoost handle missing values automatically during split evaluations?",
            "What is the role of the shrinkage parameter (eta) in XGBoost updates?"
        ],
        "references": [
            {
                "title": "XGBoost: A Scalable Tree Boosting System",
                "url": "https://arxiv.org/abs/1603.02754"
            }
        ]
    })

    # Q43: Naive Bayes & Laplace Smoothing
    questions.append({
        "id": 43,
        "slug": "naive-bayes-laplace-smoothing",
        "title": "Build a Naive Bayes Classifier with Laplace Smoothing",
        "section": "Machine Learning",
        "difficulty": "Hard",
        "question_type": "coding",
        "tensortrack_skill": "Classical Machine Learning",
        "estimated_time_minutes": 20,
        "tags": ["naive-bayes", "probability", "laplace-smoothing"],
        "learning_objectives": [
            "Build a Multinomial Naive Bayes classifier utilizing log-likelihood additions",
            "Incorporate Laplace smoothing to resolve the zero-frequency problem"
        ],
        "problem_statement": "Build a python function `naive_bayes_predict(word_counts, class_priors, word_probs, vocabulary_size, smoothing)` that classifies text documents using Log-Likelihood additions and incorporates Laplace (add-one) smoothing.",
        "real_world_context": "Naive Bayes classifiers are highly efficient baselines for spam filtering, sentiment analysis, and topic classification due to their speed and minimal data requirements.",
        "hints": [
            "The conditional independence assumption states that features are independent given the class label: P(x1, x2 | y) = P(x1 | y) * P(x2 | y).",
            "Without smoothing, if a word is never seen in a class during training, `P(word | class) = 0`, making the entire product probability 0. We use logs to prevent underflow: `sum(log(P(word | class)))`.",
            "Laplace smoothing formula: `P(w | class) = (count(w, class) + alpha) / (total_words_in_class + alpha * vocabulary_size)`."
        ],
        "solution": {
            "explanation": "Naive Bayes is called 'naive' because it assumes all input features are independent given the class label. In reality, words in a text are highly correlated (e.g. 'deep' and 'learning'). Despite this, it performs well because classification decisions only require the correct relative ordering of class probabilities, not exact probability values. Laplace smoothing adds a small pseudo-count `alpha` (usually 1) to all classes, ensuring no probability is ever zero.",
            "key_takeaways": [
                "The independence assumption simplifies high-dimensional joint probability calculations.",
                "Laplace smoothing prevents zero probability outcomes for unseen features."
            ]
        },
        "starter_code": {
            "python": "import numpy as np\n\ndef naive_bayes_predict(doc_word_counts, class_priors, word_counts_by_class, total_words_by_class, vocab_size, alpha=1.0):\n    # TODO: Build log-likelihood + prior classifier using Laplace smoothing\n    pass"
        },
        "expected_output": "The class label with the highest computed log-posterior probability.",
        "follow_up_questions": [
            "Why do we perform additions of log-probabilities instead of multiplying raw probabilities in Naive Bayes implementations?",
            "How does Gaussian Naive Bayes differ from Multinomial Naive Bayes?"
        ],
        "references": [
            {
                "title": "Naive Bayes Classification (Stanford CS124)",
                "url": "https://web.stanford.edu/~jurafsky/slp3/4.pdf"
            }
        ]
    })

    # Q44: Expectation Maximization (GMM)
    questions.append({
        "id": 44,
        "slug": "expectation-maximization",
        "title": "Build a GMM Expectation Step",
        "section": "Machine Learning",
        "difficulty": "Hard",
        "question_type": "coding",
        "tensortrack_skill": "Classical Machine Learning",
        "estimated_time_minutes": 25,
        "tags": ["gmm", "expectation-maximization", "unsupervised-learning"],
        "learning_objectives": [
            "Build the E-step (responsibility calculations) of a GMM model",
            "Trace parameter updates inside the Expectation-Maximization loop"
        ],
        "problem_statement": "Build a python function `gmm_e_step(X, weights, means, covariances)` that computes the cluster membership responsibilities (posterior probabilities) for all data points under a Gaussian Mixture Model.",
        "real_world_context": "GMMs are used for soft clustering (e.g., classifying audio segments, anomalies, or user behavior cohorts) where points can belong to multiple clusters with varying probabilities.",
        "hints": [
            "Use `scipy.stats.multivariate_normal` to compute the probability density of a point given a mean and covariance.",
            "The responsibility of component k for point i is: `gamma_ik = weight_k * N(x_i | mean_k, cov_k) / sum(weight_j * N(x_i | mean_j, cov_j))`."
        ],
        "solution": {
            "explanation": "When models contain hidden or latent variables (like cluster identities), the log-likelihood function cannot be maximized directly. The EM algorithm solves this iteratively. The E-step estimates the values of the latent variables using current parameters (responsibility calculation). The M-step updates the parameters (means, covariances, mixing weights) to maximize the expected log-likelihood under those estimated latent states.",
            "key_takeaways": [
                "EM provides a framework for parameter estimation in models with latent variables.",
                "E-step calculates cluster memberships; M-step updates cluster shapes and positions."
            ]
        },
        "starter_code": {
            "python": "import numpy as np\nfrom scipy.stats import multivariate_normal\n\ndef gmm_e_step(X, weights, means, covariances):\n    # X: (N, D)\n    # weights: (K,)\n    # means: (K, D)\n    # covariances: (K, D, D)\n    # TODO: Build responsibility calculation matrix of shape (N, K)\n    responsibilities = None\n    return responsibilities"
        },
        "expected_output": "A numpy array of shape (N, K) where rows sum to 1.0.",
        "follow_up_questions": [
            "Why is the EM algorithm guaranteed to increase or maintain the log-likelihood at each iteration?",
            "What happens if the covariance matrix of a GMM component collapses to zero variance during updates?"
        ],
        "references": [
            {
                "title": "Expectation-Maximization (Stanford CS229)",
                "url": "https://cs229.stanford.edu/notes2021fall/cs229-notes8.pdf"
            }
        ]
    })

    # Q45: Kernel PCA & Manifold Learning
    questions.append({
        "id": 45,
        "slug": "kernel-pca-manifold-learning",
        "title": "Build a Kernel Matrix Centering Utility",
        "section": "Machine Learning",
        "difficulty": "Hard",
        "question_type": "coding",
        "tensortrack_skill": "Classical Machine Learning",
        "estimated_time_minutes": 25,
        "tags": ["manifold-learning", "t-sne", "umap", "kernel-pca"],
        "learning_objectives": [
            "Build a kernel matrix centering function for high-dimensional spaces",
            "Contrast topological assumptions of t-SNE vs UMAP"
        ],
        "problem_statement": "Build a python function `kernel_pca_matrix(K)` that centers the kernel matrix `K` in high-dimensional reproducing kernel Hilbert spaces. Explain the mathematical differences between t-SNE and UMAP regarding global structure retention.",
        "real_world_context": "Visualizing high-dimensional embeddings (e.g. LLM token embeddings or single-cell RNA sequences) requires non-linear projections like t-SNE or UMAP to group similar concepts together.",
        "hints": [
            "To center a kernel matrix K: `K_centered = K - I_N * K - K * I_N + I_N * K * I_N`, where `I_N = 1/N * np.ones((N, N))`.",
            "t-SNE uses Student-t distributions to model local probabilities and minimizes KL divergence via gradient descent. This struggles to preserve global structures.",
            "UMAP uses fuzzy simplicial sets, modeling geometry on Riemannian manifolds, preserving local and global structures while running faster."
        ],
        "solution": {
            "explanation": "Kernel PCA maps features into a high-dimensional reproducing kernel Hilbert space (RKHS) and performs PCA. The kernel matrix must be centered to ensure the projection coordinates are centered. t-SNE maps high-dimensional similarities to probabilities and optimizes low-dimensional placements using a Student-t distribution to solve the crowding problem, minimizing KL divergence. UMAP models local structures on a Riemannian manifold, mapping similarities to fuzzy relations and optimizing coordinates via cross-entropy loss, which preserves global distances better and executes much faster.",
            "key_takeaways": [
                "Kernel PCA centers the kernel matrix to ensure orthogonal projections in RKHS.",
                "t-SNE preserves local clusters via KL divergence; UMAP preserves global and local relations via cross-entropy."
            ]
        },
        "starter_code": {
            "python": "import numpy as np\n\ndef kernel_pca_matrix(K):\n    # K: (N, N) kernel matrix\n    # TODO: Build centering matrix calculation and apply to K\n    K_centered = None\n    return K_centered"
        },
        "expected_output": "Centered kernel matrix of shape (N, N).",
        "follow_up_questions": [
            "What is the significance of the perplexity hyperparameter in t-SNE?",
            "Why is t-SNE not suitable for reducing dimensions of features prior to feeding a machine learning classifier?"
        ],
        "references": [
            {
                "title": "Visualizing Data using t-SNE",
                "url": "https://www.jmlr.org/papers/volume9/vandermaaten08a/vandermaaten08a.pdf"
            },
            {
                "title": "UMAP: Uniform Manifold Approximation and Projection",
                "url": "https://arxiv.org/abs/1802.03426"
            }
        ]
    })
    
    return questions
