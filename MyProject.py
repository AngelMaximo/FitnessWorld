from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from datetime import date
import sqlite3
import os

class ConexionDB:
     def __init__(self):

          self.ruta = os.path.join(os.path.dirname(__file__),'MedidasSemanales.db')

     def conectar(self):
          return sqlite3.connect(self.ruta)

class ventanaPrincipal:
    def __init__(self,contenedor):

        self.insertar = Button(contenedor,text='Introduce measures',fg='black', bg='white',width=15, height=2,command=lambda:Insertar())
        self.consultar = Button(contenedor,text='Consul measures',fg='black', bg='white',width=15, height=2,command=lambda:Consultar())
        self.borrar = Button(contenedor,text='Delete mensures',fg='black',bg='white',width=15,height=2,command=lambda:Borrar())

        self.insertar.grid(column=0,row=0)
        self.consultar.grid(column=1,row=0)
        self.borrar.grid(column=2,row=0)

class Insertar:
     def __init__(self):
          windowsInsert=Toplevel()
          windowsInsert.geometry('400x300')
          windowsInsert.title('Fitness World')

          self.date=Label(windowsInsert,text='date',fg='black',bg='white').pack(side=TOP)
          self.date1=Label(windowsInsert,text=date.today().isoformat(),fg='black',bg='white',).pack(side=TOP)

          self.weight=Label(windowsInsert,text='weight',fg='black',bg='white').pack(side=TOP)
          self.weight1=Entry(windowsInsert,fg='black',bg='white')
          self.weight1.pack(side=TOP)

          self.waist=Label(windowsInsert,text='waist',fg='black',bg='white').pack(side=TOP)
          self.waist1=Entry(windowsInsert,fg='black',bg='white')
          self.waist1.pack(side=TOP)

          self.biceps=Label(windowsInsert,text='biceps',fg='black',bg='white').pack(side=TOP)
          self.biceps1=Entry(windowsInsert,fg='black',bg='white')
          self.biceps1.pack(side=TOP)

          self.leg=Label(windowsInsert,text='leg',fg='black',bg='white').pack(side=TOP)
          self.leg1=Entry(windowsInsert,fg='black',bg='white')
          self.leg1.pack(side=TOP)
            
          self.gluteus=Label(windowsInsert,text='gluteus',fg='black',bg='white').pack(side=TOP)
          self.gluteus1=Entry(windowsInsert,fg='black',bg='white')
          self.gluteus1.pack(side=TOP)

          self.send=Button(windowsInsert,text='send',fg='black',bg='cyan',command=self.insertData)
          self.send.pack(side=TOP)
          


     def insertData(self):

          date1 =date.today().isoformat()
          weight=self.weight1.get()
          waist=self.waist1.get()
          biceps=self.biceps1.get()
          leg=self.leg1.get()
          gluteus=self.gluteus1.get()
          print('date:',date1,'weight:',weight,'waist:',waist,'biceps:',biceps,'leg:',leg,'gluteus:',gluteus)
             
             
          if not all ([weight,waist,biceps,leg,gluteus]):
                  messagebox.showwarning('Fitness world','Empty fields: You must complete all fields.')
                  return #La función termina y no intenta hacer el insert
          
          try:
               weight=float(weight)
               waist=float(waist)
               biceps=float(biceps)
               leg=float(leg)
               gluteus=float(gluteus)  
          except ValueError:
               messagebox.showerror('Fitness World','Invalid data: The measurements must be numerical.')
               return
             
          conexion = ConexionDB()
          db1 = conexion.conectar()

          print('Insert function')
          consulta=db1.cursor()

          try:
               consulta.execute("INSERT INTO medidas (date, weight, waist, biceps, leg, gluteus) VALUES(?, ?, ?, ?, ?, ?)",
                                   (date1,weight,waist,biceps,leg,gluteus))
               db1.commit()

               messagebox.showinfo(title='Fitness world',message='Data sent successfully')

               #Borrar el contenido de los Entry
               self.weight1.delete(0,END)
               self.waist1.delete(0,END)
               self.biceps1.delete(0,END)
               self.leg1.delete(0,END)
               self.gluteus1.delete(0,END)

               print('Record inserted successfully.')

          except sqlite3.Error as e:
               messagebox.showerror("Fitness world",f"ERROR: It was not possible to save the record.\n\n{e}")

          finally:
               consulta.close()
               db1.close()

