import codecademylib3_seaborn
import pandas as pd
import matplotlib.pyplot as plt

# load rankings data here:

wood_winners = pd.read_csv('Golden_Ticket_Award_Winners_Wood.csv')
steel_winners = pd.read_csv("Golden_Ticket_Award_Winners_Steel.csv")
#print(wood_winners)

# write function to plot rankings over time for 1 roller coaster here:

def ranking_function(name, df, park_name):
  new_df = df[(df.Name == name) & (df.Park==park_name)].reset_index()
  x_values = list(new_df['Year of Rank'])
  ax = plt.subplot()
  ax.set_xticks(range(len(x_values)))
  ax.set_xticklabels(x_values)
  y_values = list(new_df.Rank)
  plt.plot(range(len(x_values)), y_values, marker = 's')
  ax1 = plt.gca()
  ax1.invert_yaxis()
  plt.title(name)
  plt.xlabel("Years")
  plt.ylabel("Ranking")
  print(new_df)
  return plt.show()

#ranking_function("El Toro", wood_winners, "Six Flags Great Adventure")

plt.clf()

# write function to plot rankings over time for 2 roller coasters here:

def ranking_function2(name1, name2, df, park_name1, park_name2):
  new_df1 = df[(df.Name == name1) & (df.Park == park_name1)]
  new_df2 = df[(df.Name == name2) & (df.Park == park_name2)]
  x_values1 = list(new_df1['Year of Rank'])
  ax = plt.subplot()
  ax.set_xticks(range(len(x_values1)))
  ax.set_xticklabels(x_values1)
  x_values2 = list(new_df2['Year of Rank'])
  y_values1 = list(new_df1.Rank)
  y_values2 = list(new_df2.Rank)
  ax1 = plt.gca()
  ax1.invert_yaxis()
  plt.plot(range(len(x_values1)), y_values1, marker = 's', color= 'green', label = name1)
  plt.plot(range(len(x_values1)), y_values2, marker = 's', color = "red", label = name2)
  plt.legend()
  plt.title(name1 +" & "+ name2)
  plt.xlabel("Years")
  plt.ylabel("Ranking")
  return plt.show()
  
#ranking_function2("El Toro", "Boulder Dash", wood_winners, "Six Flags Great Adventure", "Lake Compounce")
#plt.clf()

# write function to plot top n rankings over time here:

def ranking_function3(n,df):
  new_df = df[df.Rank <= n]
  for name in set(new_df.Name):
    name_ranking = new_df[new_df.Name == name]
    plt.plot(name_ranking['Year of Rank'], name_ranking.Rank, label = name, marker = 's')
  ax1 = plt.gca()
  ax1.invert_yaxis()
  plt.legend(loc = 2)
  return plt.show()
  
#ranking_function3(3, wood_winners)

plt.clf()

# load roller coaster data here:

coasters = pd.read_csv("roller_coasters.csv")
#print(coasters.head())

# write function to plot histogram of column values here:

def histogram(df, column):
  plt.hist(df[column], range=(0, 100), bins = 30)#genius
  legend = [column]
  plt.legend()
  plt.show()

def histogram_heights(coaster_df):
  heights = coaster_df[coaster_df['height'] <= 140]
  plt.hist(heights, range = (0,100), bins=20)
  legend = [heights]
  plt.legend(legend)
  plt.show()
  
#print(histogram(coasters, 'speed'))

plt.clf()

# write function to plot inversions by coaster at a park here:

def inversions(df, park_name):
  park_df = df[(df.park == park_name)]
  roller_coaster = park_df['name']
  inversions = park_df['num_inversions']
  plt.bar(range(len(roller_coaster)), inversions)
  ax = plt.subplot()
  ax.set_xticks(range(len(roller_coaster)))
  ax.set_xticklabels(roller_coaster)
  plt.xticks(rotation=45)
  plt.legend([park_name])
  return plt.show()
 

#inversions(coasters, 'Parc Asterix')


plt.clf()
    
# write function to plot pie chart of operating status here:

def pie(coasters):
  df_operating = coasters[coasters.status == 'status.operating']
  df_closed = coasters[coasters.status == 'status.closed.definitely']
  count = [len(df_operating), len(df_closed)] #it was difficult and unlogical
  labelsdata = ['Operating', 'Closed']
  plt.pie(count, autopct = '%0.1f%%', labels = labelsdata)
  plt.legend()
  plt.axis('equal')
  plt.show()
  
#pie(coasters)


plt.clf()
  
# write function to create scatter plot of any two numeric columns here:

def scatter(df, column1, column2):
  c1 = df[column1]
  c2 = df[column2]
  x = range(len(df))
  ax = plt.subplot()
  plt.scatter(x, c1, color= 'blue', alpha= 0.5)
  plt.scatter(x, c2, color= 'green', alpha=0.5)
  ax.set_xlabel('Variables')
  ax.set_ylabel('Roller Coasters')
  plt.ylim(0, 200)
  plt.legend([column1, column2])
  return plt.show()
  
scatter(coasters, "speed", "height")








plt.clf()