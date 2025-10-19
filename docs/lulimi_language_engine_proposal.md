Project Proposal: The Lulimi Language Engine

Suggested Name: Lulimi

The name Lulimi is adopted, meaning "tongue" or "language" in Nyanja. This name is culturally resonant and directly communicates the engine's purpose: to serve as a voice for the primary languages of Zambia.

I. Recommended Technical Approach: Neural Machine Translation (NMT) with Pivoting

Creating direct translation models for every single language pair (e.g., Bemba $\leftrightarrow$ Lozi) is challenging because high-quality, parallel training data (sentences paired side-by-side) is extremely scarce for low-resource pairs.

The most practical and robust approach for an initial launch is to use a Pivot Language strategy based on Neural Machine Translation (NMT) architecture.

1. Model Core: English as the Pivot

Instead of training 12 separate models (Bemba $\leftrightarrow$ English, Tonga $\leftrightarrow$ English, Bemba $\leftrightarrow$ Tonga, etc.), the Lulimi engine will focus on mastering the six core pairs that link each Zambian language to English:

|

| Language Pair | Translation Direction |
| Bemba $\leftrightarrow$ English | Two separate NMT models |
| Nyanja $\leftrightarrow$ English | Two separate NMT models |
| Tonga $\leftrightarrow$ English | Two separate NMT models |
| Lozi $\leftrightarrow$ English | Two separate NMT models |

How Inter-Zambian Translation Works (The Pivot Strategy):

When a user requests a translation from Bemba to Lozi, the Lulimi engine performs a two-step "pivot" translation:

Bemba $\to$ English: The Bemba sentence is translated into an intermediate English sentence using the Bemba-to-English model.

English $\to$ Lozi: The resulting English sentence is then translated into Lozi using the English-to-Lozi model.

This approach significantly reduces the data required and ensures quality, as the English-to-Zambian models are the most critical components.

2. Architecture: Transformer Model

The Lulimi engine should be built on a Transformer architecture (like a fine-tuned mBART, M2M-100, or a T5 variant). These models are state-of-the-art for NMT and are designed to handle multilingual tasks efficiently.

II. Phased Implementation Roadmap

Phase 1: Data Collection and Preprocessing (Focus on English Pairs)

The success of the engine hinges entirely on the quality and quantity of the training data.

Corpus Development: Digitally harvest, clean, and align parallel corpora for the six Zambian Language $\leftrightarrow$ English pairs. Sources include:

Existing Bibles or religious texts (often fully digitized and parallel).

Government publications, educational materials.

News articles translated into English.

A community contribution platform (a public interface where volunteers can submit or validate translations).

Monolingual Data: Collect large amounts of single-language text for all five languages (English + four Zambian languages). This is crucial for pre-training the Transformer model to understand the nuances and grammatical structures of each language.

Tokenization and Normalization: Develop specific tokenizers for each Zambian language to handle common orthographic variations, contractions, and dialects, ensuring consistency.

Phase 2: Model Training and Deployment

Baseline Model: Train the initial NMT models for the six $Z \leftrightarrow E$ pairs using the collected parallel data.

Deployment API: Wrap the deployed models in a fast, scalable API (e.g., using Python and Flask/Django) that handles the translation request logic.

Pivot Logic Implementation: The API must intelligently handle the routing:

Bemba $\to$ English: Call bemba_to_english_model.

Bemba $\to$ Lozi: Call bemba_to_english_model, then pass output to english_to_lozi_model.

User Interface (UI): Launch a simple, mobile-friendly web application for the Lulimi engine where users can select source/target languages and input text.

Phase 3: Post-Deployment Improvement (Iterative Refinement)

Community Feedback Loop: Capture user translations that are deemed "poor" or "incorrect" and feed them back into the training data pipeline.

Direct Pair Training (Optional): Once a critical mass of high-quality pivot translations has been generated, use these "synthetic" parallel pairs (e.g., the Bemba $\to$ English $\to$ Lozi output) to attempt training a direct Bemba $\leftrightarrow$ Lozi model. This can often improve speed and accuracy, bypassing the intermediate English step.

Speech-to-Text Integration: Begin exploring integration with speech recognition services for Bemba and Nyanja to allow users to speak their phrases directly.

III. Key Challenges

| Challenge | Mitigation Strategy |
| Data Scarcity | Focus resources on community-driven parallel corpus collection and digitization of physical texts. Leverage existing multilingual models (like M2M-100) that have some latent knowledge of Bantu languages. |
| Dialectal Variation | Train the model to recognize and standardize common dialectal forms (especially in Nyanja and Tonga) during the preprocessing stage to ensure broad usability. |
| Orthography | Ensure a consistent, standardized approach to spelling and diacritics, which can vary between texts, to prevent model confusion. |
