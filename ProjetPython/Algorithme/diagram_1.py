import matplotlib.pyplot as plt
# Fonction pour mesurer le temps d'exécution en fonction du nombre de données
def measure_execution_time(data_range):
    execution_times = []
    for num_data in data_range:
        sub_actions = Action.list_action[:num_data]
        start_time = time.time()
        combi_actions_possible = search_all_possibilities(COUT_MAX)
        max_benefit, benefit_array = search_max_profit(combi_actions_possible)
        most_profitable_combinaison, price = search_max_profitable_combinaison(combi_actions_possible, benefit_array, max_benefit)
        end_time = time.time()
        execution_time = end_time - start_time
        execution_times.append(execution_time)
    return execution_times
# Création des données pour le graphique
data_range = range(10, len(Action.list_action) + 1, 10)
execution_times = measure_execution_time(data_range)
# Création du graphique
plt.plot(data_range, execution_times, marker='o', linestyle='-')
plt.xlabel('Nombre de données')
plt.ylabel('Temps d\'exécution (s)')
plt.title('Temps d\'exécution en fonction du nombre de données')
plt.grid(True)
 # Affichage du graphique
plt.show()


    
            
# Fonction pour mesurer le temps d'exécution en fonction du nombre de données
def measure_execution_time(data_range, csv_file):
    execution_times = []
    for num_data in data_range:
        sub_actions = read_file_csv(csv_file)[:num_data]
        start_time = time.time()
        ordered_list_actions = reorder_list(sub_actions)
        best_combinaison, total_price, total_gain = get_best_combinaison(ordered_list_actions, COUT_MAX)
        end_time = time.time()
        execution_time = end_time - start_time
        execution_times.append(execution_time)
    return execution_times
# Définissez les chemins de fichier pour vos données
CSV_FILE_1 = 'C:/Users/Uriel-Marie/OneDrive/Bureau/coursPython/TD/data/data_test.csv'
CSV_FILE_2 = 'C:/Users/Uriel-Marie/OneDrive/Bureau/coursPython/Algorithme/dataset1_Python+P7.csv'
# Création des données pour le graphique
data_range = range(10, len(read_file_csv(CSV_FILE_2)) + 1, 10)
execution_times = measure_execution_time(data_range, CSV_FILE_2)
# Création du graphique
plt.plot(data_range, execution_times, marker='o', linestyle='-')
plt.xlabel('Nombre de données')
plt.ylabel('Temps d\'exécution (s)')
plt.title('Temps d\'exécution en fonction du nombre de données')
plt.grid(True)
# Affichage du graphique
plt.show()