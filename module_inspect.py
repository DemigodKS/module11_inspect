import inspect

class Adder:
    def __init__(self, number):
         self.number = number
    def __call__(self, x):
        print(self.number + x)

plus_7 = Adder(7)
results_search = []
type_ = type(plus_7)
results_search.append(type_)

has_attr = hasattr(plus_7, 'number')
results_search.append(has_attr)

dir_ = dir(plus_7)
results_search.append(dir_)

module_ = inspect.ismodule(Adder)
results_search.append(module_)

inspect_1 = ['type', 'results of dir', 'result of hasattr', 'ismodule']
inspect_2 = results_search

results_search_1 = dict(zip(inspect_1, inspect_2))
print(results_search_1)






