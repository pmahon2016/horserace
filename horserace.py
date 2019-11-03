import replit
import time
from random import randrange, uniform


def sel_horse():
    while True:
        h1 = 0
        h2 = 0
        h3 = 0
        h4 = 0
        print(
            "\t            ,--,\n\t    ,;_ ___/ /\|\n\t   ,;( )__, )   \n\t  ;;; //\\\ ||--.   \n\t  D---' || //  \\\ \n^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")

        message = "\n What horse do you bet on? "
        try:
            horse = input(message)
            horse_int = int(horse)
        except ValueError:
            replit.clear()
            print("\n" + str(horse) + " is not a number!")
            sel_horse()

        if horse_int < 5 and horse_int > 0:
            while 1:
                if h1 > 89:
                    print("\n END OF RACE")
                    if horse_int == 1:
                        print("\n YOU WIN!!!")
                        sel_horse()
                    else:
                        print("\n YOU LOSE!")
                        sel_horse()
                if h2 > 89:
                    print("\n END OF RACE")
                    if horse_int == 2:
                        print("\n YOU WIN!!!")
                        sel_horse()
                    else:
                        print("\n YOU LOSE!")
                        sel_horse()
                if h3 > 89:
                    print("\n END OF RACE")
                    if horse_int == 3:
                        print("\n YOU WIN!!!")
                        sel_horse()
                    else:
                        print("\n YOU LOSE!")
                        sel_horse()
                if h4 > 89:
                    print("\n END OF RACE")
                    if horse_int == 4:
                        print("\n YOU WIN!!!")
                        sel_horse()
                    else:
                        print("\n YOU LOSE!")
                        sel_horse()
                else:
                    h1_int = int(h1)
                    h2_int = int(h2)
                    h3_int = int(h3)
                    h4_int = int(h4)
                    # horse1
                    random1 = randrange(0, 3)
                    h1 = h1 + random1
                    # horse2
                    random2 = randrange(0, 3)
                    h2 = h2 + random2
                    # horse3
                    random3 = randrange(0, 3)
                    h3 = h3 + random3
                    # horse 4
                    random4 = randrange(0, 3)
                    h4 = h4 + random4
                    # visual
                    HorseModel1 = "\t            ,--,\n\t    ,;_ ___/ /\|\n\t   ,;( )_1, )   \n\t  ;;; //\\\ ||--.   \n\t  D---' || //  \\\ \n^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^"
                    HorseModel2 = "\t            ,--,\n\t    ,;_ ___/ /\|\n\t   ,;( )_2, )   \n\t  ;;; //\\\ ||--.   \n\t  D---' || //  \\\ \n^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^"
                    HorseModel3 = "\t            ,--,\n\t    ,;_ ___/ /\|\n\t   ,;( )_3, )   \n\t  ;;; //\\\ ||--.   \n\t  D---' || //  \\\ \n^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^"
                    HorseModel4 = "\t            ,--,\n\t    ,;_ ___/ /\|\n\t   ,;( )_4, )   \n\t  ;;; //\\\ ||--.   \n\t  D---' || //  \\\ \n^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^"
                    print(HorseModel1.expandtabs(h1_int))
                    print(HorseModel2.expandtabs(h2_int))
                    print(HorseModel3.expandtabs(h3_int))
                    print(HorseModel4.expandtabs(h4_int))
                    replit.clear()
                    time.sleep(0.1)  # Change the speed here- making it more or less choppy

        else:
            replit.clear()
            print("\n" + "We do not have a " + str(horse_int) + "th horse! Bet on horse 1, 2, 3, or 4!")


sel_horse()