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
from extras.colors import bcolors
import keyboard
import time
import os

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
	'w': 'Go Mining' , 
	'e': 'Sell Resources',
	'r': 'Inventory' ,
    'a': 'Stats',
	'q': 'Quit' ,
}

def print_game_logo():
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

def print_shop_logo():
    print(
        '                     :%@@@@@%                      \n',
        '                   .*@@%*==#@@%                    \n',
        '                   -@@#     :@@#                   \n',
        '               :%@@@@@@@@@@@@@@@@@@+               \n',
        '              #@@@@@@@@@@@@@@@@@@@@@@              \n',
        '             .@@@@@@@@@+   @@@@@@@@@@-             \n',
        '             .@@@@@@@:       #@@@@@@@=             \n',
        '             -@@@@@@=   =@*   #@@@@@@*             \n',
        '             +@@@@@@#.    :*@@@@@@@@@%             \n',
        '             *@@@@@@@@%-      @@@@@@@@             \n',
        '            .%@@@@@@+:-*@@#   :@@@@@@@:            \n',
        '            .@@@@@@@#.        *@@@@@@@=            \n',
        '            :@@@@@@@@@@+   -*@@@@@@@@@*            \n',
        '            =@@@@@@@@@@@%**%@@@@@@@@@@%            \n',
        '            +@@@@@@@@@@@@@@@@@@@@@@@@@%            \n',
        '             *@@@@@@@@@@@@@@@@@@@@@@@%=            \n',
        '                                                   \n',
        '                                                   \n',
        '           +@+-++ :@   *% .%%+*@  =@+=#@           \n',
        '           *@=    :@-..#% :@   #% =%  +@=          \n',
        '              :#% :@+-:#% :@   #% =@+==            \n',
        '           %+==%# :@   *%  ##=#@- =%               \n',
    )

def print_options():
    for key in option_menu.keys():
        print(key , '---' , option_menu[key])
    print("")

def goMining():
    game.gatherMaterials()

def sellResources(): # UNFINISHED!
    os.system('cls')

    print_shop_logo()
    # This block of code is for printing 0 blockname x quantity \n ... etc
    blocksIndexed = {}
    playersInventory = game.player.getInventory()
    index = 0
    for block in playersInventory:
        blocksIndexed[index] = block
        index += 1
    for key in blocksIndexed.keys():
        print(f'{key} --- {blocksIndexed[key]["name"]} x{blocksIndexed[key]["quantity"]}')

        # Check to detect if this is the last item in the array, if so print a newline
        if index-1 == key:
            print("")


    # VERIFY INPUTS!
    try:
        blockIndex = int(input(f"What do you want to sell? (0-{index-1}) "))
        if blockIndex > index-1:
            print(f'{bcolors.WARNING}OUT OF RANGE!{bcolors.ENDC}')
            time.sleep(1)
            sellResources()
            return

        quantityToSell = int(input(f'How much {blocksIndexed[blockIndex]["name"]} do you want to sell? '))
        if quantityToSell > blocksIndexed[blockIndex]["quantity"]:
            print(f"{bcolors.WARNING}You cant sell something you don't have...{bcolors.ENDC}")
            time.sleep(1)
            return
        
        blockWorth = game.shop.calculateWorth(blocksIndexed[blockIndex]["name"], quantityToSell)
        confirmSell = input(f'Are you sure you want to sell {blocksIndexed[blockIndex]["name"]} x{quantityToSell} for ${blockWorth}. (y/n) ')
    except KeyboardInterrupt:
        return
    except:
        if type(blocksIndexed) != int or type(blocksIndexed) != int:
            print(f'{bcolors.WARNING}INVALID CHOICE!{bcolors.ENDC}')
            time.sleep(1)
            sellResources()
            return


    
    if confirmSell == 'y' or confirmSell == 'yes':
        confirmSell = True
    else:
        confirmSell = False

    if confirmSell:
        game.shop.sellResource(blocksIndexed[blockIndex]["name"], quantityToSell)

    time.sleep(5)


if __name__ == '__main__':
    while(True):
        os.system('cls')
        print_game_logo()
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