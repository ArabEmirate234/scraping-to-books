import csv
from itertools import combinations
import time
from action import Action, OAction
from decimal import Decimal


reboot = input("Voulez vous commencez le programme (oui pour continuer, non pour stopper): ")

while reboot.lower() == "oui":
    print("Voici les différentes opérations possibles: ")
    print("1- force brute")
    print("2- algorithme optimisé")
    choix = int(input("Veuillez entrer votre choix: "))
    
    if(choix == 1):
        COUT_MAX = 500
        CSV_FILE = 'C:/Users/adecoin/Desktop/ProjetPython/Algorithme/data_test.csv'

        def r_combine_set(array, r):
            return list(combinations(array, r))

        # Récupérer les éléments qui sont dans le fichier csv puis les passer en paramètre à des instances d'actions
        def read_file_csv(file):
            with open(file) as csvfile:
                reader = csv.DictReader(csvfile, delimiter=';')
                print(reader)
                for row in reader:
                    Action(row['name'], float(row['price']), float(row['profit']))

        # test toutes les combinaisons de prix possibles et stock toutes celles inférieures à max_cost=500
        def toutes_possibilite(max_cost):
            combi_actions_possible = []
            for l in range(len(Action.list_action)+1):
                combinaisons = r_combine_set(Action.list_action, l)
                for combinaison in combinaisons:
                    price_sum = 0
                    for el in combinaison:
                        price_sum += el.price
                    if price_sum <= max_cost:
                        combi_actions_possible.append(combinaison)
                    else:
                        break
            return combi_actions_possible

        # récupère la liste des combinaisons dont la somme des prix est inférieure à max_cost et renvoie le plus grand bénéfice total et la liste des bénéfices totaux
        def cherche_profit_maximum(combi_actions_possible):
            benefit_array = []
            for combinaison in combi_actions_possible:
                benefit_sum = 0
                for el in combinaison:
                    benefit_sum += (el.profit * el.price)/100
                benefit_array.append(benefit_sum)
            max_benefit = max(benefit_array)
            return (max_benefit, benefit_array)

        # permet de retourner la liste de combinaison la plus rentable et son prix total avec le benefice total max, la liste des benefices totales et la liste des combinaisons
        def get_combinaison_most_profitable(combi_actions_possible, benefit_array, max_benefit):
            for i in range(len(benefit_array)):
                if benefit_array[i] == max_benefit:
                    price = 0
                    for action in combi_actions_possible[i]:
                        price += action.price

                    return (combi_actions_possible[i], price)

        # Affiche la combinaison la plus rentable, son prix et son rendement
        def display(most_profitable_combinaison, price, max_benefit):
            for action in most_profitable_combinaison:
                print("--------")
                print(action)
            print("--------------------------------------------")
            print("Coût total : ", round(price, 2),"€")
            print("Bénefice total : ", round(max_benefit, 2),"€")
            print("--------------------------------------------")

        debut = time.time()

        def main(file):
            read_file_csv(file)
            combi_actions_possible = toutes_possibilite(COUT_MAX)
            max_benefit, benefit_array = cherche_profit_maximum(combi_actions_possible)
            most_profitable_combinaison, price = get_combinaison_most_profitable(combi_actions_possible, benefit_array, max_benefit)

            display(most_profitable_combinaison, price, max_benefit)



        if __name__ == "__main__":
            main(CSV_FILE)

        fin = time.time()

        duree = fin - debut

        print("Le programme a mis", round(duree, 3), "secondes pour s'exécuter.")
        
        
    elif(choix == 2):
        # Initialisation
        COUT_MAX = 500

        CSV_FILE = 'C:/Users/adecoin/Desktop/ProjetPython/Algorithme/data_test.csv'
        CSV_FILE_2 = 'C:/Users/adecoin/Desktop/ProjetPython/Algorithme/dataset1_Python+P7.csv'
        CSV_FILE_3 = 'C:/Users/adecoin/Desktop/ProjetPython/Algorithme/dataset2_Python+P7 (1).csv'

        
        # Lecture et récupération des fichiers par la méthode DictReader par trie
        def read_file_csv(file):
            list_actions = []
            with open(file) as csvfile:
                reader = csv.DictReader(csvfile,delimiter=",")
                for row in reader:
                    price = float(row['price'])
                    profit = float(row['profit'])
                    if(price > 0.0 and profit > 0.0):
                        list_actions.append(OAction(row['name'], price, profit))
                    else:
                        pass
                return list_actions

        # Réarrangement de la liste des actions par ordre de profitabilité
        def reorder_list(list_actions):
            sorted_list = sorted(list_actions,key=lambda action: action.profitability, reverse=True)
            return sorted_list
        
        # Permet de donner la meilleur combinaison possible
        def get_best_combinaison(ordered_list_actions, cout_max):
            best_combinaison = []
            total_price = 0
            total_gain = 0
            for i in range(len(ordered_list_actions)):
                total_price += ordered_list_actions[i].price
                if(total_price <= cout_max):   
                    total_gain += ordered_list_actions[i].gain
                    best_combinaison.append(ordered_list_actions[i])
                else:
                    total_price -= ordered_list_actions[i].price
            return best_combinaison,total_price,total_gain
        
        if __name__ == "__main__":
            debut2 = time.time()
            list_actions = read_file_csv(CSV_FILE_3)
            ordered_list_actions = reorder_list(list_actions)
            best_combinaison,total_price,total_gain = get_best_combinaison(ordered_list_actions,COUT_MAX)
            print("------------------- Voici les résultats de l'algorithme optimisé ---------------------")
            print("--------------------------------------------------------------------------------------")
            for i in range(len(best_combinaison)):
                print(best_combinaison[i].name,", prix: ",str(round(best_combinaison[i].price,3)),"€, gain en 2 ans: ",str(round(best_combinaison[i].gain,3)),"€, profitabilité: ",str(round(best_combinaison[i].profitability,2)),"%")
            print("coût total: ",round(total_price,3), "€")
            print("Bénéfice total: ",round(total_gain,3),"€")
            fin2 = time.time()
            duree2 = fin2 - debut2
            print("Le programme a mis", round(duree2, 4), "secondes pour s'exécuter.")
            
    else:
        print("syntaxe non reconnu")
    
    reboot = input("Voulez vous continuez (oui pour continuer, non pour stopper): ")
        


