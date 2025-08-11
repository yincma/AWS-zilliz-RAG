# Minimal pandas stub for pymilvus compatibility
# This is a stub to avoid installing the full pandas package in Lambda

# api.types module
class APITypes:
    @staticmethod
    def is_list_like(obj):
        """Check if object is list-like."""
        return hasattr(obj, '__iter__') and not isinstance(obj, (str, bytes))

# Create api module structure
class API:
    types = APITypes()

api = API()

class DataFrame:
    def __init__(self, data=None, index=None, columns=None, dtype=None, copy=False):
        self.data = data if data is not None else {}
        self.columns = columns if columns is not None else []
        self.index = index if index is not None else []
    
    def to_dict(self, orient='dict'):
        return self.data
    
    def __len__(self):
        return 0
    
    def __getitem__(self, key):
        return self
    
    def __setitem__(self, key, value):
        pass

class Series:
    def __init__(self, data=None, index=None, dtype=None, name=None, copy=False):
        self.data = data if data is not None else []
        self.index = index if index is not None else []
        self.name = name
    
    def to_list(self):
        return list(self.data) if hasattr(self.data, '__iter__') else [self.data]
    
    def __len__(self):
        return len(self.data) if hasattr(self.data, '__len__') else 0

# Stub functions
def read_csv(*args, **kwargs):
    return DataFrame()

def read_json(*args, **kwargs):
    return DataFrame()

def concat(*args, **kwargs):
    return DataFrame()

# Module-level attributes
__version__ = "1.0.0"