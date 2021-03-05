from typing import Optional

from adapters.psql_database.base import BasePsqlRepo
from adapters.psql_database.cars.presenters import present_car
from adapters.psql_database.cars.tables import CarsTable
from core.cars.entities import Car
from core.cars.repos import ICarsRepo


class PsqlCarsRepo(BasePsqlRepo, ICarsRepo):

    def create(self, account_email: str, car: dict) -> Car:
        car = CarsTable(
            car_id=car.car_id,
            model=car.model,
            category=car.category,
            year_of_manufacture=car.year_of_manufacture,
            hoster_email=account_email,
            tags=car.tags,
            reviews=car.reviews,
            extras=car.extras,
            description=car.description,
            features=car.features,
            guidelines=car.guidelines,
            faqs=car.faqs,
            current_geotag=car.current_geotag,
            price=car.price,
        )

        self.session.begin()
        self.session.add(car)
        self.session.commit()

        return present_car(car)

    def get_by_id(self, car_id: int) -> Optional[Car]:
        car = self.session.query(CarsTable).get(car_id)
        return present_car(car) if car else None

    def get_list(self, limit: int, offset: int) -> list[Car]:
        cars = self.session.query(CarsTable)
        return [present_car(car) for car in cars]

    def update(self, car_id: int, car_data: dict) -> None:
        car = self.session.query(CarsTable).get(car_id)

        # TODO а что если в car_data не будет всех полей?
        updated_car = CarsTable(
            car_id=car.id,
            model=car_data.model,
            category=car_data.category,
            year_of_manufacture=car_data.year_of_manufacture,
            hoster_email=car_data.hoster_email,
            hoster=car_data.hoster,
            tags=car_data.tags,
            reviews=car_data.reviews,
            extras=car_data.extras,
            description=car_data.description,
            features=car_data.features,
            guidelines=car_data.guidelines,
            faqs=car_data.faqs,
            current_geotag=car_data.current_geotag,
            price=car_data.price,
        )

        self.session.begin()
        self.session.add(updated_car)
        self.session.commit()

    def delete(self, car_id: int) -> None:
        car = self.session.query(CarsTable).get(car_id)

        self.session.begin()
        self.session.delete(car)
        self.session.commit()
