import smtplib 

s = smtplib.SMTP('smtp.gmail.com', 587) 

s.starttls() 

s.login("yashjain516@gmail.com", "") 

message = "Hello"

s.sendmail("yashjain516@gmail.com", "bpl.trainer15@gmail.com", message) 

s.quit() 
