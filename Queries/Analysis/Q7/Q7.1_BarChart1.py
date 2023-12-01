import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

csvFile = pd.read_csv('./Queries/Query/Q7/Q7.csv', sep=',', names=['RepositoryName','NumOfPullRequests', 'NumOfForks'],
                      skiprows=1)

dfCsv = pd.DataFrame(csvFile)

pullRequestDf = dfCsv["NumOfPullRequests"].to_numpy()

barChartData = pd.cut(pullRequestDf, [-np.inf,0,3,5,10,20,50,np.inf], labels=['0','[1,3]','[4,5]','[6,10]','[11,20]','[21,50]','[50+]'] )
barChart = barChartData.value_counts().plot.bar(color="green" ,yticks=[100,500,1000,2000,3000,4000,5000,6000])

plt.xticks(rotation=0)
plt.title("Distribution Of Pull Requests By Repository")
plt.xlabel('Number Of Pull Requests') 
plt.ylabel('Number Of Repositories')

barChart.bar_label(barChart.containers[0])

plt.show()


