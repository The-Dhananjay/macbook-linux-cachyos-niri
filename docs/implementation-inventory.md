# Feature inventory and implementation criteria

This file defines desired behavior for a reversible, macOS-inspired Linux desktop. It is a checklist, not evidence that a feature is already installed. Inspect the actual target system and mark each item verified, unsupported, or incomplete after testing.

## Desktop shell and workflow

| Feature | Implementation and verification |
|---|---|
| Niri session | Preserve the existing desktop; add Niri as a separate login session when supported. Never replace the default session or boot setup. |
| Noctalia top bar | Translucent, compact (~32 px), readable typography, consistent spacing, crisp vector icons and tidy date/time. Show the focused app title only while a window is focused. |
| Control Center | Truthful Wi-Fi, Bluetooth, audio, battery, brightness, focus and settings controls. Use working native backends; dismiss on outside click and Escape. |
| Dock and launcher | Light translucent blurred dock with auto-hide, reveal and resizing. Alt+Space opens launcher/search with four useful categories; avoid duplicate launcher controls. |
| Window controls | Shell controls can close the focused app, hide/restore it through workspace behavior, and maximize/restore. Explain that Wayland cannot universally replace app-native titlebars or global menus. |
| Notifications and panels | Consistent shell styling, clear contrast, keyboard access and outside-click dismissal where supported. |
| Lock screen | Win+L with a compositor session-lock protocol and native authentication. Correctly capture the first typed character, reject wrong passwords, preserve password fallback, and fail closed. Keep profile and wallpaper media local. Any fingerprint support must use a verified Linux driver, preserve fallback, and receive a separate security review before PAM or privileged driver changes. |
| Wallpaper | Use locally provided or appropriately licensed media; optimize motion for the device and avoid bundling Apple-owned assets. |
| File preview and gestures | Nautilus Space preview tap/hold and compositor-supported trackpad gestures only when reliable and reversible. |
| Screenshot and recording | Win+Shift+5 toolbar using the supported Wayland portal for screen/window/region capture and recording. Test destination and recording flow. |
| Android integration | KDE Connect pairing and file integration over narrowly scoped local-network access. |

## Optional assistant

Ask once whether to enable an assistant and what to call it. Support a custom name or no assistant; store the selection as an editable user preference. Keep voice opt-in, local wake listening visible and paused while locked. Use a compact Siri-inspired glowing bar, a keyboard shortcut, optional local wake phrase, English interaction, continuous follow-up, speech-end auto-submit, and clear cancellation via goodbye, Escape, outside click, lock, or privacy control.

Provide deterministic allowlisted actions for installed apps, requested websites in the selected browser, real system volume and brightness, media, time, battery, window/workspace actions, screenshots, notes, timers and safe search. General answers may use local AI; optional web search sends query text only. Always show text. Speak only when an external audio output is explicitly selected and available; prefer a properly licensed English voice. Measure real microphone accuracy and latency; ask the user to repeat when uncertain.

## Privacy, security and rollout

- Never send speech or model output to a shell, eval, generated command or arbitrary URL handler. Map recognized intent only to fixed typed action IDs.
- Confirm messaging, financial, destructive, shutdown and restart actions.
- Keep audio temporary and local; do not commit credentials, personal photos, recordings, biometric data, private system identifiers, local model weights or backups.
- Prefer official signed distro packages and documented APIs. Avoid opaque root installers and broad permission changes.
- Back up exact files before edits, preserve user changes, implement reversible modules, and maintain a safe route back to the original session.
- Validate syntax, services, real interactions, privacy boundaries and rollback. Do not claim pixel identity or unsupported behavior. Report limitations and evidence clearly.
