import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import mailparser
import imaplib

def get_filename(filepath):
    string=filepath.split("\\")
    return string[len(string)-1]




def send_mail_with_attach(receiver_address,subject,mail_content,attachment_file,username,pwd):
    
    fromaddr = username
    toaddr = receiver_address
    
    # instance of MIMEMultipart 
    msg = MIMEMultipart() 
    
    # storing the senders email address   
    msg['From'] = fromaddr 
    
    # storing the receivers email address  
    msg['To'] = toaddr 
    
    # storing the subject  
    msg['Subject'] = subject
    
    # string to store the body of the mail 
    body = mail_content
    
    # attach the body with the msg instance 
    msg.attach(MIMEText(body, 'plain')) 
    
    # open the file to be sent  
    filename = get_filename(attachment_file)
    attachment = open(attachment_file, "rb") 
    
    # instance of MIMEBase and named as p 
    p = MIMEBase('application', 'octet-stream') 
    
    # To change the payload into encoded form 
    p.set_payload((attachment).read()) 
    
    # encode into base64 
    encoders.encode_base64(p) 
    
    p.add_header('Content-Disposition', "attachment; filename= %s" % filename) 
    
    # attach the instance 'p' to instance 'msg' 
    msg.attach(p) 
    
    # creates SMTP session 
    s = smtplib.SMTP('smtp.gmail.com', 587) 
    
    # start TLS for security 
    s.starttls() 
    
    # Authentication 
    s.login(fromaddr, pwd) 
    
    # Converts the Multipart msg into a string 
    text = msg.as_string() 
    
    # sending the mail 
    s.sendmail(fromaddr, toaddr, text) 
    
    # terminating the session 
    s.quit() 
    print('Mail Sent')

def send_mail(receiver_address,subject,mail_content,username,pwd):
    sender_address = username
    sender_pass = pwd
   
    #Setup the MIME
    message = MIMEMultipart()
    message['From'] = sender_address
    message['To'] = receiver_address
    message['Subject'] = subject
    #The subject line
    #The body and the attachments for the mail
    message.attach(MIMEText(mail_content, 'plain'))
    #Create SMTP session for sending the mail
    session = smtplib.SMTP('smtp.gmail.com', 587) #use gmail with port
    session.starttls() #enable security
    session.login(sender_address, sender_pass) #login with mail_id and password
    text = message.as_string()
    session.sendmail(sender_address, receiver_address, text)
    session.quit()
    print('Mail Sent')
    
#send_mail("suryaramachandran@outlook.com","Just testing","hi hello its working buddy ! you did it !","crypto2709@gmail.com","9940940832")
#send_mail_with_attach("suryaramachandran@outlook.com","testing","hey hello","F:\BE_PEOJECT_CODES\Voice-based-email-clients-for-blind\\notes.txt","crypto2709@gmail.com","9940940832")



def read(username, password, sender_of_interest=None):
    # Login to INBOX
    imap = imaplib.IMAP4_SSL("imap.gmail.com", 993)
    imap.login(username, password)
    imap.select('INBOX')
    # Use search(), not status()
    # Print all unread messages from a certain sender of interest
    if sender_of_interest:
        status, response = imap.uid('search', None, 'UNSEEN', 'FROM {0}'.format(sender_of_interest))
    else:
        status, response = imap.uid('search', None, 'UNSEEN')
    if status == 'OK':
        unread_msg_nums = response[0].split()
    else:
        unread_msg_nums = []
    
    for e_id in unread_msg_nums:
    
        e_id = e_id.decode('utf-8')
        _, response = imap.uid('fetch', e_id, '(RFC822)')
        html = response[0][1].decode('utf-8')

        msg=mailparser.parse_from_string(html)

        a=msg.body
        a=a.split("-")
        
        return [msg.from_,msg.subject,a[0]]
