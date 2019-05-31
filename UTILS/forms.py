""" Form Description """

from wtforms import Form, StringField, IntegerField


class RegistrationForm(Form):
    name: str = StringField('Name')
    fty: int = IntegerField('Faculty')
    rl: int = IntegerField('Role')
    ss: int = IntegerField('Status')
    desc: str = StringField('Description')
