Lulimi Translation API Structure

The Lulimi API will be the high-speed gateway providing access to the Neural Machine Translation (NMT) models. It will be built for high concurrency, using a lightweight framework (like FastAPI or Flask with optimized model serving) and structured around the Pivot Strategy.

I. Core Technology and Data Flow

Technology Stack: Python (for machine learning models), FastAPI/Flask (for API serving), and an optimized serving engine (e.g., ONNX Runtime or TorchServe) for low-latency translation inference.

Language Codes: We will use simple, distinct identifiers for the five languages:

NY (Nyanja)

BM (Bemba)

TO (Tonga)

LO (Lozi)

EN (English)

Database Integration: The API interacts with the validated_sentences (Gold Standard) collection from the CCP (Phase 1) only during model training, not for runtime translation.

II. Primary Endpoint: /translate

This single endpoint handles all language combinations based on the input parameters.

HTTP Method

POST

Endpoint Path

/api/v1/translate

Request Body (JSON)

| Field | Type | Description | Required | Example |
| text | string | The text to be translated. | Yes | "Muli bwanji?" |
| source_lang | string | The two-letter code for the source language (NY, BM, TO, LO, EN). | Yes | "NY" |
| target_lang | string | The two-letter code for the target language (NY, BM, TO, LO, EN). | Yes | "EN" |

Success Response (HTTP 200 OK)

| Field | Type | Description | Example |
| translation | string | The final translated text. | "How are you?" |
| source_lang | string | Echoes the input source language code. | "NY" |
| target_lang | string | Echoes the input target language code. | "EN" |
| route | string | Indicates the internal translation path taken (direct or pivot). | "direct" |

III. Internal Routing and Logic

The API is responsible for checking the source_lang and target_lang to determine the most efficient translation path.

Scenario A: Direct Translation (Zambian $\leftrightarrow$ English)

This is the fastest and most accurate route, requiring only one model call.

Condition: source_lang or target_lang is EN.

Steps:

Validate input languages and text.

Select the corresponding NMT model (e.g., NY_to_EN or EN_to_NY).

Call the model and return the result.

Response Route: "direct"

Scenario B: Pivot Translation (Zambian $\leftrightarrow$ Zambian)

This is the crucial inter-Zambian communication route, requiring two sequential model calls using English as the intermediary.

Condition: Neither source_lang nor target_lang is EN. (e.g., Bemba $\to$ Lozi).

Steps (Example: Bemba $\to$ Lozi):

Step 1 (First Model Call): Call the BM_to_EN model.

Input: "Cimoza citali" (Bemba)

Intermediate Output (English Pivot): "A long thing"

Step 2 (Second Model Call): Pass the Intermediate Output to the EN_to_LO model.

Final Output (Lozi): "Sinte ye telele"

Return the final output.

Response Route: "pivot"

IV. Utility and Administrative Endpoints

These endpoints support the development and monitoring of the Lulimi service.

| Endpoint | HTTP Method | Description |
| /api/v1/status | GET | Returns the current operational status of the API, model versions, and latency benchmarks. |
| /api/v1/supported_languages | GET | Returns a list of all supported language codes and their full names (e.g., { "NY": "Nyanja", ... }). |
| /api/v1/feedback | POST | Allows user applications (like the main Lulimi UI) to submit translations flagged as poor for review (feeding back into Phase 3). |

This API design provides a stable, unified interface while gracefully managing the complexity of the low-resource pivot strategy on the backend.

Would you like to detail the specifics of Phase 2: Model Training and Deployment, or perhaps define the structure of the feedback endpoint for quality control?
