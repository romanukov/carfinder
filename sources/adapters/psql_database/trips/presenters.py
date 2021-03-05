from adapters.psql_database.trips.tables import TripsTable
from core.accounts.entities import Account, PersonalData

from core.cars.entities import Car
from core.trips.entities import Trip


def present_trip(trip_table: TripsTable) -> Trip:
    return Trip(
        trip_id=trip_table.trip_id,
        start_datetime=trip_table.start_datetime,
        estimated_end_date=trip_table.estimated_end_date,
        car=Car(
            car_id=trip_table.car.car_id,
            model=trip_table.car.model,
            category=trip_table.car.category,
            year_of_manufacture=trip_table.car.year_of_manufacture,
            hoster=Account(
                email=trip_table.car.hoster.email,
                personal_data=PersonalData(
                    first_name=trip_table.car.hoster.personal_data.first_name,
                    last_name=trip_table.car.hoster.personal_data.last_name,
                )
            ),
            tags=trip_table.car.tags,
            reviews=trip_table.car.reviews,
            extras=trip_table.car.extras,
            description=trip_table.car.description,
            features=trip_table.car.features,
            guidelines=trip_table.car.guidelines,
            faqs=trip_table.car.faqs,
            current_geotag=trip_table.car.current_geotag,
            price=trip_table.car.price,
        ),
        customer=Account(
            email=trip_table.customer.email,
            personal_data=PersonalData(
                first_name=trip_table.customer.personal_data.first_name,
                last_name=trip_table.customer.personal_data.last_name,
            )
        ),
        price_amount=trip_table.price_amount,
        paid=trip_table.paid,
        started=trip_table.started,
        ended=trip_table.ended,
        cancelled=trip_table.cancelled,
        real_end_date=trip_table.real_end_date,
    )
