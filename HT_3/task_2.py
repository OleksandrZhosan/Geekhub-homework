"""
2. Write a script to remove empty elements from a list.    Test list:
[(), ('hey'), ('',), ('ma', 'ke', 'my'), [''], {}, ['d', 'a', 'y'], '', []]
"""

lst = [(), ('hey'), ('',), ('ma', 'ke', 'my'), [''], {}, ['d', 'a', 'y'], '', []]

lst_new = [_ for _ in lst if _]
print(lst_new)

