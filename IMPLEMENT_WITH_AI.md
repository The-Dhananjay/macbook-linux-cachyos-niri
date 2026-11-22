# One-prompt implementation contract

Paste this instruction into a coding agent opened in the cloned repository:

> Execute this file end to end. Complete the supported Mac-inspired Linux setup using the source in this repo, inspect my target machine, ask once for my assistant name or no assistant, then implement, verify and document the result. Do not stop after advice, a plan, source staging or a style override.

## 1. Read and inspect

Run `python3 setup.py doctor`, `python3 setup.py check`, then `python3 setup.py extract` as the normal desktop user. Read `.setup-state/source/docs/module-map.md`, `implementation-inventory.md`, `design-refinement.md`, `testing.md` and `safety-and-rollback.md`. The old root `docs/` inventory is a feature specification, never evidence that the target is already configured.

Inspect OS/version, architecture, actual desktop/session, package availability, active compositor, shell version/schema/API, display scaling, free disk/RAM, input/audio/network support and installed apps. Do not log raw personal identifiers, saved networks, private device names, passwords or audio. Recheck current official upstream documentation; the source is a reference implementation, not proof that every API exists on this target.

Ask one preference question: “What would you like to name your assistant? Choose a short single-word name such as Nova/Friday, or no assistant.” Save once with `python3 setup.py configure --assistant-name NAME` or `--no-assistant`, then run `python3 setup.py stage`. Do not silently enable wake listening or web search; those remain off until the user opts in. Internal file/application IDs may retain `friday`; the visible assistant name and local wake phrase must use the selected name. Verify custom-name parsing before enabling.

## 2. Plan one coordinated run

Produce one concise package/download/file/service plan with estimated optional model sizes, compatibility exceptions and rollback. Continue automatically within the user's requested scope.

Prefer signed distribution packages. Verify actual repository package names/versions rather than executing a static cross-distro package list. Batch dependency installation into one transaction per package manager. Use native declarative configuration on NixOS/immutable systems. If a new external source or security-sensitive driver is needed, review it and obtain the relevant decision; do not silently add a repository, disable signatures or run `curl | sh`.

Keep the existing desktop/display manager/session as a recovery route. Add Niri as a separate session when missing; do not replace the default session or force a live compositor switch. Detect legacy Noctalia v4 versus native v5 and adapt: v5 TOML/plugin source must not be copied into a v4 configuration. Probe Niri blur/geometry extensions; fall back to supported effects when absent.

Package installation/system changes may need native OS authentication. Group reviewed privileged work into one narrow operation where possible; use normal OS policy. Never ask for, capture, store, paste or reuse a password; never change sudoers or suppress authentication. Do not repeatedly ask permission for ordinary reversible work already authorized. Never promise the OS will show exactly one authentication prompt.

## 3. Deploy real modules

Use `.setup-state/staged/` and the deployment map as source. Inspect and adapt it; do not substitute screenshots, fake status or placeholder buttons for working behavior.

Before editing explicit user destinations, run `python3 setup.py checkpoint PATH...`. Keep package/service enablement and privileged-file recovery records separately. Install user files with correct modes; validate each module before enabling it. Run `seal CHECKPOINT_ID` once the intended file changes are applied. `restore CHECKPOINT_ID` refuses to erase later user edits; handle conflicts with a diff instead.

Implement all supported inventory items:

- Niri-native input/workspaces/window rules/shortcuts, natural scrolling and supported gestures. Retain the user's existing bindings when possible and resolve conflicts explicitly.
- Compact 32-logical-pixel bar, consistent readable type/spacing/clock, generated 3× original icons, active-app menus only while an app is focused. Use app-exported menus or reviewed shortcut mappings; unavailable commands must be disabled.
- Real NetworkManager/BlueZ/PipeWire controls, true connecting/connected/error states, no duplicate operations, battery view and matching native settings entry points. Keep current network/audio routes while testing.
- Glass Dock with smart hide, restore behavior and persistent size control. No full-screen blur shield. Alt+Space launcher and useful application/file/action/clipboard paths; remove duplicate launcher affordances.
- Working close/hide-restore/maximize shell controls. Keep the supported Niri approach where a toolkit cannot expose native per-window traffic lights; never promise uniform third-party window decorations.
- Shared `desktop_design.py` materials/theme/accessibility module for custom panels. Preserve press/disabled/focus states; transient panels coordinate dismissal. Recording remains independent so opening another popup cannot stop it.
- Neutral notification/OSD/authentication surfaces where supported. Reduce motion/transparency across compositor, shell, GTK and lock rendering. Verify effective settings through Noctalia IPC because saved UI settings override TOML fragments.
- Screenshot/window/region capture and recording toolbar, clean window framing and consent portal. Test synthetic framing and mocked dispatch before a user-approved real recording.
- Password-backed session lock using compositor session-lock protocol, native PAM and a recovery route. Test visual preview before lock integration. Preserve first typed character, password fallback, and fail-closed behavior. Use local/user-provided or appropriately licensed media and a generated fallback; never bundle another user's profile image. Fingerprint drivers/PAM are a separate explicit review; no experimental driver is included or automatically enabled.
- Stock file preview first, narrowly scoped hold-preview only when reliable; Android pairing only with user trust and scoped firewall rules.
- Optional named assistant: compact continuous glow, shortcut, optional opt-in local wake, English recognition, automatic speech endpoint, follow-up, uncertainty/repeat prompt, goodbye/Escape/outside/lock cancellation, text always and voice only on a verified available external output. No unrelated listening/output-scan notifications.
- Assistant actions use typed allowlists and installed-app discovery: real system volume/brightness, bounded app/URL launch with duplicate suppression, media, time/battery, windows, capture, safe notes/timers/search. Never pass speech/model text to shell/eval or arbitrary generated commands. Confirm destructive/power/messaging/financial actions. Offline commands remain useful without a local AI model or internet.

Resolve native runtime libraries, VAD/ASR/TTS resources and optional AI from official sources for this architecture. Record source/license/checksum/size in the local report. Never transplant the reference laptop's binaries, ABI-specific libraries or CPU-specific backend. Benchmark latency and memory before enabling background services; smaller devices may use a lower-resource profile.

## 4. Verify and finish

Validate Niri and Noctalia configs, QML visual preview, Python syntax and user services. Run bundled action-disabled assistant tests against rendered source, using mocks for volume/network/app launch. Verify real stateful controls without disconnecting the current session. Visually check light/dark/high-contrast backgrounds, output scale, focus, icons, outside click and Escape. Check empty-desktop title clearing and Dock hide/reveal/restore.

Ask for required physical actions only when ready: mic speech, external headphones, pairing, actual screenshot-recording consent, or lock/authentication. Never equate synthetic ASR or a successful config parse with a physical test. Never lock/log out/suspend or change PAM/driver settings without the agreed recovery route.

Use `.setup-state/RESULTS.md` to record each feature as verified (with evidence), configured but unverified, unsupported (reason/native alternative), or blocked (specific requirement). Record source/API versions, file/checkpoint paths, service enablement and rollback. Keep personal data and runtime artifacts out of Git.

Complete every safe supported module in this run. If a dependency/hardware/session boundary requires user action, finish independent work first and state the exact action needed. Do not say “everything is done” when source was only staged, tests were mocked, or a required feature is still incomplete. Report the actual implemented behavior and remaining platform boundaries clearly.
