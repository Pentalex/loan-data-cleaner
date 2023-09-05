from enum import Enum, unique


@unique
class EnumFromTable(Enum):
    @classmethod
    def generate(cls, model_class, enum_name, session):
        data = session.query(model_class.name, model_class.id).all()
        enum = Enum(enum_name, data)
        return enum
