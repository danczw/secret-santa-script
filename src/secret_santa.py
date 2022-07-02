import random
import numpy as np

def main():
    print("This is a secret santa shuffle script!\n")
    print("\nPlease enter your secret santa participants separated by a comma:")
    teilnehmer = input()
    teilnehmer = teilnehmer.replace(" ", "").split(sep=",")
    x = np.arange(len(teilnehmer))
    runs = 1

    while True:
        random.shuffle(x)
        index_check =  []

        for number in x:
            if number == x[number]:
                index_check.append(1)
            else:
                index_check.append(0)
        sum_index_check = sum(index_check)

        if sum_index_check == 0:
            partner = 0
            print(f'Total number of runs: {runs}\n')
            for person in teilnehmer:
                print(f'{person} has to gift {teilnehmer[x[partner]]}.')
                partner = partner + 1
            break
        else:
            runs += 1

if __name__ == '__main__':
    main()