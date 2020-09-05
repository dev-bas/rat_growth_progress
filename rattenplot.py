import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('rats.csv', index_col=0)

rats = ['Kiwi', 'Oscar', 'Moomin', 'Freddie', 'Daffy']

for rat in rats:
    df2 = df[df['Name'] == rat]
    plt.scatter(df2['Age'], df2['Weight'])
    plt.plot(df2['Age'], df2['Weight'])

plt.title('Rat grow rate')
plt.xlabel('Age in days')
plt.ylabel('Weight in grams')
plt.legend(rats)
plt.show()
