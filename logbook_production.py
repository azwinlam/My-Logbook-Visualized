import pandas as pd
import matplotlib.pyplot as plt
import dateutil
import seaborn as sns
import numpy as np
plt.style.use('seaborn-deep')
colors = {"A330": "#7D94CA", "A321": '#3F569D', "A320": '#1E3174'}

#load logbook csv file
logbook = "mylogbook.csv"

#skipping 5 rows for the standard logbook format for Cathay Pacific
df = pd.read_csv(logbook, encoding="utf-8",skiprows=5)

#label columns 
columns = ['date','flight_num','city_pair','ac_reg','block_time','off_block','airborne','landing','on_block','takeoff','landing','autoland','commander']
df.columns = columns

#change flight number from float to int.
df['flight_num'] = df['flight_num'].astype(int)


#split city pairs to origin and destination
orig_dest = df['city_pair'].str.split(expand = True)
df['origin'] = orig_dest[0]
df['destination'] = orig_dest[1]

#renaming columns with origin and destination
df = df[['date',
 'flight_num',
 'city_pair',
 'origin',
 'destination',
 'ac_reg',
 'block_time',
 'off_block',
 'airborne',
 'landing',
 'on_block',
 'takeoff',
 'landing',
 'autoland',
 'commander']]


 #The most flown flight number
plt.figure(num=None, figsize=(18, 10), dpi=80, facecolor='w')
df['flight_num'].value_counts().head(50).plot(kind='bar',color= colors["A320"]);
plt.title("Which route did I fly most?")
plt.savefig('Which route did I fly most.png', bbox_inches='tight')

new_df = df.assign(ac_type = "airbus")

new_df.loc[new_df['ac_reg'].str.contains("B-HS"),'ac_type'] = 'A320'
new_df.loc[new_df['ac_reg'].str.contains("B-HT"),'ac_type'] = 'A321'
new_df.loc[new_df['ac_reg'].str.contains("B-L"),'ac_type'] = 'A330'
new_df.loc[new_df['ac_reg'].str.contains("B-HL"),'ac_type'] = 'A330'
new_df.loc[new_df['ac_reg'].str.contains("B-HY"),'ac_type'] = 'A330'
new_df.loc[new_df['ac_reg'].str.contains("B-HW"),'ac_type'] = 'A330'

#which aircraft type did I fly most?
plt.figure(num=None, figsize=(18, 10), dpi=80, facecolor='w')
ax = new_df['ac_type'].value_counts().plot(kind='barh', fontsize=13, color = colors["A320"]);
ax.set_alpha(0.8)
ax.set_title("Which aircraft type did I fly most?", fontsize=18)
ax.set_xlabel("Number of Sectors", fontsize=18);
ax.set_xticks(range(0,1100,100))

# totals = []
# for i in ax.patches:
#     totals.append(i.get_width())
# total = sum(totals)

# for i in ax.patches:
#     # get_width pulls left or right; get_y pushes up or down
#     ax.text(i.get_width()+.5, i.get_y()+.3, \
#             str(round((i.get_width()/total)*100, 1))+'%', 
#             fontsize=15,color='dimgrey')
    
ax.invert_yaxis()
plt.savefig('Which aircraft type did I fly most.png', bbox_inches='tight')
plt.clf()

#Which captain did I fly with most?
df["commander"].value_counts().head(20).plot(kind="barh",figsize=(10,7),color = colors["A320"]).invert_yaxis()
plt.title("Which captain did I fly with most by Sectors?")
plt.xlabel("Sectors")
plt.savefig('Which captain did I fly with most by sectors.png',bbox_inches='tight')

#changing block time to date_time
new_df['block_time'] = pd.to_datetime(new_df['block_time'])
new_df['block_time'] = new_df['block_time'].dt.strftime('%H:%M:%S')
new_df['block_time'] = pd.to_timedelta(new_df['block_time'])



#Cockpit Hours Shared Top 30 Commanders
timespent = new_df.groupby('commander')['block_time'].sum()
timespent = timespent.reset_index().set_index('commander')
plt.figure(num=None, figsize=(18, 10), dpi=80, facecolor='w')

timespent.block_time.astype('timedelta64[h]').sort_values(ascending=True)[-30:].plot.barh(color = colors["A320"])
plt.title("Cockpit Hours Shared, Top 30 Commanders")
plt.xlabel("Hours")
plt.ylabel("Commander")
plt.savefig('Cockpit Hours Shared Top 30 Commanders.png', bbox_inches='tight')

#Sectors sorted by each Airframe
import matplotlib.patches as mpatches

plt.figure(num=None, figsize=(18, 10), dpi=80, facecolor='w')
colors = {"A330": "#7D94CA", "A321": '#3F569D', "A320": '#1E3174'}
sort_graph = new_df.groupby(["ac_type","ac_reg"]).count()
sort_graph = sort_graph.sort_values(by=["ac_type","date"],ascending=False).date
# sort_graph.plot.bar(color= [colors[i] for i in sort_graph.index.get_level_values(0)],legend=False)
sort_graph.plot.bar(color=[colors[i] for i in sort_graph.index.get_level_values(0)])
plt.title("Sectors On Each Airframe Sorted by Type and Registration")
plt.ylabel("Count")
plt.xlabel("Type and Registration")
plt.xticks(np.arange(sort_graph.shape[0], step=1), [i for i in sort_graph.index.get_level_values(1)])

a330_patch = mpatches.Patch(color="#7D94CA", label='A330')
a321_patch = mpatches.Patch(color="#3F569D", label='A321')
a320_patch = mpatches.Patch(color="#1E3174", label='A320')
plt.legend(handles=[a330_patch,a321_patch,a320_patch],loc="best")
plt.savefig('Sectors By Airframe.png', bbox_inches='tight')



#'Destinations Count Not Hong Kong.png Mainly Tailored to KA Routes
china_l = ['HKG','HGH','SYX','NGB','PVG','CSX','HAK','NKG','CGO','WNZ','XMN','FOC','CKG','CAN','XIY','WUH','CTU','PEK','TAO','KWL','KMG','SHA','TNA',"NNG","KMQ"]
non_china_l = ['HKT','HAN','CRK','OKA','BKI','TPE', 'PNH','RMQ','KHH','FUK','CJU','CNX','RGN','DAD','MNL','CCU','REP','PUS','HND','HIJ','BLR','PEN','KIJ','DPS','KUL','DAC','KTM',"DVO","TKS"]
china_colors = {k:"#df2407" for k in china_l}
non_china_colors = {k:"#22559E" for k in non_china_l}

def merge_two_dicts(x, y):
    z = x.copy()   # start with x's keys and values
    z.update(y)    # modifies z with y's keys and values & returns None
    return z

port_colors =  merge_two_dicts(china_colors, non_china_colors)


plt.figure(num=None, figsize=(18, 10), dpi=80, facecolor='w')
dest_graph = new_df.destination.value_counts()[1:]
dest_graph.plot.bar(color=["black" if i not in port_colors else port_colors[i] for i in dest_graph.index])
plt.title("Sectors To Each Destination (Not-HKG)")
plt.ylabel("Count")
plt.xlabel("Destinations")


china_patch = mpatches.Patch(color="#df2407", label='China')
non_china_patch = mpatches.Patch(color="#22559E", label='Non-China')

plt.legend(handles=[china_patch,non_china_patch],loc="best")
plt.savefig('Destinations Count Not Hong Kong.png', bbox_inches='tight')