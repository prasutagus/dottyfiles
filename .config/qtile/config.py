##### David's qtile Config #####

##### IMPORTS #####
import os
import subprocess

from libqtile.widget import base

from libqtile.config import Key, Screen, Group, Drag, Click
from libqtile.lazy import lazy
from libqtile import layout, bar, widget, hook
from typing import List  # noqa: F401


##### VARIABLES #####
mod = "mod4"
myTerm = "alacritty"

##### KEYBINDINGS #####
keys = [
    # Switch between windows in current stack pane
    Key([mod], "j", lazy.layout.down()),
    Key([mod], "k", lazy.layout.up()),

    Key([mod], "h", lazy.layout.left()),
    Key([mod], "l", lazy.layout.right()),

    # Move windows left, right,up or down in current stack
    Key([mod, "control"], "h", lazy.layout.swap_left()),
    Key([mod, "control"], "l", lazy.layout.swap_right()),
    Key([mod, "control"], "k", lazy.layout.shuffle_up()),
    Key([mod, "control"], "j", lazy.layout.shuffle_down()),

    # Switch window focus to other pane(s) of stack
    Key([mod], "space", lazy.layout.next()),

    # Swap panes of split stack
    Key([mod, "shift"], "space", lazy.layout.rotate()),

    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key([mod, "shift"], "Return", lazy.layout.toggle_split()),

    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout()),
    Key([mod], "w", lazy.window.kill()),

    Key([mod, "control"], "r", lazy.restart()),
    Key([mod, "control"], "q", lazy.shutdown()),
    Key([mod], "r", lazy.spawncmd()),

    # For MonadTall
    Key([mod, "shift"], "space", lazy.layout.flip()),
    Key([mod], "z", lazy.layout.grow()),
    Key([mod], "m", lazy.layout.shrink()),
    Key([mod], "n", lazy.layout.normalize()),

    # Launcher Keys
    Key([mod], "Return", lazy.spawn(myTerm)),
    Key([mod, "control"], "f", lazy.spawn("firefox")),
    Key([mod, "control"], "v", lazy.spawn(myTerm+" -e vim")),
    Key([mod, "control"], "m", lazy.spawn(myTerm+" -e thunar")),
    Key([mod, "control"], "e", lazy.spawn("emacs"))
]
##### GROUPS (WORdKSPACES) #####
groups = [Group(i) for i in "123456789"]

for i in groups:
    keys.extend([
        # mod1 + letter of group = switch to group
        Key([mod], i.name, lazy.group[i.name].toscreen()),

        # mod1 + shift + letter of group = switch to & move focused window to group
        Key([mod, "shift"], i.name, lazy.window.togroup(i.name, switch_group=True)),
        # Or, use below if you prefer not to switch to that group.
        # # mod1 + shift + letter of group = move focused window to group
        # Key([mod, "shift"], i.name, lazy.window.togroup(i.name)),
    ])

