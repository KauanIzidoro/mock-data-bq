import random
from datetime import date

from faker import Faker
from models import Account, BuyEvent, Card, Person

fake = Faker(['pt_BR'])


def generate_person():
    person = Person(
        person_id=fake.unique.random_int(min=1, max=1002, step=1),
        name=fake.unique.name(),
        email=fake.unique.email(),
        gender=fake.passport_gender(),
        birth_date=fake.date(
            end_datetime=date(day=1, month=1, year=2000)),
        address=fake.address(),
        salary=fake.random_number(digits=4),
        cpf=fake.cpf()
    )

    person_dict = person.__dict__

    return person_dict


def generate_account():
    account = Account(
        account_id=fake.unique.random_int(min=1, max=2002, step=1),
        status_id=fake.random_int(min=1, max=10),
        due_day=fake.random_int(min=1, max=30),
        person_id=fake.unique.random_int(min=1, max=1002, step=1),
        balance=fake.random_number(digits=4),
        available_balance=fake.random_number(digits=3)
    )

    account_dict = account.__dict__

    return account_dict


def generate_card():
    card = Card(
        card_id=fake.unique.random_int(min=1, max=4002, step=1),
        card_number=fake.credit_card_number(),
        account_id=fake.unique.random_int(min=1, max=2002, step=1),
        status_id=fake.random_int(min=0, max=10),
        limit=fake.random_number(digits=3),
        expiration_date=fake.credit_card_expire()
    )

    card_dict = card.__dict__

    return card_dict


def generate_buy():
    buy = BuyEvent(
        person_id=fake.unique.random_int(min=1, max=2002, step=1),
        name=fake.unique.name(),
        email=fake.unique.email(),
        address=fake.unique.address(),
        salary=fake.random_number(digits=4),
        cpf=fake.cpf(),
        card_id=fake.unique.random_int(min=1, max=2002, step=1),
        card_number=fake.credit_card_number(),
        account_id=fake.unique.random_int(min=1, max=2002, step=1),
        status_id=fake.random_int(min=0, max=10),
        limit=fake.random_number(digits=3),
        expiration_date=fake.credit_card_expire()
    )

    buy_dict = buy.__dict__

    return buy_dict


def generate_event():
    event_type = random.randint(1, 4)
    if (event_type == 1):
        event_data = generate_person()
    elif (event_type == 2):
        event_data = generate_card()
    elif (event_type == 3):
        event_data = generate_buy()
    else:
        event_data = generate_account()
    return event_data