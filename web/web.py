import sys 
import webbrowser

sites = {
    "multitran": "Your url here",
    "deepl": "Your url here",
    "cambridge": "Your url here",
    "notion": "Your url here",
    "github": "Your url here",
    "gitlab": "Your url here",
    "turtle": "Your url here",
    "gmail": "Your url here",
    "mail": "Your url here",
    "pocket": "Your url here",
    "reddit": "Your url here",
    "twitter": "Your url here",
    "instagram": "Your url here",
    "ytranslate": "Your url here",
    "gtranslate": "Your url here",
}


def _show_aveilable_sites(sites_dict):
    list_commands = _quick_sort(list(sites_dict.keys()))
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


def open_sites(args, sites_dict):
    for argument in args:
        if argument == "showall":
            _show_aveilable_sites(sites_dict)
            continue
        try:
            url = sites_dict[argument]
            webbrowser.open(url, new=0)
        except KeyError:
            print(f"{argument} not found in available sites")


if __name__ == "__main__":
    open_sites(sys.argv[1:], sites)
