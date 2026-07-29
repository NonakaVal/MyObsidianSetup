---
dateCreated: "[[2026-04-23]]"
share_link: https://share.note.sx/fb9s9fd7#bXAaQ+NfN9clkR8SGtkpJfgcpARxxy/Tj8PmcifEoGQ
share_updated: 2026-04-23T16:05:09-03:00
---
```bash
###############################################################################
# CONFIGURAÇÃO i3WM - EndevourOS 
###############################################################################

set $mod Mod4
font pango:JetBrainsMono Nerd Font 12
set $term kitty

# ================================
# AUTOSTART (APLICATIVOS/SERVIÇOS)
# ================================

# 🔧 Ambiente / Sessão
exec_always --no-startup-id dbus-update-activation-environment --systemd DISPLAY XAUTHORITY
exec_always --no-startup-id $HOME/.config/i3/scripts/import-gsettings
exec --no-startup-id dex --autostart --environment i3

# 🔐 Autenticação (sudo / GUI)
exec --no-startup-id /usr/lib/polkit-gnome/polkit-gnome-authentication-agent-1

# 🖥️ Monitores
exec --no-startup-id ~/.screenlayout/monitor.sh

# 🎨 Wallpaper
exec --no-startup-id feh --bg-fill /home/val/Pictures/walls/wallhaven-yxdrex.jpg

# ⚡ Energia / Screen
exec --no-startup-id xset s 480 dpms 600 600 600
exec --no-startup-id xss-lock -l ~/.config/i3/scripts/blur-lock

# 🔔 Notificações
exec --no-startup-id dunst

# 📋 Clipboard
exec_always --no-startup-id copyq

# 🌐 Applets (tray)
exec_always --no-startup-id nm-applet
exec_always --no-startup-id blueman-applet

# 🎞️ Compositor
exec_always --no-startup-id picom --config ~/.config/picom/picom.conf

# 🌍 Startup opcional (browser)
exec --no-startup-id sleep 5 && firefox https://github.com/endeavouros-team/endeavouros-i3wm-setup/blob/main/force-knowledge.md

# 🚀 Launcher
bindsym $mod+a exec --no-startup-id ~/.config/i3/scripts/fav-apps.sh


# ================================
# ATALHOS DE SISTEMA (i3)
# ================================
bindsym $mod+q kill
bindsym $mod+Shift+c reload
bindsym $mod+Shift+r restart
bindsym $mod+Shift+e exec --no-startup-id ~/.config/i3/scripts/powermenu
bindsym $mod+l exec --no-startup-id ~/.config/i3/scripts/blur-lock
bindsym $mod+v exec copyq toggle
bindsym $mod+ exec --no-startup-id xed .config/i3/config

# ================================
# LAYOUT E JANELAS
# ================================
workspace_layout default
new_window pixel 1
floating_modifier $mod
gaps inner 1
gaps outer 2

exec --no-startup-id i3-msg "workspace $ws10; workspace $ws9; workspace $ws8; workspace $ws7; workspace $ws6; workspace $ws5; workspace $ws4; workspace $ws3; workspace $ws2; workspace $ws1"

# ================================
# NAVEGAÇÃO E WORKSPACES
# ================================
# Win + clique do meio fecha a janela
bindsym --whole-window $mod+button2 kill

# overview de janelas - começa com todas
bindsym Control+apostrophe exec --no-startup-id ~/.config/i3/scripts/rofi-window-overview.sh all
bindsym Mod1+Tab --release exec rofi -show window -modi window -show-icons -window-format "{w}  {t}"

# overview de janelas - começa já filtrado na workspace atual
bindsym Mod1+Shift+Tab exec --no-startup-id ~/.config/i3/scripts/rofi-window-overview.sh current

bindsym $mod+Tab workspace next
bindsym $mod+Shift+Tab workspace prev

bindsym $mod+Left focus left
bindsym $mod+Down focus down
bindsym $mod+Up focus up
bindsym $mod+Right focus right

bindsym $mod+Shift+Left move left
bindsym $mod+Shift+Down move down
bindsym $mod+Shift+Up move up
bindsym $mod+Shift+Right move right

bindsym $mod+h split h
bindsym $mod+n split v
bindsym $mod+Shift+f fullscreen toggle
bindsym $mod+f floating toggle
bindsym $mod+space focus mode_toggle

bindsym $mod+s layout stacking
bindsym $mod+g layout tabbed
bindsym $mod+t layout toggle split

bindsym $mod+Next workspace next
bindsym $mod+Prior workspace prev
bindsym $mod+Shift+Next move container to workspace next; workspace next
bindsym $mod+Shift+Prior move container to workspace prev; workspace prev
bindsym $mod+Shift+n exec --no-startup-id ~/.config/i3/scripts/empty_workspace

# ================================
# WORKSPACES
# ================================
set $ws1 "1:1 "
set $ws2 "2:2 "
set $ws3 "3:3 "
set $ws4 "4:4 󰈙"
set $ws5 "5:5 "
set $ws6 "6:6 "
set $ws7 "7:7 "
set $ws8 "8:8 "
set $ws9 "9:9 "
set $ws10 "10:10 "

exec --no-startup-id i3-msg "workspace $ws10; workspace $ws9; workspace $ws8; workspace $ws7; workspace $ws6; workspace $ws5; workspace $ws4; workspace $ws3; workspace $ws2; workspace $ws1"

# switch to workspace
bindcode $mod+10 workspace $ws1
bindcode $mod+11 workspace $ws2
bindcode $mod+12 workspace $ws3
bindcode $mod+13 workspace $ws4
bindcode $mod+14 workspace $ws5
bindcode $mod+15 workspace $ws6
bindcode $mod+16 workspace $ws7
bindcode $mod+17 workspace $ws8
bindcode $mod+18 workspace $ws9
bindcode $mod+19 workspace $ws10

# switch to workspace with numpad keys
bindcode $mod+87 workspace $ws1
bindcode $mod+88 workspace $ws2
bindcode $mod+89 workspace $ws3
bindcode $mod+83 workspace $ws4
bindcode $mod+84 workspace $ws5
bindcode $mod+85 workspace $ws6
bindcode $mod+79 workspace $ws7
bindcode $mod+80 workspace $ws8
bindcode $mod+81 workspace $ws9
bindcode $mod+90 workspace $ws10

# switch to workspace with numlock numpad keys
bindcode $mod+Mod2+87 workspace $ws1
bindcode $mod+Mod2+88 workspace $ws2
bindcode $mod+Mod2+89 workspace $ws3
bindcode $mod+Mod2+83 workspace $ws4
bindcode $mod+Mod2+84 workspace $ws5
bindcode $mod+Mod2+85 workspace $ws6
bindcode $mod+Mod2+79 workspace $ws7
bindcode $mod+Mod2+80 workspace $ws8
bindcode $mod+Mod2+81 workspace $ws9
bindcode $mod+Mod2+90 workspace $ws10

# mover container e acompanhar
bindcode $mod+Shift+10 move container to workspace $ws1; workspace $ws1
bindcode $mod+Shift+11 move container to workspace $ws2; workspace $ws2
bindcode $mod+Shift+12 move container to workspace $ws3; workspace $ws3
bindcode $mod+Shift+13 move container to workspace $ws4; workspace $ws4
bindcode $mod+Shift+14 move container to workspace $ws5; workspace $ws5
bindcode $mod+Shift+15 move container to workspace $ws6; workspace $ws6
bindcode $mod+Shift+16 move container to workspace $ws7; workspace $ws7
bindcode $mod+Shift+17 move container to workspace $ws8; workspace $ws8
bindcode $mod+Shift+18 move container to workspace $ws9; workspace $ws9
bindcode $mod+Shift+19 move container to workspace $ws10; workspace $ws10

# move focused container to workspace with numpad keys e acompanhar
bindcode $mod+Shift+Mod2+87 move container to workspace $ws1; workspace $ws1
bindcode $mod+Shift+Mod2+88 move container to workspace $ws2; workspace $ws2
bindcode $mod+Shift+Mod2+89 move container to workspace $ws3; workspace $ws3
bindcode $mod+Shift+Mod2+83 move container to workspace $ws4; workspace $ws4
bindcode $mod+Shift+Mod2+84 move container to workspace $ws5; workspace $ws5
bindcode $mod+Shift+Mod2+85 move container to workspace $ws6; workspace $ws6
bindcode $mod+Shift+Mod2+79 move container to workspace $ws7; workspace $ws7
bindcode $mod+Shift+Mod2+80 move container to workspace $ws8; workspace $ws8
bindcode $mod+Shift+Mod2+81 move container to workspace $ws9; workspace $ws9
bindcode $mod+Shift+Mod2+90 move container to workspace $ws10; workspace $ws10

# move focused container to workspace with numpad keys e acompanhar
bindcode $mod+Shift+87 move container to workspace $ws1; workspace $ws1
bindcode $mod+Shift+88 move container to workspace $ws2; workspace $ws2
bindcode $mod+Shift+89 move container to workspace $ws3; workspace $ws3
bindcode $mod+Shift+83 move container to workspace $ws4; workspace $ws4
bindcode $mod+Shift+84 move container to workspace $ws5; workspace $ws5
bindcode $mod+Shift+85 move container to workspace $ws6; workspace $ws6
bindcode $mod+Shift+79 move container to workspace $ws7; workspace $ws7
bindcode $mod+Shift+80 move container to workspace $ws8; workspace $ws8
bindcode $mod+Shift+81 move container to workspace $ws9; workspace $ws9
bindcode $mod+Shift+90 move container to workspace $ws10; workspace $ws10

# resize window (you can also use the mouse for that):
mode "resize" {
    bindsym h resize shrink width 5 px or 5 ppt
    bindsym j resize grow height 5 px or 5 ppt
    bindsym k resize shrink height 5 px or 5 ppt
    bindsym l resize grow width 5 px or 5 ppt

    # arrow keys
    bindsym Left resize shrink width 5 px or 5 ppt
    bindsym Down resize grow height 5 px or 5 ppt
    bindsym Up resize shrink height 5 px or 5 ppt
    bindsym Right resize grow width 5 px or 5 ppt

    # exit resize mode
    bindsym Return mode "default"
    bindsym Escape mode "default"
}

bindsym $mod+r mode "resize"

# atalhos de apps abrindo já na workspace certa
bindsym $mod+semicolon exec --no-startup-id xed /home/val/.config/i3/config
bindsym $mod+Return workspace $ws1; exec --no-startup-id kitty
bindsym $mod+e workspace $ws3; exec --no-startup-id thunar
bindsym $mod+Mod1+e workspace $ws3; exec --no-startup-id thunar
bindsym $mod+Mod1+n workspace $ws4; exec --no-startup-id xed
bindsym $mod+Shift+s workspace $ws4; exec --no-startup-id /home/val/.config/i3/scripts/snippet-holder.sh
bindsym Control+Mod1+f workspace $ws2; exec --no-startup-id google-chrome-stable

bindsym Control+Mod1+1 exec --no-startup-id kitty --directory ~/Documents/Github
bindsym Control+Mod1+2 exec --no-startup-id kitty --directory ~/Documents/Notes/X/Scripts
bindsym Control+Mod1+3 exec --no-startup-id kitty --directory "$HOME/.config"

# ================================
# MULTIMÍDIA E SISTEMA
# ================================
bindsym XF86AudioRaiseVolume exec --no-startup-id ~/.config/i3/scripts/volume_brightness.sh volume_up
bindsym XF86AudioLowerVolume exec --no-startup-id ~/.config/i3/scripts/volume_brightness.sh volume_down
bindsym XF86AudioMute exec --no-startup-id ~/.config/i3/scripts/volume_brightness.sh volume_mute
bindsym XF86AudioMicMute exec amixer sset Capture toggle
bindsym XF86MonBrightnessUp exec --no-startup-id ~/.config/i3/scripts/volume_brightness.sh brightness_up
bindsym XF86MonBrightnessDown exec --no-startup-id ~/.config/i3/scripts/volume_brightness.sh brightness_down

bindsym XF86AudioPlay exec --no-startup-id playerctl play-pause
bindsym XF86AudioNext exec --no-startup-id playerctl next
bindsym XF86AudioPrev exec --no-startup-id playerctl previous

bindsym Print exec --no-startup-id scrot ~/Pictures/Screenshots/%Y-%m-%d-%H-%M-%S-screenshot.png
bindsym $mod+Print exec --no-startup-id scrot -u ~/Pictures/Screenshots/%Y-%m-%d-%H-%M-%S-screenshot.png
bindsym $mod+Shift+Print exec --no-startup-id scrot -s ~/Pictures/Screenshots/%Y-%m-%d-%H-%M-%S-screenshot.png

# ================================
# ROFI (MENUS)
# ================================
bindsym $mod+p exec --no-startup-id rofi -modi drun -show drun -config ~/.config/rofi/rofidmenu.rasi
bindsym $mod+d exec --no-startup-id ~/.config/i3/scripts/audio-device-switch
bindsym $mod+Shift+p exec --no-startup-id ~/.config/i3/scripts/power-profiles
bindsym F1 exec --no-startup-id ~/.config/i3/scripts/keyhint-2

# ================================
# REGRAS DE JANELAS (FLOATING)
# ================================
for_window [class="Yad" instance="yad"] floating enable
for_window [class="Galculator" instance="galculator"] floating enable
for_window [class="Pavucontrol" instance="pavucontrol"] floating enable
for_window [class="Blueberry.py" instance="blueberry.py"] floating enable
for_window [window_role="About"] floating enable


# ================================
# CORES
# ================================
set $darkblue #08052b
set $lightblue #5294e2
set $urgentred #e53935
set $white #ffffff
set $grey #b0b5bd
set $mediumgrey #8b8b8b

# Estilo das Janelas
# class                 border      bground     text        indicator   child_border
set $focus_border #FF0000
set $unfocus_border #1a1a1a

client.focused          $focus_border  #000000   #ffffff   $focus_border $focus_border
client.unfocused        $unfocus_border #000000  #777777   $unfocus_border $unfocus_border

# ================================
# BARRA (i3BAR)
# ================================
bar {
    font pango: Noto Sans Regular 10
    status_command i3blocks -c ~/.config/i3/i3blocks.conf
    position bottom
    strip_workspace_numbers yes
    tray_output primary
    tray_padding 2
    
    colors {
        separator #e345ff
        background #383c4a
        statusline #ffffff
        focused_workspace  #8b8b8b #b0b5bd #383c4a #e345ff
        active_workspace   #5294e2 #8b8b8b #383c4a #e345ff
        inactive_workspace #383c4a #383c4a #b0b5bd #e345ff
        urgent_workspace   #e53935 #e53935 #ffffff #e345ff
    }
}
```


