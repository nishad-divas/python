test_str = 'best Campusx for DS students.'
repl_dict = {"best" : "is the best channel", "DS" : "Data-Science"}
word=test_str.split()
r=[]
for i in word:
    if i in repl_dict:
        r.append(repl_dict[i])
    else:
        r.append(i)

output=" ".join(r)
print(output)