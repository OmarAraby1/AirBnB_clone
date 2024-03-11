#!/usr/bin/python3
import unittest
from models.base_model import BaseModel


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
        expected_string = f"
        [{base_model.__class__.__name__}]
        ({base_model.id})
        {base_model.__dict__}"
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


if __name__ == "__main__":
    unittest.main()
