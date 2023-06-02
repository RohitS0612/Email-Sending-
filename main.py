import smtplib as s

ob = s.SMTP('smtp.gmail.com', 587) # gmail  port number 587 , SMTP function used to  connection method
ob.ehlo() 
ob.starttls()
ob.login('email', 'type youe email password') #login requires aunthentication , use sending email account
subject  = input("Enter The Subject Here :  ")  
body = input("Enter Message Here :  ")
msg = "subject:{}\n\n{}".format(subject, body) 
                     # adding reciver emails we can ad multiple email in list
listAdd = []
n = int(input("Enter the number of emails you sending :- "))
for i in range(0, n):
    ele = input(f" [{i}] =>  ")
    listAdd.append(ele)
ob.sendmail('enter login email', listAdd, msg)   
print("\n Sending.....")
print("\nMail Send Successfully!")
ob.quit()
