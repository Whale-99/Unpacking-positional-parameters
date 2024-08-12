def print_params(a=1, b='строка', c=True):
    print(f"a = {a}")
    print(f"b = {b}")
    print(f"c = {c}")

print_params()
print_params(b = 25)
print_params(c = [1, 2, 3])

values_list = [10, 'текст', False]
values_dict = {'a': 100, 'b': 'новая строка', 'c': [1, 2, 3]}
print_params(*values_list)
print_params(**values_dict)

values_list_2 = [5, 'новый текст']
print_params(*values_list_2, 42)
