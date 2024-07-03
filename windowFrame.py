"""
The custom tkinter user window
"""

# Imports
from tkinter import *
import customtkinter
import copiedCodeCustomTkinter as ccCTk

# Initial system settings
customtkinter.set_appearance_mode('dark')
customtkinter.set_default_color_theme('blue')

# Create the root
root = customtkinter.CTk()
root.title('Dagboek')
root._state_before_windows_set_titlebar_color = 'zoomed'
root.minsize(1000,500)

# Main window grid settings
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=0)
root.grid_columnconfigure(1, weight=1)

#
# LEFT FRAME
#

# Entry Frame
entryFrame = customtkinter.CTkFrame(root, width=500)
entryFrame.grid_propagate(0)
entryFrame.grid(row=0, column=0, sticky='nsw')
entryFrame.grid_rowconfigure(0, weight=1)
entryFrame.grid_rowconfigure(1, weight=0)
entryFrame.grid_columnconfigure(0, weight=1)

# Title
entryTitleFrame = customtkinter.CTkFrame(entryFrame, fg_color='grey', bg_color='black', border_width=2)
entryTitleFrame.grid_propagate(0)
entryTitleFrame.grid(row=0, column=0, sticky='nswe')
entryTitleFrame.grid_columnconfigure(0, weight=1)
entryTitleFrame.grid_rowconfigure((0,1), weight=0)
entryTitleFrame.grid_rowconfigure(2, weight=1)
entryTitleFont = ("Times",30,'bold')
entryTitle = customtkinter.CTkLabel(entryTitleFrame, text='NOTITIES', font=entryTitleFont)
entryTitle.grid(row=0, column=0, padx=10, pady=25, sticky='we')

# Filter options
filterFrame = customtkinter.CTkFrame(entryTitleFrame, height=140)
filterFrame.grid(row=1, column=0, sticky='we', padx=10)
filterFrame.grid_propagate(0)
filterFont = ("Times",15, 'bold')
firstPady = (20,10)
yearLabel = customtkinter.CTkLabel(filterFrame, text='JAAR', font=filterFont)
yearLabel.grid(row=0, column=0, padx=20, pady=firstPady)
yearFilter = customtkinter.CTkOptionMenu(filterFrame)
yearFilter.grid(row=0, column=1, pady=firstPady)
monthLabel = customtkinter.CTkLabel(filterFrame, text='MAAND', font=filterFont)
monthLabel.grid(row=1, column=0, padx=20)
monthFilter = customtkinter.CTkOptionMenu(filterFrame)
monthFilter.grid(row=1, column=1)

filterButton = customtkinter.CTkButton(filterFrame, text='FILTER', font=filterFont)
filterButton.grid(row=2, column=1, padx=20, pady=10)

# Page overview
overviewFrame = customtkinter.CTkFrame(entryTitleFrame)
overviewFrame.grid(row=2, column=0, sticky='nswe', padx=10, pady=10)
overviewFrame.grid_propagate(0)
overviewFrame.grid_columnconfigure(0, weight=1)
overviewFrame.grid_rowconfigure(0, weight=0)
overviewFrame.grid_rowconfigure(1, weight=1)
filterFont = ("Times",20, 'bold')
pageLabel = customtkinter.CTkLabel(overviewFrame, text='BLADZIJDEN', font=filterFont)
pageLabel.grid(row=0, column=0, padx=5, pady=10, sticky='ew')
pageList = ccCTk.CTkListbox(overviewFrame)
pageList.grid(row=1, column=0, padx=10, pady=(0,10), sticky='nsew')


#
# RIGTH FRAME
#

# Page Frame
pageFrame = customtkinter.CTkFrame(root)
pageFrame.grid_propagate(0)
pageFrame.grid(row=0, column=1, sticky='nswe')
pageFrame.grid_columnconfigure(0, weight=1)
pageFrame.grid_rowconfigure(0, weight=0)
pageFrame.grid_rowconfigure(1, weight=1)

# Title Frame
pageTitleFrame = customtkinter.CTkFrame(pageFrame, height=80)
pageTitleFrame.grid_propagate(0)
pageTitleFrame.grid(row=0, column=0, padx=10, sticky='we')
pageTitleFrame.grid_columnconfigure(0, weight=1)
pageTitleFrame.grid_columnconfigure(1, weight=0)
pageTitleFrame.grid_rowconfigure(0, weight=0)
pageTitleFrame.grid_rowconfigure(1, weight=1)
pageTitleFont = ("Times",30,'bold')
pageFont = ("Times",20, 'bold')
# Text
entryTitle = customtkinter.CTkLabel(pageTitleFrame, text='DATUM', font=pageTitleFont, text_color='grey')
entryTitle.grid(row=0, column=0, pady=25, sticky='we')
# Button
filterButton = customtkinter.CTkButton(pageTitleFrame, text='NIEUW', font=pageFont, height=50)
filterButton.grid(row=0, column=1, padx=20)

# Visualize page Frame
showPageFrame = customtkinter.CTkFrame(pageFrame)
showPageFrame.grid(row=1, column=0, padx=10, pady=10, sticky='nswe')
showPageFrame.grid_columnconfigure(0, weight=1)
showPageFrame.grid_rowconfigure(0, weight=1)

pageTextBox = customtkinter.CTkTextbox(showPageFrame, fg_color='white', text_color='black', wrap='word', activate_scrollbars=True)
pageTextBox.grid(row=0, column=0, sticky='nswe')

# Save frame
saveFrame = customtkinter.CTkFrame(pageFrame, height=50)
saveFrame.grid(row=2, column=0, padx=10, pady=(0,5), sticky='we')
saveFrame.grid_columnconfigure(0, weight=1)
saveButton = customtkinter.CTkButton(saveFrame, text='OPSLAAN', font=pageFont, height=40)
saveButton.grid(row=0, column=0, sticky='we')