import random
import matplotlib.pyplot as plt

def simulate_dice_rolls(num_rolls: int):
    """
    Симулює задану кількість кидків двох гральних кубиків.
    """
    if num_rolls <= 0:
        print("Кількість кидків має бути додатнім числом.")
        return {}
        
    sums_count = {i: 0 for i in range(2, 13)}
    for _ in range(num_rolls):
        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)
        roll_sum = die1 + die2
        sums_count[roll_sum] += 1
    
    probabilities = {s: count / num_rolls for s, count in sums_count.items()}
    return probabilities

def analytical_probabilities():
    """
    Повертає аналітичні (теоретичні) ймовірності сум для двох кубиків.
    """
    # Всього існує 36 можливих комбінацій (6 граней * 6 граней).
    # Кількість способів отримати кожну суму:
    # 2: (1,1) - 1 спосіб
    # 3: (1,2), (2,1) - 2 способи
    # 4: (1,3), (2,2), (3,1) - 3 способи
    # ...
    # 7: (1,6), (2,5), (3,4), (4,3), (5,2), (6,1) - 6 способів
    return {
        2: 1/36, 3: 2/36, 4: 3/36, 5: 4/36, 6: 5/36, 7: 6/36,
        8: 5/36, 9: 4/36, 10: 3/36, 11: 2/36, 12: 1/36
    }

def print_results_table(simulated, analytical):
    """
    Друкує таблицю з порівнянням симульованих та аналітичних ймовірностей.
    """
    print("Сума | Симульована ймовірність (%) | Аналітична ймовірність (%)")
    print("--------------------------------------------------------------------")
    for s in sorted(simulated.keys()):
        sim_prob = simulated[s] * 100
        ana_prob = analytical[s] * 100
        print(f"{s:4} | {sim_prob:26.2f} | {ana_prob:26.2f}")

def plot_results(simulated, analytical):
    """
    Будує графік для порівняння симульованих та аналітичних ймовірностей.
    """
    sums = sorted(simulated.keys())
    sim_probs = [simulated[s] for s in sums]
    ana_probs = [analytical[s] for s in sums]
    
    plt.figure(figsize=(10, 6))
    plt.plot(sums, sim_probs, 'o-', label='Симуляція (Монте-Карло)')
    plt.plot(sums, ana_probs, 's-', label='Аналітичний розрахунок')
    plt.title('Порівняння ймовірностей сум при киданні двох кубиків')
    plt.xlabel('Сума чисел на кубиках')
    plt.ylabel('Ймовірність')
    plt.xticks(sums)
    plt.grid(True)
    plt.legend()
    plt.show()

# --- Демонстрація ---
num_simulations = 1000000

# Виконання симуляції
simulated_probs = simulate_dice_rolls(num_simulations)
if simulated_probs:
    analytical_probs = analytical_probabilities()
    # Виведення результатів
    print_results_table(simulated_probs, analytical_probs)
    plot_results(simulated_probs, analytical_probs)
