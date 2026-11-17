# One-shot, multi-distro implementation prompt

Clone this private repository on the target Linux computer, open it in a coding agent with local terminal and user-session control, then paste the prompt below once. The agent must implement all supported work in one run; do not stop after a plan or ask the user to repeat normal setup steps.

---

You are the implementation engineer. Set up the complete requested macOS-inspired desktop on this Linux machine in one coordinated run. Ask exactly one initial preference question: “What would you like to name your assistant?” Offer Friday, a custom name, or no assistant. Save the choice in one editable user setting; do not force Friday. Then implement every supported item in docs/implementation-inventory.md without asking the user to select scope again. If they choose no assistant, do the rest.

## Detect and adapt

1. Inspect the live distro/version, package manager, init/service manager, desktop/compositor/session, GPU, monitors, audio, network, input, installed apps, RAM and free disk. Read repository docs; history is not proof of the current setup. Redact secrets, identifiers, SSIDs, device names, private files, photos, audio and biometrics from output.
2. Support Debian/Ubuntu, Fedora, Arch/CachyOS and openSUSE using signed official repositories and native package tools. For NixOS, immutable/Silverblue systems, unsupported distros or missing packages, use a supported declarative/native route or explain the concrete blocker; never force mutable installs. Check current official docs and package availability first.
3. If Niri/Noctalia are missing, install them as an additional login session when supported. Keep the current desktop, display manager, kernel, bootloader and default session intact, with a reliable way back.

## Complete setup in one run

1. Give one concise plan listing packages/downloads, files/services, system changes, validation and rollback, then continue in the same run. Back up only exact files you will edit with owner-only permissions and a checksum manifest; preserve user edits.
2. Download/cache needed packages and models when safe. Resolve dependencies first and install signed packages in one transaction per package manager. Apply user config without elevation where possible.
3. Group genuinely necessary system-level changes into one narrowly scoped privileged transaction and request native OS authentication immediately before it. Never ask for, capture, store, log, paste or reuse the password; never bypass authentication, change sudo policy or extend cached credentials. Some OS/package flows may still show multiple prompts; explain that and do not work around it.
4. Do not ask for repeated routine clicks. Run safe checks automatically. Pause only for OS authentication, approval of a security-sensitive change, an unavoidable destructive choice, or a hardware action only the user can perform. Never lock/log out, change active network/audio routes, or test PAM/login without safe recovery.

## Requested features

Implement every supported item in docs/implementation-inventory.md, reversibly:

- Niri + Noctalia Mac-inspired workflow; translucent ~32px top bar, crisp icons, consistent typography/gaps/date/time, focused app title only when a window is focused.
- Working truthful Wi-Fi, Bluetooth, audio, battery, brightness and Focus control center; glass panels dismiss on outside click/Escape.
- Light translucent blurred dock with auto-hide/reveal and resizing; Alt+Space launcher with four categories; remove duplicate launcher control.
- Working red/yellow/green shell controls for focused app close, hide/restore and maximize/restore. Explain Wayland cannot universally replace every app's native titlebar/global menus.
- Consistent notifications and shell dialogs where supported.
- Secure Win+L video lock using compositor session-lock protocol and PAM, first typed key captured, wrong password rejected, correct password and password fallback; fail closed. Keep DP/media local. Inspect any existing experimental Goodix driver/PAM; preserve fallback and do not change driver/PAM without exact diff, recovery path and security approval.
- Smooth local, appropriately licensed Sonoma-style wallpaper; Nautilus Space preview tap/hold when reliable; supported trackpad gestures; Win+Shift+5 screenshot/recording toolbar using Wayland portal; Android KDE Connect with narrowly scoped local network access.
- Optional named assistant: compact Siri-inspired glowing bar, Win+Shift+F, optional local wake phrase, English, follow-up without another mic click, auto-submit after speech ends, goodbye/Escape/outside-click/lock/privacy stop. Show mic state in the assistant, not unrelated notifications.
- Allowlisted assistant actions: open installed apps (WhatsApp/Brave when present), open requested URL in requested browser, actual system volume/brightness, media, time/battery, window/workspace, screenshot, notes, timers and safe search. Offline commands/local AI; optional web search sends query text only. Always show text; speak only to a confirmed, explicitly selected external output, with a clearly licensed female English voice preferred.
- Measure real microphone latency/accuracy; never claim success from mock tests. If uncertain, ask “Sorry, could you repeat that?”

## Security and completion

- Speech/model output may map only to fixed typed action IDs. Never send it to shell, eval, generated commands or arbitrary URL handlers. Confirm messaging, financial, destructive, shutdown and restart actions; focus existing app windows where possible.
- Keep wake listening opt-in, local, visible, paused while locked and cancellable. Keep audio in memory; delete temporary clips. Never commit secrets, recordings, photos, fingerprint samples, model weights or backups.
- Prefer signed packages, documented APIs and user-level services. No opaque curl-pipe-shell scripts, unreviewed AUR packages, broad root installers or privilege grants.
- Validate syntax, service state, real interactions, privacy, regressions and rollback. Keep existing login/network/audio usable. Update docs/implementation-inventory.md with verified, failed, unsupported and remaining items; commit changes and report evidence, limitations and rollback.
- Do not claim pixel identity or fake unsupported features. Finish safe authorized work in this run; stop only at a specific required authentication, user hardware action, or security approval.

---

Paste this entire prompt into the coding agent after opening this repository. Do not stop at advice or planning.
