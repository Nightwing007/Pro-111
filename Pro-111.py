import csv
import pandas as pd
import plotly.figure_factory as pf
import statistics as st
import random
import plotly.graph_objects as pg

f = pd.read_csv("School3.csv")
df = f["Math_score"].tolist()

mean = st.mean(df)
deviation = st.stdev(df)
print(mean)
print(deviation)

# ----------------------------------------------------------------------------------------------
def sampling(counter):
  dataset = []
  for i in range(0,counter):
    randomN = random.randint(0,len(df)-1)
    value = df[randomN]
    dataset.append(value)
  mean = st.mean(dataset)
  return mean
# ---------------------------
meanList = []
for i in range(0,100):
  num = sampling(30)
  meanList.append(num)
meanS = st.mean(meanList)
deS = st.stdev(meanList)
print(meanS)
print(deS)

# ----------------------------------------------------------------------------------------------
# Range 1
start_dev_1 = mean - deS
end_dev_1 = mean + deS
dev_range_1 = [result for result in meanList if result > start_dev_1 and result < end_dev_1] 
dev_p_1 = format(len(dev_range_1) * 100.0 / len(meanList))
print("1st deS percentage : ",dev_p_1)

# Range 2
start_dev_2 = mean - 2*deS
end_dev_2 = mean + 2*deS
dev_range_2 = [result for result in meanList if result > start_dev_2 and result < end_dev_2] 
dev_p_2 = format(len(dev_range_2) * 100.0 / len(meanList))
print("2nd deS percentage : ",dev_p_2)

# Range 3
start_dev_3 = mean - 3*deS
end_dev_3 = mean + 3*deS
dev_range_3 = [result for result in meanList if result > start_dev_3 and result < end_dev_3] 
dev_p_3 = format(len(dev_range_3) * 100.0 / len(meanList))
print("3rd deS percentage : ",dev_p_3)
# ----------------------------------------------------------------------------------------------
f1 = pd.read_csv("School_3_Sample.csv")
df1 = f1["Math_score"].tolist()
mean1 = st.mean(df1)
print(mean1)

z = (mean1 - meanS) / deS
print("z score - ",z)

# ----------------------------------------------------------------------------------------------
fig = pf.create_distplot([meanList],["sample marks"],show_hist = False)
fig.add_trace(pg.Scatter(x = [meanS,meanS],y= [0,0.2],name = "Sample mean",mode = "lines"))
fig.add_trace(pg.Scatter(x = [start_dev_1,start_dev_1],y=[0,0.2],mode = "lines",name = "stdev1_start"))
fig.add_trace(pg.Scatter(x = [start_dev_2,start_dev_2],y=[0,0.2],mode = "lines",name = "stdev2_start"))
fig.add_trace(pg.Scatter(x = [start_dev_3,start_dev_3],y=[0,0.2],mode = "lines",name = "stdev3_start"))
fig.add_trace(pg.Scatter(x = [end_dev_1,end_dev_1],y=[0,0.2],mode = "lines",name = "stdev1_end"))
fig.add_trace(pg.Scatter(x = [end_dev_2,end_dev_2],y=[0,0.2],mode = "lines",name = "stdev2_end"))
fig.add_trace(pg.Scatter(x = [end_dev_3,end_dev_3],y=[0,0.2],mode = "lines",name = "stdev3_end"))
fig.add_trace(pg.Scatter(x = [mean1,mean1],y= [0,0.2],name = "after mean",mode = "lines"))
fig.show()
