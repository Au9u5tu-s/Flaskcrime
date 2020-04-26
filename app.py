from flask import Flask, render_template, url_for
import pandas as pd
import os
import time
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import folium
from flask import request
from flask import jsonify
import pickle


dfd = pd.read_csv("crime.csv")
'exec(%matplotlib inline)'

import math
import io
import base64
from folium import plugins

data = pd.read_csv("crimech.csv")

crimes_df = data[data.IS_CRIME==1]
traffic_df = data[data.IS_TRAFFIC==1]

df = pd.read_csv("crimetime1.csv")

sns_plot = sns.countplot(x="OFFENSE_CATEGORY_ID", data=df)
max = dfd["OFFENSE_CATEGORY_ID"].mode().iloc[0]

fig1 = sns_plot.get_figure()
fig1.savefig("static/img/charts/output1.jpg")
fig1.clf()

sns_plot = sns.countplot(x="OFFENSE_CATEGORY_ID", hue="DISTRICT_ID",data=df)
fig2 = sns_plot.get_figure()
fig2.savefig("static/img/charts/output2.jpg")
fig2.clf()

sns_plot = sns.countplot(x="OFFENSE_CATEGORY_ID", hue="IS_CRIME",data=df)
fig3 = sns_plot.get_figure()
fig3.savefig("static/img/charts/output3.jpg")
fig3.clf()

mplt = plt.matshow(df.corr())
fig4 = mplt.get_figure()
fig4.savefig("static/img/charts/output4.jpg")
fig4.clf()

sns_plot = sns.heatmap(df.isnull(),cmap="viridis")
fig5 = sns_plot.get_figure()
fig5.savefig("static/img/charts/output5.jpg")
fig5.clf()

y=dfd.isnull().sum().sort_values(ascending=False)[:6].index
x=dfd.isnull().sum().sort_values(ascending=False)[:6]
plt.figure(figsize=(8,8))
sns_plot = sns.barplot(x,y)
plt.title("counts of missing value",size=20)
fig6 = sns_plot.get_figure()
fig6.savefig("static/img/charts/output6.jpg")
fig6.clf()

months = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
crimes_pt = crimes_df.pivot_table(index='OFFENSE_CATEGORY_ID', columns='MONTH', aggfunc='size')
crimes_scaled = crimes_pt.apply(lambda x: x / crimes_pt.max(axis=1))
crimes_scaled.columns = months
plt.figure(figsize=(8,10))
plt.title('Average Number of Crimes per Category and Month', fontsize=14)
sns_plot = sns.heatmap(crimes_scaled, cmap='inferno', cbar=True, annot=False, fmt=".0f")
fig7 = sns_plot.get_figure()
fig7.savefig("static/img/charts/output7.jpg", bbox_inches = 'tight')
fig7.clf()

crimes_pt = crimes_df.pivot_table(values='YEAR', index='DAY', columns='MONTH', aggfunc=len)
crimes_pt_year_count = crimes_df.pivot_table(values='YEAR', index='DAY', columns='MONTH', aggfunc=lambda x: len(x.unique()))
crimes_avg = crimes_pt / crimes_pt_year_count
crimes_avg.columns = months
plt.figure(figsize=(10,12))
plt.title('Average Number of Complaints per Day and Month', fontsize=14)
sns_plot = sns.heatmap(crimes_avg.round(), cmap='inferno', linecolor='grey',linewidths=0.1, cbar=True, annot=True, fmt=".0f")
fig8 = sns_plot.get_figure()
fig8.savefig("static/img/charts/output8.jpg", bbox_inches = 'tight')
fig8.clf()


app = Flask(__name__)

data = pd.read_csv("crimech.csv")
lastmodified = time.ctime(os.path.getmtime('crimech.csv'))

@app.route('/')
def dashboard():
    return render_template("dashboard.html", value = [len(data),lastmodified, max])


@app.route('/maps')
def maps():
    return render_template("maps.html")

@app.route('/map')
def map():
    data = pd.read_csv("crimech.csv")
    crimes_df = data[data.IS_CRIME==1]
    traffic_df = data[data.IS_TRAFFIC==1]
    crimes_df = crimes_df.dropna(subset=['GEO_LAT', 'GEO_LON'])
    robbery_df = crimes_df[(crimes_df.OFFENSE_CATEGORY_ID=='robbery') & (crimes_df.YEAR==2019)]
    denver_map = folium.Map(location=[39.72378, -104.899157],
                           zoom_start=12)
    for i in range(len(robbery_df)):
        lat = robbery_df.iloc[i]['GEO_LAT']
        long = robbery_df.iloc[i]['GEO_LON']
        popup_text = """Neighborhood: {}<br>
                        Date Occurred: {}<br>""".format(crimes_df.iloc[i]['NEIGHBORHOOD_ID'],
                                                   crimes_df.iloc[i]['FIRST_OCCURRENCE_DATE'])
        folium.CircleMarker(location=[lat, long], popup=popup_text, radius=8, color='#800080', fill=True).add_to(denver_map)
    denver_map.save('static/maap.html')
    return render_template("map.html")

