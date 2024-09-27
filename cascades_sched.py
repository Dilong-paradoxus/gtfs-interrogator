#Plots a couple amtrak cascades runs
import matplotlib.pyplot as plt
import numpy as np

#Trains, from Vancouver headed south
casc_516 = [12.5,10.617,10.067,9.85,9.35,8.933,8.5]
casc_517 = [7.25,9.23,9.717,9.95,10.617,11.0,11.667]
casc_518 = [22.0,20.117,19.567,19.35,18.85,18.433,18.0]

#x = [0,1,2,3,4,5,6]
x = ["Vancouver, BC","Bellingham, WA","Mount Vernon, WA","Stanwood, WA","Everett, WA", "Edmonds, WA","Seattle, WA"]

# plot
fig, ax = plt.subplots()

ax.plot(x, casc_516, linewidth=1.5, label="Cascades 516")
ax.plot(x, casc_517, linewidth=1.5, label="Cascades 517")
ax.plot(x, casc_518, linewidth=1.5, label="Cascades 518")

ax.set(xlim=(-1, 7), xticks=np.arange(1, 8),
       ylim=(7,23), yticks=np.arange(7, 23))

plt.xticks(rotation=90)
ax.grid(True)
ax.legend(bbox_to_anchor=(1.05, 1),
                         loc='upper left', borderaxespad=0.)

plt.tight_layout()
plt.show()
