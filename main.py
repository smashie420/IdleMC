#!/usr/bin/env python3

# PIP INSTALL REQUIREMENTS:
#   keyboard
'''
    Rio Hondo College
    CIT 128: Python Programming II
    Student Directed Project
'''
#from player import Player

#from items import Items
#items = Items()
#print(items.getWorth("Diamond"))
from game import IdleMC
import keyboard
import time
game = IdleMC() 


game.loadData() # This changes the class from a class 'player.Player' class to a class 'dict'
#game.gatherMaterials()
#print("\n\nINVENTORY: ")
#game.player.print_inventory()

#print(f"BEFORE SELL {game.player.getMineCoins()}")
#game.player.print_inventory()
#game.sellResource('Cobblestone')
#
#print(f"AFTER SELL {game.player.getMineCoins()}")
#game.player.print_inventory()


option_menu = {
	'm': 'Go Mining' , 
	's': 'Sell Resources',
	'i': 'Inventory' ,
	'q': 'Quit' ,
}


def print_logo():
        print(''
        '        #=====##=======+====  @=====*        *======+=====+@+====+     %=====* ==============*           \n',
        '       +----=@*--------=---+%%=----%        *------------=@+----=++  +*-=--==@*--=----------=%         \n',
        '      #-----*%+---+===------@+-----%       @*=-=--========@#=--====##+=-=----%%----=-========*         \n',
        '     @=----=@+-----%%%----=+@-----=@       @*-==--#%%%%%%%@#------=-----=----+%===---%%%%%%%%@         \n',
        '     *-----#%-----+@ #-----%@--=--*@       @+--==--==-----%#-------=----------@%-----*                 \n',
        '    %*+--==@*=----% @---==-@*-+---#@       @=---=---=+=--=%%==----------==----%%==----#                \n',
        '   @+--=--%%-----=@ %-----*@=-----%        @==+---++*+++++%%-----=%----=%-=---=@#-----*                \n',
        '   *----=+@+-----#%%+=----%@-----=%%@%%%%%%@+-===-%%%%%%%%%@-=----@%%%%%%-=----%%-=-+=-#%@%%%%%%@      \n',
        '  %=-----%#-----------=---@%------------=-%@=-----=-------+@=-----#     @*-----+@+-------=-------#     \n',
        '  +-----+@=----=--------++@=----------=---%@--=-----------=@*-----+     @%------@%-----=-=------==@    \n',
        ' %++++++%%+++++++++++++#@@@++++++++++++*++%@*++++++++++++++@#+++++*      %++++++%%++*+++++*++++*++#    \n',
        ' @@%%%%@ @@%%%%%%%@%@@@@   @%@@%%@@@@%%@@@ @@@@@%%@@@@%@%@@ @@@%%@@       @@%%%@@ @%@@%%%@@%@%@@@@@    \n'
        )

def print_options():
    for key in option_menu.keys():
        print(key , '---' , option_menu[key])
    print("")

def goMining():
    game.gatherMaterials()

def sellResources(): # UNFINISHED!
    sellAmount = input("What do you want to sell? ")
    print(sellAmount)
    time.sleep(5)


if __name__ == '__main__':
    while(True):
        print_logo()
        print_options()
        event = keyboard.read_event(suppress=True)
        if (event.event_type == keyboard.KEY_DOWN) and event.name == 'm':
            goMining()
        if (event.event_type == keyboard.KEY_DOWN) and event.name == 's':
            sellResources()
        if (event.event_type == keyboard.KEY_DOWN) and event.name == 'q':
            print("Quitting.")
            break





game.saveData()