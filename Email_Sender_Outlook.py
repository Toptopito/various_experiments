# -*- coding: utf-8 -*-

import win32com.client as client

mail_list_file_path = "C:/Users/vladc/OneDrive/Desktop/list of emails.txt"

fhandle = open(mail_list_file_path, 'r')

mail_list = fhandle.read().split(';')
mail_list = [mail.strip() for mail in mail_list]

chunk_size = 100

chunks = []
for i in range(0, len(mail_list), chunk_size):
    chunk = mail_list[i:i+chunk_size]
    chunks.append(chunk)

outlook = client.Dispatch('outlook.application')

for recipients in chunks:
    newmail = outlook.CreateItem(0)
    newmail.Subject = '(Follow Up) Request for Participation: Research Study on ChatGPT and Diagnosis of COVID-19'
    newmail.CC = 'falemi@gmu.edu'
    newmail.BCC = ';'.join(recipients)
    newmail.HTMLBody = """<i>Sent on behalf of Dr. Farrokh Alemi, PhD by research assistant, Vladimir “Vlad” Cardenas (<a href=mailto:vcarden@gmu.edu>vcarden@gmu.edu</a>).</i>
    <br><br>
    Dear Colleague,
    <br><br>
    I hope this email finds you well. I am a professor at George Mason University conducting research on ChatGPT and diagnosis of COVID-19. 
    <br><br>
    You may have already submitted a response to this survey. Since respondents do not provide their contact information, we do not know who has responded. If you have, we thank you and you can ignore this email. If you have not, please consider filling in this short 7-question survey.
    <br><br>
    To succeed, I need descriptions of symptoms you experienced when you suspected COVID-19 and did a COVID-19 home test. I would be interested in a description of your symptoms even if you did not do a home test. To validate our models, we need these descriptions in your style and with your words, so this survey has open-ended questions. These descriptions can be about you or someone you know well. It can be about an occasion from anytime in the past. 
    <br><br>
    The research is approved by IRB. I estimate that you can complete the survey in under four minutes. Your name and identity are not collected. I hope you will be willing to help. 
    <br><br>
    Here is a link to complete this short 7-question survey: <a href=https://forms.office.com/r/k3AhCxBDYv> https://forms.office.com/r/k3AhCxBDYv </a>
    <br><br>
    Again, remember not to put your name anywhere. Please feel free to Contact me at (703) 893-3799,  if I can answer any questions you have about this research. My email is <a href=mailto:falemi@gmu.edu> falemi@gmu.edu</a>. 
    <br><br>
    <br>
    Best regards,<br><br>
    Farrokh Alemi PhD<br>
    Professor<br>
    Health informatics<br>
    Health Administration and Policy  """
    newmail.Save()