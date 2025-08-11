"""
Minimal numpy stub for pymilvus compatibility in Lambda
This avoids the full numpy installation which is too large for Lambda
"""

class ndarray:
    def __init__(self, *args, **kwargs):
        pass
    
    def tolist(self):
        return []

def array(*args, **kwargs):
    return ndarray()

def float32(*args, **kwargs):
    return float

def float64(*args, **kwargs):
    return float

# Add other minimal stubs as needed
dtype = type('dtype', (), {'name': 'float32'})
float32 = dtype()
float64 = dtype()