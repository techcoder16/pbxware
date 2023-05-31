import os
import time 
import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


file_data = []

current_directory = os.getcwd()

for filename in os.listdir(current_directory):
   
    if os.path.isfile(os.path.join(current_directory, filename)):

        file_size = os.path.getsize(filename)
      
        creation_date = os.path.getctime(filename)

        creation_date_formatted =  time.ctime(creation_date)
        file_data.append((filename, file_size, creation_date_formatted))


        print(f"File Name: {filename}")
        print(f"File Size: {file_size} bytes")
        print(f"Creation Date: {creation_date_formatted}")
        print()



file_data_string = ""
for file_info in file_data:
    file_data_string += f"File Name: {file_info[0]}\n"
    file_data_string += f"File Size: {file_info[1]} bytes\n"
    file_data_string += f"Creation Date: {file_info[2]}\n\n"


smtp_server = 'smtp.gmail.com'
smtp_port = 587
sender_email = 'fefurqan@gmail.com'
receiver_email = 'furqan9651@gmail.com'
password = 'leapord45'


message = MIMEMultipart()
message['From'] = sender_email
message['To'] = receiver_email
message['Subject'] = 'File Data in Current Directory'


message.attach(MIMEText(file_data_string, 'plain'))

with smtplib.SMTP(smtp_server, smtp_port) as server:
    server.starttls()
    server.login(sender_email, password)
    server.send_message(message)

print("Email sent successfully!")
