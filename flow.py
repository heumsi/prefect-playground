import emoji
from prefect import flow


@flow(log_prints=True)
def my_first_flow(name: str = "world"):
    print(f"Hello {name} from Prefect! 🤗 This is modified!")


@flow(log_prints=True)
def my_second_flow():
    print(emoji.emojize('Python is :thumbs_up:'))
