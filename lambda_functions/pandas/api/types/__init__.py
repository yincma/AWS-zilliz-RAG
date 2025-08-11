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