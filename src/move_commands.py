# from src.game import g

def show_score(score,key):           # Show score now
    # print("Your score is : ", score)
    print("********************************************")
    print(f"* Your total score is: {score} points     ")
    if key ==0:
        print("* You have no key                          *")
    else:
        print(f"* Nr of keys you have: {key}              ")
    print("********************************************")


    # g.set(37, 9, f" * score qis: {score} points")
    # g.set(37, 10,f" * keys you have: {key}")


def inventory(fruit_list, fruit, pos_x,pos_y,key, treasure):
# - E) Inventory - alla saker som man plockar upp ska sparas i en lista.
    fruit =[fruit, pos_x,pos_y]
    fruit_list.append(fruit)


def showlist(fruit_list):
# - F) Nytt kommando: "i", skriver ut innehållet i spelarens inventory.

    mylist=len(fruit_list)
    # print(mylist)
    if mylist==0:
        print("\t***********************************")
        print("\t* You have not collect fruits yet  :-(     *")
        print("\t***********************************")
    else:
        print("\t***********************************")
        print(f"\t** Fruit basket ({mylist}) ***************")
        print("\t***********************************")
        for lista in fruit_list:
            item = fruit_list.index(lista)+1
            print(f"\t   [{item}]  {lista[0]} ")
        print('\n')

def print_status(game_grid):
    """Visa spelvärlden och antal poäng."""
    # print("\n--------------------------------------")
    print(game_grid)
    # print("\n--------------------------------------")