import PySimpleGUI as sg
import sqlite3

conn = sqlite3.Connection('cica.db')
c    = conn.cursor()

sql  = 'CREATE TABLE if not exists tb (Név text,Telefonszám text,Életkor integer)'
c.execute(sql)
conn.commit()
sql  =  "INSERT INTO tb VALUES ('Klára','0620696969',23)"
sql2 =  "INSERT INTO tb VALUES (?,?,?)"
name = 'Rozi'
tel  = '06204368234'
kor  = '19'
#c.execute(sql2,(name,tel,kor ))
conn.commit()
sql  = "SELECT Telefonszám FROM tb WHERE Név like 'Rozi'  "
c.execute(sql)
res  =  c.fetchall()  




# Név tel kor
#Rozi 06204368234 19
#Juli 06202312312 23


sg.theme('LightGrey2')   # Add a touch of color
# All the stuff inside your window.
layout = [
            [sg.Text('Név'),         sg.InputText(key='Név')],
            [sg.Text('Telefonszám'), sg.InputText(key='Telefonszám')],
            [sg.Text('Életkor'),     sg.InputText(key='Életkor')],
            [sg.Button('Tárol'),     sg.Button('Kilép')] ,
            [sg.Button('Keres')] ,
            
         ]

# Create the Window
window = sg.Window('Csajok telefonszámai', layout)
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    print(event,values)
    if event in (None, 'Kilép'):   # if user closes window or clicks cancel
        break
    if event in ('Tárol',):
        print('You entered ', values['Név'])
        név = values['Név']
        tel = values['Telefonszám']
        kor = values['Életkor']
        sql =  "INSERT INTO tb values (?,?,?)"
        c.execute(sql,(név,tel,kor))
        conn.commit()
        c.execute('SELECT * FROM tb') 
        res  =  c.fetchall()
        print(res)
    if event in ('Keres',):
        név = values['Név']   
        c.execute("SELECT * FROM tb WHERE Név like ?",(név,))
        res  =  c.fetchall()
        telefon = res[0][1]
        életkor = res[0][2]
        window['Telefonszám'].update(telefon)
        window['Életkor'].update(életkor) 
        print('***',res)
window.close()