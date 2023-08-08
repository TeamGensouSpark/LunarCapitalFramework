from Remilia.log import Fore, Style


def info(*msg):
    print(Fore.LIGHTGREEN_EX + "✅ %s" % " ".join(msg) + Style.RESET_ALL)


def warn(*msg):
    print(Fore.LIGHTYELLOW_EX + "💡 %s" % " ".join(msg) + Style.RESET_ALL)


def error(*msg):
    print(Fore.LIGHTRED_EX + "🚨 %s" % " ".join(msg) + Style.RESET_ALL)
