from prefect import flow


@flow
def my_first_flow(name: str = "world"):
    print(f"Hello {name} from Prefect! 🤗")

