from typing import Optional

from adapters.psql_database.accounts.presenters import present_account
from adapters.psql_database.accounts.tables import AccountsTable, PersonalDataTable
from adapters.psql_database.base import BasePsqlRepo
from core.accounts.entities import Account
from core.accounts.repos import IAccountsRepo


class PsqlAccountsRepo(BasePsqlRepo, IAccountsRepo):

    def create(self, email: str, password_hash: str, first_name: str, last_name: str) -> Account:
        account = AccountsTable(
            email=email,
            password_hash=password_hash,
            confirmed=False,
            personal_data=PersonalDataTable(
                first_name=first_name,
                last_name=last_name,
            ),
        )

        self.session.begin()
        self.session.add(account)
        self.session.commit()

        return present_account(account)

    def get_by_email(self, email: str) -> Optional[Account]:
        account = self.session.query(AccountsTable).get(email)
        return present_account(account) if account else None

    def authorize(self, email: str, password_hash: str) -> Optional[Account]:
        account = self.session.query(AccountsTable).get(email)
        if not account:
            return None

        if account.password_hash != password_hash:
            return None

        return present_account(account)

    def update_email(self, old_email: str, new_email: str) -> None:
        account = self.session.query(AccountsTable).get(old_email)
        if not account:
            return None

        account.email = new_email

        self.session.begin()
        self.session.add(account)
        self.session.commit()

    def update_personal_data(self, email: str, first_name: str, last_name: str) -> None:
        account = self.session.query(AccountsTable).get(email)
        if not account:
            return None

        account.personal_data = PersonalDataTable(
            first_name=first_name,
            last_name=last_name,
        ),

        self.session.begin()
        self.session.add(account)
        self.session.commit()

    def update_password(self, email: str, new_password_hash: str) -> None:
        account = self.session.query(AccountsTable).get(email)
        if not account:
            return None

        account.password_hash = new_password_hash

        self.session.begin()
        self.session.add(account)
        self.session.commit()

    def delete(self, email: str) -> None:
        account = self.session.query(AccountsTable).get(email)
        if not account:
            return None

        self.session.begin()
        self.session.delete(account)
        self.session.commit()
