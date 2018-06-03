from tkinter import*
import tkinter.messagebox as tkMessageBox
import random
import time;
import datetime

root=Tk()
root.title("Locadora Sangiorgio :")
root.geometry("1350x630+0+0")
root.configure(bg='green')

LeftmainFrame=Frame(root,width=1000,height=650,bg='black',bd=8,relief="raise")
LeftmainFrame.pack(side=LEFT)

RightmainFrame=Frame(root,width=350,height=650,bd=8,relief="raise",bg='black')
RightmainFrame.pack(side=RIGHT)


#=======================FRAME DO TITLE=====================================================================
LeftmainFrame0=Frame(LeftmainFrame,width=350,height=50,bd=8,relief="raise",bg='black')
LeftmainFrame0.pack(side=TOP)

lblTitle=Label(LeftmainFrame0,font=('arial',74,'bold'),text='Locadora Sangiorgio',bd=8,bg='lightsalmon')
lblTitle.grid(row=0,column=0,sticky=W)
#===========================================================================================================
LeftmainFrame1=Frame(LeftmainFrame,width=1000,height=225,bd=8,relief="raise",bg='sandybrown')
LeftmainFrame1.pack(side=TOP)
LeftmainFrame2=Frame(LeftmainFrame,width=1000,height=225,bd=8,bg='moccasin',relief="raise")
LeftmainFrame2.pack(side=TOP)
LeftmainFrame3=Frame(LeftmainFrame,width=1000,height=100,bd=8,relief="raise",bg='lightskyblue')
LeftmainFrame3.pack(side=TOP)
LeftmainFrame4=Frame(LeftmainFrame,width=1000,height=100,bd=8,relief="raise")
LeftmainFrame4.pack(side=TOP)


RightmainFrame1=Frame(RightmainFrame,width=350,height=325,bd=8,relief="raise",bg='lightskyblue')
RightmainFrame1.pack(side=TOP)

RightmainFrame2=Frame(RightmainFrame,width=380,height=325,bd=9,relief="raise")
RightmainFrame2.pack(side=BOTTOM)

#========================CALCULOS============================================================================
def CarRentalCost():
 NoofDays = float(NumberofDays.get())
 CarDiscount = float(Discount.get())
 DailyRate = float(DaysRented.get())

 RentalCost = ((NoofDays * DailyRate)* CarDiscount)/100
 CostofRental = "£", str('%.2f'%((NoofDays * DailyRate)- RentalCost))
 Total.set(CostofRental)


 ID = random.randint(51, 95)
 randomID = str (ID)
 CustomerID.set("Car"+ randomID)


 Inv = random.randint(15, 112)
 InvID = str(Inv)
 InvoiceID.set("INV"+ InvID)



#=====================================VARIAVEIS==============================================================
Var1 = IntVar()
Var2 = IntVar()
Var3 = IntVar()
Var4 = IntVar()
Var5 = IntVar()
Var6 = IntVar()
Var7 = IntVar()
Var8 = IntVar()
CustomerID = StringVar()
DaysRented = StringVar()
Discount = StringVar()
NumberofDays = StringVar()
InvoiceID = StringVar()
Total = StringVar()
Receipt_Ref = StringVar()
DateofOrder = StringVar()
EngineSize = StringVar()
Style = StringVar()
RegisteredYear = StringVar()
ClassID = StringVar()
CarDescription = StringVar()
MilesBefore = StringVar()
MilesAfter = StringVar()
Make = StringVar()
Model = StringVar()
CarColor = StringVar()
EngineMake = StringVar()
CarInsurance = StringVar()
Area = StringVar()
DailyRentalRate = StringVar()
RegistrationNo = StringVar()
IssueBy = StringVar()
IssueDate = StringVar()
LicenceN = StringVar()
Surname = StringVar()
Street = StringVar()
Firstname = StringVar()
Title = StringVar()
Customer = StringVar()
PostCode = StringVar()
#==================================BOTAO SAIR================================================================
def Exit():
    result = tkMessageBox.askquestion("LOCADORA SANGIORGIO :")
    if result == 'yes' :
        root.destroy()
        return

