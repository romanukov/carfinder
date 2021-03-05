from adapters.psql_database.base import BasePsqlRepo
from adapters.psql_database.trips.presenters import present_trip
from adapters.psql_database.trips.tables import TripsTable
from core.trips.entities import Trip
from core.trips.repos import ITripsRepo


class PsqlTripsRepo(BasePsqlRepo, ITripsRepo):

    def create(self, customer_email: str, trip_data: dict) -> Trip:
        trip = TripsTable(
            start_datetime=trip_data.start_datetime,
            estimated_end_date=trip_data.estimated_end_date,
            car_id=trip_data.car_id,
            car=trip_data.car,
            customer_email=customer_email,
            customer=trip_data.customer,
            price_amount=trip_data.price_amount,
            paid=trip_data.paid,
            started=trip_data.started,
            ended=trip_data.ended,
            cancelled=trip_data.cancelled,
            real_end_date=trip_data.real_end_date,
        )

        self.session.begin()
        self.session.add(trip)
        self.session.commit()

        return present_trip(trip)

    def set_paid(self, trip_id: int) -> None:
        trip = self.session.query(TripsTable).get(trip_id)
        if not trip:
            return None

        trip.paid = True

        self.session.begin()
        self.session.add(trip)
        self.session.commit()

    def set_started(self, trip_id: int) -> None:
        trip = self.session.query(TripsTable).get(trip_id)
        if not trip:
            return None

        trip.started = True

        self.session.begin()
        self.session.add(trip)
        self.session.commit()

    def set_ended(self, trip_id: int) -> None:
        trip = self.session.query(TripsTable).get(trip_id)
        if not trip:
            return None

        trip.ended = True

        self.session.begin()
        self.session.add(trip)
        self.session.commit()

    def set_cancelled(self, trip_id: int) -> None:
        trip = self.session.query(TripsTable).get(trip_id)
        if not trip:
            return None

        trip.cancelled = True

        self.session.begin()
        self.session.add(trip)
        self.session.commit()
