from sqlalchemy import String, Column, Boolean, Integer, ForeignKey, DateTime, \
    Float
from sqlalchemy.orm import relationship

from adapters.psql_database.accounts.tables import AccountsTable
from adapters.psql_database.base import BaseTable
from adapters.psql_database.cars.tables import CarsTable


class TripsTable(BaseTable):
    trip_id = Column(Integer, primary_key=True)
    start_datetime = Column(DateTime)
    estimated_end_date = Column(DateTime)
    car_id = Column(Integer, ForeignKey(CarsTable.car_id))
    car = relationship(CarsTable, uselist=False, backref='trips_table')
    customer_email = Column(String, ForeignKey(AccountsTable.email))
    customer = relationship(AccountsTable, uselist=False, backref='trips_table')
    price_amount = Column(Float)
    paid = Column(Boolean, default=False)
    started = Column(Boolean, default=False)
    ended = Column(Boolean, default=False)
    cancelled = Column(Boolean, default=False)
    real_end_date = Column(DateTime)