@app.route('/tables')
def tables():
    dff = pd.read_csv("crimecheckpoint.csv")
    dff = dff.head(15)
    return render_template("tables.html", tables=[dff.to_html(classes='data')], titles=dff.columns.values)

@app.route('/user', methods=['POST','GET'])
def user():
    return render_template("user.html")

@app.route('/square', methods=['POST','GET'])
def square():
    # Firstcol = ['YEAR','DAY','DAY_OF_WEEK','MONTH']
    # Secondcol = ['assault','drug-alcohol','murder','other-crimes','public-disorder','theft','traffic-accident','white-collar-crime']
    # Thirdcol = ['D1','D2','D3','D4','D5','D6','D7']
    # Fourthcol = ['P111','P112','P113','P121','P122','P123','P211','P212','P213','P221','P222','P223','P311','P312','P313','P314','P321','P322','P323','P324','P411','P412','P421','P422','P423','P511','P512','P521','P522','P523','P611','P612','P621','P622','P623','P759']
    # Lastcol = ['N0','N1','N2','N3','N4','N5','N6','N7','N8','N9','N10','N11','N12','N13','N14','N15','N16','N17','N18','N19','N20','N21','N22','N23','N24','N25','N26','N27','N28','N29','N30','N31','N32','N33','N34','N35','N36','N37','N38','N39','N40','N41','N42','N43','N44','N45','N46','N47','N48','N49','N50','N51','N52','N53','N54','N55','N56','N57','N58','N59','N60','N61','N62','N63','N64','N65','N66','N67','N68','N69','N70','N71','N72','N73','N74','N75','N76','N77']
    colnames = ['YEAR','DAY','DAY_OF_WEEK','MONTH','assault','drug-alcohol','murder','other-crimes','public-disorder','theft','traffic-accident','white-collar-crime','D1','D2','D3','D4','D5','D6','D7','P111','P112','P113','P121','P122','P123','P211','P212','P213','P221','P222','P223','P311','P312','P313','P314','P321','P322','P323','P324','P411','P412','P421','P422','P423','P511','P512','P521','P522','P523','P611','P612','P621','P622','P623','P759','N0','N1','N2','N3','N4','N5','N6','N7','N8','N9','N10','N11','N12','N13','N14','N15','N16','N17','N18','N19','N20','N21','N22','N23','N24','N25','N26','N27','N28','N29','N30','N31','N32','N33','N34','N35','N36','N37','N38','N39','N40','N41','N42','N43','N44','N45','N46','N47','N48','N49','N50','N51','N52','N53','N54','N55','N56','N57','N58','N59','N60','N61','N62','N63','N64','N65','N66','N67','N68','N69','N70','N71','N72','N73','N74','N75','N76','N77']
    if request.method == "POST":
        OFFENSE_CATEGORY_ID = request.form["OFFENSE_CATEGORY_ID"]
        DISTRICT_ID = request.form["DISTRICT_ID"]
        PRECINCT_ID = request.form["PRECINCT_ID"]
        NEIGHBORHOOD_ID = request.form["NEIGHBORHOOD_ID"]
        YEAR = request.form["YEAR"]
        DAY = request.form["DAY"]
        DAY_OF_WEEK = request.form["DAY_OF_WEEK"]
        MONTH = request.form["MONTH"]

        data = [{ 'YEAR' : YEAR, 'DAY' : DAY, 'DAY_OF_WEEK' : DAY_OF_WEEK, 'MONTH' : MONTH, OFFENSE_CATEGORY_ID : 1, DISTRICT_ID : 1, PRECINCT_ID : 1, NEIGHBORHOOD_ID : 1}]
        dfd = pd.DataFrame(data, columns = colnames)
        dfd = dfd.fillna(0)
        loaded_model = pickle.load(open('RandomForestNew.sav', 'rb'))
        result = loaded_model.predict(dfd)
        if result[0] == 1.0:
            resultS = "9am to 9pm"
        else:
            resultS = "9pm to 9am"
        return render_template('user.html', message=resultS)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port = int (os.environ.get ("PORT", 5000)))