#============================================================================================================
def Reset():
    Var1.set(0)
    Var2.set(0)
    Var3.set(0)
    Var4.set(0)
    Var5.set(0)
    Var6.set(0)
    Var7.set(0)
    Var8.set(0)
    CustomerID.set("")
    DaysRented.set("")
    NumberofDays.set("")
    InvoiceID.set("")
    Total.set("")
    Receipt_Ref.set("")
    Discount.set("")
    DateofOrder.set("")
    EngineSize.set("")
    Style.set("")
    RegisteredYear.set("")
    ClassID.set("")
    CarDescription.set("")
    MilesBefore.set("")
    MilesAfter.set("")
    Make.set("")
    Model.set("")
    CarColor.set("")
    EngineMake.set("")
    CarInsurance.set("")
    Area.set("")
    DailyRentalRate.set("")
    RegistrationNo.set("")
    IssueBy.set("")
    IssueDate.set("")
    LicenceN.set("")
    Surname.set("")
    Street.set("")
    Firstname.set("")
    Title.set("")
    Customer.set("")
    PostCode.set("")
    txtReceipt.delete("1.0",END)
#========================================================Imprimir===================================
def retrive_imput():
    imputValue = txtReceipt.get("1.0","end-1c")
    print(imputValue)
#========================================================RECIBO======================================
def Receipt():
 txtReceipt.delete("1.0",END)
 x = random.randint(108, 506)
 randomRef = str(x)
 Receipt_Ref.set("BILL"+ randomRef)

 txtReceipt.insert(END,'RCIBO Ref:\t'+ Receipt_Ref.get()+'\n\nData:\t'+ DateofOrder.get()+"\n\n")
 txtReceipt.insert(END, "Servicos: \n\n")

 txtReceipt.insert(END, 'ClienteID: \t'+ CustomerID.get()+ "\n\n")

 txtReceipt.insert(END, 'Valor Diaria: \t\t'+ DaysRented.get()+ "\n\n")


 txtReceipt.insert(END, 'Qtos Dias: \t\t'+ NumberofDays.get()+ "\n\n")

 txtReceipt.insert(END, 'ReciboID: \t\t'+ InvoiceID.get()+ "\n\n")

 txtReceipt.insert(END, 'Disconto: \t\t'+ Discount.get()+ "\n\n")

 txtReceipt.insert(END, 'Total: \t'+ Total.get()+ "\n\n")

#=====================================CAMPO DO RECIBO================================================
txtReceipt=Text(RightmainFrame2,height=17,width=30,bd=8,bg='lemonchiffon',font=('arial',12,'bold'))
txtReceipt.grid(row=0,column=0)

DateofOrder.set(time.strftime("%d/%m/%y"))
#=====================================botoes=========================================================

#=================================FRAME primeiro numero 1 ===========================================

lblCustomer=Label(LeftmainFrame1,font=('arial',11,'bold'),text='Cliente   :',bd=8,bg='sandybrown')
lblCustomer.grid(row=0,column=0,sticky=W)
txtCustomer=Entry(LeftmainFrame1,font=('arial',10,'bold'),bd=2,textvariable=Customer,
                   width=31,justify='left')
txtCustomer.grid(row=0,column=1)


lblTitle=Label(LeftmainFrame1,font=('arial',11,'bold'),text='Apelido   :',bd=8,bg='sandybrown')
lblTitle.grid(row=0,column=2,sticky=W)
txtTitle=Entry(LeftmainFrame1,font=('arial',10,'bold'),bd=2,textvariable=Title,
                   width=31,justify='left')
txtTitle.grid(row=0,column=3)


lblFirstname=Label(LeftmainFrame1,font=('arial',11,'bold'),text='Nome   :',bd=8,bg='sandybrown')
lblFirstname.grid(row=0,column=4,sticky=W)
txtFirstname=Entry(LeftmainFrame1,font=('arial',10,'bold'),bd=2,textvariable=Firstname,
                   width=31,justify='left')
txtFirstname.grid(row=0,column=5)


lblSurname=Label(LeftmainFrame1,font=('arial',11,'bold'),text='S-Nome   :',bd=8,bg='sandybrown')
lblSurname.grid(row=1,column=0,sticky=W)
txtSurname=Entry(LeftmainFrame1,font=('arial',10,'bold'),bd=2,textvariable=Surname,
                   width=31,justify='left')
txtSurname.grid(row=1,column=1)


lblStreet=Label(LeftmainFrame1,font=('arial',11,'bold'),text='Rua   :',bd=8,bg='sandybrown')
lblStreet.grid(row=1,column=2,sticky=W)
txtStreet=Entry(LeftmainFrame1,font=('arial',10,'bold'),bd=2,textvariable=Street,
                   width=31,justify='left')
txtStreet.grid(row=1,column=3)


