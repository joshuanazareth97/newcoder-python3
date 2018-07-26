import matplotlib.pyplot as plt
from collections import Counter

def plot_count_of(parsed_data, term, mode="plot", w=11, h=6, filename = None):
    """Takes a list of dicts and plots (as a graph) the number of times
    a certain key is present."""
    if filename is None: filename = term
    filename = "Images/" + filename
    count =  Counter(item[term] for item in parsed_data)
    x = [key for key in count.keys()]
    y = [count[key] for key in x]
    plt.figure(figsize = (w,h))
    plt.ylabel('Count')
    plt.xlabel(term)
    plt.xticks(rotation=90)
    plt.subplots_adjust(bottom=0.5)
    if mode=="bar": plt.bar(x,y)
    else: plt.plot(x,y)
    plt.savefig("{}.png".format(filename))
    plt.clf()
