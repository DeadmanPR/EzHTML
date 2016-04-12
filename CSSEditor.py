from Tkinter import *
import webbrowser

class CSSEditor():
    
    elements = []
    def saveAndQuit(self):  
        quit()
        return
        
    def quitWithoutSaving(self):
        quit()
        return
    
    def edit(self, var):
        if var.get() is not 'Please select the element to edit':
            print var.get()
        return
    
    def __init__(self, elements):
        webbrowser.open('MyWebsite.html')
        self.elements = elements
        
        window = Tk()
        window.title("CSS Editor")
        
        var = StringVar(window)
        var.set('Please select the element to edit')
        drop = OptionMenu(window, var, *self.elements)
        drop.config(width=75)
        drop.pack()
        
        edit = Button(window, text='Edit', command=lambda: self.edit(var))
        edit.pack(side=TOP)
        saveandquit = Button(window, text='Save & Close', command=self.saveAndQuit)
        saveandquit.pack(side=LEFT, padx=100)
        
        closeWS = Button(window, text='Close without Saving', command=self.quitWithoutSaving)
        closeWS.pack(side=LEFT, padx=100)
        
        window.mainloop()
        
      
   
    
