import random, time, colorama
from colorama import Fore

comp_turn = ["r", "s", "p"]
count = [0, 0]


def rsp_choice(t):
    if t == "r":
        print("<Rock>")
    elif t == "p":
        print("<Paper>")
    elif t == "s":
        print("<Scissors>")


def main():
    gameloop = True
    while gameloop:
        turn = input(Fore.YELLOW + "START GAME, SELECT: " +
                     Fore.GREEN + "r - ROCK" + Fore.BLUE + " / s - SCISSORS" +
                     Fore.WHITE + " / p - PAPER" + Fore.LIGHTRED_EX + " / exit - EXIT: ")
        print(Fore.WHITE + "-----------------------------------------------------------------------")
        time.sleep(0.2)

        if turn == "exit":
            print("EXIT")
            gameloop = False

        else:
            rsp_choice(turn)
            c_turn = random.choice(comp_turn)
            rsp_choice(c_turn)
            if (turn == "r" and c_turn == "s") or (turn == "s" and c_turn == "p") \
                    or (turn == "p" and c_turn == "r"):
                print("__Client WIN!__")
                count[0] += 1

            if (turn == "s" and c_turn == "r") or (turn == "p" and c_turn == "s") \
                    or (turn == "r" and c_turn == "p"):
                print("__Computer WIN!__")
                count[1] += 1

            if (turn == "r" and c_turn == "r") or (turn == "p" and c_turn == "p") \
                    or (turn == "s" and c_turn == "s"):
                print("DRAW")
        print("Score - ", count[0], ":", count[1])
        if count[0] == 3 or count[1] == 3:
            print(Fore.LIGHTYELLOW_EX, "GAME OVER")
            if count[0] == 3:
                print(Fore.BLUE, "CLIENT WON THE GAME !!!")
            else:
                print(Fore.CYAN, "COMPUTER WON THE GAME !!!")
            gameloop = False
        print(Fore.WHITE + "-----------------------------------------------------------------------")


if __name__ == "__main__":
    main()

