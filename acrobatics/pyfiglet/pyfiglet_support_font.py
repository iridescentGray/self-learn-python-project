from pyfiglet import Figlet, FigletFont

print(FigletFont().getFonts())


print("----------------------------------use font------------------------------------")

f = Figlet(font="slant")
print(f.renderText("hanser"))

print(
    "--------------------------------specify width------------------------------------"
)

f = Figlet(font="slant", width=20)
print(f.renderText("hanser"))
