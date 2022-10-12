import tkinter as ttk
import pandas as pd
import warnings
from unittest import result

from tblib import Frame
app = ttk.Tk()
app.title('Movie Recommonder')
app.geometry('600x400')
cols = ['user_id','movie_id','rating','ts']
df = pd.read_csv('u.data', sep='\t', names=cols).drop('ts',axis=1)
item_cols = ['movie_id','title'] + [str(i) for i in range(22)]
df1 = pd.read_csv('u.item', sep='|', names = item_cols, encoding = "ISO-8859-1")[['movie_id','title']]
movie = pd.merge(df,df1, on='movie_id')

result= ttk.Variable(app)

frame = ttk.Frame(app)
frame.place(x=10,y=10)

box = ttk.Listbox(frame, height=10,width=50)
for title in movie['title'].unique():
    box.insert(ttk.END,title)  
box.pack(side='left',fill = 'y')
#box.place(x=10,y=10)

scroll = ttk.Scrollbar(frame,orient=ttk.VERTICAL)
scroll.config(command=box.yview)
box.config(yscrollcommand=scroll.set)
scroll.pack(side='right',fill='y')

def get_movie():

ttk.Button(app ,text = 'Find Recommandations ', font=('Arial',22)).place(x=200,y=50)
ttk.Label(app, textvariable=result , font = ('Arial',22)).place(x=200,y=100)
## important
if movie_selected in top_recom:
    top_recom.remove(movie_selected)
    print('Recommandation:',top_recom)

if top_recom:
    result.set(top_recom[0])
else:
    result.set('sorry no recommandation found!!')    


app.mainloop()