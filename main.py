
import pandas as pd

if __name__ == '__main__':
    gyemantok = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/diamonds.csv')

    sum = 0
    for i in gyemantok['carat']:
        sum += i
    print('karat osszesen: ' + str(sum))


    atlag = sum / gyemantok.count()
    print('atlag: ' + str(atlag))

    szum = 0

    for gyemant in gyemantok.iterrows():
        pass


    print("Osszes ara: " + str(szum))

