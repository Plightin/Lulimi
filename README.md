Lulimi: The Zambian Language Engine

Lulimi (Nyanja for "tongue" or "language") is a pioneering Neural Machine Translation (NMT) engine designed to bridge communication gaps between Zambia's four primary local languages—Nyanja (NY), Bemba (BM), Tonga (TO), and Lozi (LO)—and English (EN).

🎯 Project Goal

To deliver high-quality, real-time machine translation that empowers digital inclusion, governance, and economic growth across Zambia.

⚙️ Architecture: The Pivot Strategy

Due to the low-resource nature of the Zambian languages, the Lulimi engine employs a Pivot Strategy using English as the central intermediary language.

Translation Route

Model Calls

Example (Bemba $\to$ Lozi)

Direct (Zambian $\leftrightarrow$ English)

1 Model Call

BM_to_EN or EN_to_BM

Pivot (Zambian $\leftrightarrow$ Zambian)

2 Model Calls

BM_to_EN then EN_to_LO

🚀 Repository Structure

The repository is organized to separate the community data collection, the core API, and the documentation.

/Lulimi/
├── /backend/                        # Python API and NMT models (Phase 2)
│   ├── api.py                       # FastAPI/Flask server and routing logic
│   ├── models/                      # Trained NMT model files (large files managed via Git LFS)
│   └── requirements.txt             # Python dependencies (TensorFlow/PyTorch, FastAPI)
│
├── /frontend/                       # Community Contribution Platform (CCP) UI
│   └── lulimi_ccp_interface.html    # The main CCP HTML/JS file
│
├── /docs/                           # Project planning and phase documentation
│   ├── lulimi_api_structure.md      # API specification
│   ├── lulimi_language_engine_proposal.md
│   └── lulimi_phase1_data.md        # Data Strategy
│
├── README.md                        # This file
└── .gitignore                       # Standard exclusion list for development


🛠️ Getting Started (Phase 1: Data Collection)

Currently, the most active component is the Community Contribution Platform (CCP), which generates the training data.

Database: Ensure a Firebase Firestore instance is set up to match the public collection paths defined in the CCP code: /artifacts/{appId}/public/data/unvalidated_sentences.

Frontend: The /frontend/lulimi_ccp_interface.html file can be run directly in any browser for immediate community testing and data collection.

📝 Contribution

We welcome contributions from native speakers, linguists, and developers! Please check the docs/ folder for the full plan and submit issues or pull requests.