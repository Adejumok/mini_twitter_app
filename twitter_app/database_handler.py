import json
from pathlib import Path

db_ = Path.cwd() / "db.json"

db_.touch()


def read_data_base() -> list:
    with db_.open(mode="r", encoding="utf-8") as file:
        return json.load(file)


def write_to_data_base(user_data: list) -> None:
    with db_.open(mode="w", encoding="utf-8") as file:
        json.dump(user_data, file, indent=2)


def get_user(user_name: str):
    db_input: list = read_data_base()
    for user in db_input:
        if user["user_name"] == user_name:
            return user
    return None


def profile_update(user_name: str, profile: dict):
    user: dict = get_user(user_name)
    if user is None:
        return Exception("This user does not exist in the database!")
    user["profile"].append(profile)

    db_input = read_data_base()
    for user_ in range(len(db_input)):
        if db_input[user_]["user_name"] == user_name:
            db_input[user_] = user
            break

    write_to_data_base(db_input)


def write_tweet(user_name: str, tweet: dict):
    user: dict = get_user(user_name)
    if user is None:
        return Exception("This user does not exist in the database!")
    user["profile"][0]["tweets"].append(tweet)

    db_input = read_data_base()
    for user_ in range(len(db_input)):
        if db_input[user_]["user_name"] == user_name:
            db_input[user_] = user
            break

    write_to_data_base(db_input)
