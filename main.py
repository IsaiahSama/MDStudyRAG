"""This will launch the CLI version of the tool."""

from tools import CliMenu
    

def main():
    """The entry point"""
    
    menu = CliMenu()
    
    # The while loop!
    while True:
        # Display the menu!
        
        menu.display_menu()
        break
    
    pass

if __name__ == "__main__":
    main()