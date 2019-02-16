#appJar UI Library Import
from appJar import gui
#Template function are here
#Get The user name entered
def get_user_name():
    user_name = PocketHelpDeskUI.getEntry("User")
    return user_name

#Get Company name entered
def get_company_name():
    company_name = PocketHelpDeskUI.getEntry("Company")
    return company_name

def get_ticket_number():
    ticket_number = PocketHelpDeskUI.getEntry("Ticket Number")
    return ticket_number

#Popup that confirms a button working
def buttontest(buttonmsg):
    PocketHelpDeskUI.infoBox("Button testing", "This buttton for "+ buttonmsg + " is working" )
    
#Sending the text template to the notes section
def new_call_default():
    new_call_text = ("{} called in because needs assistance with \n\n PC Name: PC_NAME\n\n How did you verify? \n Any other users affected? \n When is the last time it worked?\n \n Additional Troubleshooting:".format(get_user_name()))
    button = PocketHelpDeskUI.setTextArea("Notes",new_call_text)
    return button

def called_no_answer():
    no_answer_text = 'Called {} at ###. No Answer, left a voice mail, sending mail.'.format(get_user_name())
    button = PocketHelpDeskUI.setTextArea("Notes", no_answer_text)
    return button

def pwd_reset(pwd_chosen):
    if pwd_chosen == "psswd AD":
        pwd_text_ad = "getting his domain password Reset. Logged in to the DC - \n \n Located the user, reset the password \n \n Was the user able to login? \n"
        button = PocketHelpDeskUI.setTextArea("Notes", pwd_text_ad)
    else:
        pwd_text_365 = "\n getting the passowrd for office 365 reset.\n \n Logged in to O365 Admin console, resetting the password \n \n Are user able to change their own passwords? \n Did you set a password or entered a TEMP so the user can change it? \n Was the user able to Authenticate? \n \n Aditional Information:"
        button = PocketHelpDeskUI.setTextArea("Notes", pwd_text_365)
        return button
#Email template Section
def change_mgmnt_email(text, subject, recipient, auto = True):
    import win32com.client as win32
    outlook = win32.Dispatch('outlook.application')
    mail = outlook.CreateItem(0)
    mail.To = recipient
    mail.Subject = subject
    mail.HtmlBody = text
    if auto:
        mail.send
    else:
        mail.Display(False)

    
     

def save_to_text():
    notes_text = PocketHelpDeskUI.getTextArea("Notes")
    file = open("./tickets/{}.txt".format(get_ticket_number()),"w")
    file.write(notes_text)
    file.close()

#SButton event
def press(button):
    if button == "Clear":
        PocketHelpDeskUI.clearTextArea("Notes")
    else:
        PocketHelpDeskUI.stop()


#Pocket HelpDesk UI
PocketHelpDeskUI = gui("Pocket HelpDesk")
PocketHelpDeskUI.setSize(500, 650)
PocketHelpDeskUI.setBg("Grey")
PocketHelpDeskUI.setFont(12)
PocketHelpDeskUI.setButtonFont(size = 10, family = 'times', underline = True)
PocketHelpDeskUI.setOnTop(stay=True)

#Widgets
#Ticket Entry
PocketHelpDeskUI.addLabelEntry("Ticket Number",0, 0)

#Company name Entry
PocketHelpDeskUI.addLabelEntry("Company",1, 4)

#User Entry
PocketHelpDeskUI.addLabelEntry("User",2, 4)

#Email Templete Widget
PocketHelpDeskUI.addButton("Emails", change_mgmnt_email,3,0)

#Button Templates for ticket notes
PocketHelpDeskUI.addButton("New Call", new_call_default,3,4)


PocketHelpDeskUI.addButton("No Answer", called_no_answer)
PocketHelpDeskUI.addButtons(["psswd AD","psswd 365"], pwd_reset)
#Notes Widget
PocketHelpDeskUI.addLabel("Notes")
PocketHelpDeskUI.addScrolledTextArea("Notes", text = None, colspan=6)
#ocketHelpDeskUI.searchTextArea("Search",start=None, stop=None, nocase=True, backwards=False)
#Link button to function press
PocketHelpDeskUI.addButtons(["Clear", "Cancel"], press, colspan=6)
#PocketHelpDeskUI.setFocus("Company")
PocketHelpDeskUI.go()



