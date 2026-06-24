import hashlib

class BiometricAFISDriver:
    def __init__(self, authorized_print_hash: str):
        self.authorized_print_hash = authorized_print_hash

    def extract_minutiae(self, raw_bitmap: bytes) -> str:
        """
        Simulates extracting a biometric template from a scanner.
        In production, use bindings for SourceAFIS here.
        """
        template_hash = hashlib.sha256(raw_bitmap).hexdigest()
        return template_hash

    def verify_scan(self, live_scan_bitmap: bytes) -> bool:
        live_hash = self.extract_minutiae(live_scan_bitmap)
        return live_hash == self.authorized_print_hash
      
