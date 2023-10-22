import random

import numpy as np


def _calc_secret_pairs(santas: list) -> int:
    """Calculates random pairs of secret santa participants.
    Assures that no one has to gift himself.

    Args:
        santas (list): list of participants

    Returns:
        int: number of runs needed to find valid pairs
    """
    # iterate until no one has to gift himself
    while True:
        idx = np.arange(len(santas))
        random.shuffle(idx)  # type: ignore
        index_check = 0
        runs = 1

        # check if index is equal to value -> equals someone has to gift himself
        for nr in idx:
            if nr == idx[nr]:
                index_check += 1

        # if no one has to gift himself print pairs and return
        if index_check == 0:
            partner = 0
            print(f"\nTotal number of runs: {runs}\n####################")
            for person in santas:
                print(f"{person} has to gift {santas[idx[partner]]}.")
                partner = partner + 1
            return index_check
        # else increase runs and try again
        else:
            runs += 1


def main():
    # get input and split it into a list
    print("This is a secret santa shuffle script!\n")
    print("\nPlease enter your secret santa participants separated by a comma:")
    santas_str = input()
    santas_ls = santas_str.replace(" ", "").split(sep=",")

    # random shufle of wichtel to ensure randomness of pairs
    random.shuffle(santas_ls)

    _calc_secret_pairs(santas_ls)


if __name__ == "__main__":
    main()
