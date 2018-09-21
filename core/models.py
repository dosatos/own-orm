import re


TABLE_MISSING_ERROR = "Please, specify the table name"


class BaseField:
    def __init__(self):
        self.value = None

    def __get__(self, instance, owner):
        return self.value

    def __set__(self, instance, value):
        self._validate(value)
        self.value = value

    def _validate(self, value):
        self._validate_required()
        self._validate_nuallable()

    def _validate_required(self):
        pass

    def _validate_nuallable(self):
        pass



class CharField(BaseField):
    def _validate(self, value):
        super()._validate(value)
        if not isinstance(value, str):
            raise TypeError



class EmailField(CharField):
    def _validate(self, value):
        super()._validate(value)
        regex = re.compile(r"^[\w]+@[\w]+\.[a-zA-Z]+$")
        if not regex.match(value):
            raise ValueError



class Model:
    def __init__(self, **kwargs):
        if "__tablename__" not in [attr for attr in self.__class__.__dict__.keys()]:
            raise AttributeError(TABLE_MISSING_ERROR)

        for attr in self.fields:
            setattr(self, attr, kwargs[attr])

    @property
    def fields(self):
        return [attr for (attr, field) in self.__class__.__dict__.items() if isinstance(field, BaseField)]