lblArea=Label(LeftmainFrame1,font=('arial',11,'bold'),text='Area   :',bd=8,bg='sandybrown')
lblArea.grid(row=1,column=4,sticky=W)
txtArea=Entry(LeftmainFrame1,font=('arial',10,'bold'),bd=2,textvariable=Area,
                   width=31,justify='left')
txtArea.grid(row=1,column=5)



lblPostCode=Label(LeftmainFrame1,font=('arial',11,'bold'),text='Cod Postal  :',bd=8,bg='sandybrown')
lblPostCode.grid(row=2,column=0,sticky=W)
txtPostCode=Entry(LeftmainFrame1,font=('arial',10,'bold'),bd=2,textvariable=PostCode,
                   width=31,justify='left')
txtPostCode.grid(row=2,column=1)


lblLicenceNo=Label(LeftmainFrame1,font=('arial',11,'bold'),text='N-CNH   :',bd=8,bg='sandybrown')
lblLicenceNo.grid(row=2,column=2,sticky=W)
txtLicenceNo=Entry(LeftmainFrame1,font=('arial',10,'bold'),bd=2,textvariable=LicenceN,
                   width=31,justify='left')
txtLicenceNo.grid(row=2,column=3)


lblIssueDate=Label(LeftmainFrame1,font=('arial',11,'bold'),text='Data  :',bd=8,bg='sandybrown')
lblIssueDate.grid(row=2,column=4,sticky=W)
txtIssueDate=Entry(LeftmainFrame1,font=('arial',10,'bold'),bd=2,textvariable=IssueDate,
                   width=31,justify='left')
txtIssueDate.grid(row=2,column=5)



lblIssueBy=Label(LeftmainFrame1,font=('arial',11,'bold'),text='Local   :',bd=8,bg='sandybrown')
lblIssueBy.grid(row=3,column=0,sticky=W)
txtIssueBy=Entry(LeftmainFrame1,font=('arial',10,'bold'),bd=2,textvariable=IssueBy,
                   width=31,justify='left')
txtIssueBy.grid(row=3,column=1)


lblRegistrationNo=Label(LeftmainFrame1,font=('arial',11,'bold'),text='N-Doc-Carro   :',bd=8,bg='sandybrown')
lblRegistrationNo.grid(row=3,column=2,sticky=W)
txtRegistrationNo=Entry(LeftmainFrame1,font=('arial',10,'bold'),bd=2,textvariable=RegistrationNo,
                   width=31,justify='left')
txtRegistrationNo.grid(row=3,column=3)


lblRentalRate=Label(LeftmainFrame1,font=('arial',11,'bold'),text='Total Dias   :',bd=8,bg='sandybrown')
lblRentalRate.grid(row=3,column=4,sticky=W)
txtRentalRate=Entry(LeftmainFrame1,font=('arial',10,'bold'),bd=2,textvariable=DailyRentalRate,
                   width=31,justify='left')
txtRentalRate.grid(row=3,column=5)
#=================================FRAME SEGUNDO ========================================================

lblEngineSize=Label(LeftmainFrame2,font=('arial',11,'bold'),text='Tipo Motor:',bd=8,bg='moccasin')
lblEngineSize.grid(row=0,column=0,sticky=W)
txtEngineSize=Entry(LeftmainFrame2,font=('arial',10,'bold'),bd=2,textvariable=EngineSize,
                   width=31,justify='left')
txtEngineSize.grid(row=0,column=1)


lblStyle=Label(LeftmainFrame2,font=('arial',11,'bold'),text='Estilo:',bd=8,bg='moccasin')
lblStyle.grid(row=0,column=2,sticky=W)
txtStyle=Entry(LeftmainFrame2,font=('arial',10,'bold'),bd=2,textvariable=Style,
                   width=31,justify='left')
txtStyle.grid(row=0,column=3)


lblRegisteredYear=Label(LeftmainFrame2,font=('arial',11,'bold'),text='Carro-Ano:',bd=8,bg='moccasin')
lblRegisteredYear.grid(row=0,column=4,sticky=W)
txtRegisteredYear=Entry(LeftmainFrame2,font=('arial',10,'bold'),bd=2,textvariable=RegisteredYear,
                   width=31,justify='left')
txtRegisteredYear.grid(row=0,column=5)


lblClassID=Label(LeftmainFrame2,font=('arial',11,'bold'),text='Clase-Carro:',bd=8,bg='moccasin')
lblClassID.grid(row=1,column=0,sticky=W)
txtClassID=Entry(LeftmainFrame2,font=('arial',10,'bold'),bd=2,textvariable=ClassID,
                   width=31,justify='left')
txtClassID.grid(row=1,column=1)


