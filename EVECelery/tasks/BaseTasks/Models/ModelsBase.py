from pydantic import BaseModel, Field, validator


class ModelBaseEVECelery(BaseModel):
    """
    A base response model used by EVECelery tasks.

    """

    class Config:
        allow_population_by_field_name = True


class ModelBaseWithModelInfo(ModelBaseEVECelery):
    """
    A base response model to be serialized and deserialized by EVECelery tasks.

    This model has a pydantic model attribute that is used to deserialize the response data in a cache system such as Redis.
    """
    pydantic_model: str = Field(default=None,
                                description='The name of the pydantic model class that this model was initialized with.')

    @validator('pydantic_model', pre=True, always=True)
    def dynamic_set_pydantic_model(cls, v):
        return v or cls.class_name()

    @classmethod
    def class_name(cls) -> str:
        return cls.__name__
