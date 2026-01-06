def nearestMultiple(num: int) -> int:
    if num >= 4:
        near = num + (4 - (num % 4))
    else:
        near = 4
    return near


def lose():
    print("\n\nYOU LOSE !")
    print("Better luck next time !")
    exit(0)


def check(xyz: list[int]) -> bool:
    i = 1
    while i < len(xyz):
        if (xyz[i] - xyz[i - 1]) != 1:
            return False
        i = i + 1
    return True


def start():
    xyz: list[int] = []
    last: int = 0

    while True:
        print("Enter 'F' to take the first chance.")
        print("Enter 'S' to take the second chance.")
        chance = input("> ")

        # player takes the first chance
        if chance.lower() == "f":
            while True:
                if last == 20:
                    lose()
                else:
                    print("\n Your Turn.")
                    print("\n How many numbers do you wish to enter ?")
                    inp = int(input("> "))

                    if inp > 0 and inp <= 3:
                        comp = 4 - inp
                    else:
                        print("Wrong input. You are disqualified from the game.")
                        lose()

                    i, j = 1, 1

                    print("Now enter the values")

                    while i <= inp:
                        a = input("> ")
                        a = int(a)
                        xyz.append(a)
                        i = i + 1

                    last = xyz[-1]

                    if check(xyz):
                        if last == 21:
                            lose()
                        else:
                            while j <= comp:
                                xyz.append(last + j)

                                j = j + 1

                            print("Order of inputs after computer's turn is: ")
                            print(xyz)
                            last = xyz[-1]
                    else:
                        print("\n You did not input consecutive intergers.")

        elif chance.lower() == "S":
            comp = 1
            last = 0
            while last < 20:
                j = 1
                while j <= comp:
                    xyz.append(last + j)
                    j = j + 1

                print("Order of inputs after computer's turn is: ")
                print(xyz)

                if xyz[-1] == 20:
                    lose()
                else:
                    print("\nYour turn.")
                    print("\nHow many numbers do you wish to enter ?")

                    inp = input("> ")
                    inp = int(inp)
                    i = 1
                    print("Enter your values")
                    while i <= inp:
                        xyz.append(int(input("> ")))
                        i += 1

                    last = xyz[-1]

                    if check(xyz):
                        near = nearestMultiple(last)
                        comp = near - last
                        if comp == 4:
                            comp = 3
                        else:
                            comp = comp
                    else:
                        print("\nYou did not input consecutive integers.")
                        lose()
        else:
            print("wrong choice")


if __name__ == "__main__":
    game = True
    while game:
        print("Player 2 is Computer.")
        print("Do you want to play the 21 number game? (Yes / No)")
        ans: str = input("> ")
        if ans.lower() == "yes":
            start()
        else:
            print("Do you want quit the game?(yes / no)")
            nex = input("> ")
            if nex.lower() == "yes":
                print("You are quitting the game...")
                exit(0)
            elif nex.lower() == "no":
                print("Continuing...")
            else:
                print("Wrong choice")
