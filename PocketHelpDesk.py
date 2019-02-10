#appJar UI Library Import
from appJar import gui

def get_user_name():
    user_name = PocketHelpDeskUI.getEntry("User")
    return user_name

#Popup that confirms a button working
def buttontest(buttonmsg):
    PocketHelpDeskUI.infoBox("Button testing", "This buttton for "+ buttonmsg + " is working" )
    

#Sending the text template to the notes section
def new_call_default():
    new_call_text = "{} called in because  .".format(usr)
    PocketHelpDeskUI.setTextArea("Notes",new_call_text)  
 #   buttontest("Button")

def called_no_answer(get_user_name):
    no_answer_text = 'Called {} at ###. No Answer, left a voice mail, sending mail.'.format(get_user_name)
    button = PocketHelpDeskUI.setTextArea("Notes", no_answer_text)
    return button

#SButton event
def press(button):
    if button == "Cancel":
        PocketHelpDeskUI.stop()
    else:
        pressed_button = button
        button = PocketHelpDeskUI.setTextArea("Notes", button)
        return button

#Sending the text on the checked boxes
#def checkBoxTemplate(cbt):
#    checkedtext = "This is the text that goes on the notes after Checking the Box."
#    PocketHelpDeskUI.setTextArea("Notes", checkedtext)
#    buttontest("Checked")

#def get(btn):
#    tickdict = PocketHelpDeskUI.getOptionBox("Task")
#      checkBoxTemplate("cbt")
    
    #if tickdict['template1']:
    #     firstNoteTemplate("x")
    #elif tickdict["template2"]:
    #    buttontest("tick options")
    #else:
    #    return


#def noteTemplate():
 #   PocketHelpDeskUI.setTextArea("Text Template", firstNoteTemplate)

#Pocket HelpDesk UI
PocketHelpDeskUI = gui("Pocket HelpDesk")
#PocketHelpDeskUI.startTabbedFrame("Tabs")
#PocketHelpDeskUI.startTab(tab_naming())
#PocketHelpDeskUI.addLabel("L1","Tab 1")
PocketHelpDeskUI.setSize(400, 650)
PocketHelpDeskUI.setBg("Blue")
PocketHelpDeskUI.setFont(18)


#Widgets
#Ticket Entry
PocketHelpDeskUI.addLabelEntry("Ticket Number")

#Company name Entry
PocketHelpDeskUI.addLabelEntry("Company")

#User Entry
PocketHelpDeskUI.addLabelEntry("User")


#Email Templete Widget
#PocketHelpDeskUI.addButton("Emails",buttontest)
#PocketHelpDeskUI.setButtonTooltip("Emails", "Pick the email you want to send")
#PocketHelpDeskUI.enableButtonTooltip("Emails")

#Button Templates for ticket notes
PocketHelpDeskUI.addButton("New Call", press)
PocketHelpDeskUI.addButton("No Answer", called_no_answer)

#CheckBoxes for Templates
#PocketHelpDeskUI.addCheckBox("Text Template 2 ")


#Tick Options
#PocketHelpDeskUI.addLabelOptionBox("Task", ["template1","template2","template3"])
#PocketHelpDeskUI.addButton("Get", get)

#PocketHelpDeskUI.addButton("Get", buttontest)
#Notes Widget
PocketHelpDeskUI.addLabel("Notes")
PocketHelpDeskUI.addScrolledTextArea("Notes", text = None)

#Link button to function press
PocketHelpDeskUI.addButtons(["clear", "Cancel"], press)
#PocketHelpDeskUI.setFocus("Company")
PocketHelpDeskUI.go()



