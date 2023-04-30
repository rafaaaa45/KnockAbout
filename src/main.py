from games.game_simulator import GameSimulator
from games.KnockAbout.simulator import TictactoeSimulator
from games.KnockAbout.players.human import HumanTictactoePlayer


def run_simulation(desc: str, simulator: GameSimulator, iterations: int):
    print(f"----- {desc} -----")

    for i in range(0, iterations):
        simulator.change_player_positions()
        simulator.run_simulation()

    print("Results for the game:")
    simulator.print_stats()


def main():
    print("ESTG IA Games Simulator")

    num_iterations = 1

    knockabout = [
        {
            "name": "KnockAbout - Human VS Random",
            "player1": HumanTictactoePlayer("Human"),
            "player2": HumanTictactoePlayer("Human")
        }
    ]

    for sim in knockabout:
        run_simulation(sim["name"], TictactoeSimulator(sim["player1"], sim["player2"]), num_iterations)


if __name__ == "__main__":
    main()
