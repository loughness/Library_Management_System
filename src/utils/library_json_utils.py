from json import JSONEncoder
from datetime import datetime, date

class LibraryJsonEncoder(JSONEncoder):
    """Custom JSON encoder for library objects"""
    def default(self, obj):
        try:
            if isinstance(obj, (date, datetime)):
                return obj.isoformat()
            iterable = iter(obj)
        except TypeError:
            pass
        else:
            return list(iterable)
        # Default json encoding using the __dict__
        return obj.__dict__