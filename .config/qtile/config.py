##### David's qTile Config #####

##### IMPORTS #####
import os
import subprocess
from libqtile.config import Key, Screen, Group, Drag, Click
from libqtile.lazy import lazy
from libqtile import layout, bar, widget, hook
from typing import List  # noqa: F401 ##### SETUP #####

##### Settings #####
mod = "mod4"
myTerm = "termite"

##### KEYBINDINGS #####
keys = [
    # Switch between windows in current stack pane
    Key([mod], "k", lazy.layout.down()),
    Key([mod], "j", lazy.layout.up()),

    Key([mod], "h", lazy.layout.left()),
    Key([mod], "l", lazy.layout.right()),

    Key([mod, "shift"], "h", lazy.layout.swap_left()),
    Key([mod, "shift"], "l", lazy.layout.swap_right()),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down()),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up()),
    # Move windows up or down in current stack
    # Key([mod, "control"], "k", lazy.layout.shuffle_down()),
    # Key([mod, "control"], "j", lazy.layout.shuffle_up()),

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
    Key([mod], "Return", lazy.spawn("termite")),
    Key([mod, "control"], "f", lazy.spawn("firefox")),
    Key([mod, "control"], "v", lazy.spawn(myTerm+" -e vim")),
    Key([mod, "control"], "m", lazy.spawn(myTerm+" -e thunar")),

]
##### GROUPS (WORKSPACES) #####
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


##### WIDGETS (BAR) #####

widget_defaults = dict(
    font='freesans',
    fontsize=16,
    padding=3,
)
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        top=bar.Bar(
            [
                widget.CurrentLayout(foreground=colors[10], padding=8),
                widget.GroupBox(inactive='99a3a4', active='f7dc6f', this_current_screen_border=colors[13]),
                widget.Prompt(),
                widget.WindowName(),
                widget.TextBox("davidArch"),
                widget.DF(format='({uf}{m})', visible_on_warn=False),
                widget.KeyboardLayout(configured_keyboards=['us', 'gb'], foreground=colors[1]),
                widget.TextBox("Vol:", foreground=colors[11]),
                widget.PulseVolume(foreground=colors[11]),
                widget.Sep(padding=6),
                widget.CheckUpdates(distro='Arch_checkupdates', colour_no_updates=colors[1], colour_have_updates=colors[10]),
                widget.Sep(padding=6),
                widget.CPU(format='CPU {load_percent}%', foreground=colors[9]),
                widget.Sep(padding=6),
                widget.Memory(foreground=colors[8]),
                widget.Sep(padding=6),
                widget.Clock(format='%A, %d %B %Y %H:%M'),
                widget.Sep(padding=6),
                widget.Systray(icon_size=24),
                widget.QuickExit(foreground=colors[7], padding=8),
            ],
            28,
            background=colors[12],
            margin=[2, 0, 2, 0],
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