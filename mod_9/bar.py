import matplotlib.pyplot as plt
import numpy as np

def createLabels(data):
    for item in data:
        height = item.get_height()
        plt.text(item.get_x() + item.get_width()/2, height*1.05,
                '%d' % int(height),
                ha='center', va='bottom')


col_count = 3
bar_width = 0.2
korea_score = (554, 536, 538)
canada_score = (518, 523, 525)
china_score = (613,570,580)
france_score = (495,505,499)

index = np.arange(col_count)

k1 = plt.bar(index, korea_score, bar_width,
            alpha = 0.4, label ="Korea")
c1 = plt.bar(index+bar_width, canada_score, bar_width,
            alpha = 0.4, label ="Canada")
ch1 = plt.bar(index+(bar_width*2), china_score, bar_width,
             alpha = 0.4, label ="China")
f1 = plt.bar(index+(bar_width*3), france_score, bar_width,
             alpha = 0.4, label ="France")

createLabels(k1)
createLabels(c1)
createLabels(ch1)
createLabels(f1)

plt.ylabel('Mean PISA 2012 Scores')
plt.xlabel('Subjects')
plt.title('Test Scores By Countries')
plt.xticks(index+0.6/2, ("Math","Reading","Science"))
plt.legend(frameon= False, bbox_to_anchor=(1,1) ,loc=2)
plt.grid(True)

plt.show()

