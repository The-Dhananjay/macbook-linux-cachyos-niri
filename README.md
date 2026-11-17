# Mac-like CachyOS + Niri

Private, reversible desktop engineering project for building a polished macOS-inspired experience on CachyOS with Niri and Noctalia, plus the local-first Friday assistant.

This is a Linux customization project, not macOS. It targets the documented CachyOS/Niri stack and avoids replacing the compositor or installing another desktop environment. Upstream APIs and packages move quickly; check the compatibility matrix before applying changes.

## Start here

1. Read [docs/current-state.md](docs/current-state.md) for what has already been installed and what is only a mockup or known limitation.
2. Read [docs/safety-and-rollback.md](docs/safety-and-rollback.md) before changing the live machine.
3. Give [IMPLEMENT_WITH_AI.md](IMPLEMENT_WITH_AI.md) to the coding agent in the repository root. It contains the single end-to-end implementation prompt and requires the agent to inspect the machine, plan, implement in stages, test, and leave rollback instructions.
4. Use [docs/feature-spec.md](docs/feature-spec.md) as the desired product specification.

## Feature areas

- Niri workflow, trackpad gestures, workspaces, window rules and shortcut map
- Noctalia mac-style menu bar, Control Center, launch/search, dock and notifications
- lock screen, fingerprint status, screenshot toolbar, file preview and Android integration
- Friday voice and text assistant, command permissions, speech recognition and response behavior
- rollback, backup, validation, privacy and security practices

## Principles

- Keep Niri as the compositor; use its native configuration and documented protocols.
- Treat every feature as an opt-in, independently reversible module.
- Back up exact files before edits; never overwrite the user's existing configuration without a diff and a recoverable copy.
- Use signed distribution packages first. Avoid running downloaded scripts as root.
- Never put passwords, tokens, voice recordings, profile photos, fingerprint samples, model weights, private machine identifiers, or raw home-directory backups in Git.
- Friday may execute only explicit, allowlisted desktop actions. No arbitrary shell, model-generated commands, or destructive actions without confirmation.
- State limitations honestly: styling cannot make Linux identical to macOS, and hardware features require verified Linux driver support.

## Layout

| Path | Purpose |
|---|---|
| [IMPLEMENT_WITH_AI.md](IMPLEMENT_WITH_AI.md) | One prompt for an AI implementer |
| [docs/feature-spec.md](docs/feature-spec.md) | Desired behavior and acceptance criteria |
| [docs/architecture.md](docs/architecture.md) | Components, data flow and boundaries |
| [docs/current-state.md](docs/current-state.md) | Evidence-based snapshot of the target machine |
| [docs/setup.md](docs/setup.md) | Staged installation and verification approach |
| [docs/safety-and-rollback.md](docs/safety-and-rollback.md) | Security rules, backup and restore |
| [docs/testing.md](docs/testing.md) | Test matrix and completion gate |
| [docs/sources.md](docs/sources.md) | Official upstream references |

## Target baseline

The working setup documented here is CachyOS + Niri 26.04 + Noctalia 5.5.0 on Wayland. The currently installed setup also uses a native Quickshell session-lock surface and local user services. Versions are a snapshot, not a promise that future package versions are compatible.

## License

Documentation and original scripts in this repository are licensed under MIT unless a file says otherwise. Third-party software, fonts, images, models and trademarks retain their owners' licenses. No Apple system font, Apple executable, or bundled Apple wallpaper/video is redistributed here.
