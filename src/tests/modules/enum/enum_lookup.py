# @ALLOWED_VERSIONS: 3.6, 3.7, 3.8, 3.9, 3.10, 3.11, 3.12, 3.13, 3.14

from enum import Enum
from random import choices, randint
from string import ascii_letters
from typing import Dict, List


class AccountTypeId(Enum):
    Admin = "".join(choices(ascii_letters, k=16))
    Business = "".join(choices(ascii_letters, k=16))
    Developer = "".join(choices(ascii_letters, k=16))
    Support = "".join(choices(ascii_letters, k=16))
    Guest = "".join(choices(ascii_letters, k=16))
    Manager = "".join(choices(ascii_letters, k=16))


def get_account_type_id(user_id: str, account_types: str) -> List[Dict[str, str]]:
    return [
        {"user_id": user_id, "account_type_id": getattr(AccountTypeId, acc_type).value}
        for acc_type in account_types.split(";")
    ]


def main():
    account_options = [k for k, v in AccountTypeId.__members__.items()]
    for _ in range(20_000):
        user_id = "".join(choices(ascii_letters, k=15))
        accounts = choices(account_options, k=randint(1, 3))
        assert get_account_type_id(user_id, ";".join(accounts)) == [
            {"user_id": user_id, "account_type_id": getattr(AccountTypeId, acc).value} for acc in accounts
        ]
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
