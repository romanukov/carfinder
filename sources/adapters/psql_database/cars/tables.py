from sqlalchemy import String, Column, Integer, ForeignKey, Float, \
    DateTime
from sqlalchemy.orm import relationship

from adapters.psql_database.accounts.tables import AccountsTable
from adapters.psql_database.base import BaseTable


class CarsTable(BaseTable):
    car_id = Column(Integer, primary_key=True)
    model = Column(String)
    category = Column(String)
    year_of_manufacture = Column(Integer)
    hoster_email = Column(Integer, ForeignKey(AccountsTable.email))
    hoster = relationship(AccountsTable, uselist=False, backref='cars_table')
    tags = list['TagsTable']
    reviews = list['ReviewsTable']
    extras = list['Extra']
    description = Column(String)
    features = list['TagsTable']
    guidelines = Column(String)
    faqs = dict[str, str]
    current_geotag = Column(String)
    price = Column(Float)


class TagsTable:
    id = Column(Integer, primary_key=True)
    icon = Column(String)
    name = Column(String)


class ReviewsTable:
    id = Column(Integer, primary_key=True)
    account_email = Column(Integer, ForeignKey(AccountsTable.email))
    account = relationship(AccountsTable, uselist=False,
                           backref='reviews_table')
    datetime_of_create = Column(DateTime)
    evaluation = Column(Integer)
    comment = Column(String)


class Extra:
    id = Column(Integer, primary_key=True)
    name = Column(Integer)
    description = Column(String)
    price = Column(Float)
