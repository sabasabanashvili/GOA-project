def manual_range(start, end, step):
    for i in range(start, end, step):
        if i % 2 == 0:
            print(i)

manual_range(1, 10, 2)
manual_range(10, 1, -2)
manual_range(1, 10, 1)
manual_range(1, 10, 3)
manual_range(10, 1, -1)