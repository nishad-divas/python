sample_string='CampusX is an Online Mentorship Program fOr EnginEering studentS'
result=[]
words=sample_string.split(' ')
for word in words:
    for i in word:
        if i.isupper():
            result.append(i)
print(len(result))
print(len(sample_string)-len(result)-len(words)+1)
print(len(sample_string))