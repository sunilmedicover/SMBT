from mongoengine import Document,StringField,IntField,ListField,DateField,SequenceField

class Data(Document):
    emp_id=IntField(min_value=1)
    name=StringField(max_length=15)
    country=StringField(max_length=15)
    country_code=IntField()
    state=StringField(max_length=9)
    state_code=IntField()
    city=StringField(max_length=12)
    pincode=IntField()