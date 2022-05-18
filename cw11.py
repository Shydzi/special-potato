
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#Wykres liniowy
# sns.set(rc={'figure.figsize': (8, 8)})
# sns.lineplot(x=[1,2,3,4], y=[1,4,9,16],
#              label='linia nr1', color='red',
#              marker='o', linestyle=':')
# sns.lineplot(x=[1,2,3,4], y=[2,5,10,17],
#              label='linia nr2', color='green',
#              marker='^', linestyle=':')
# plt.xlabel('oś x')
# plt.ylabel('oś y')
# plt.title('Wykres liniowy')
# plt.show()

#Wykres liniowy
# s = pd.Series(np.random.randn(1000))
# s = s.cumsum()
# sns.set()
# wykres = sns.relplot(kind='line', data=s, label='linia')
# wykres.fig.set_size_inches(8, 6)
# wykres.fig.suptitle('Wykres linowy losowych danych')
# wykres.set_xlabels('indeksy')
# wykres.set_ylabels('wartości')
# wykres.add_legend()
# wykres.figure.subplots_adjust(left=0.1, right=0.9,
#                               bottom=0.1, top=0.9)
# plt.show()

#Wykres punktowy
# sns.set()
# df = pd.read_csv('iris.data',header=None,sep=',',decimal='.')
# df.columns=['sepal lenght','sepal height','petal length','petal width','class']
# print(df)
# wykres = sns.lineplot(data=df, x=df.index, y='sepal lenght',
#                       hue='class',palette=['yellow','orange','red'])
# wykres.set_xlabel('indeksy')
# wykres.set_title('Wykres linowy dabych z Iris database')
# wykres.legend(title='Rodzaj kwaitu')
# plt.show()

#Wykres
# sns.set()
# data={'a':np.arange(10),
#       'c':np.random.randint(0,50,10),
#       'd':np.random.randn(10)}
# data['b']=data['a']+10+np.random.randn(10)
# data['d']=np.abs(data['d'])*100
# print(data['c'])
# print(data['d'])
# df=pd.DataFrame(data)
# plot=sns.relplot(data=df,x="a",y="b",
#                 hue="c",palette='bright',size="d",legend=True)
# plot.fig.set_size_inches(6,6)
# plot.set(xticks=data['a'])
# plt.show()

#Wykres kolumnowy
# dane = {'Kraj': ['Belgia','Indie','Brazylia','Polska'],
#         'Stolica': ['Bruksela','New Delhi', 'Brasilia','Warszawa'],
#         'Populacja':[11190846,1303171035,207847528,38675467],
#         'Kontynet':['Europa','Azja','Ameryka Połódniowa','Europa']}
#
# df = pd.DataFrame(dane)
#
# sns.set()
# plot = sns.barplot(data=df,x='Kontynet',y='Populacja',
#                    ci=None, hue='Kontynet', estimator=np.sum,
#                    dodge=False, palette=['yellow','orange','red'])
# plot.legend(title='Populacja na kontynentach')
# plot.set(title='Wykres słupkowy')
# plt.show()

#Wykres 3D
# fig = plt.figure()
# ax = fig.add_subplot(111, projection='3d')
# print(type(ax))
# t=np.linspace(0,2*np.pi,100)
# z=t
# x=np.sin(t)*np.cos(t)
# y=np.tan(t)
# ax.plot(x,y,z,label='zadanie 1')
# ax.legend()
# plt.show()

#Wykres kolumnowy2
# dane = {'Kraj': ['Belgia','Indie','Brazylia','Polska'],
#         'Stolica': ['Bruksela','New Delhi', 'Brasilia','Warszawa'],
#         'Populacja':[11190846,1303171035,207847528,38675467],
#         'Kontynet':['Europa','Azja','Ameryka Połódniowa','Europa']}
#
# df = pd.DataFrame(dane)
# sns.set()
# plot = sns.catplot(data=df,x='Kontynet',y='Populacja',
#                    kind='bar',ci=None,hue='Kontynet')

# from mpl_toolkits.mplot3d.axes3d import get_test_data
#
# fig = plt.figure(figsize=plt.figaspect(0.5))
#
# ax = fig.add_subplot(1,2,1,projection='3d')
# np.random.seed(19680801)
# def rendrange(n,vmin,vmax):
#     return (vmax-vmin)*np

# fig = plt.figure()
# ax = fig.add_subplot(111,projection='3d')
# x=np.linespace(0,1,)