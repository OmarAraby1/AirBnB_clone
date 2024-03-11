import uuid
from datetime import datetime


class BaseModel:
    """Base class for all model classes."""

    def __init__(self, *args, **kwargs):
        """Initializes a BaseModel instance."""

        if kwargs:
            # Initialize from a dictionary
            self.__dict__.update(kwargs)
            self.id = kwargs.get("id", str(uuid.uuid4()))  # Ensure a unique ID
            self.created_at = datetime.fromisoformat(kwargs.get("created_at"))
            self.updated_at = datetime.fromisoformat(kwargs.get("updated_at"))
        else:
            # Initialize a new instance
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        """Returns a formatted string representation of the instance."""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """Updates the updated_at attribute to the current datetime."""
        self.updated_at = datetime.now()

    def to_dict(self):
        """Returns a dictionary representation of the instance."""
        data = self.__dict__.copy()
        data["__class__"] = self.__class__.__name__
        data["created_at"] = self.created_at.isoformat()
        data["updated_at"] = self.updated_at.isoformat()
        return data