class Consultar:
     def __init__(self):
          windowsconsult=Toplevel()
          windowsconsult.geometry('1200x400')
          windowsconsult.title('Fitness World')

          

          self.week=Label(windowsconsult,text='Date',fg='black',bg='white')
          self.week.pack(side=TOP)

          #Combobox para seleccionar por fecha
          self.combo=ttk.Combobox(
               windowsconsult,
               state="readonly"
          )
          self.combo.pack(pady=20)

          #Boton consultar
          self.consult=Button(
               windowsconsult,
               text='Consult',
               fg='black',
               bg='cyan',
               command=self.consultData
          )
          self.consult.pack(side=TOP)

          #TABLA
          columnas = ('date','weight','waist','biceps','leg','gluteus')

          self.tabla=ttk.Treeview(#mostrar en forma de tabla
               windowsconsult,
               columns=columnas,
               show='headings'
          )

          self.tabla.heading('date',text='Date')
          self.tabla.heading('weight',text='Weight')
          self.tabla.heading('waist',text='Weist')
          self.tabla.heading('biceps',text='Biceps')
          self.tabla.heading('leg',text='Leg')
          self.tabla.heading('gluteus',text='Gluteus')

          self.tabla.pack(
               fill='both',
               expand=True,
               padx=10,
               pady=10
          )

          #Carga las fechas de la base de datos
          self.loadDates()

     def loadDates(self):
          conexion = ConexionDB()
          db3 = conexion.conectar()

          consulta=db3.cursor()
          try:
               consulta.execute("""SELECT DISTINCT date
                                   FROM medidas
                                   ORDER BY date""")
               fechas=consulta.fetchall()

               #COnvertimos las tuplas en una lista
               opciones=[]
               for fecha in fechas:
                    opciones.append(fecha[0])
               #Introducir las fechas en el combobox
               self.combo['values']=opciones
          except sqlite3.Error as e:
               messagebox.showerror('Fitness World', f'ERROR: It was not possible to load the dates. \n\n{e}')
          finally:
               consulta.close()
               db3.close()

     def consultData(self):
          fecha=self.combo.get()
          #comprobar que se hay seleccionado una fecha
          if not fecha:
               messagebox.showerror('Fitness World','Select a date')
               return
          
          conexion = ConexionDB()
          db2 = conexion.conectar()
          
          print('Consult function')
          db2.row_factory=sqlite3.Row
          consulta=db2.cursor()

          try:
               #Buscar el registro en la fecha seleccionada
               consulta.execute(""" SELECT date, weight, waist, biceps, leg, gluteus
               FROM medidas
               WHERE date=?""",(fecha,))

               registros=consulta.fetchall()#guarda todos los resultados 

               #Limpiar la tabla antes de mostrar los datos
               for registro in self.tabla.get_children():
                    self.tabla.delete(registro)

               #Insertar los registros a la tabla
               for registro in registros:
                    self.tabla.insert(
                         "",
                         "end",
                         values=(
                              registro['date'],
                              registro['weight'],
                              registro['waist'],
                              registro['biceps'],
                              registro['leg'],
                              registro['gluteus']
                         )
                    )
          except sqlite3.Error as e:
               messagebox.showerror("Fitness world", f"ERROR: It was not possible to consult the records.\n\n{e}")
          finally:
               consulta.close()
               db2.close()

class Borrar:
     def __init__(self):
          windowDelete=Toplevel()
          windowDelete.geometry('400x300')
          windowDelete.title('Fitness World')

          self.select=Label(windowDelete,text='Select records',fg='black',bg='white')
          self.select.pack(side=TOP)

          self.combo=ttk.Combobox(windowDelete,state='readonly')
          self.combo.pack(pady=20)
          self.delete=Button(windowDelete,text='Delete',fg='black',bg='cyan',command=self.deleteData)
          self.delete.pack(side=TOP)

          self.loadDates()

     def loadDates(self):
          conexion = ConexionDB()
          db4 = conexion.conectar()
          consulta=db4.cursor()

          try:
               consulta.execute("""SELECT DISTINCT date
                                   FROM medidas
                                   ORDER BY date""")
               fechas=consulta.fetchall()#guarda el resultado de la consulta

               opciones=[]
               for fecha in fechas:
                    opciones.append(fecha[0])
               #Introducir las fechas en el combobox
               self.combo['values']=opciones
          except sqlite3.Error as e:
               messagebox.showerror('Fitness World', f'ERROR: It was not possible to load the dates. \n\n{e}')
          finally:
               consulta.close()
               db4.close()

     def deleteData(self):

          fecha=self.combo.get()

          if not fecha:
               messagebox.showerror('Fitness World','Select a date')
               return
          
          mensaje=f"Are you sure you want to delete the record? {fecha} ?"
          respuesta=messagebox.askyesno('Fitness Word',message=mensaje)

          if respuesta:

               conexion = ConexionDB()
               db5 = conexion.conectar()
               consulta=db5.cursor()          
               print('Delete function')
          

               try:
                    consulta.execute("""DELETE FROM medidas
                                        WHERE date=?""",(fecha,))#DeELETE elimina la tabla completa
               
                    db5.commit()#Guarda los cambios permanentemente realizados en la base

                    messagebox.showinfo('Fitness World','Record deleted seccessfully')

                    self.loadDates()#RECARGAMOS LAS FECHAS

               except sqlite3.Error as e:
                    messagebox.showerror("Fitness world", f"ERROR: It was not possible to delete the records.\n\n{e}")
               finally:
                    consulta.close()
                    db5.close()
          else:
               messagebox.showinfo('Fitness World','Operation cancelled')

          
     
ventana=Tk()
miInterfaz=ventanaPrincipal(ventana)
ventana.title('Mundo Fit')
ventana.geometry('400x300')
ventana.columnconfigure(0,weight=1)
ventana.columnconfigure(1,weight=1)
ventana.columnconfigure(2,weight=1)
ventana.rowconfigure(0,weight=1)

ventana.mainloop()
