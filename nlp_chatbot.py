import colorama
from colorama import Fore, Style
from textblob import TextBlob
colorama.init()
print(f"{Fore.CYAN} 🙏 🌻 welcome to the seniment spy {Style.RESET_ALL}")
user_name=input(f"{Fore.BLUE} please enter your name; {Style.RESET_ALL}").strip()
print(f"{Fore.GREEN}nice to meeet you ,{user_name}")
user_in=input(f"{Fore.BLUE} how are you feeling today? {Style.RESET_ALL}").strip()
user_input=user_in.lower()

polarity=TextBlob(user_input).sentiment.polarity
if polarity>0:
    sentiment="positive"
    emoji="😊"
    color=Fore.GREEN
elif polarity<0:
    sentiment="negative"
    emoji="😞"
    color=Fore.RED
else:
    sentiment="neutral"
    emoji="😐"
    color=Fore.YELLOW
print(f"{color}{emoji}{sentiment}sentiment detected!"f"{polarity:.2f} {Style.RESET_ALL}")