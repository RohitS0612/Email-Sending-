import smtplib as s

ob = s.SMTP('smtp.gmail.com', 587) # gmail  port number 587 , SMTP function used to  connection method
ob.ehlo() 
ob.starttls()
ob.login('shetakerohit2@gmail.com', 'zikswpkcpyplfyca') #login requires aunnthentication , use sending email account
subject  = input("Enter The Subject Here :  ")  
body = input("Enter Message Here :  ")
msg = "subject:{}\n\n{}".format(subject, body) 
listAdd = ['shetakeyash@gmail.com']                     # adding reciver emails we can ad multiple email in list
ob.sendmail('shetakerohit2@gmail.com', listAdd, msg)   
print(" Mail Send Successfully!")
ob.quit()
