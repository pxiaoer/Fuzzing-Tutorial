def quadratic_solver(a, b, c):
    q = b * b - 4 * a * c
    solution_1 = (-b + my_sqrt_fixed(q)) / (2 * a)
    solution_2 = (-b - my_sqrt_fixed(q)) / (2 * a)
    return (solution_1, solution_2)




def quadratic_solver_fixed(a, b, c):
    if a == 0:
        if b == 0:
            if c == 0:
                # Actually, any value of x
                return (0, None)
            else:
                # No value of x can satisfy c = 0
                return (None, None)
        else:
            return (-c / b, None)

    q = b * b - 4 * a * c
    if q < 0:
        return (None, None)

    if q == 0:
        solution = -b / 2 * a
        return (solution, None)

    solution_1 = (-b + my_sqrt_fixed(q)) / (2 * a)
    solution_2 = (-b - my_sqrt_fixed(q)) / (2 * a)
    return (solution_1, solution_2)



quadratic_solver(3, 4, 1)