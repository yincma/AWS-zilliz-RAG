# pandas.api.types module stub for pymilvus compatibility

def is_list_like(obj):
    """Check if object is list-like."""
    return hasattr(obj, '__iter__') and not isinstance(obj, (str, bytes))

def is_scalar(obj):
    """Check if object is scalar."""
    return not hasattr(obj, '__iter__') or isinstance(obj, (str, bytes))

def is_integer(obj):
    """Check if object is integer."""
    return isinstance(obj, int) and not isinstance(obj, bool)

def is_float(obj):
    """Check if object is float."""
    return isinstance(obj, float)

def is_number(obj):
    """Check if object is number."""
    return isinstance(obj, (int, float)) and not isinstance(obj, bool)

def is_bool(obj):
    """Check if object is boolean."""
    return isinstance(obj, bool)

def is_string_dtype(obj):
    """Check if object has string dtype."""
    return isinstance(obj, str)

def is_numeric_dtype(obj):
    """Check if object has numeric dtype."""
    return isinstance(obj, (int, float)) and not isinstance(obj, bool)

def is_object_dtype(obj):
    """Check if object has object dtype."""
    return True  # Simplified stub

# Additional utility functions that might be used
def infer_dtype_from_object(obj):
    """Infer dtype from object."""
    if isinstance(obj, bool):
        return 'bool'
    elif isinstance(obj, int):
        return 'int64'
    elif isinstance(obj, float):
        return 'float64'
    elif isinstance(obj, str):
        return 'object'
    else:
        return 'object'

def infer_dtype(obj):
    """Infer dtype from object (alias for pymilvus compatibility)."""
    return infer_dtype_from_object(obj)

def is_array_like(obj):
    """Check if object is array-like."""
    return hasattr(obj, '__iter__') and hasattr(obj, '__len__') and not isinstance(obj, (str, bytes))

def is_dict_like(obj):
    """Check if object is dict-like."""
    return hasattr(obj, 'keys') and hasattr(obj, '__getitem__')

def is_file_like(obj):
    """Check if object is file-like."""
    return hasattr(obj, 'read') or hasattr(obj, 'write')

def is_extension_array_dtype(obj):
    """Check if object is extension array dtype."""
    return False  # Simplified stub

def is_categorical_dtype(obj):
    """Check if object is categorical dtype."""
    return False  # Simplified stub

def is_datetime64_any_dtype(obj):
    """Check if object is datetime64 dtype."""
    return False  # Simplified stub

def is_datetime64_dtype(obj):
    """Check if object is datetime64 dtype."""
    return False  # Simplified stub

def is_datetime64_ns_dtype(obj):
    """Check if object is datetime64[ns] dtype."""
    return False  # Simplified stub

def is_datetime64tz_dtype(obj):
    """Check if object is datetime64tz dtype."""
    return False  # Simplified stub

def is_interval_dtype(obj):
    """Check if object is interval dtype."""
    return False  # Simplified stub

def is_period_dtype(obj):
    """Check if object is period dtype."""
    return False  # Simplified stub

def is_sparse(obj):
    """Check if object is sparse."""
    return False  # Simplified stub

def is_timedelta64_dtype(obj):
    """Check if object is timedelta64 dtype."""
    return False  # Simplified stub

def is_timedelta64_ns_dtype(obj):
    """Check if object is timedelta64[ns] dtype."""
    return False  # Simplified stub

def is_unsigned_integer_dtype(obj):
    """Check if object is unsigned integer dtype."""
    return False  # Simplified stub

def is_int64_dtype(obj):
    """Check if object is int64 dtype."""
    return isinstance(obj, int) and not isinstance(obj, bool)

def is_float_dtype(obj):
    """Check if object is float dtype."""
    return isinstance(obj, float)

def is_complex_dtype(obj):
    """Check if object is complex dtype."""
    return isinstance(obj, complex)

def is_bool_dtype(obj):
    """Check if object is bool dtype."""
    return isinstance(obj, bool)

def pandas_dtype(dtype):
    """Convert input to pandas dtype."""
    return dtype  # Simplified stub
