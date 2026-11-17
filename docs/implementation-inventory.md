# Feature inventory and evidence

Use this as a reconciliation checklist, not proof that every item is currently installed. Prior user confirmations below are historical; inspect the live system and update this file after work.

**Evidence labels:** Confirmed by user interaction; Configured—verify current state; Partial/known issue; Requested; Platform limitation. Do not mark a feature complete from a mockup or prior claim alone.

## Desktop shell and workflow

| Feature | Historical evidence / status | Recheck |
|---|---|---|
| Keep CachyOS + Niri; user rejected KDE | Confirmed preference | Preserve Niri and inspect exact versions. |
| Noctalia macOS-like top bar: translucent/glass, ~32px, crisp vector icons, consistent font/gaps/date-time | Configured—verify | Inspect scaling, contrast, spacing, quality. |
| Focused app name/menu only while focused; no stale title on desktop; remove duplicate launcher icon | Requested/configured | Test focus and empty workspace. |
| Wi-Fi/Bluetooth glass Control Center with truthful state, Settings route | User confirmed joining Wi-Fi and Bluetooth audio playback | Recheck NetworkManager/BlueZ/PipeWire backend, error-free actions. |
| Outside-click/Escape close for menus/panels | User confirmed for panels after a click-area fix | Check each popup independently, keyboard focus. |
| Light translucent auto-hiding/resizable dock | Configured—verify | Check hide/reveal, translucency and resize. |
| Alt+Space search/launcher and four categories | Configured—verify | Check shortcut, category hover/reveal, focus. |
| Bar traffic lights close, hide/restore, maximize/restore | Confirmed on test window | These are shell controls; hide is workspace behavior. Not universal native titlebar controls. |
| Notifications/control center glass style | Requested/configured | Inspect notification stack, system auth prompt and all panel states. |
| Win+L Quickshell video lock, DP, hidden password field, first key preserved, wrong password rejected, correct password accepted | Confirmed by user | Recheck session-lock protocol, PAM, fail-closed and fallback. SDDM login theme is separate. |
| Sonoma hills moving wallpaper and user DP | Configured—verify | Keep local private media out of repo; check crop/performance. |
| Nautilus Space preview tap + hold | Configured; had intermittent reports | Verify helper lifecycle, reliability and scope. |
| Trackpad gestures/natural scroll/tap | Requested/configured | Hardware-specific; test Niri settings and conflicts. |
| Win+Shift+5 screenshot/recording toolbar | Partial | Portal picker was used in tests; verify screen/window/region/save and recording end-to-end. |
| Android KDE Connect + Nautilus integration | Paired and firewall setup reported | Verify pairing, plugins and narrow local-only firewall scope. |

## Fingerprint

Goodix USB 27c6:5e0a is not established here as upstream-supported. Earlier isolated capture attempts failed; later the user reported successful enrollment/matches, then explicitly approved the experimental driver installation. The user tested rejection of another finger, unlock by enrolled right index, and password fallback. **Verify current driver, service, key/template permissions and dedicated lock PAM include on the live machine.** Keep password fallback. Do not make further PAM or root-driver changes without showing exact diff, recovery route and obtaining fresh approval. These conversational results are not a substitute for current inspection.

## Voice/text assistant (name is selectable)

| Feature | Historical evidence / status | Recheck |
|---|---|---|
| First-run name selection: Friday, custom name, or disable; editable setting | Newly requested | Ask once, never force Friday. |
| Win+Shift+F, optional local Hey-name wake | User confirmed shortcut/wake at points | Check current binding, privacy indicator and lock pause. |
| Compact Siri-inspired glowing bar; mic/listening indicator in same UI | User disliked old large popup and requested redesign | Inspect actual popup. |
| Follow-up without repeated mic click; auto VAD stop/reply; bye closes; Esc/outside/lock/privacy stop | Automatic text reply and follow-up worked in a test | Test turn timing, cancellation and lock behavior. |
| English speech / robust recognition | Known issue | User reported slow listening and transcription errors. Benchmark live voice; fast ASR confused 50% with 250%, slower recognizer got it right. |
| App commands (WhatsApp, Brave, YouTube in Brave), volume/brightness, media, time/battery, windows/workspaces, notes/timers/search | Partial/known issue | User reported YouTube was the only reliably opened app and volume hit assistant output instead of system sink. Verify typed actions individually. |
| Local model/offline commands + optional web search | Requested/configured | Verify installed model, RAM/disk, license, latency. Search sends query text only. |
| Always show text; speak only on explicit external output; female English voice preference | Text-only on built-in output confirmed; external device unavailable for test | Verify actual sink and licensed voice before speaking. |
| Confirmation for messaging, destructive, financial, shutdown/restart | Required | Enforce in backend allowlist, never arbitrary shell. |

## Platform and privacy constraints

- Wayland/Niri cannot uniformly replace every app's native menus/titlebars; toolkit support varies. Shell bar controls are not in-app controls.
- Avoid promising pixel-identical macOS, proprietary Apple assets/fonts, Apple-only haptics or universal gestures.
- Keep passwords, tokens, photos, wallpaper/video, voice clips, biometric templates, local model weights, SSIDs, addresses, device names and private backups out of Git.
- Before implementation: inspect machine, back up exact files, make small reversible changes, test, update evidence and provide rollback. Never let speech or a language model construct shell commands.
