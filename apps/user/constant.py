from collections import OrderedDict


class Gender:
    MALE = "male"
    FEMALE = "female"
    OTHER = "other"

    FieldStr = OrderedDict({
        MALE: "Male",
        FEMALE: "Female",
        OTHER: "Other"
    })

    @classmethod
    def choice(cls):
        return cls.FieldStr.items()
