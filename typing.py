import time as t
import matplotlib.pyplot as plt

times = []
many = []
legend = []
count = 1
x = input('How many times do you wanna type? ')

print('This program count the time expend to typing the word PROGRAMMING. Do you will type the word '+str(x)+' times.')
input('Press ENTER to start.')

while count <= int(x):
    start = t.perf_counter()
    input('Type the word: ')
    end = t.perf_counter()
    time = round(end-start)
    times.append(time)
    many.append(count)
    xstr = str(count)+'a time'
    legend.append(xstr)
    count += 1

plt.xticks(many, legend)
plt.plot(many, times)
plt.show()
