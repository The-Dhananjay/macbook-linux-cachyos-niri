# Mac-inspired CachyOS + Niri

A private, reversible plan for the user's CachyOS + Niri setup. This is Linux theming and workflow work, not macOS; it does not replace Niri with KDE.

## Start here

1. Read [IMPLEMENT_WITH_AI.md](IMPLEMENT_WITH_AI.md) for the one-shot implementation prompt.
2. Read [docs/implementation-inventory.md](docs/implementation-inventory.md) for the full requested feature list, historical evidence, known issues and platform limits.
3. The implementer must inspect the live machine, confirm scope, back up exact files, make reversible changes, verify each feature, and update the evidence. Do not assume prior chat reports are current state.

## Feature scope

- Niri/Noctalia macOS-inspired bar, Control Center, launcher, dock, notifications, app/window controls and focused-app title.
- Secure PAM-backed moving lock screen, profile picture, fingerprint status, file preview, trackpad gestures, screenshot toolbar and Android/KDE Connect.
- User-named voice/text assistant: Friday is optional; custom name or disabling it are valid. Local commands/AI, optional web search and external-output-only voice preference.
- Safety, rollback, privacy and truthful implementation status.

## Principles

- Preserve Niri. Use signed packages and documented interfaces; avoid opaque root installers.
- Back up before changes; keep each feature independently reversible.
- Never send speech/model text to a shell. Use fixed, reviewed action IDs and confirmations for consequential actions.
- Never commit credentials, voice recordings, personal photos, wallpaper/video, biometric templates, model weights or private machine identifiers.
- State limits honestly: apps own their native titlebars/menus and Linux cannot be pixel-identical to macOS.

## License

Documentation and original scripts are MIT unless a file says otherwise. Third-party assets and marks retain their owners' licenses. No Apple system assets are included.
