#appJar UI Library Import
from appJar import gui

#SButton event
def press(button):
    if button == "Cancel":
        PocketHelpDeskUI.stop()
    else:
        company = PocketHelpDeskUI.getEntry("Company")
        user = PocketHelpDeskUI.getEntry("User")
        print(user, "With", company)

#Popup that confirms a button working
def buttontest(buttonmsg):
    PocketHelpDeskUI.infoBox("Button testing", "This buttton for "+ buttonmsg + " is working" )

#Sending the text template to the notes section
def firstNoteTemplate(x):
    textVariable = "Here Goes my text to be sent to the notes when the button is clicked"  
    PocketHelpDeskUI.setTextArea("Notes",textVariable)  
    buttontest("Button")

#Sending the text on the checked boxes
def checkBoxTemplate(ctt):
    checkedtext = "This is the text that goes on the notes after Checking the Box."
    PocketHelpDeskUI.setTextArea("Notes", checkedtext)
    buttontest("Checked")

def get(btn):
    tickdict = PocketHelpDeskUI.getOptionBox("Options")
    print('I was called')
    print(tickdict)
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
PocketHelpDeskUI.setSize(300, 550)
PocketHelpDeskUI.setBg("Blue")
PocketHelpDeskUI.setFont(18)

#Widgets
#Company name Entry
PocketHelpDeskUI.addLabelEntry("Company")
#User Entry
PocketHelpDeskUI.addLabelEntry("User")
#Ticket Entry
PocketHelpDeskUI.addLabelEntry("Ticket Number")

#Notes Widget
PocketHelpDeskUI.addLabel('Notes')
PocketHelpDeskUI.addScrolledTextArea("Notes", text = None)

#Email Templete Widget
PocketHelpDeskUI.addButton("Emails",buttontest)
#PocketHelpDeskUI.setButtonTooltip("Emails", "Pick the email you want to send")
#PocketHelpDeskUI.enableButtonTooltip("Emails")

#Button Templates for ticket notes
PocketHelpDeskUI.addButton("Note Template",firstNoteTemplate)

#CheckBoxes for Templates
PocketHelpDeskUI.addCheckBox("Text Template 2 ")


#Tick Options
PocketHelpDeskUI.addLabelOptionBox("Options", ["template1","template2","template3"])
PocketHelpDeskUI.addButton("Get", get)

#PocketHelpDeskUI.addButton("Get", buttontest)

#Link button to function press
PocketHelpDeskUI.addButtons(["Submit", "Cancel"], press)
PocketHelpDeskUI.setFocus("Company")
PocketHelpDeskUI.go()



