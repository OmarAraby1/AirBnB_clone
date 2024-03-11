#!/usr/bin/python3
import unittest
from models.base_model import BaseModel
from models import storage


class TestBaseModel(unittest.TestCase):
    """Unit tests for the BaseModel class"""

    def test_init_with_kwargs(self):
        """Tests the initialization of a BaseModel
        instance from a dictionary"""

        base_model_dict = {
            "id": "123e4567-e89b-12d3-a456-426655440000",
            "created_at": "2024-03-10T12:00:00",
            "updated_at": "2024-03-11T15:30:00",
            "name": "My Test Object",  # Additional attribute
        }

        base_model = BaseModel(**base_model_dict)

        self.assertEqual(base_model.id, base_model_dict["id"])
        self.assertIsInstance(base_model.created_at, datetime)
        self.assertEqual(
                base_model.created_at,
                datetime.fromisoformat(base_model_dict["created_at"]))
        self.assertIsInstance(base_model.updated_at, datetime)
        self.assertEqual(
                base_model.updated_at,
                datetime.fromisoformat(base_model_dict["updated_at"]))
        self.assertEqual(base_model.name, base_model_dict["name"])

    def test_str(self):
        """Tests the string representation of a BaseModel instance"""
        base_model = BaseModel()
        expected_string = f"[{base_model.__class__.__name__}] ({base_model.id}) {base_model.__dict__}"
        self.assertEqual(str(base_model), expected_string)

    def test_save(self):
        """Tests the save method of a BaseModel instance"""
        base_model = BaseModel()
        initial_updated_at = base_model.updated_at

        base_model.save()
        self.assertGreater(base_model.updated_at, initial_updated_at)

    def test_to_dict(self):
        """Tests the to_dict method of a BaseModel instance"""
        base_model = BaseModel()
        base_model_dict = base_model.to_dict()

        self.assertIsInstance(base_model_dict, dict)
        self.assertEqual(
                base_model_dict["__class__"],
                base_model.__class__.__name__)
        self.assertIsInstance(base_model_dict["created_at"], str)
        self.assertIsInstance(base_model_dict["updated_at"], str)
        self.assertEqual(
                base_model_dict["created_at"],
                base_model.created_at.isoformat())
        self.assertEqual(
                base_model_dict["updated_at"],
                base_model.updated_at.isoformat())

    def test_file_storage(self):
        """Tests the FileStorage class functionality"""

        base_model = BaseModel()
        base_model.save()
        storage.reload()  # Reload objects from the file
        self.assertEqual(len(storage.all()), 1)
        new_model = BaseModel()
        new_model.save()
        storage.reload()
        self.assertEqual(len(storage.all()), 2)
        # Check if the retrieved objects are the same as the created ones
        obj1 = storage.all().get(
                f"{base_model.__class__.__name__}.{base_model.id}"
                )
        self.assertIsInstance(obj1, BaseModel)
        self.assertEqual(obj1, base_model)
        obj2 = storage.all().get(
                f"{new_model.__class__.__name__}.{new_model.id}"
                )
        self.assertIsInstance(obj2, BaseModel)
        self.assertEqual(obj2, new_model)


if __name__ == "__main__":
    unittest.main()
