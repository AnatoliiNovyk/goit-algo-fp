import turtle
import math

# Функція pythagoras_tree залишається без змін
def pythagoras_tree(t: turtle.Turtle, length: float, level: int) -> None:
    if level <= 0:
        return

    initial_pos = t.pos()
    initial_heading = t.heading()

    t.pendown()
    for _ in range(4):
        t.forward(length)
        t.right(90)
    t.penup()

    t.forward(length)
    new_length = length * math.sqrt(2) / 2
    
    t.right(45)
    pythagoras_tree(t, new_length, level - 1)

    t.setheading(initial_heading)
    t.setpos(initial_pos)
    
    t.forward(length)
    t.left(90)
    t.forward(length)
    t.right(90)
    
    t.left(45)
    pythagoras_tree(t, new_length, level - 1)

    t.setheading(initial_heading)
    t.setpos(initial_pos)


def main() -> None:
    screen = turtle.Screen()
    screen.title("Дерево Піфагора")

    # Створимо окрему turtle для повідомлень
    msg_turtle = turtle.Turtle()
    msg_turtle.hideturtle()
    msg_turtle.penup()
    msg_turtle.goto(0, 150)

    level = 0
    while level <= 0:
        msg_turtle.clear() # Очищуємо попереднє повідомлення
        try:
            user_input = screen.textinput("Рівень рекурсії", "Введіть рівень рекурсії (ціле, > 0):")
            if user_input is None: 
                return
            level = int(user_input)
            if level <= 0:
                msg_turtle.write("Рівень має бути додатнім числом!", align="center", font=("Arial", 16, "normal"))
        except (ValueError, TypeError):
            msg_turtle.write("Будь ласка, введіть ціле число.", align="center", font=("Arial", 16, "normal"))
            level = 0
    
    msg_turtle.clear() # Очищуємо повідомлення після успішного вводу

    # Основна turtle для малювання
    t = turtle.Turtle()
    t.speed(0)
    t.hideturtle()
    
    initial_length = 80
    t.penup()
    t.goto(-initial_length / 2, -250)
    t.left(90)
    
    pythagoras_tree(t, initial_length, level)

    screen.exitonclick()

if __name__ == "__main__":
    main()
