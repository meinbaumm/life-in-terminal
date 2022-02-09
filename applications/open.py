import sys 
import os

apps = {
    "webstorm": "~/path/to/your_app_here.app/",
    "datagrip": "~/path/to/your_app_here.app/",
    "pycharm":  "~/path/to/your_app_here.app/",
    "telegram": "~/path/to/your_app_here.app/",
    "music": "~/path/to/your_app_here.app/",
    "toptracker":  "~/path/to/your_app_here.app/",
    "todo":  "~/path/to/your_app_here.app/",
    "postgres":  "~/path/to/your_app_here.app/",
    "safari":  "~/path/to/your_app_here.app/",
    "figma":  "~/path/to/your_app_here.app/",
    "trello":  "~/path/to/your_app_here.app/",
    "postman":  "~/path/to/your_app_here.app/",
    "excel":  "~/path/to/your_app_here.app/",
    "word":  "~/path/to/your_app_here.app/",
    "chrome":  "~/path/to/your_app_here.app/",
    "skype":  "~/path/to/your_app_here.app/",
    "slack":  "~/path/to/your_app_here.app/",
    "notion":  "~/path/to/your_app_here.app/",
    "zoom":  "~/path/to/your_app_here.app/",
    "docker":  "~/path/to/your_app_here.app/",
    "settings": "~/path/to/your_app_here.app/",
    "calendar": "~/path/to/your_app_here.app/",
    "photos": "~/path/to/your_app_here.app/",
    "podcasts": "~/path/to/your_app_here.app/",
    "vscode": "~/path/to/your_app_here.app/",
    "appstore": "~/path/to/your_app_here.app/",
    "books": "~/path/to/your_app_here.app/",
}


def open_apps(args, apps_dict):
    for argument in args:
        if argument == "showall":
            _show_aveilable_apps(apps_dict)
            continue
        path = apps_dict[argument]
        os.system(f"open {path}")


def _show_aveilable_apps(apps_dict):
    list_commands = _quick_sort(list(apps_dict.keys()))
    for i in range(len(list_commands)):
        print(f"{i}: {list_commands[i]}")


def _quick_sort(data):
    if len(data) <= 1:
        return data
    else:
        return (
            _quick_sort([e for e in data[1:] if e <= data[0]])
            + [data[0]]
            + _quick_sort([e for e in data[1:] if e > data[0]])
        )


if __name__ == "__main__":
    open_apps(sys.argv[1:], apps)
