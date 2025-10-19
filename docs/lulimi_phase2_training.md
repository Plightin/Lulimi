Phase 2: Model Training and Deployment Strategy

This phase focuses on translating the curated data from the Community Contribution Platform (CCP) into functional, high-performance translation models, and then deploying them via the API.

I. Model Selection and Architecture

1. Pre-trained Foundation Model

We will leverage a large, pre-trained multilingual Transformer model (like Google's M2M-100 or a multilingual T5/BART variant). These models already have a foundation in many languages, including some Bantu languages, significantly accelerating the training process compared to building a model from scratch.

2. Fine-tuning Strategy

The strategy involves fine-tuning this base model specifically on our high-quality, validated parallel corpora for the six Zambian Language $\leftrightarrow$ English pairs.

Task: Sequence-to-Sequence (Seq2Seq) translation.

Goal: Maximize translation accuracy and fluency for the four target languages.

II. Data Preparation Pipeline

The data collected in Phase 1 requires final preparation before training:

Load Gold Standard Data: Retrieve the parallel sentences from the Firestore validated_sentences collection.

Split Data: Divide each language pair's data into three sets:

Training Set (80%): Used for model optimization.

Validation Set (10%): Used to monitor model performance and prevent overfitting during training.

Test Set (10%): Used for final, unbiased performance evaluation.

Tokenization: Apply a specialized sub-word tokenizer (e.g., SentencePiece or BPE) that has been optimized or fine-tuned to handle the unique vocabulary and morphology of Nyanja, Bemba, Tonga, and Lozi.

Batching and Padding: Organize the tokenized data into batches and pad sequences to a uniform length to ensure efficient GPU processing.

III. Training Process (Using train_models.py)

The training script will iterate through all six models, fine-tuning each one separately.

1. Hyperparameter Selection

We will use standard NMT hyperparameters, adjusting them based on the size of our dataset:

Optimizer: AdamW (standard for Transformers).

Learning Rate Scheduler: Warmup and linear decay (crucial for stability).

Epochs: Start with 5-10 epochs and use early stopping based on the loss of the Validation Set.

2. Evaluation Metrics

Training progress and final model quality will be measured using standard industry metrics:

BLEU Score (Bilingual Evaluation Understudy): The primary metric, measuring the overlap between the model's output and the reference translation.

ChrF++: A character-level metric that often performs better than BLEU for morphologically rich, low-resource languages.

3. Model Saving

After training, the best-performing model checkpoint (based on the highest validation BLEU/ChrF++ score) will be saved as a dedicated directory (e.g., NY_to_EN_model) containing the model weights and tokenizer files, ready for inference. These files will be stored in the /backend/models/ directory.

IV. Deployment and API Integration

Once the six models are trained, they must be integrated into the Lulimi API (api.py):

Model Loading: The api.py server will load all six models into GPU/CPU memory upon startup for instant access.

Inference Pipeline: The API endpoints will use the loaded models to perform translations.

Pivot Logic Execution: The core API function will intelligently route requests:

Direct Translation (e.g., Bemba $\leftrightarrow$ English): Calls one model.

Pivot Translation (e.g., Bemba $\leftrightarrow$ Lozi): Calls the two sequential models with English as the pivot.

This structured approach ensures that the Lulimi engine is built on a solid foundation of modern machine learning practices.
