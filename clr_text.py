# import pyfiglet

# # Get a list of available fonts
# fonts = pyfiglet.FigletFont().getFonts()

# # Print the list of fonts
# for fonty in fonts:
#     print(f"name of font :{fonty}")
#     text = pyfiglet.figlet_format("starting in ", font=fonty)
#     print(text)




# import pyfiglet

# # Get all available fonts
# all_fonts = pyfiglet.FigletFont().getFonts()

# # Filter medium-sized fonts
# medium_fonts = [font for font in all_fonts if 10 < pyfiglet.FigletFont(font).height <= 20]

# # Print the list of medium-sized fonts
# print("Medium-sized fonts:")
# for font in medium_fonts:
#     print(font)


from colorama import Fore, Style

# Set the text color to yellow
yellow_text = Fore.YELLOW + "This is a simple yellow string" + Style.RESET_ALL

# Print the yellow string
print(yellow_text)
