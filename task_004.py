def my_foo(i):
    try:
        copy_list = my_list.copy()
        copy_list.remove(i)
        copy_list.index(i)
        return False
    except ValueError:
        return True


my_list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]

new_list = [my_list[i] for i in range(len(my_list)) if my_foo(my_list[i]) == True]

print(new_list)
