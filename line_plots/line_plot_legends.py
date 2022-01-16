import codecademylib
from matplotlib import pyplot as plt

months = range(12)
hyrule = [63, 65, 68, 70, 72, 72, 73, 74, 71, 70, 68, 64]
kakariko = [52, 52, 53, 68, 73, 74, 74, 76, 71, 62, 58, 54]
gerudo = [98, 99, 99, 100, 99, 100, 98, 101, 101, 97, 98, 99]

plt.plot(months, hyrule, label="Hyrule")
plt.plot(months, kakariko, label="Kakariko")
plt.plot(months, gerudo, label="Gerudo Valley")

#create your legend here
# legend_labels = ["Hyrule", "Kakariko", "Gerudo Valley"]

plt.legend(loc=8)
plt.show()