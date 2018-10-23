import time
from concurrent.futures import ThreadPoolExecutor

from api import GameRunner, ConnectFourClient, RandomPlayerStrategy

NUMBER_OF_GAMES = 1000
SERVER_URL = "http://localhost:8080"


def main():
    executor = ThreadPoolExecutor(max_workers=2)

    client = ConnectFourClient(SERVER_URL)

    strategy = RandomPlayerStrategy()

    future1 = executor.submit(
        GameRunner(client=client, player_id='Alice', strategy=strategy, number_of_games=NUMBER_OF_GAMES).run)
    future2 = executor.submit(
        GameRunner(client=client, player_id='Bob', strategy=strategy, number_of_games=NUMBER_OF_GAMES).run)

    while not future1.done() and not future2.done():
        time.sleep(1)


if __name__ == '__main__':
    main()
