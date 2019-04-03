import tkinter as tk
import wallisproduct
import pentagonalnumbers

def createComputationMenu(master, topMenu, availableComputations):
    computationMenu = tk.Menu(master=topMenu, tearoff=0)
    computationMenu.add_command(label=availableComputations[0], command=lambda: changeComputation(master, topMenu, availableComputations[0], 0))
    computationMenu.add_command(label=availableComputations[1], command=lambda: changeComputation(master, topMenu, availableComputations[1], 1))

    return computationMenu

def changeComputation(master, topMenu, compName, n):
    topMenu.entryconfig(0, label=compName)
    try:
        oldFrame = master.winfo_children()[1]
        oldFrame.destroy()
    except IndexError:
        print('The old frame is already destroyed')
    if n == 0:
        currentFrame = wallisproduct.WallisProductFrame(master)
        currentFrame.drawFrame()
    elif n == 1:
        currentFrame = pentagonalnumbers.PentagonalNumbersFrame(master)
        currentFrame.drawFrame()
    
def main():
    master = tk.Tk()
    master.title('Computations')
    
    availableComputations = ['Wallis Product', 'Pentagonal Numbers', 'Quit']
    
    topMenu = tk.Menu(master=master, tearoff=0)
    computationMenu = createComputationMenu(master, topMenu, availableComputations)    
    topMenu.add_cascade(label=availableComputations[0], menu=computationMenu)
    master.config(menu=topMenu)
    
    currentFrame = wallisproduct.WallisProductFrame(master)
    currentFrame.drawFrame()

    master.mainloop()
    
if __name__ == '__main__':
    main()