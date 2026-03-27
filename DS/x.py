test_str = 'CampusX best for DS students.'
repl_dict = {"best" : "is the best channel", "DS" : "Data-Science"}
word=test_str.split()
for i in word:
    for j in repl_dict.keys():
        if i==j:
            new=test_str.replace(i,repl_dict[j])
            print(new)