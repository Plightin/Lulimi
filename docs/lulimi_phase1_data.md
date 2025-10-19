Phase 1: Data Collection and Preprocessing Strategy

The Data Challenge: Low-Resource Context

Languages like Nyanja, Bemba, Tonga, and Lozi are classified as low-resource languages in the digital world. This means they lack the massive, clean, publicly available datasets that languages like French or Spanish possess. Our strategy must focus on creative harvesting, digitization, and community engagement to build the necessary foundation.

The primary goal of Phase 1 is to gather data that supports the six core translation pairs (each Zambian language $\leftrightarrow$ English), which fuel the entire Pivot Strategy.

I. Data Type 1: Parallel Corpora (The Pivot Engine Fuel)

Parallel Corpora consist of sentences aligned side-by-side in two different languages (e.g., a Bemba sentence matched with its official English translation). This data is the only thing that teaches the NMT model how to map meaning from one language to another.

Acquisition Strategies

| Source Type | Examples & Target Languages | Strategy |
| Religious Texts (High Priority) | Bibles, hymns, catechisms in all four languages (Nyanja, Bemba, Tonga, Lozi) and English. | Digitize and Align: These texts are often already professionally translated and are one of the richest sources of parallel text. The focus here is on cleaning the digital format and aligning the verses/sentences automatically. |
| Official Documentation | Government reports, parliamentary speeches, legal texts, and public health documents that were officially translated into one or more Zambian languages. | Scraping and OCR: Use web scraping tools on government sites and Optical Character Recognition (OCR) on digitized PDF archives to extract text. |
| Educational Materials | Primary and secondary school textbooks (especially those related to local culture or history) that exist in both English and a local language. | Partner with Ministries/Publishers: Establish relationships to gain access to digital copies of educational content for alignment. |
| News & Media Archives | Articles from local newspapers (print or online) that provide both an English version and a local language version of the same story. | Targeted Web Scraping: Focus on archives of major Zambian media houses that historically published in multiple languages. |

Data Cleaning and Validation

Before training, the parallel data must be meticulously cleaned:

Normalization: Standardize orthography (spelling, capitalization, and punctuation) to handle regional dialectal variations (e.g., in Nyanja or Tonga).

Sentence Alignment: Automatically check and manually review that sentences are correctly matched, discarding pairs where the meaning is lost or the alignment is broken.

Deduplication: Remove identical sentence pairs to prevent the model from overfitting to common phrases.

II. Data Type 2: Monolingual Data (The Grammar Foundation)

Monolingual Data is vast amounts of single-language text (e.g., 5 million sentences purely in Bemba). This data teaches the NMT model the internal structure of the language—its grammar, common phrases, morphology (word structure), and vocabulary.

Acquisition Strategies

Web Crawls: Conduct extensive web crawls focusing on Zambian blogs, forums, social media archives, and general-interest websites written entirely in Bemba, Nyanja, etc.

Literature: Digitize classic and modern literature, poetry, and academic writings originally composed in the local languages.

Radio Transcripts (Future): In Phase 3, transcripts from local radio shows can provide invaluable conversational and modern language use.

III. The Critical Component: Community Contribution Platform (CCP)

Given the inherent scarcity of parallel data, a dedicated platform to engage native speakers is mandatory for long-term data sustainability and quality.

CCP Functionality

The CCP will have two primary functions:

Translation Input: Volunteers submit English phrases and provide their verified translation into one of the four local languages, or vice-versa.

Validation/Correction: Existing parallel pairs (especially those extracted from automated alignment) are presented to multiple community validators. The pair is only accepted into the gold-standard training set once it has been approved by a consensus of native speakers.

This community feedback loop, which is a key technical commitment, ensures the data remains modern, accurate, and reflective of actual usage across different regions.
