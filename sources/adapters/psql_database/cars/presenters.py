from adapters.psql_database.cars.tables import CarsTable
from core.accounts.entities import Account, PersonalData
from core.cars.entities import Car, Tag, Review, Extra


def present_car(car_table: CarsTable) -> Car:
    return Car(
        car_id=car_table.car_id,
        model=car_table.model,
        category=car_table.category,
        year_of_manufacture=car_table.year_of_manufacture,
        hoster=Account(
            email=car_table.hoster.email,
            personal_data=PersonalData(
                first_name=car_table.hoster.personal_data.first_name,
                last_name=car_table.hoster.personal_data.last_name,
            ),
            password_hash=car_table.hoster.password_hash,
            confirmed=car_table.hoster.confirmed,
        ),
        tags=[
            Tag(
                icon=tag.icon,
                name=tag.name
            ) for tag in car_table.tags
        ],
        reviews=[
            Review(
                account=review.account,
                datetime_of_create=review.datetime_of_create,
                evaluation=review.evaluation,
                comment=review.comment,
            ) for review in car_table.reviews
        ],
        extras=[
            Extra(
                name=extra.name,
                description=extra.description,
                price=extra.price,
            ) for extra in car_table.extras
        ],
        description=car_table.description,
        features=[
            Tag(
                icon=feature.icon,
                name=feature.name
            ) for feature in car_table.features
        ],
        guidelines=car_table.guidelines,
        faqs=car_table.faqs,
        current_geotag=car_table.current_geotag,
        price=car_table.price
    )
