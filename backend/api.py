# api.py
# Core backend server for the Lulimi Translation Engine.
# Uses FastAPI for high-performance and Pydantic for robust data validation.

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
import time
import asyncio
from typing import List, Dict, Union

# --- CONFIGURATION AND SETUP ---

app = FastAPI(
    title="Lulimi (Zambian Language) Translation API",
    description="Provides real-time translation for Nyanja, Bemba, Tonga, Lozi, and English using a Pivot Strategy.",
    version="1.0.0"
)

# Language Codes
LANG_CODES = {
    "NY": "Nyanja",
    "BM": "Bemba",
    "TO": "Tonga",
    "LO": "Lozi",
    "EN": "English",
}

# --- DATA MODELS (Pydantic) ---

class TranslationRequest(BaseModel):
    """Defines the expected structure for incoming translation requests."""
    text: str = Field(..., description="The text string to be translated.")
    source_lang: str = Field(..., description="Source language code (NY, BM, TO, LO, EN).")
    target_lang: str = Field(..., description="Target language code (NY, BM, TO, LO, EN).")

class TranslationResponse(BaseModel):
    """Defines the structure for the successful translation response."""
    translation: str = Field(..., description="The final translated text.")
    source_lang: str
    target_lang: str
    route: str = Field(..., description="The internal translation path: 'direct' or 'pivot'.")
    latency_ms: float = Field(..., description="Total time taken for the translation, in milliseconds.")


# --- CORE NMT MODEL SIMULATION ---

# NOTE: In a production environment (Phase 2), this function would load and execute
# the actual PyTorch or TensorFlow NMT model (e.g., a fine-tuned mBART or M2M-100).
async def simulate_model_call(text: str, source_code: str, target_code: str) -> str:
    """
    Placeholder for the actual NMT model inference call.
    Simulates model latency and returns a mock translation.
    """
    
    # Simulate the actual model inference time (e.g., 50ms to 200ms)
    await asyncio.sleep(0.15) 

    # Mock translation logic based on the core goal (meaning transfer)
    if source_code != "EN" and target_code == "EN":
        # Simulating Z -> EN translation
        return f"The English meaning of '{text}' is understood here."
    elif source_code == "EN" and target_code != "EN":
        # Simulating EN -> Z translation
        return f"'{text}' is successfully localized to {LANG_CODES[target_code]}."
    elif source_code != "EN" and target_code != "EN":
        # Simulating Pivot translation (should not happen directly in this function, 
        # but included for robust testing)
        return f"Pivot: '{text}' was converted to English then to {LANG_CODES[target_code]}."
    else:
        # English -> English (should be handled by the endpoint, but safe return)
        return text

# --- INTERNAL ROUTING LOGIC ---

async def handle_translation(request: TranslationRequest) -> TranslationResponse:
    """Handles the core translation logic, choosing between Direct and Pivot routes."""
    start_time = time.time()
    
    src = request.source_lang.upper()
    tgt = request.target_lang.upper()
    text = request.text.strip()
    
    # 1. Validation Checks
    if src == tgt:
        raise HTTPException(status_code=400, detail="Source and target languages cannot be the same.")
    if src not in LANG_CODES or tgt not in LANG_CODES:
        raise HTTPException(status_code=400, detail="Invalid language code provided.")
    if not text:
        raise HTTPException(status_code=400, detail="Input text cannot be empty.")
        
    final_translation = ""
    route_type = ""
    
    # --- SCENARIO A: DIRECT TRANSLATION (Zambian <-> English) ---
    if src == "EN" or tgt == "EN":
        # This requires only one model call (e.g., BM <-> EN)
        route_type = "direct"
        final_translation = await simulate_model_call(text, src, tgt)
        
    # --- SCENARIO B: PIVOT TRANSLATION (Zambian <-> Zambian) ---
    else:
        # This requires two model calls using English (EN) as the pivot.
        # Example: Bemba (BM) -> English (EN) -> Lozi (LO)
        route_type = "pivot"
        
        # 1. First Model Call: Source Language to English (Pivot)
        # e.g., BM -> EN
        pivot_text = await simulate_model_call(text, src, "EN")
        
        # 2. Second Model Call: English (Pivot) to Target Language
        # e.g., EN -> LO
        final_translation = await simulate_model_call(pivot_text, "EN", tgt)
        
    end_time = time.time()
    
    return TranslationResponse(
        translation=final_translation,
        source_lang=src,
        target_lang=tgt,
        route=route_type,
        latency_ms=round((end_time - start_time) * 1000, 2)
    )


# --- API ENDPOINTS ---

@app.post("/api/v1/translate", response_model=TranslationResponse, tags=["Translation"])
async def translate_text(request: TranslationRequest):
    """
    Performs translation using the Lulimi NMT models. 
    Routes the request internally to either a direct or pivot translation path.
    """
    return await handle_translation(request)

@app.get("/api/v1/status", tags=["Utility"])
async def get_status() -> Dict[str, Union[str, bool]]:
    """Returns the current operational status of the API."""
    return {
        "status": "Operational",
        "api_version": "v1",
        "models_loaded": True, # Assume models are loaded in a real implementation
        "pivot_strategy_active": True
    }

@app.get("/api/v1/supported_languages", tags=["Utility"])
async def get_supported_languages() -> List[Dict[str, str]]:
    """Returns a list of all supported language codes and their full names."""
    return [{"code": code, "name": name} for code, name in LANG_CODES.items()]

# --- RUN INSTRUCTIONS (For development/local testing) ---
# To run this server locally:
# 1. Ensure you have the dependencies installed (from requirements.txt):
#    pip install fastapi uvicorn[standard] pydantic
# 2. Execute the server:
#    uvicorn api:app --reload
# 3. Access the interactive documentation at: http://127.0.0.1:8000/docs