##### LAYOUTS #####
layouts = [
    layout.MonadTall(border_focus='#00ff99', margin=10),
    layout.Max(),
    layout.Stack(num_stacks=2),
    # Try more layouts by unleashing below layouts.
    layout.Bsp(),
    # layout.Columns(),
    # layout.Matrix(),
    # layout.MonadTall(border_focus='#00ff99', margin=10),
    # layout.MonadWide(),
    # layout.RatioTile(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]

##### COLORS #####
colors = [["#282a36", "#282a36"], # 0 colour black shade
          ["#808080", "#808080"], # 1 colour grey
          ["#ffffff", "#ffffff"], # 2 colour white
          ["#ff5555", "#ff5555"], # 3 colour bright red
          ["#8d62a9", "#8d62a9"], # 4 colour purple
          ["#668bd7", "#668bd7"], # 5 colour slate blue
          ["#2c3e50", "#2c3e50"], # 6 dark grey panel background
          ["#ff0000", "#ff0000"], # 7 red shutdown color
          ["#e1acff", "#e1acff"], # 8 colour mauve
          ["#9999e6", "#9999e6"], # 9 colour light blue
          ["#40bf80", "#40bf80"], # 10 colour light green
          ["#ffcc00", "#ffcc00"], # 11 colour yellow
          ["#364d63", "#364d63"], # 12 colour blue/grey panel alt
          ["#3399ff", "#3399ff"]] # 13 colour light blue


alt_colors = [["#d5f4e6"],   # 0
                ["#80ced6"], # 1
                ["#fefbd8"], # 2
                ["#618685"], # 3
                ["#ffef96"], # 4
                ["#4F84C4"], # 5 Marina
                ["#b2b2b2"], # 6 Light Grey
                ["#223A5E"]  # 7 Navy Peony
]

##### MOUSE CALLBACKS #####

def open_cal(qtile):
    qtile.cmd_spawn('alacritty -e calcurse')

def run_yay(qtile):
    qtile.cmd_spawn('alacritty -e yay -Syu')

 


##### WIDGETS (BAR) #####

widget_defaults = dict(
    font='freesans',
    fontsize=14,
    padding=3,
)
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        top=bar.Bar(
            [
                widget.CurrentLayout(foreground=colors[10], padding=8),
                widget.GroupBox(
                    inactive='99a3a4',
                    active='f7dc6f',
                    this_current_screen_border=colors[13],
                    borderwidth=1
                ),
                widget.Prompt(),
                widget.Sep(foreground=colors[10], padding=6, size_percent=60),
                widget.WindowName(),
                widget.TextBox(
                    text="davidArch",
                ),
                widget.DF(format='SSD Free: {uf}{m})', visible_on_warn=False),
                widget.Sep(foreground=colors[10], padding=6, size_percent=60),
                widget.KeyboardLayout(fmt='kbd {}', configured_keyboards=['gb', 'us']),
                widget.Sep(foreground=colors[10], padding=6, size_percent=60),
                widget.PulseVolume(fmt='Vol: {}'),
                widget.Sep(foreground=colors[10], padding=6, size_percent=60),
                widget.CheckUpdates(
                    distro="Arch_checkupdates",
                    colour_no_updates=colors[1],
                    colour_have_updates=colors[3],
                    mouse_callbacks={'Button1': run_yay}),
                widget.Sep(foreground=colors[10], padding=6, size_percent=60),
                widget.CPU(format='CPU {load_percent}%'),
                widget.Sep(foreground=colors[10], padding=6, size_percent=60),
                widget.Memory(format='Mem Used: {MemUsed}Mb'),
                widget.Sep(foreground=colors[10], padding=6, size_percent=60),
                widget.Clock(
                    format='%A, %d %B %Y %H:%M',
                    mouse_callbacks={'Button1': open_cal}
                ),
                widget.Sep(foreground=colors[10], padding=6, size_percent=60),
                widget.Systray(icon_size=24),
                widget.QuickExit(
                    foreground=colors[3],
                    padding=10,
                    font='Liberation Mono'
                ),
            ],
            28,
            background=alt_colors[7],
            margin=[1, 0, 2, 0],
        ),
    ),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front())
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: List
main = None
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(float_rules=[
    # Run the utility of `xprop` to see the wm class and name of an X client.
    {'wmclass': 'confirm'},
    {'wmclass': 'dialog'},
    {'wmclass': 'download'},
    {'wmclass': 'error'},
    {'wmclass': 'file_progress'},
    {'wmclass': 'notification'},
    {'wmclass': 'splash'},
    {'wmclass': 'toolbar'},
    {'wmclass': 'confirmreset'},  # gitk
    {'wmclass': 'makebranch'},  # gitk
    {'wmclass': 'maketag'},  # gitk
    {'wname': 'branchdialog'},  # gitk
    {'wname': 'pinentry'},  # GPG key password entry
    {'wmclass': 'ssh-askpass'},  # ssh-askpass
])
auto_fullscreen = True
focus_on_window_activation = "smart"

##### STARTUP APPS #####
@hook.subscribe.startup_once
def autostart():
    home = os.path.expanduser('~/.config/qtile/autostart.sh')
    subprocess.call([home])

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
