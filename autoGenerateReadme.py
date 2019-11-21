import os
import re

def atoi(text):
    return int(text) if text.isdigit() else text

def natural_keys(text):
    '''
    alist.sort(key=natural_keys) sorts in human order
    http://nedbatchelder.com/blog/200712/human_sorting.html
    (See Toothy's implementation in the comments)
    '''
    return [ atoi(c) for c in re.split(r'(\d+)', text) ]

folder = "Questions"
filenames = os.listdir("./" + folder)
filenames.sort(key=natural_keys)

with open('README.md','w') as f:
    content = """| 题号 | 题目&题解                                                    |
| ---- | ------------------------------------------------------------ |\n"""
    f.write(content)

    for name in filenames:
        if name[0].isdigit():
            number = name[:name.index(".")] 
            title = name[name.index(".")+1: -3].replace("-", " ").replace("_", " ").title()
            link = "https://github.com/Kaiwenkevinz/MyLeetCode/blob/master/" + folder + "/" + name
            content = "|  " + number + " | [" + title + "](" + link + ") |\n"
            f.write(content)
