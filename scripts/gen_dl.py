def get_questions():
    questions = []
    
    # Q46: Perceptron and Activations
    questions.append({
        "id": 46,
        "slug": "perceptron-neural-network-basics",
        "title": "Build Neural Activation Functions",
        "section": "Deep Learning",
        "difficulty": "Easy",
        "question_type": "coding",
        "neuroforge_skill": "Deep Learning Architecture",
        "estimated_time_minutes": 10,
        "tags": ["neural-networks", "activations", "foundations"],
        "learning_objectives": [
            "Build ReLU and its derivative calculation mathematically",
            "Explain why non-linear activation functions are necessary in deep networks"
        ],
        "problem_statement": "Build a python function `relu(x)` and `relu_derivative(x)` that computes the Rectified Linear Unit and its derivative for a numpy array. Explain why stacking multiple linear layers without activation functions collapses into a single linear model.",
        "real_world_context": "ReLU is the default activation function in computer vision and transformer models because it does not suffer from vanishing gradients in the positive domain, making training much faster.",
        "hints": [
            "ReLU(x) = max(0, x). The derivative is 1 for x > 0 and 0 for x <= 0.",
            "Recall that multiplying matrices represents linear transformations: `W2 * (W1 * x) = (W2 * W1) * x = W_effective * x`."
        ],
        "solution": {
            "explanation": "If we do not apply a non-linear activation function between layers, a network of any depth collapses into a single linear transformation: `y = W3 * (W2 * (W1 * x + b1) + b2) + b3 = W_eff * x + b_eff`. Non-linear activations allow the network to approximate arbitrary continuous functions (Universal Approximation Theorem).",
            "key_takeaways": [
                "Without non-linear activations, neural networks cannot model non-linear relationships.",
                "ReLU avoids vanishing gradients for positive inputs but can lead to 'dying neurons' if weights update such that they never activate."
            ]
        },
        "starter_code": {
            "python": "import numpy as np\n\ndef relu(x):\n    # TODO: Build ReLU activation function\n    pass\n\ndef relu_derivative(x):\n    # TODO: Build derivative of ReLU\n    pass"
        },
        "expected_output": "Numpy arrays of transformed values.",
        "follow_up_questions": [
            "How does Leaky ReLU address the 'dying ReLU' problem?",
            "What is the output range of the Tanh activation function?"
        ],
        "references": [
            {
                "title": "Deep Learning Activation Functions (DeepLearning.AI)",
                "url": "https://www.deeplearning.ai/resources/activation-functions/"
            }
        ]
    })
    
    # Q47: Forward Propagation
    questions.append({
        "id": 47,
        "slug": "forward-propagation",
        "title": "Build a Two-Layer Neural Forward Pass",
        "section": "Deep Learning",
        "difficulty": "Easy",
        "question_type": "coding",
        "neuroforge_skill": "Deep Learning Architecture",
        "estimated_time_minutes": 10,
        "tags": ["neural-networks", "forward-pass", "shapes"],
        "learning_objectives": [
            "Build weight dot products and bias additions for forward passes",
            "Map dimensions across multiple feed-forward layers"
        ],
        "problem_statement": "Build a python function `forward_pass(X, W1, b1, W2, b2)` that computes the output of a 2-layer Feed-Forward Neural Network. The first layer uses ReLU activation; the second layer is a linear projection.",
        "real_world_context": "Understanding weight shapes is the first step in debugging model declaration errors in PyTorch or TensorFlow, where mismatching dimensions cause compile-time failures.",
        "hints": [
            "Layer 1 output is `H = relu(X @ W1 + b1)`.",
            "Layer 2 output is `Y = H @ W2 + b2`.",
            "Ensure shapes match: X is (N, D), W1 is (D, H_dim), b1 is (H_dim,), W2 is (H_dim, O_dim), b2 is (O_dim,)."
        ],
        "solution": {
            "explanation": "Forward propagation is a series of matrix multiplications followed by non-linear activations. In batch processing, if `X` has shape `(N, D)` and we multiply by `W1` of shape `(D, H_dim)`, the resulting matrix is `(N, H_dim)`. Biases are added using numpy broadcasting. This shape matching must be preserved across all layers in the architecture.",
            "key_takeaways": [
                "Forward propagation passes inputs through weights, biases, and activations.",
                "Broadcasting allows adding bias vectors directly to batch matrices."
            ]
        },
        "starter_code": {
            "python": "import numpy as np\n\ndef relu(x):\n    return np.maximum(0, x)\n\ndef forward_pass(X, W1, b1, W2, b2):\n    # TODO: Build forward pass computations through both layers\n    pass"
        },
        "expected_output": "Numpy array output representing predictions.",
        "follow_up_questions": [
            "How does batch size affect the dimensions of intermediate activations?",
            "What is the mathematical definition of broadcasting in NumPy?"
        ],
        "references": [
            {
                "title": "Neural Networks Part 1 (Stanford CS231n)",
                "url": "https://cs231n.github.io/neural-networks-1/"
            }
        ]
    })

    # Q48: Backpropagation
    questions.append({
        "id": 48,
        "slug": "backpropagation",
        "title": "Build a Backpropagation Gradient Calculator",
        "section": "Deep Learning",
        "difficulty": "Easy",
        "question_type": "coding",
        "neuroforge_skill": "Deep Learning Architecture",
        "estimated_time_minutes": 15,
        "tags": ["backpropagation", "gradients", "math"],
        "learning_objectives": [
            "Build gradient calculators using chain rule derivations",
            "Implement a backward pass step for a single hidden layer"
        ],
        "problem_statement": "Build a python function `backward_pass(X, h, y_pred, y_true, W2)` that computes the gradients of a Mean Squared Error loss with respect to the output weights `W2` and hidden weights `W1`. Assume the hidden layer output is `h` (after ReLU) and the output is linear: `y_pred = h @ W2`.",
        "real_world_context": "Although PyTorch handles backpropagation automatically via Autograd, understanding these derivatives is essential when writing custom cuda kernels, designing custom loss functions, or debugging gradient flow.",
        "hints": [
            "Let `d_loss/d_ypred = 2/N * (y_pred - y_true)`.",
            "Gradient for W2: `dW2 = h.T @ d_loss/d_ypred`.",
            "Gradient for W1: First find `d_loss/d_h = d_loss/d_ypred @ W2.T`. Then multiply by the derivative of ReLU: `d_loss/d_z1 = d_loss/d_h * (h > 0)`. Finally, `dW1 = X.T @ d_loss/d_z1`."
        ],
        "solution": {
            "explanation": "Backpropagation computes the gradient of the loss function with respect to the weights of the network, working backward from the output layer. This is accomplished using the chain rule of calculus. First, we compute the gradient of the loss at the output layer. We then project this gradient back through the weight matrix W2, multiply by the local derivative of the ReLU activation (which is 1 for positive values, 0 otherwise), and compute the gradient with respect to W1.",
            "key_takeaways": [
                "Backpropagation calculates gradients by propagating loss errors backward using the chain rule.",
                "Gradients of weights depend on activation values from the forward pass."
            ]
        },
        "starter_code": {
            "python": "import numpy as np\n\ndef backward_pass(X, h, y_pred, y_true, W2):\n    # X: (N, D), h: (N, H), y_pred: (N, O), y_true: (N, O), W2: (H, O)\n    # TODO: Build gradients calculation for both weight matrices (dW1, dW2)\n    dW2 = None\n    dW1 = None\n    return dW1, dW2"
        },
        "expected_output": "A tuple of numpy arrays representing gradients (dW1, dW2).",
        "follow_up_questions": [
            "Why do we cache activation values during the forward pass of a neural network?",
            "How does backpropagation handle nodes with multiple outgoing branches?"
        ],
        "references": [
            {
                "title": "Backpropagation Calculus (Stanford CS231n)",
                "url": "https://cs231n.github.io/optimization-2/"
            }
        ]
    })

    # Q49: Loss Functions
    questions.append({
        "id": 49,
        "slug": "loss-functions",
        "title": "Build a Softmax Cross-Entropy Loss Gradient Solver",
        "section": "Deep Learning",
        "difficulty": "Easy",
        "question_type": "coding",
        "neuroforge_skill": "Deep Learning Architecture",
        "estimated_time_minutes": 10,
        "tags": ["loss-functions", "cross-entropy", "gradients"],
        "learning_objectives": [
            "Build cross-entropy loss gradients for softmax outputs",
            "Explain how cross-entropy loss bypasses vanishing gradients in classification tasks"
        ],
        "problem_statement": "Build a python function `softmax_cross_entropy_gradient(probs, targets)` that calculates the derivative of the categorical cross-entropy loss with respect to the input logits (pre-softmax activations). Explain why MSE loss paired with Sigmoid outputs leads to vanishing gradients.",
        "real_world_context": "Using MSE for classification models causes slow convergence during early training phases because incorrect predictions get stuck in the flat saturated regions of the Sigmoid curve.",
        "hints": [
            "Sigmoid derivative is `sigma'(z) = sigma(z) * (1 - sigma(z))`.",
            "For MSE: `L = 0.5 * (sigma(z) - y)^2`. The derivative with respect to z is `(sigma(z) - y) * sigma(z) * (1 - sigma(z))`. If y=1 and sigma(z)=0 (highly incorrect), the gradient is 0 because of the `sigma(z)` term.",
            "For Cross-Entropy: `L = -y * log(sigma(z)) - (1 - y) * log(1 - sigma(z))`. The derivative with respect to z simplifies to `sigma(z) - y` (the error), which is proportional to the discrepancy."
        ],
        "solution": {
            "explanation": "Pairing Sigmoid with MSE yields a gradient containing the term `sigma(z)*(1 - sigma(z))`. When the prediction is highly wrong (e.g. z is very negative, but y=1), this term approaches 0, saturating the neuron and halting weight updates. Cross-Entropy loss cancels this term out during derivation, resulting in a gradient of `y_pred - y_true`. This ensures that the further the model is from the correct label, the larger the update step it takes.",
            "key_takeaways": [
                "Cross-Entropy cancels out the derivative of sigmoid/softmax, preventing gradient saturation.",
                "MSE is suited for regression; Cross-Entropy is suited for classification."
            ]
        },
        "starter_code": {
            "python": "import numpy as np\n\ndef softmax_cross_entropy_gradient(probs, targets):\n    # probs: (N, K) softmax output probabilities\n    # targets: (N, K) one-hot encoded targets\n    # TODO: Build loss gradient with respect to logits\n    pass"
        },
        "expected_output": "Numpy array of shape (N, K) containing gradients.",
        "follow_up_questions": [
            "What is the mathematical formulation of Kullback-Leibler (KL) divergence, and how does it relate to Cross-Entropy?",
            "Why is the Softmax function preferred over Sigmoid for multi-class classification?"
        ],
        "references": [
            {
                "title": "Cross-Entropy Loss (DeepLearning.AI)",
                "url": "https://www.deeplearning.ai/resources/cross-entropy/"
            }
        ]
    })

    # Q50: Vanishing and Exploding Gradients
    questions.append({
        "id": 50,
        "slug": "vanishing-exploding-gradients",
        "title": "Build a Gradient Norm Health Checker",
        "section": "Deep Learning",
        "difficulty": "Easy",
        "question_type": "coding",
        "neuroforge_skill": "Deep Learning Architecture",
        "estimated_time_minutes": 15,
        "tags": ["gradients", "vanishing-gradients", "resnet"],
        "learning_objectives": [
            "Build a diagnostic tool detecting gradient health across layers",
            "Identify how ResNet residual connections bypass vanishing gradient loops"
        ],
        "problem_statement": "Build a python function `check_gradient_norms(gradients, min_threshold, max_threshold)` that calculates the Frobenius norm of each layer's gradient matrix and classifies the network state ('normal', 'vanishing', 'exploding'). Explain how ResNet shortcuts resolve vanishing issues.",
        "real_world_context": "Before ResNets, training neural networks with more than 20 layers was impossible because the gradients became too small to update early layers. Residual connections enabled models to scale to hundreds of layers.",
        "hints": [
            "Gradients of deep networks involve products of layer weights and activation derivatives due to the chain rule.",
            "If weights are initialized too small, or activations saturate (like Sigmoid), product terms scale as `c^L` where `c < 1`.",
            "For ResNets, `dy/dx = dF/dx + 1`. The added `+1` term guarantees that gradients propagate back to earlier layers even if `dF/dx` vanishes."
        ],
        "solution": {
            "explanation": "During backpropagation, gradients are multiplied by weight matrices and activation derivatives at each layer. If these terms are smaller than 1.0 (e.g. Sigmoid derivative max is 0.25), the gradient decays exponentially with depth, meaning early layers receive no updates. If weights are large, gradients grow exponentially (exploding). ResNet's residual connection `y = F(x) + x` adds a constant 1 to the derivative: `dLoss/dx = dLoss/dy * (dF/dx + 1)`. Even if `dF/dx` approaches zero, the gradient flows directly back via the `+ 1` term.",
            "key_takeaways": [
                "Vanishing gradients occur when multiplying many small values during backpropagation.",
                "Residual connections allow gradients to flow unimpeded through the shortcut connections, avoiding exponential decay."
            ]
        },
        "starter_code": {
            "python": "import numpy as np\n\ndef check_gradient_norms(gradients, min_threshold=1e-5, max_threshold=100.0):\n    # gradients: list of numpy arrays representing layer gradients\n    # TODO: Compute Frobenius norm for each layer and return health category\n    pass"
        },
        "expected_output": "A string status indicator.",
        "follow_up_questions": [
            "How does Xavier (Glorot) initialization help prevent vanishing gradients at the start of training?",
            "What is Gradient Clipping, and when should you use it?"
        ],
        "references": [
            {
                "title": "Deep Residual Learning for Image Recognition",
                "url": "https://arxiv.org/abs/1512.03385"
            }
        ]
    })

    # Q51: Optimizers
    questions.append({
        "id": 51,
        "slug": "optimizers-adam-momentum",
        "title": "Build an Adam Optimizer Update Step",
        "section": "Deep Learning",
        "difficulty": "Medium",
        "question_type": "coding",
        "neuroforge_skill": "Deep Learning Architecture",
        "estimated_time_minutes": 20,
        "tags": ["optimizers", "adam", "sgd-momentum"],
        "learning_objectives": [
            "Build the mathematical update step for the Adam optimizer",
            "Incorporate bias corrections to compensate for zero initialization states"
        ],
        "problem_statement": "Build a python function `adam_update(w, g, m, v, t, lr, beta1, beta2, eps)` that updates weight parameter vector `w` based on Adam update equations, including first and second moment updates and bias corrections.",
        "real_world_context": "Adam is the standard optimizer used to train LLMs (like GPT) and deep reinforcement learning systems because it adapts learning rates per parameter, handling sparse gradients.",
        "hints": [
            "First moment update: `m = beta1 * m + (1 - beta1) * g`.",
            "Second moment update: `v = beta2 * v + (1 - beta2) * g^2`.",
            "Bias correction: `m_hat = m / (1 - beta1^t)`, `v_hat = v / (1 - beta2^t)`.",
            "Weight update: `w = w - lr * m_hat / (sqrt(v_hat) + eps)`."
        ],
        "solution": {
            "explanation": "Adam (Adaptive Moment Estimation) combines momentum (damping oscillations by keeping a running average of gradients) and RMSProp (scaling steps inversely by the running average of squared gradients). The bias corrections `1 - beta^t` are necessary because `m` and `v` are initialized to zero, causing them to be biased toward zero during early training steps (when t is small).",
            "key_takeaways": [
                "Momentum tracks the direction of weight updates; RMSProp scales learning rates per weight based on gradient variance.",
                "Bias correction adjusts moments during early steps to compensate for zero initialization."
            ]
        },
        "starter_code": {
            "python": "import numpy as np\n\ndef adam_update(w, g, m, v, t, lr=0.001, beta1=0.9, beta2=0.999, eps=1e-8):\n    # w, g, m, v: numpy arrays representing weights, gradients, first moments, second moments\n    # t: current training step integer\n    # TODO: Build first/second moments, bias corrections, and update w\n    pass"
        },
        "expected_output": "A tuple of numpy arrays (updated_w, updated_m, updated_v).",
        "follow_up_questions": [
            "Why is the epsilon parameter included in the denominator of the Adam update step?",
            "What is AdamW, and why is it preferred over Adam for models with L2 weight decay?"
        ],
        "references": [
            {
                "title": "Adam: A Method for Stochastic Optimization",
                "url": "https://arxiv.org/abs/1412.6980"
            }
        ]
    })

    # Q52: Regularization and Dropout
    questions.append({
        "id": 52,
        "slug": "regularization-dropout",
        "title": "Build an Inverted Dropout Layer",
        "section": "Deep Learning",
        "difficulty": "Medium",
        "question_type": "coding",
        "neuroforge_skill": "Deep Learning Architecture",
        "estimated_time_minutes": 15,
        "tags": ["regularization", "dropout", "inference"],
        "learning_objectives": [
            "Build an Inverted Dropout layer for deep models",
            "Explain why scaling activations during training simplifies inference evaluation"
        ],
        "problem_statement": "Build a python function `dropout_layer(x, drop_prob, training)` that applies inverted dropout to activations. Scale the surviving activations during training to keep the evaluation mode untouched.",
        "real_world_context": "Dropout prevents co-adaptation of features in fully connected layers, forcing the network to learn redundant representations, which improves generalization.",
        "hints": [
            "In training mode, generate a binary mask where a class is set to 0 with probability `drop_prob`, and 1 otherwise.",
            "For Inverted Dropout, scale the active values by dividing by `(1 - drop_prob)` during training.",
            "During inference (`training=False`), return the input activations unchanged."
        ],
        "solution": {
            "explanation": "Standard dropout zero-out features with probability `p` during training, meaning the expected value of activations drops to `(1 - p)*E[x]` at inference. To compensate, early implementations scaled weights by `(1 - p)` during inference. Inverted dropout scales the activations by dividing by `(1 - p)` during training instead. This keeps the expected activation scale constant, meaning the model can be evaluated at inference without performing any extra computations or modifications.",
            "key_takeaways": [
                "Inverted dropout scales training activations by 1/(1-p) to keep expectations constant.",
                "Dropout acts as an ensemble technique by implicitly training exponential variations of sub-networks."
            ]
        },
        "starter_code": {
            "python": "import numpy as np\n\ndef dropout_layer(x, drop_prob, training=True):\n    # x: numpy array of activations\n    # TODO: Build inverted dropout layer logic\n    pass"
        },
        "expected_output": "Numpy array with scaled activations (some zeroed out if training=True, otherwise unchanged).",
        "follow_up_questions": [
            "Why does PyTorch require calling `model.eval()` before running validation or inference?",
            "Can dropout be used during inference to estimate model uncertainty? What is this technique called?"
        ],
        "references": [
            {
                "title": "Dropout: A Simple Way to Prevent Neural Networks from Overfitting",
                "url": "https://jmlr.org/papers/v15/srivastava14a.html"
            }
        ]
    })

    # Q53: Batch Normalization
    questions.append({
        "id": 53,
        "slug": "batch-normalization",
        "title": "Build a Batch Normalization Forward Pass",
        "section": "Deep Learning",
        "difficulty": "Medium",
        "question_type": "coding",
        "neuroforge_skill": "Deep Learning Architecture",
        "estimated_time_minutes": 20,
        "tags": ["normalization", "batch-norm", "layer-norm"],
        "learning_objectives": [
            "Build forward calculations for Batch Normalization",
            "Contrast BatchNorm and LayerNorm dimensions and execution environments"
        ],
        "problem_statement": "Build a python function `batch_norm_forward(X, gamma, beta, running_mean, running_var, training, momentum, eps)` that implements the Batch Normalization forward equation, updating running metrics. Explain why LayerNorm is preferred in Transformers.",
        "real_world_context": "Normalization layers stabilize training, reduce sensitivity to initialization, and allow much higher learning rates. Transformers rely completely on LayerNorm for gradient stability.",
        "hints": [
            "BatchNorm normalizes across the batch dimension. LayerNorm normalizes across the feature dimension for each sample independently.",
            "In training mode: calculate batch mean and variance, update the running averages using the momentum factor, and normalize.",
            "In evaluation mode: use the running averages for normalization."
        ],
        "solution": {
            "explanation": "BatchNorm calculates the mean and variance across the batch dimension for each feature. This creates a dependency between samples in a batch, meaning a small batch size yields noisy mean/variance estimates that degrade performance. It is also hard to apply in RNNs due to varying sequence lengths. LayerNorm calculates mean and variance across the feature dimension for each sample independently. Since it does not aggregate across batches, it works identically regardless of batch size and is highly suited for sequence models and transformers.",
            "key_takeaways": [
                "BatchNorm normalizes across batches; LayerNorm normalizes across feature dimensions.",
                "LayerNorm is independent of batch size and sequence length, making it ideal for NLP."
            ]
        },
        "starter_code": {
            "python": "import numpy as np\n\ndef batch_norm_forward(X, gamma, beta, running_mean, running_var, training=True, momentum=0.9, eps=1e-5):\n    # X: (N, D) activation matrix\n    # TODO: Build batch normalization forward equations, updating running variables in-place\n    pass"
        },
        "expected_output": "A tuple of (normalized_X, updated_running_mean, updated_running_var).",
        "follow_up_questions": [
            "Why does BatchNorm act as a mild regularizer during training?",
            "What is the difference between Pre-LN and Post-LN architectures in Transformers?"
        ],
        "references": [
            {
                "title": "Batch Normalization: Accelerating Deep Network Training",
                "url": "https://arxiv.org/abs/1502.03167"
            }
        ]
    })

    # Q54: Convolutional Neural Networks
    questions.append({
        "id": 54,
        "slug": "convolutional-neural-networks",
        "title": "Build a CNN Shape and Receptive Field Calculator",
        "section": "Deep Learning",
        "difficulty": "Medium",
        "question_type": "coding",
        "neuroforge_skill": "Deep Learning Architecture",
        "estimated_time_minutes": 15,
        "tags": ["cnn", "shapes", "receptive-field"],
        "learning_objectives": [
            "Build calculators to determine CNN output shapes",
            "Trace receptive field sizes across nested layers of convolutions"
        ],
        "problem_statement": "Build a python function `calculate_cnn_output_shape(in_height, in_width, kernel_size, stride, padding)` that returns output spatial dimensions. Calculate the receptive field size of three stacked 3x3 convolutions with stride=1.",
        "real_world_context": "When building architectures like ResNets or UNets in computer vision, aligning tensor dimensions between downsampling, upsampling, and skip-connection layers is critical.",
        "hints": [
            "Output size formula: `O = floor((W - K + 2*P) / S) + 1` where W is input size, K is kernel size, P is padding, and S is stride.",
            "Receptive field of layer i is `RF_i = RF_(i-1) + (K_i - 1) * stride_stride_product` where `RF_0 = 1`."
        ],
        "solution": {
            "explanation": "The output size of a convolutional layer depends on the input size, kernel size, padding, and stride. The receptive field represents the size of the input region that affects a specific feature. For a stack of 3x3 convolutions with stride=1: Layer 1 has RF=3. Layer 2 has RF = 3 + (3-1)*1 = 5. Layer 3 has RF = 5 + (3-1)*1 = 7. Stacking layers increases the receptive field linearly, allowing deeper layers to capture global context.",
            "key_takeaways": [
                "Output dimensions depend on stride, padding, kernel size, and input size.",
                "Stacking small kernels (e.g. three 3x3) yields the same receptive field as a larger kernel (e.g. 7x7) but with fewer parameters and more non-linearities."
            ]
        },
        "starter_code": {
            "python": "def calculate_cnn_output_shape(in_height, in_width, kernel_size, stride, padding):\n    # TODO: Build output dimensions solver\n    out_h = 0\n    out_w = 0\n    return out_h, out_w"
        },
        "expected_output": "A tuple of integers (height, width).",
        "follow_up_questions": [
            "What is a dilated convolution, and how does it affect the receptive field size?",
            "Why is Global Average Pooling often preferred over Flattening before the final classification layer?"
        ],
        "references": [
            {
                "title": "Convolutional Neural Networks (Stanford CS231n)",
                "url": "https://cs231n.github.io/convolutional-networks/"
            }
        ]
    })

    # Q55: Recurrent Neural Networks
    questions.append({
        "id": 55,
        "slug": "recurrent-neural-networks",
        "title": "Build an LSTM Cell Forward Pass",
        "section": "Deep Learning",
        "difficulty": "Medium",
        "question_type": "coding",
        "neuroforge_skill": "Deep Learning Architecture",
        "estimated_time_minutes": 20,
        "tags": ["rnn", "lstm", "gru"],
        "learning_objectives": [
            "Build forward state update systems for an LSTM cell",
            "Explain how gating loops prevent vanishing gradients across sequence history"
        ],
        "problem_statement": "Build a python function `lstm_cell_forward(x, h_prev, c_prev, params)` that implements the complete forward pass gating equations of a single LSTM cell (input, forget, output gates, and cell state updates).",
        "real_world_context": "Before transformers, LSTMs were the standard architecture for speech recognition, machine translation, and time-series forecasting because they could remember patterns over hundreds of time steps.",
        "hints": [
            "Forget gate: `f_t = sigmoid(W_f * [h_prev, x] + b_f)`.",
            "Input gate: `i_t = sigmoid(W_i * [h_prev, x] + b_i)`.",
            "Candidate cell state: `c_tilde = tanh(W_c * [h_prev, x] + b_c)`.",
            "Cell state update: `c_t = f_t * c_prev + i_t * c_tilde`.",
            "Output gate: `o_t = sigmoid(W_o * [h_prev, x] + b_o)`. Hidden state: `h_t = o_t * tanh(c_t)`."
        ],
        "solution": {
            "explanation": "Standard RNNs suffer from vanishing gradients because backpropagation over time multiplies weight matrices repeatedly. LSTMs solve this by introducing an additive cell state `c_t`. The forget gate controls how much of the past cell state is kept, and the input gate controls how much new candidate information is added. Because the cell state update is additive, gradients can flow backward through time with minimal attenuation. GRUs simplify this by merging the cell state and hidden state, using only two gates: reset and update.",
            "key_takeaways": [
                "LSTMs use cell states and three gates to regulate information flow and preserve gradients.",
                "GRUs are computationally faster as they merge states and use fewer gates."
            ]
        },
        "starter_code": {
            "python": "import numpy as np\n\ndef lstm_cell_forward(x, h_prev, c_prev, params):\n    # params: dict containing weights Wf, Wi, Wc, Wo and biases bf, bi, bc, bo\n    # TODO: Build gates, candidate cell state, cell state update, and next hidden state\n    pass"
        },
        "expected_output": "A tuple of (h_next, c_next).",
        "follow_up_questions": [
            "Why is the Sigmoid activation used for the gates, while Tanh is used for the candidate state?",
            "What is the main limitation of LSTMs compared to self-attention architectures?"
        ],
        "references": [
            {
                "title": "Understanding LSTMs (Colah's Blog)",
                "url": "https://colah.github.io/posts/2015-08-Understanding-LSTMs/"
            }
        ]
    })

    # Q56: Autoencoders
    questions.append({
        "id": 56,
        "slug": "autoencoders",
        "title": "Build a Reconstruction Loss Utility",
        "section": "Deep Learning",
        "difficulty": "Medium",
        "question_type": "coding",
        "neuroforge_skill": "Deep Learning Architecture",
        "estimated_time_minutes": 15,
        "tags": ["autoencoders", "unsupervised-learning", "dimensionality-reduction"],
        "learning_objectives": [
            "Build reconstruction loss metrics for autoencoders",
            "Identify the role of bottleneck layers in feature compression"
        ],
        "problem_statement": "Build a python function `autoencoder_loss(inputs, reconstructed)` that computes MSE reconstruction loss. Explain how bottleneck layer limits force representation learning, and how Denoising Autoencoders differ.",
        "real_world_context": "Autoencoders are used for image denoising, anomaly detection (reconstruction error increases on anomalous samples), and generating compressed low-dimensional features for tabular data.",
        "hints": [
            "The bottleneck layer is the layer with the smallest number of dimensions.",
            "If the bottleneck layer is as large as the input, the network can overfit by learning the identity function (copying input).",
            "Denoising Autoencoders add noise to the input (e.g. Gaussian noise) but calculate reconstruction loss against the original clean input."
        ],
        "solution": {
            "explanation": "An autoencoder consists of an encoder that maps input data to a lower-dimensional latent space (bottleneck) and a decoder that reconstructs the original input. The bottleneck layer forces the network to capture only the most important features. Denoising autoencoders inject noise into the input, training the model to reconstruct the clean data. This prevents the network from learning a trivial copying function, forcing it to capture the underlying data distribution.",
            "key_takeaways": [
                "Bottleneck layers act as information filters, forcing compression.",
                "Denoising autoencoders learn robust features by reconstructing corrupted inputs."
            ]
        },
        "starter_code": {
            "python": "import numpy as np\n\ndef autoencoder_loss(inputs, reconstructed):\n    # TODO: Build Mean Squared Error reconstruction loss\n    pass"
        },
        "expected_output": "Float loss value.",
        "follow_up_questions": [
            "How does a variational autoencoder (VAE) differ from a standard autoencoder?",
            "What is the mathematical relationship between a linear autoencoder with MSE loss and PCA?"
        ],
        "references": [
            {
                "title": "Deep Learning Book - Autoencoders",
                "url": "https://www.deeplearningbook.org/contents/autoencoders.html"
            }
        ]
    })

    # Q57: Transfer Learning
    questions.append({
        "id": 57,
        "slug": "transfer-learning",
        "title": "Build a Model Parameter Freezing Utility",
        "section": "Deep Learning",
        "difficulty": "Medium",
        "question_type": "coding",
        "neuroforge_skill": "Deep Learning Architecture",
        "estimated_time_minutes": 15,
        "tags": ["transfer-learning", "fine-tuning", "methodology"],
        "learning_objectives": [
            "Build parameter freeze layers to disable gradients during transfer learning",
            "Select fine-tuning strategies based on dataset size and domain overlaps"
        ],
        "problem_statement": "Build a python function `freeze_model_layers(model)` that programmatically disables gradients (`requires_grad = False`) for all parameters except the last classifier head. Explain transfer strategies under different dataset size profiles.",
        "real_world_context": "Almost all modern AI tasks use transfer learning. We start with pre-trained vision models (ResNet, ViT) or language models (BERT, Llama) and adapt them to specific downstream tasks, saving massive compute costs.",
        "hints": [
            "Freezing parameters is done by setting `requires_grad = False` on the parameters.",
            "If data is small and similar, freeze the base and replace the head (prevents overfitting).",
            "If data is large and different, fine-tune the entire model (has enough data to adapt general features)."
        ],
        "solution": {
            "explanation": "Transfer learning strategies depend on two factors: target dataset size and similarity to the source dataset. If the dataset is small and similar, we freeze the feature extractor to avoid overfitting and train a new classification head. If the dataset is large and different, we fine-tune the entire network because we have enough data to adapt the base features. Freezing is implemented by disabling gradient calculations on the target parameters.",
            "key_takeaways": [
                "Small, similar datasets: freeze feature extractor and train new head.",
                "Large, different datasets: fine-tune the entire model.",
                "Freezing parameters in PyTorch is done by setting requires_grad=False."
            ]
        },
        "starter_code": {
            "python": "class MockParameter:\n    def __init__(self):\n        self.requires_grad = True\n\nclass MockModel:\n    def __init__(self):\n        self.params = [MockParameter() for _ in range(5)]\n        self.classifier_head = MockParameter()\n\ndef freeze_model_layers(model):\n    # TODO: Set requires_grad to False on all model.params, keeping classifier_head True\n    pass"
        },
        "expected_output": "The model parameters are updated such that only the classifier_head requires gradients.",
        "follow_up_questions": [
            "Why do we use smaller learning rates when fine-tuning pre-trained base layers?",
            "What is Catastrophic Forgetting, and how can it be mitigated during fine-tuning?"
        ],
        "references": [
            {
                "title": "A Comprehensive Survey on Transfer Learning",
                "url": "https://ieeexplore.ieee.org/document/5288526"
            }
        ]
    })

    # Q58: Attention Mechanism
    questions.append({
        "id": 58,
        "slug": "attention-mechanism",
        "title": "Build Scaled Dot-Product Attention",
        "section": "Deep Learning",
        "difficulty": "Hard",
        "question_type": "coding",
        "neuroforge_skill": "Deep Learning Architecture",
        "estimated_time_minutes": 25,
        "tags": ["attention", "transformers", "math"],
        "learning_objectives": [
            "Build the scaled dot-product attention calculation from scratch",
            "Derive how the scaling factor sqrt(d_k) preserves gradient flows"
        ],
        "problem_statement": "Build a python function `scaled_dot_product_attention(Q, K, V)` that calculates self-attention outputs. Explain mathematically why the query-key dot products are scaled by `1 / sqrt(d_k)`.",
        "real_world_context": "Scaled dot-product attention is the core mathematical building block of the Transformer architecture, which powers models like ChatGPT, Claude, and stable diffusion.",
        "hints": [
            "Attention formula: `Softmax( (Q @ K.T) / sqrt(d_k) ) @ V`.",
            "Softmax equation: `exp(z_i) / sum(exp(z_j))`.",
            "If Q and K are independent random variables with mean 0 and variance 1, their dot product has mean 0 and variance `d_k`. As `d_k` grows, the variance increases, pushing softmax inputs into regions with extremely small gradients."
        ],
        "solution": {
            "explanation": "Scaled dot-product attention maps query-key pairs to values. If query and key dimensions `d_k` are large, the variance of their dot product grows to `d_k`. This pushes the softmax inputs into flat regions where gradients vanish during backpropagation. Dividing by `sqrt(d_k)` scales the variance back to 1.0, preserving gradient flow.",
            "key_takeaways": [
                "Scaling factor sqrt(d_k) prevents softmax gradient saturation in high dimensions.",
                "Attention enables models to dynamically weigh connections between tokens regardless of distance."
            ]
        },
        "starter_code": {
            "python": "import numpy as np\n\ndef softmax(x, axis=-1):\n    exps = np.exp(x - np.max(x, axis=axis, keepdims=True))\n    return exps / np.sum(exps, axis=axis, keepdims=True)\n\ndef scaled_dot_product_attention(Q, K, V):\n    # Q: (N, seq_len, d_k), K: (N, seq_len, d_k), V: (N, seq_len, d_v)\n    # TODO: Build scaled dot product attention calculation\n    pass"
        },
        "expected_output": "Numpy array of shape (N, seq_len, d_v) containing weighted outputs.",
        "follow_up_questions": [
            "How does Multi-Head Attention differ from Single-Head Attention?",
            "What is the computational complexity of self-attention with respect to sequence length?"
        ],
        "references": [
            {
                "title": "Attention Is All You Need",
                "url": "https://arxiv.org/abs/1706.03762"
            }
        ]
    })

    # Q59: Transformer Architecture
    questions.append({
        "id": 59,
        "slug": "transformer-architecture",
        "title": "Build a Decoder Causal Attention Mask",
        "section": "Deep Learning",
        "difficulty": "Hard",
        "question_type": "coding",
        "neuroforge_skill": "Deep Learning Architecture",
        "estimated_time_minutes": 25,
        "tags": ["transformers", "attention", "causal-masking"],
        "learning_objectives": [
            "Build causal masking layers for Transformer decoders",
            "Apply triangular masks to prevent future token leaks during training"
        ],
        "problem_statement": "Build a python function `causal_attention(Q, K, V)` that applies a lower-triangular causal mask of `-inf` to Q-K dot products before the softmax calculation to prevent future token leaks.",
        "real_world_context": "Causal masking prevents the model from looking ahead at target tokens during training, ensuring that when predicting token `t`, it only uses information from tokens `1` to `t-1`.",
        "hints": [
            "During training, we compute attention for all tokens in parallel. Without masking, the representation of token `t` would attend to token `t+1`, which is cheating.",
            "Create a mask where the upper triangle (future tokens) contains a large negative number (like `-1e9` or `-inf`).",
            "Adding this mask to `(Q @ K.T)` causes `exp(-inf) = 0` in Softmax, setting attention weights to zero for future tokens."
        ],
        "solution": {
            "explanation": "Autoregressive generation generates tokens sequentially. During training, we feed the entire sequence to compute predictions in parallel. To prevent token `t` from attending to future tokens (cheating), we apply a causal mask to the attention matrix. The mask contains `-infinity` for all indices where `column > row` (upper triangle). When passed to Softmax, these inputs evaluate to zero weight, restricting attention to past and current tokens.",
            "key_takeaways": [
                "Causal masking forces the model to learn autoregressive prediction constraints.",
                "Upper triangular indices are set to -inf before softmax to eliminate future token dependencies."
            ]
        },
        "starter_code": {
            "python": "import numpy as np\n\ndef causal_attention(Q, K, V):\n    # Q, K, V: (seq_len, d_k)\n    # TODO: Build attention calculation, applying a lower-triangular mask of -inf before softmax\n    pass"
        },
        "expected_output": "Numpy array of shape (seq_len, d_k) where activations do not depend on future indexes.",
        "follow_up_questions": [
            "Why is the mask set to -infinity instead of 0 before softmax?",
            "What is the difference between Encoder-Only, Decoder-Only, and Encoder-Decoder Transformers?"
        ],
        "references": [
            {
                "title": "Attention Is All You Need",
                "url": "https://arxiv.org/abs/1706.03762"
            }
        ]
    })

    # Q60: Distributed Training
    questions.append({
        "id": 60,
        "slug": "distributed-training",
        "title": "Build a ZeRO State Memory Estimator",
        "section": "Deep Learning",
        "difficulty": "Hard",
        "question_type": "coding",
        "neuroforge_skill": "Deep Learning Architecture",
        "estimated_time_minutes": 25,
        "tags": ["distributed-training", "data-parallelism", "model-parallelism", "zero"],
        "learning_objectives": [
            "Build an estimator measuring GPU parameter footprints across ZeRO stages",
            "Contrast memory savings and communications trade-offs of Stage 1, 2, and 3 configurations"
        ],
        "problem_statement": "Build a python function `calculate_zero_stage_memory(param_count, num_gpus)` that estimates the GPU memory footprint (in gigabytes) required for model weights, gradients, and optimizer states under baseline DDP vs ZeRO Stage 1, 2, and 3.",
        "real_world_context": "Training massive LLMs (100B+ parameters) exceeds the memory capacity of a single GPU. Engineers must partition model states (weights, gradients, optimizer states) across clusters using ZeRO (DeepSpeed).",
        "hints": [
            "DDP replicates the model on all GPUs and splits the batch. Tensor Parallelism splits individual layers (matrices) across GPUs. Pipeline Parallelism splits layers sequentially (stages).",
            "ZeRO partitions model states instead of replicating them. Stage 1 partitions optimizer states. Stage 2 partitions gradients. Stage 3 partitions model parameters.",
            "Optimizer state memory is significant: using Adam, it requires 12 bytes per parameter (4 for fp32 copy, 4 for momentum, 4 for variance)."
        ],
        "solution": {
            "explanation": "DDP splits the batch and duplicates the model, which replicates model states and wastes memory. Tensor Parallelism splits matrix multiplications across GPUs, while Pipeline Parallelism partitions layers sequentially. ZeRO optimizes memory by partitioning states: Stage 1 partitions Adam optimizer states (saving ~4x), Stage 2 partitions gradients as they are calculated, and Stage 3 partitions the model weights, fetching them only-in-time for forward/backward steps, enabling training of trillion-parameter networks.",
            "key_takeaways": [
                "DDP replicates model parameters; ZeRO partitions them to reduce memory redundancy.",
                "Adam optimizer states consume 12 bytes per parameter, representing the largest memory bottleneck in FP16 training."
            ]
        },
        "starter_code": {
            "python": "def calculate_zero_stage_memory(param_count, num_gpus):\n    # Assuming Adam FP16 training: weight = 2 bytes, grad = 2 bytes, optimizer = 12 bytes\n    # TODO: Build calculator estimating baseline and Stage 1, 2, and 3 memory per GPU in GB\n    # Return a dict: {'baseline': ..., 'stage1': ..., 'stage2': ..., 'stage3': ...}\n    pass"
        },
        "expected_output": "A dictionary containing memory sizes in gigabytes for baseline and ZeRO stages.",
        "follow_up_questions": [
            "Why does Stage 3 ZeRO increase inter-GPU communication bandwidth requirements?",
            "What is the difference between synchronous and asynchronous parameter updates in distributed setups?"
        ],
        "references": [
            {
                "title": "ZeRO: Memory Optimizations for Training Trillion-Parameter Models",
                "url": "https://arxiv.org/abs/1910.02054"
            }
        ]
    })
    
    return questions
