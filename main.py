from stt_engine import get_audio
from tts_engine import speak
import utils
import smtp_hanlder
import os
import mailing_content_verifier

#the login creds
username=utils.LOGIN_CREDS[0]
pwd=utils.LOGIN_CREDS[1]

#starting the infinite loop to get the input
while True:
    
    speak("listening")
    print ("listening....")
    text = get_audio()

    for phrases in utils.COMPOSE_MAIL:
        if phrases in text:

            #getting the recievers 
            speak("please say the mail ID : ")
            reciever_id = get_audio()
            #replacing the at sign mistakes by @
            reciever_id = reciever_id.replace(" at ","@")
            reciever_id = reciever_id.replace(" ","")
            print(reciever_id)
            

            #verifying the mail ID
            verified_mail_id = mailing_content_verifier.verify_mail(reciever_id)
           
            #getting the subject
            speak("please  Say the Subject !")
            sub = get_audio()
            #verfying the subject
            subject = mailing_content_verifier.verify_subject(sub)

            #getting the message
            speak("please decribe your message now !")
            msg = get_audio()
            #verifying the message
            message = mailing_content_verifier.verify_message(msg)

            #pinging for the attachments
            speak("Do you want to add attachments ? ,Please say yes or no ?")
            is_attachments = get_audio()

            if is_attachments == "yes":   
                is_attachments = True
            else:
                is_attachments = False

            if is_attachments:
                speak("Please Enter the file path !")
                file_path = input("File path : ")
             
                file_path = mailing_content_verifier.verify_path(file_path)
                try:
                    smtp_hanlder.send_mail_with_attach(verified_mail_id,subject,message,file_path,username,pwd)
                except:
                    speak("please check the reciever's mail id")

                break
                #send_mail_with_attach("suryaramachandran@outlook.com","testing","hey hello","F:\BE_PEOJECT_CODES\Voice-based-email-clients-for-blind\\notes.txt","crypto2709@gmail.com","9940940832")
            else:
                try:
                    smtp_hanlder.send_mail(verified_mail_id,subject,message,username,pwd)
                except:
                    speak("please check the reciever's mail id")
                break
    exe=1
    for phrases in utils.INBOX_QUERY:
        if not exe==1:
            if phrases in text:

                speak("Getting the unread messages")
                msg=smtp_hanlder.read(username,pwd)
                if not msg==None:
                    speak(f"""The message was from {msg[0][0][0]} in mail id {msg[0][0][1]}, 
                    and now reading the subject, The subject starts here {msg[1]} subject ends !
                    Reading the mail content, The mail content starts {msg[2]} 
                    mail content ends here""") 
                    print(f"""The message was from {msg[0][0][0]} in mail id {msg[0][0][1]}, 
                    and now reading the subject, The subject starts here {msg[1]} subject ends !
                    Reading the mail content, The mail content starts {msg[2]} 
                    mail content ends here""")           
                    break
                else:
                    speak("You dont have any messages !")
                    break

            exe+=1   
        else:
            pass
        
