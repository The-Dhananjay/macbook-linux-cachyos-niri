# Mac-inspired Linux desktop — one-prompt setup

A reversible Niri desktop design system and local-first assistant, with real reference source and an AI-assisted setup workflow. Includes the latest glass-panel, icon, Dock-resizing, appearance/accessibility and settings-rollback fixes.

**CachyOS + Niri is the reference.** Other Linux systems need target-specific package and API adaptation. This project styles Linux and adds supported desktop behavior; it does not install Apple's macOS or guarantee identical features on every device.

## Start on another Linux laptop

You need Python 3.11+, Git, access to this private repository, and a coding agent with terminal and local desktop access. Authenticate to GitHub through the usual secure flow first:

```sh
gh auth login
gh repo clone The-Dhananjay/macbook-linux-cachyos-niri
cd macbook-linux-cachyos-niri
```

Then open the folder in your coding agent and send **one prompt**:

> Read `IMPLEMENT_WITH_AI.md` and execute it end to end on this machine. Ask once for my assistant name or no assistant, then complete every supported module, its checks and rollback. Use the actual bundled source; do not stop at a theme file or planning.

The agent detects the system, asks once for an assistant name (for example Nova or Friday, or none), checks dependencies, batches normal package work, stages the personalized source, backs up exact destinations, installs supported modules and verifies the result. It pauses only for required OS authentication, hardware interaction or a consequential decision. Passwords never go into chat; the OS may still require more than one native prompt.

## Inspect before using

```sh
python3 setup.py doctor
python3 setup.py check
python3 setup.py extract
```

`doctor` is read-only. `check` verifies bundle/file checksums and Python syntax. `extract` writes only `.setup-state/source/` inside this clone. It never installs packages or changes your desktop.

To prepare a personalized working tree:

```sh
python3 setup.py configure --assistant-name Nova
# Or: python3 setup.py configure --no-assistant
python3 setup.py stage
```

The generated source lives in `.setup-state/staged/`. Open `.setup-state/source/docs/module-map.md` for destinations, dependencies and compatibility gates. The AI then completes target-specific deployment and validation; staging alone is not installation.

## Included source

`reference-source.tar.gz` preserves the complete directory tree of original Python applications, original SVG icons, shell helpers, user-service/lock templates, appearance utilities, tests and detailed docs. `SOURCE_MANIFEST.json` lists every file and SHA-256. `setup.py` rejects path traversal, links, duplicate entries, oversized archives and hash mismatches. The manifest detects corruption; trust still comes from reviewing this repository/revision.

No executable binary, downloaded dependency, model weight, API key, password, personal portrait, voice recording, Wi-Fi profile, biometric template or Apple wallpaper/font is bundled. Lock templates use password authentication; experimental fingerprint drivers/PAM configuration are excluded.

## Features

- Compact menu/status bar, clear typography, sharp status icons and app-aware menu integration where supported.
- Stateful Wi-Fi/Bluetooth/audio/brightness controls, battery panel, matching notifications and OSD.
- Translucent Dock with smart hide, moderate magnification and persistent size control.
- Alt+Space launcher; Win+Shift+5 capture toolbar; Niri-native window/workspace/input configuration.
- Matching light/dark panels, coordinated popup dismissal, keyboard focus, pressed/disabled states.
- Reduced motion/transparency and high-contrast custom panels; validated settings changes with rollback.
- Secure session-lock templates, local media, stock file preview, optional Android integration.
- Optional user-named English assistant: local wake phrase, automatic speech endpoint, bounded PC actions, text replies, external-output-only speech, optional local AI/web search.

## Recovery and evidence

The AI must checkpoint exact user files before deployment, preserve the current session and password fallback, and write a local result for each feature: verified, configured but unverified, unsupported, or blocked. Use `setup.py checkpoint`, `seal` and guarded `restore` for supported user-file scopes. Package/service/system-level rollback is recorded separately; this tool does not uninstall packages or modify PAM.

Reference-machine checks include 43 assistant regressions, six Control Center views, five capture modes, launcher navigation, settings rollback and live Niri/Noctalia validation. They do not certify another machine or replace physical microphone, gesture, Bluetooth, lock or recording tests.

## License

Original code and documentation are MIT; see `LICENSE`. Third-party dependencies/assets retain their own licenses. This is an independent Linux customization project.
