"""
The custom tkinter user window
"""

# Imports
from tkinter import *
import customtkinter

# Initial system settings
customtkinter.set_appearance_mode('dark')
customtkinter.set_default_color_theme('blue')

# Create the root
root = customtkinter.CTk()
root.title('Dagboek')
root._state_before_windows_set_titlebar_color = 'zoomed'

# Main window grid settings
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=0)
root.grid_columnconfigure(1, weight=1)

# Entry Frame
entryFrame = customtkinter.CTkFrame(root, width=500)
entryFrame.grid_propagate(0)
entryFrame.grid(row=0, column=0, sticky='nsw')
entryFrame.grid_rowconfigure(0, weight=0)
entryFrame.grid_rowconfigure(1, weight=0)
entryFrame.grid_rowconfigure(2, weight=1)
entryFrame.grid_columnconfigure(0, weight=1)

# Title
entryTitleFrame = customtkinter.CTkFrame(entryFrame, height=80, fg_color='grey')
entryTitleFrame.grid_propagate(0)
entryTitleFrame.grid(row=0, column=0, sticky='we')
entryTitleFrame.grid_columnconfigure(0, weight=1)
entryTitleFont = ("Times",30,'bold')
entryTitle = customtkinter.CTkLabel(entryTitleFrame, text='NOTITIES', font=entryTitleFont)
entryTitle.grid(row=0, column=0, pady=25, sticky='we')

# Filter options
filterFrame = customtkinter.CTkFrame(entryFrame, height=200, fg_color='red')
filterFrame.grid(row=1, column=0, sticky='we')
filterFrame.grid_propagate(0)

# Page overview
overviewFrame = customtkinter.CTkFrame(entryFrame, fg_color='blue')
overviewFrame.grid(row=2, column=0, sticky='nswe')
overviewFrame.grid_propagate(0)

# Page Frame
pageFrame = customtkinter.CTkFrame(root, fg_color='pink')
pageFrame.grid(row=0, column=1, sticky='nswe')