lblCarDescription=Label(LeftmainFrame2,font=('arial',11,'bold'),text='Desc-Carro:',bd=8,bg='moccasin')
lblCarDescription.grid(row=1,column=2,sticky=W)
txtCarDescription=Entry(LeftmainFrame2,font=('arial',10,'bold'),bd=2,textvariable=CarDescription,
                   width=31,justify='left')
txtCarDescription.grid(row=1,column=3)


lblMilesBefore=Label(LeftmainFrame2,font=('arial',11,'bold'),text='Km-Anterior:',bd=8,bg='moccasin')
lblMilesBefore.grid(row=1,column=4,sticky=W)
txtMilesBefore=Entry(LeftmainFrame2,font=('arial',10,'bold'),bd=2,textvariable=MilesBefore,
                   width=31,justify='left')
txtMilesBefore.grid(row=1,column=5)



lblMilesAfter=Label(LeftmainFrame2,font=('arial',11,'bold'),text='Km-Entrega:',bd=8,bg='moccasin')
lblMilesAfter.grid(row=2,column=0,sticky=W)
txtMilesAfter=Entry(LeftmainFrame2,font=('arial',10,'bold'),bd=2,textvariable=MilesAfter,
                   width=31,justify='left')
txtMilesAfter.grid(row=2,column=1)


lblMake=Label(LeftmainFrame2,font=('arial',11,'bold'),text='Fab-Carro:',bd=8,bg='moccasin')
lblMake.grid(row=2,column=2,sticky=W)
txtMake=Entry(LeftmainFrame2,font=('arial',10,'bold'),bd=2,textvariable=Make,
                   width=31,justify='left')
txtMake.grid(row=2,column=3)


lblModel=Label(LeftmainFrame2,font=('arial',11,'bold'),text='Modelo:',bd=8,bg='moccasin')
lblModel.grid(row=2,column=4,sticky=W)
txtModel=Entry(LeftmainFrame2,font=('arial',10,'bold'),bd=2,textvariable=Model,
                   width=31,justify='left')
txtModel.grid(row=2,column=5)



lblEngineMake=Label(LeftmainFrame2,font=('arial',11,'bold'),text='Fab-Motor:',bd=8,bg='moccasin')
lblEngineMake.grid(row=3,column=0,sticky=W)
txtEngineMake=Entry(LeftmainFrame2,font=('arial',10,'bold'),bd=2,textvariable=EngineMake,
                   width=31,justify='left')
txtEngineMake.grid(row=3,column=1)


lblCarColor=Label(LeftmainFrame2,font=('arial',11,'bold'),text='Cor-Carro:',bd=8,bg='moccasin')
lblCarColor.grid(row=3,column=2,sticky=W)
txtCarColor=Entry(LeftmainFrame2,font=('arial',10,'bold'),bd=2,textvariable=CarColor,
                   width=31,justify='left')
txtCarColor.grid(row=3,column=3)


lblCarInsurance=Label(LeftmainFrame2,font=('arial',11,'bold'),text='Seguro-Carro:',bd=8,bg='moccasin')
lblCarInsurance.grid(row=3,column=4,sticky=W)
txtCarInsurance=Entry(LeftmainFrame2,font=('arial',10,'bold'),bd=2,textvariable=CarInsurance,
                   width=31,justify='left')
txtCarInsurance.grid(row=3,column=5)
#=================================FRAME TERCEIRO===========================================================

lblCustomerID=Label(LeftmainFrame3,font=('arial',11,'bold'),text='Cliente ID :',bd=8,bg='lightskyblue')
lblCustomerID.grid(row=0,column=0,sticky=W)
txtCustomerID=Entry(LeftmainFrame3,font=('arial',10,'bold'),bd=2,textvariable=CustomerID,
                   width=31,justify='left')
txtCustomerID.grid(row=0,column=1)


lblDaysRented=Label(LeftmainFrame3,font=('arial',11,'bold'),text='Total-D-Alugado :',bd=8,bg='lightskyblue')
lblDaysRented.grid(row=0,column=2,sticky=W)
txtDaysRented=Entry(LeftmainFrame3,font=('arial',10,'bold'),bd=2,textvariable=DaysRented,
                   width=31,justify='left')
txtDaysRented.grid(row=0,column=3)


lblDiscount=Label(LeftmainFrame3,font=('arial',11,'bold'),text='Disconto :',bd=8,bg='lightskyblue')
lblDiscount.grid(row=0,column=4,sticky=W)
txtDiscount=Entry(LeftmainFrame3,font=('arial',10,'bold'),bd=2,textvariable=Discount,
                   width=31,justify='left')
