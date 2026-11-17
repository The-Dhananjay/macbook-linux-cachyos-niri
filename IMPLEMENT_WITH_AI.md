# One-shot implementation prompt

You are implementing a Mac-inspired CachyOS desktop on the user's existing Niri setup. Keep Niri; do not install KDE or another desktop environment. The complete scope and historical evidence are in docs/implementation-inventory.md.

## First-run preference

Ask once: “What would you like to name your assistant?” Offer Friday, a custom name, or no assistant. Do not assume Friday. Save the answer in one editable user setting; derive an optional local wake phrase from the chosen name. Then continue with the full feature set below without asking the user to reselect scope. If the user chooses no assistant, skip assistant features and implement the rest. Ask for approval only for genuinely risky or irreversible choices, system authentication, and actions that change account/security policy.

## Full requested feature set

Inspect the live setup and implement every supported item in docs/implementation-inventory.md in one coordinated project, using small reversible modules:

- Niri + Noctalia macOS-inspired desktop; ~32px translucent top bar, crisp vector icons, consistent font/size/gaps and clean date/time; focused app title/menu only when a window is focused; no stale desktop title.
- Working, truthful Wi-Fi/Bluetooth/audio/battery/brightness/Focus/settings Control Center; polished translucent panels; outside-click and Escape dismiss; no fake connected states.
- Light glass dock with blur/transparency, auto-hide/reveal and resizing; Alt+Space launcher/search and four useful categories; remove duplicate launcher control.
- Working red/yellow/green shell controls for focused app close, workspace-hide/restore and maximize/restore. Explain that Wayland apps own native titlebars/menus, so universal in-app traffic lights/global menus cannot be guaranteed.
- Cohesive notifications and shell/system dialogs where supported.
- Secure Win+L video lock using compositor session-lock protocol and PAM, personal DP/media kept local, hidden password field shown on first typed key without dropping it, wrong password rejected, correct password and password fallback work, fail closed. Verify existing experimental Goodix fingerprint driver/PAM state carefully; preserve fallback and do not alter PAM/driver security settings without reviewing exact diff, recovery path and approval.
- Smooth local Sonoma-style wallpaper if user-provided/appropriately licensed; Nautilus Space preview with tap/hold if reliable; trackpad gestures; Win+Shift+5 screenshot/recording toolbar through supported Wayland portal; Android KDE Connect with narrow local-network firewall scope.
- Assistant UI: compact Siri-inspired glowing bar, optional local wake phrase, shortcut Win+Shift+F, English, persistent follow-up without another mic click, automatic speech-end detection/reply, and goodbye/Escape/outside-click/lock/privacy stop. Do not show unrelated mic notifications.
- Assistant actions: installed-app launching (including WhatsApp/Brave if installed), opening a requested URL in a requested browser (YouTube in Brave), actual system volume and brightness, media, time/battery, window/workspace actions, screenshots, notes, timers and safe search. Always show text; speak only to an explicitly selected, available external output, with a clearly licensed female English voice as a preference. Local/offline commands and local AI; optional web search sends query text only.
- Improve recognition latency and accuracy using safe measured approaches. Never claim ASR solved without real microphone tests. If uncertain, ask “Sorry, could you repeat that?”

## Required engineering workflow

1. Inspect CachyOS release, Wayland session, Niri/Noctalia/Quickshell/helper versions, exact config paths, packages/sources, user services, disk/RAM, audio routes, input/hardware metadata and installed apps. Treat chat and inventory as history, not current-state proof. Redact secrets, personal identifiers, SSIDs, MAC/IP addresses, device names, photos, audio and biometrics from output.
2. Reconcile each inventory entry against live evidence. Check current official upstream docs and signed package availability before relying on APIs or installing. Do not add Apple-owned fonts, binaries or wallpapers.
3. Before edits, give a concise plan, conflicts and intended tests. Back up each exact file with owner-only permissions and checksums; preserve unrelated edits and provide a diff/dry-run. Implement all safe, authorized modules in the same run, but keep the changes small, reversible and independently recoverable.
4. Security: assistant transcripts and model output must only map to fixed typed action IDs; never pass them to shell, eval, arbitrary URL handler or generated command. Confirm messaging, financial, destructive, shutdown/restart actions. Avoid duplicate app launches; resolve desktop files and focus existing windows. Keep audio local/in memory and delete temporary clips. Wake listening is opt-in, visible, paused while locked, and cancellable. Never weaken PAM, login, firewall or device permissions casually. Never commit credentials, photos, recordings, fingerprints, model weights or private backups.
5. Prefer signed CachyOS packages, documented APIs and user-level services. No opaque curl-pipe-shell, unreviewed AUR script, blanket root installer or broad privilege grant. Do not disrupt active networking, audio, login or lock during validation.
6. Validate config syntax, service state, privacy boundaries, rollback, real interactions and regressions. Test each available feature; mark unavailable hardware/platform support honestly instead of pretending. Update docs/implementation-inventory.md with what was implemented, confirmed, failed or remains requested. Commit clean changes and report exact paths, evidence, limits and rollback steps.

Deliver the whole supported feature set in this run; do not stop at advice or a plan. Match macOS visual language without promising pixel identity. When a feature cannot be made universal or safe, explain the exact limitation and implement the closest reliable Niri-native option.
