import pandas as pd

def counter(lst):
    no_true = [i for i in lst if (i is not True)]
    no_false_no_true = [i for i in no_true if (i is not False)]
    
    no_false_no_true = pd.Series(no_false_no_true)
    result = pd.value_counts(no_false_no_true)
    
    num_of_true = (len(lst) - len(no_true))
    num_of_false = len(no_true) - len(no_false_no_true) 
    
    for index, i in result.iteritems():
        print(f'{index} --> {i}')
    print(f'True --> {num_of_true}')
    print(f'False --> {num_of_false}')

        
lst = [1, '1', 'foo', True, [1, 2], 'foo', True, 1, {1, 2, 3}, (12,), {1: 'one', 2: 'two'}, 0, False, False]
counter(lst)