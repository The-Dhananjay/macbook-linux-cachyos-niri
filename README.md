# Mac-inspired Linux setup for Niri

Private, reversible plan for a macOS-inspired Linux desktop. CachyOS + Niri is the reference; the implementation prompt detects common distributions and adapts when possible. It does not promise every feature works on every Linux machine.

## Clone and run once

This repository is private. On the target machine, authenticate to GitHub using your normal secure method first (GitHub CLI or SSH key). Then run:

    gh auth login
    gh repo clone The-Dhananjay/macbook-linux-cachyos-niri
    cd macbook-linux-cachyos-niri

Open this folder in a coding agent with terminal and local desktop control. Paste the full prompt in IMPLEMENT_WITH_AI.md once. It asks what to name your assistant (Friday, a custom name, or none), then proceeds with all supported setup items. Read docs/implementation-inventory.md for historical evidence and limitations.

The prompt batches package installation and narrowly scopes system changes to reduce repeated OS authentication. It never asks for, saves or bypasses your password. Some distros may still show multiple native auth prompts; the OS controls this. A fresh machine needs GitHub access and an agent with local computer-control capability.

## Scope

- Niri/Noctalia mac-style bar, Control Center, launcher, dock, notifications, focused app title and window controls.
- Secure PAM-backed video lock, fingerprint status, Nautilus preview, trackpad gestures, screenshot toolbar and Android KDE Connect.
- Optional user-named voice/text assistant, safe desktop commands, local AI, optional web search and external-output-only speech.
- Backups, rollback, validation and privacy guidance.

## Principles

- Preserve the current desktop and install Niri as an additional session if supported.
- Use signed distribution packages and documented APIs. Immutable/declarative systems need native config.
- Back up before edits. Keep changes reversible and test them.
- Never pass speech/model output to a shell. Confirm consequential actions.
- Keep credentials, voice clips, personal photos, wallpaper, biometrics and local models out of Git.
- Linux can imitate macOS styling but cannot guarantee pixel identity or universal app titlebars/menus.

## License

Documentation and original scripts are MIT unless otherwise stated. Third-party assets retain their owners' licenses; no Apple system assets are included.
