import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(layout="centered", page_title="System Activity Tracker")
st.title("System Activity Tracker")
st.write("This application helps you to track the user's system activities.")

def appBilling(billingApps):
	totalBill=0
	for bill in billingApps:
		st.write('**Application name:**'+"  "+bill)
		singleBill=round((df[df.application == bill].time.count()/3600)*50,2)
		st.write('**Billed amount (in CAD):**$ ', singleBill)
		totalBill+=singleBill
	st.write('**Total Bill:**$',round(totalBill,2))
	st.download_button('Print Invoice', 'The estimated invoice amount for '+client+' on '+empData+' is CAD $'+str(round(totalBill,2)), file_name=empData+'_'+client+'.txt')

empData = st.selectbox("Select an employee:", ('Select','John','Kane','Raj','Steve','William'), index=0)
if empData == 'Select':
	st.write("Need a data file to visualize the employee's activity.")
else:
	if empData == 'John':
		data = pd.read_csv("\\Data\\John.csv")
	elif empData == 'Kane':
		data = pd.read_csv("/home/boss/Bombarding/projects/Activity Tracker/Data/Kane.csv")
	elif empData == 'Raj':
		data = pd.read_csv("/home/boss/Bombarding/projects/Activity Tracker/Data/Raj.csv")
	elif empData == 'Steve':
		data = pd.read_csv("/home/boss/Bombarding/projects/Activity Tracker/Data/Steve.csv")
	elif empData == 'William':
		data = pd.read_csv("/home/boss/Bombarding/projects/Activity Tracker/Data/William.csv")
	df = pd.DataFrame(data)	
	st.write(px.pie(df, names='application', title='Visiualization of overall application usage.'))
	uniqueApps = sorted(df['application'].unique())
	c1_apps=[]
	c2_apps=[]
	other_apps=[]
	all_apps=[]
	appCount=[]

	for app in uniqueApps:
		all_apps.append(app)
		if app.startswith('C1'):
			c1_apps.append(app)
		elif app.startswith('C2'):
			c2_apps.append(app)
		else:
			other_apps.append(app)
	for count in df.application.value_counts():
		appCount.append((count/3600))
	st.write(px.bar(title='Individual application usage', x=all_apps, y=appCount, labels={'x':'Used applications', 'y':'Usage in hours'},))
	st.write("**Client Billing:**")
	client = st.radio('Select the client', ("Client 1", "Client 2", "Common applications"), horizontal=True)
	if client == "Client 1":
		appBilling(c1_apps)
	elif client == "Client 2":
		appBilling(c2_apps)
	else:
		appBilling(other_apps)
