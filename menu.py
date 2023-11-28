from extras.colors import bcolors
from items import Items

import os
import time
import keyboard
class menu:
    def __init__(self, game):
        self.game = game

        self.option_menu = {
            'w': 'Go Mining' , 
            'e': 'Sell Resources',
            't': 'Buy Upgrades/Tools',
            'r': 'Inventory' ,
            'a': 'Stats',
            'q': 'Quit' ,
        }
    def print_game_logo(self):
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

    def print_shop_logo(self):
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

    def print_inventory_logo(self):
        print(
            '                #########################%%               \n',
            '               #+=========++++==========*%               \n',
            '               #*++==+++++*****++++++++=*%               \n',
            '               #*++++++=++-  .+#*+++++++#%               \n',
            '               ##%%%%%%%%%= .-*%%%%%%%%%%@               \n',
            '               #*+++++++++=:-=**++++++++#%               \n',
            '               #*+++++++++=:-=++++++++++#%               \n',
            '               #*======+===+++++========#%               \n',
            '               #*=========++++=========+#%               \n',
            '               #*======================+#%               \n',
            '               #*========+=+++===+====++#%               \n',
            '               #*=====+++===========++++#%               \n',
            '               #*=======================#%               \n',
            '               #*+++++++++++++++++++++++#%               \n',
            '               *************************##               \n',
        )

    def print_stats_logo(self):
        print(
            "                  @@@@@@@@@@        \n"
            "                   @@@@@@@@         \n"
            "               @@@@@@@@@@           \n"
            "            @@@@@@   @@@   @@@@@@   \n"
            "           @@@@            @@@@@@   \n"
            "@@@@@@    @@@@             @@@@@@   \n"
            "   @@@@@@@@@@      @@@@@@  @@@@@@   \n"
            "       @@@@        @@@@@@@ @@@@@@   \n"
            "                   @@@@@@@ @@@@@@   \n"
            "   @@@@@@          @@@@@@@ @@@@@@   \n"
            "   @@@@@@          @@@@@@@ @@@@@@   \n"
            "   @@@@@@  @@@@@@  @@@@@@@ @@@@@@   \n"
            "   @@@@@@  @@@@@@  @@@@@@@ @@@@@@   \n"
            "   @@@@@@  @@@@@@  @@@@@@@ @@@@@@   \n"
            "   @@@@@@  @@@@@@  @@@@@@@ @@@@@@   \n"
            "   @@@@@@  @@@@@@  @@@@@@  @@@@@@   \n"
            "                                    \n"
            "@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n"
            "@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n"
        )

    def print_shop_logo(self):
        print(
            "                  ========                \n"
            "                ============              \n"
            "               ====      ====             \n"
            "              ====       ====             \n"
            "              ===         ===             \n"
            "              ===         ===             \n"
            "       ++++++ === ======= === ===--       \n"
            "      +++++++ === ======= === ====--      \n"
            "      ++++++++= =========== ======--      \n"
            "      ++++++++====================--      \n"
            "      ++++++++===    =============--      \n"
            "      ++++++++===       ==========-=      \n"
            "       +++++++===          =======-       \n"
            "       +++++++===       ===========       \n"
            "        ++++++===    =============        \n"
            "        ++++++====================        \n"
            "        ++++++====================        \n"
            "         +++++===================         \n"
        )

    def print_options(self):
        for key in self.option_menu.keys():
            print(key , '---' , self.option_menu[key])
        print("")

    def goMining(self):
        self.game.gatherMaterials()

    def sellResources(self): # UNFINISHED!
        os.system('cls')
        self.print_shop_logo()

        # This block of code is for printing 0 blockname x quantity \n ... etc
        blocksIndexed = {}
        playersInventory = self.game.player.getInventory()
        index = 0
        for block in playersInventory:
            blocksIndexed[index] = block
            index += 1
        for key in blocksIndexed.keys():
            print(f'{key} --- {blocksIndexed[key]["name"]} x{blocksIndexed[key]["quantity"]}')
            if index-1 == key: # This is used to detect if this is the last item in the array, if so print a newline
                print("")


        # VERIFY INPUTS!
        try:
            blockIndex = int(input(f"What do you want to sell? (0-{index-1}) "))
            if blockIndex > index-1:
                print(f'{bcolors.WARNING}OUT OF RANGE!{bcolors.ENDC}')
                time.sleep(1)
                self.sellResources()
                return

            quantityToSell = int(input(f'How much {blocksIndexed[blockIndex]["name"]} do you want to sell? '))
            if quantityToSell > blocksIndexed[blockIndex]["quantity"]:
                print(f"{bcolors.WARNING}You cant sell something you don't have...{bcolors.ENDC}")
                time.sleep(1)
                return
            
            blockWorth = self.game.shop.calculateWorth(blocksIndexed[blockIndex]["name"], quantityToSell)
            confirmSell = input(f'Are you sure you want to sell {blocksIndexed[blockIndex]["name"]} x{quantityToSell} for ${blockWorth}. (y/n) ')
        except KeyboardInterrupt:
            return
        except:
            if type(blocksIndexed) != int or type(blocksIndexed) != int:
                print(f'{bcolors.WARNING}INVALID CHOICE!{bcolors.ENDC}')
                time.sleep(1)
                self.sellResources()
                return

        if confirmSell == 'y' or confirmSell == 'yes':
            confirmSell = True
        else:
            confirmSell = False

        if confirmSell:
            self.game.shop.sellResource(blocksIndexed[blockIndex]["name"], quantityToSell)
        time.sleep(2.5)

    def inventory(self):
        try:
            os.system('cls')
            self.print_inventory_logo()
            self.game.player.print_inventory()

            print(f"{bcolors.WARNING}Press Q to go back to main menu{bcolors.ENDC}")
            while True:
                event = keyboard.read_event(suppress=True)
                if (event.event_type == keyboard.KEY_DOWN) and event.name == 'q':
                    break

                '''
                if keyboard.is_pressed('q'):
                    break
                THIS IS A BAD WAY TO CHECK IF KEY PRESSED
                WHY?
                    It doesnt erase whatever you typed, which isnt great
                '''
        except KeyboardInterrupt:
            return

    def stats(self):
        os.system('cls')
        self.print_stats_logo()
        print(f"{bcolors.WARNING}Press Q to go back to main menu{bcolors.ENDC}\n")

        print(f"{bcolors.HEADER}Stats:{bcolors.ENDC}")
        print(f"    {bcolors.HEADER}Player Stats:{bcolors.ENDC}")
        print(f'        Minecoins:    {self.game.player.minecoins}')
        print(f'        Mining Speed: {self.game.player.miningSpeed}')
        print(f'        Mining Level: {self.game.player.miningLvl}')
        print(f"    {bcolors.HEADER}Upgrades:{bcolors.ENDC}")
        for upgrade in self.game.player.upgrades:
            print(f'        {upgrade["name"]}')
            print(f'            Mining Speed: {upgrade["miningSpeed"]}')

        try:
            while True:
                event = keyboard.read_event(suppress=True)
                if (event.event_type == keyboard.KEY_DOWN) and event.name == 'q':
                    break
        except KeyboardInterrupt:
            return
        
    def shop(self):
        os.system('cls')
        self.print_shop_logo()

        allTools = Items().items

        for i in allTools:
            print(f"{i} --- {allTools[i]['name']} --- ${allTools[i]['price']}")

            if(i == len(allTools)-1): # Print a newline if this is the last item
                print("")

        try:
            toolToBuy = int(input(f"What do you want to buy? (0-{len(allTools)-1}) "))
            if toolToBuy > len(allTools)-1:
                print(f'{bcolors.WARNING}OUT OF RANGE!{bcolors.ENDC}')
                time.sleep(1)
                self.sellResources()
                return
            if toolToBuy > len(allTools)-1:
                print(f'{bcolors.WARNING}OUT OF RANGE!{bcolors.ENDC}')
                time.sleep(1)
                self.sellResources()
                return
            
            confirmation = input(f"Are you sure you want to buy a {allTools[toolToBuy]['name']}? (y/n) ")
            if confirmation == 'y' or confirmation == 'yes':
                confirmation = True
            else:
                confirmation = False
            
            if confirmation:
                self.game.shop.buyTool(allTools[toolToBuy]['name'])
            time.sleep(2.5)
        except KeyboardInterrupt:
            return