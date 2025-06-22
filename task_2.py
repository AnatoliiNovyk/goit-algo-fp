import turtle

def draw_tree(branch_len, t, level):
    if level > 0:
        t.forward(branch_len)
        t.right(45)  # Фіксований кут розгалуження
        draw_tree(branch_len * 0.6, t, level - 1)  # Фіксований коефіцієнт зменшення довжини гілки
        t.left(90)
        draw_tree(branch_len * 0.6, t, level - 1)
        t.right(45)
        t.backward(branch_len)

def main():
    level = int(input("Введіть рівень рекурсії: "))

    screen = turtle.Screen()
    screen.bgcolor("white")
    t = turtle.Turtle()
    t.left(90)
    t.speed(0)
    t.penup()
    t.goto(0, -200)
    t.pendown()
    draw_tree(100, t, level)
    t.hideturtle()
    screen.mainloop()

if __name__ == "__main__":
    main()
