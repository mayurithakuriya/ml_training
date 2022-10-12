import tkinter as ttk

app=ttk.Tk()
app.title('Recommandation System')
app.geometry('400x400')

result = ttk.Variable(app)
box = ttk.Listbox(app.height=10)
box.place(x=10,y=10)

def get_movie():
    pass
ttk.Button(
    app,text='Find Recoomamdation',font=