from wtforms import Form, StringField, validators
from wtforms.validators import ValidationError


def without_space(form, field):
    if ' ' in field.data:
        raise ValidationError('Username must without space')


class UsernameForm(Form):
    username = StringField('Username', [validators.Length(min=5), without_space], default='test')


def main():
    form1 = UsernameForm()
    print('>>> form1')
    print(type(form1['username']))
    print(form1.data)
    print(form1.username.data)
    print(form1.errors)
    print(form1.validate())
    print(form1.errors)

    print('>>> form2')
    form2 = UsernameForm(username='Robert')
    print(form2.data)
    print(form2.validate())
    print(form2.errors)

    print('>>> form3')
    form3 = UsernameForm(username='Foo Bar')
    form3.validate()
    print(form3.errors)


if __name__ == '__main__':
    main()
