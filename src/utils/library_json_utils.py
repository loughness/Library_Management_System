from json import JSONEncoder
from datetime import datetime, date

class LibraryJsonEncoder(JSONEncoder):
    """Custom JSON encoder for library objects"""
    def default(self, obj):
        # Handle datetime objects first
        if isinstance(obj, (date, datetime)):
            return obj.isoformat()
        
        # Handle custom objects (Book, Member, Section, etc.) by converting to dict
        # Check if it's a class instance (not a built-in type)
        if hasattr(obj, '__dict__') and not isinstance(obj, (str, int, float, bool, type(None), list, dict, tuple)):
            # Recursively serialize the dict
            result = {}
            for key, value in obj.__dict__.items():
                if isinstance(value, (date, datetime)):
                    result[key] = value.isoformat()
                elif isinstance(value, list):
                    # Handle lists that might contain objects
                    result[key] = [self.default(item) if (hasattr(item, '__dict__') and not isinstance(item, (str, int, float, bool, type(None), list, dict, tuple))) or isinstance(item, (date, datetime)) else item for item in value]
                elif isinstance(value, dict):
                    # Handle dictionaries
                    result[key] = {k: self.default(v) if (hasattr(v, '__dict__') and not isinstance(v, (str, int, float, bool, type(None), list, dict, tuple))) or isinstance(v, (date, datetime)) else v for k, v in value.items()}
                elif hasattr(value, '__dict__') and not isinstance(value, (str, int, float, bool, type(None), list, dict, tuple)):
                    # Recursively handle nested objects
                    result[key] = self.default(value)
                else:
                    result[key] = value
            return result
        
        # Try to iterate if it's an iterable (but not a string or bytes)
        try:
            if isinstance(obj, (str, bytes)):
                raise TypeError
            iterable = iter(obj)
        except TypeError:
            # Not iterable, use default JSON encoding
            return super().default(obj)
        else:
            return list(iterable)