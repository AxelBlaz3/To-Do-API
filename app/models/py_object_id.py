from bson import ObjectId


class PyObjectId(ObjectId):
    """Python ObjectId.

    Raises:
        ValueError: If an invalid ObjectId string is provided.

    Returns:
        ObjectId: Instance of the class.

    Yields:
        ObjectId: Instance of ObjectId.
    """
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        if not ObjectId.is_valid(v):
            raise ValueError("Invalid objectid")
        return ObjectId(v)

    @classmethod
    def __modify_schema__(cls, field_schema):
        field_schema.update(type="string")