txtDiscount.grid(row=0,column=5)


lblNumberofDays=Label(LeftmainFrame3,font=('arial',11,'bold'),text='Total-Dias :',bd=8,bg='lightskyblue')
lblNumberofDays.grid(row=1,column=0,sticky=W)
txtNumberofDays=Entry(LeftmainFrame3,font=('arial',10,'bold'),bd=2,textvariable=NumberofDays,
                   width=31,justify='left')
txtNumberofDays.grid(row=1,column=1)


lblInvoiceID=Label(LeftmainFrame3,font=('arial',11,'bold'),text='ID-Fatura :',bd=8,bg='lightskyblue')
lblInvoiceID.grid(row=1,column=2,sticky=W)
txtInvoiceID=Entry(LeftmainFrame3,font=('arial',10,'bold'),bd=2,textvariable=InvoiceID,
                   width=31,justify='left')
txtInvoiceID.grid(row=1,column=3)


lblTotal=Label(LeftmainFrame3,font=('arial',11,'bold'),text='Total  :',bd=8,bg='lightskyblue')
lblTotal.grid(row=1,column=4,sticky=W)
txtTotal=Entry(LeftmainFrame3,font=('arial',10,'bold'),bd=2,textvariable=Total,
                   width=31,justify='left')
txtTotal.grid(row=1,column=5)


#=======================CAMPOS checkbutton=======================================================================================================================
style=Checkbutton(RightmainFrame1,text='Estilo\t\t\t',onvalue=1,offvalue=0,variable=Var1,bg='lightskyblue',font=('arial',12,'bold')).grid(row=0,sticky=W)
style=Checkbutton(RightmainFrame1,text='ClaseID\t\t\t',onvalue=1,offvalue=0,variable=Var2,bg='lightskyblue',font=('arial',12,'bold')).grid(row=1,sticky=W)
style=Checkbutton(RightmainFrame1,text='FaturaID\t\t\t',onvalue=1,offvalue=0,variable=Var3,bg='lightskyblue',font=('arial',12,'bold')).grid(row=2,sticky=W)
style=Checkbutton(RightmainFrame1,text='Diaria\t\t\t',onvalue=1,offvalue=0,variable=Var4,bg='lightskyblue',font=('arial',12,'bold')).grid(row=3,sticky=W)
style=Checkbutton(RightmainFrame1,text='Automatico\t\t',onvalue=1,offvalue=0,variable=Var5,bg='lightskyblue',font=('arial',12,'bold')).grid(row=4,sticky=W)
style=Checkbutton(RightmainFrame1,text='Ar Condicionado \t',onvalue=1,offvalue=0,variable=Var6,bg='lightskyblue',font=('arial',12,'bold')).grid(row=5,sticky=W)
style=Checkbutton(RightmainFrame1,text='Seguro\t\t',onvalue=1,offvalue=0,variable=Var7,bg='lightskyblue',font=('arial',12,'bold')).grid(row=6,sticky=W)
style=Checkbutton(RightmainFrame1,text='Detalhes Cliente\t\t',onvalue=1,offvalue=0,variable=Var8,bg='lightskyblue',font=('arial',12,'bold')).grid(row=7,sticky=W)
#================================================================================================================================================================
#===============================BOTOES=================================================================
btnTotal=Button(LeftmainFrame4,text='TOTAL',padx=6,bd=3,fg='yellow',bg='black',
                font=('arial',10,'bold'),width=22,height=2,command=CarRentalCost).grid(row=0,column=0)

btnReceipt=Button(LeftmainFrame4,text='Recibo',padx=6,bd=3,fg='yellow',bg='black',
                font=('arial',10,'bold'),width=22,height=2,command=Receipt).grid(row=0,column=2)

btnReset=Button(LeftmainFrame4,text='Limpar',padx=6,bd=3,fg='yellow',bg='black',
                font=('arial',10,'bold'),width=22,height=2,command=Reset).grid(row=0,column=3)

btnExit=Button(LeftmainFrame4,text='Sair',padx=6,bd=3,fg='yellow',bg='black',
                font=('arial',10,'bold'),width=22,height=2,command=Exit).grid(row=0,column=4)

btnImprimir=Button(LeftmainFrame4,text='Imprimir',padx=6,bd=3,fg='yellow',bg='black',
                font=('arial',10,'bold'),width=22,height=2,command=lambda:  retrive_imput()).grid(row=0,column=5)
#=====================================================================================================

root.mainloop()
