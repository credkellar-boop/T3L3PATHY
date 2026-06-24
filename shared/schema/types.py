from typing import TypedDict, List, Dict, Optional

class BiometricIdentity(TypedDict):
    face_embedding_hash: str
    fingerprint_match: bool

class NeuralDecoding(TypedDict):
    predicted_phonemes: List[str]
    phoneme_confidence: float
    prefrontal_oxygenation_delta: float

class CardiovascularPhysiological(TypedDict):
    heart_rate_bpm: float
    hrv_rmssd_ms: float
    phasic_scr_amplitude_us: float
    expiration_suppression_ratio: float
    somatic_arousal_index: Optional[float]

class S3lfC0n8ious(TypedDict):
    inference_latency_ms: float
    system_coherence_score: float
    cognitive_alignment_factor: float
    execution_permitted: bool
    action_gate_status: str

class T3l3pathyFrame(TypedDict):
    timestamp: float
    session_id: str
    biometric_identity: BiometricIdentity
    neural_decoding: NeuralDecoding
    cardiovascular_physiological: CardiovascularPhysiological
    s3lf_c0n8ious: Optional[S3lfC0n8ious]
  
