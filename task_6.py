def greedy_algorithm(items, budget):
    """
    Вирішує задачу вибору їжі за допомогою жадібного алгоритму.

    Примітка: Цей алгоритм є евристикою для задачі 0/1 про рюкзак.
    Він не завжди гарантує знаходження оптимального рішення, оскільки
    вибір найкращого локального варіанту на кожному кроці може 
    призвести до неоптимального глобального результату.
    """
    sorted_items = sorted(items.items(), key=lambda x: x[1]['calories'] / x[1]['cost'], reverse=True)
    
    chosen_dishes = []
    total_calories = 0
    current_budget = budget
    
    for item_name, details in sorted_items:
        if details['cost'] <= current_budget:
            chosen_dishes.append(item_name)
            total_calories += details['calories']
            current_budget -= details['cost']
            
    return chosen_dishes, total_calories, budget - current_budget

def dynamic_programming(items, budget):
    """
    Вирішує задачу вибору їжі за допомогою динамічного програмування.
    Гарантовано знаходить оптимальний набір страв для максимізації 
    калорійності при заданому бюджеті.
    """
    item_list = list(items.items())
    n = len(item_list)
    
    dp = [[0 for _ in range(budget + 1)] for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        item_name, details = item_list[i-1]
        cost = details['cost']
        calories = details['calories']
        for w in range(1, budget + 1):
            if cost <= w:
                dp[i][w] = max(calories + dp[i-1][w-cost], dp[i-1][w])
            else:
                dp[i][w] = dp[i-1][w]

    max_calories = dp[n][budget]
    chosen_dishes = []
    w = budget
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i-1][w]:
            item_name, details = item_list[i-1]
            chosen_dishes.append(item_name)
            w -= details['cost']
    
    chosen_dishes.reverse()
    return chosen_dishes, max_calories, budget - w

# Демонстрація залишається без змін...
