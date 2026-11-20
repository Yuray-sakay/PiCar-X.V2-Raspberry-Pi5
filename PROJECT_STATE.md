# PiCar-X V4 + Raspberry Pi 5 — Project State

**Document version:** 0.1 (initial record; pending user review)  
**Recorded:** 2026-11-20  
**Governing Project Instructions:** v3.0  
**Related Master Roadmap:** v2.0 (established 2026-11-19)  
**Language:** English only  
**Purpose:** Record the most recent *evidenced* project state, not aspirations or assumed progress.

> **Status rule:** APPROVED = decision made; PLANNED = future work; IN PROGRESS = work confirmed underway; COMPLETED = delivered; VERIFIED = relevant test/evidence passed; BLOCKED = cannot proceed safely. **UNKNOWN / UNVERIFIED** means evidence is absent, not necessarily that the action never occurred.

## 1. Current position

- **Current workstreams:** M0 — inventory, hardware revisions, BOM and safety; M1 — independent GitHub repository and engineering documentation. They may proceed in parallel.
- **Milestone completion:** Neither M0 nor M1 has a verified Exit Gate. No subsequent milestone has a verified Exit Gate.
- **Physical robot status:** Assembly, wiring, power-on, calibration and functional tests are **UNVERIFIED**.
- **Software status:** Raspberry Pi OS installation, SSH, Python dependencies, running code and device control are **UNVERIFIED**.
- **Repository status:** GitHub-first workflow is **APPROVED**; creation or synchronization of our dedicated repository is **UNVERIFIED**. This file has **not** been committed or uploaded to GitHub.
- **Tested baseline / release:** None evidenced. Proposed tags in `ROADMAP.md` are not existing Releases.

## 2. Confirmed and approved baseline

| Item | Evidenced status | Qualification |
|---|---|---|
| SunFounder PiCar-X **V4 kit** | **CONFIRMED** | User identified the received kit; photo/manual available. This does **not** identify the Robot HAT PCB revision. |
| Raspberry Pi 5 | **APPROVED / PLANNED** | Exact model, RAM, possession and accessories **UNVERIFIED**. |
| Development workstation and tools | **APPROVED** | Linux Mint, VS Code, Git/GitHub; Python primary; Pi OS 64-bit planned. |
| Language | **APPROVED** | English for all project conversations, documents, code, interfaces, commands and logs. |
| GitHub engineering journal | **APPROVED** | Independent repo; BOM, wiring, photos, decisions, tests, Issues, PRs and Releases. |
| Telemetry | **APPROVED** | Power/battery where measurable, CPU/RAM, temperature, sensors, control/network latency, failures. |
| Safety Controller | **APPROVED** | Command validation, motion limits, watchdog/timeouts, fail-safe behavior; physical drive-power isolation assessed separately. |
| Hybrid AI | **APPROVED** | Pi 5 retains local motion execution and safety; external PC/LLM/VLM/API supplies untrusted requests. |
| Pico 2 W expansion | **APPROVED FUTURE DIRECTION** | Implement only after electrical/software compatibility and demonstrated benefit over Robot HAT. |

**Approval does not confirm acquisition, installation, implementation, successful testing, or permission to purchase.**

## 3. Hardware and software evidence gaps (M0 / M2 prerequisites)

| Required finding | Current status | Evidence needed |
|---|---|---|
| Robot HAT PCB revision and ZERO control | **VERIFIED** | SunFounder Robot HAT V4, PCB `01902V44`, ZERO button `SW3`; confirmed from user photograph IMG_4292.jpeg on 2026-11-20 |
| Battery pack and voltage | **PARTIALLY VERIFIED** | SunFounder SFB20002S3C, 7.4 V, 2000 mAh, 14.8 Wh; measured +7.88 V DC using UNI-T UT139C on 2026-11-20. Photos: IMG_4294.jpeg, IMG_4295.jpeg. Connector compatibility user-confirmed; electrical load test not performed. |
| Kit inventory and component condition | **UNVERIFIED** | Part-by-part count against the supplied manual |
| Battery chemistry, label, polarity, charging/protection | **UNVERIFIED** | Photos, manufacturer-specific documentation, safe measurements as appropriate |
| Actual power topology and Pi 5 power headroom | **UNVERIFIED — SAFETY GATE** | Board/input identification, verified specifications, measurements before load |
| Raspberry Pi 5 RAM, microSD, cooling and power accessories | **UNVERIFIED** | Model/label inventory |
| Operating system, network, Python and libraries | **UNVERIFIED** | Local system information and repeatable installation/test output |
| Assembly, servo zeroing, motor/sensor tests | **UNVERIFIED — SAFETY GATE** | Dated step records, photographs, calibration/test evidence |

**Known documentation conflict, not a verified device defect:** The general PiCar-X page mentions a 7–12 V input, whereas Robot HAT V4 documentation specifies 6.0–8.4 V battery input. The applicable connector and exact board must be identified before wiring. The documented Robot HAT 5 V/3 A output and Pi 5 full-power 5 A recommendation also require a verified power budget; neither alone establishes that this specific configuration is safe under load.

**Servo dependency:** Use the revision-correct zeroing procedure **before attaching servo horns**. Any temporary powered zeroing setup requires electrical verification first. Initial motor tests require the wheels raised and a reliable means to stop the drive.

## 4. Milestone register

| Stage | Current evidence-based status | Next verification / Exit Gate |
|---|---|---|
| **M0** Inventory, revisions, BOM, safety | **PLANNED; completion UNVERIFIED** | Identify exact critical revisions; resolve electrical hazards before power |
| **M1** GitHub repository / documentation | **PLANNED; completion UNVERIFIED** | Verify repo, protected local work, first reviewed commit and M0 Issue |
| **M2** Pi 5 OS, SSH, Python | **UNVERIFIED** | Boot, SSH, imports, dependency versions and recovery procedure |
| **M3** Mechanical assembly | **UNVERIFIED** | Correct assembly and servo zeroing; no binding/pinched cables |
| **M4** Wiring, power and calibration | **UNVERIFIED** | Inspected wiring and controlled actuator/calibration tests |
| **M5** First functional baseline | **UNVERIFIED** | Repeatable drive, stop, camera and sensor tests; then proposed `v0.1.0` |
| **M6** Modular Python control | **UNVERIFIED** | Working API and tests |
| **M7** Telemetry and Safety Controller | **UNVERIFIED** | Verified fault handling and measured telemetry; then proposed `v0.2.0` |
| **M8** Sensors/basic autonomy | **UNVERIFIED** | Reproducible safe autonomous scenarios |
| **M9** Computer vision/local AI | **UNVERIFIED** | Measured perception pipeline; then proposed `v0.3.0` after M8 + M9 |
| **M10** Hybrid AI | **UNVERIFIED** | Bounded, safe remote-AI integration including disconnect tests |
| **M11** Pico 2 W/embedded | **UNVERIFIED** | Demonstrated compatibility and measurable added value |
| **M12** ROS 2/advanced robotics | **UNVERIFIED** | Specific reproducible research demonstration |
| **M13+** Open R&D | **FUTURE / OPEN-ENDED** | Per-experiment evidence, review and adoption decision |

The detailed scope, ordering and Exit Gates remain in `ROADMAP.md` **v2.0**. Do not silently renumber milestones or promote status without evidence.

## 5. Sources and version relationships

**Project records presently available in conversation/project context:**
- `ROADMAP.md` — Master Roadmap v2.0; governing instructions v3.0.
- `PROJECT_INSTRUCTIONS_v3.0.txt` — governing instruction text; the live Project Settings application is not verified from this file alone.
- `PiCar-X.v2 Assemble.pdf` — five-page illustrated assembly sheet provided with the project; revision applicability must be matched to the physical kit.
- `IMG_4291.jpeg` — project photograph; does not by itself certify board revision or wiring.
- Historical instruction/roadmap drafts and quality audit — reference for changes, not authoritative current state.

**Official references:** [PiCar-X documentation](https://docs.sunfounder.com/projects/picar-x-v20/en/latest/) · [PiCar-X source](https://github.com/sunfounder/picar-x) · [Robot HAT documentation](https://docs.sunfounder.com/projects/robot-hat-v4/en/latest/) · [Robot HAT source](https://github.com/sunfounder/robot-hat) · [Vilib](https://github.com/sunfounder/vilib).

**Version rule:** Document versions are independent; state the applicable governing instructions and roadmap explicitly. An updated copy in ChatGPT Project Sources is not automatically synchronized with GitHub.

## 6. Immediate next actions (not yet verified complete)

1. **M0:** Identify Robot HAT revision and ZERO control from clear photos; compare the supplied booklet with actual hardware.
2. **M0:** Count inventory and confirm the Pi 5, power pack/battery, charging, microSD and cooling; populate `hardware/BOM.csv`.
3. **M0:** Resolve actual electrical interfaces and Pi 5 power budget **before any power-on**.
4. **M1:** Check whether a local/remote repo already exists and protect all local/untracked/unpublished work before creating, cloning or syncing anything.
5. **M1:** Add approved English `README.md`, `ROADMAP.md` and this `PROJECT_STATE.md` to the dedicated repo; review the initial commit and open an M0 Issue.
6. **M2 → M3:** Prepare revision-compatible software and complete verified servo zeroing before attaching servo horns.

## 7. Update and evidence protocol

On each significant change, record **date, milestone, action, evidence source/path or commit SHA, status, test ID/outcome (PASS / FAIL / BLOCKED / NOT RUN), outstanding risk, next action**. A claimed test without observed evidence is **not VERIFIED**. Before Git sync/reset/merge, inspect branch, worktree, untracked files, local commits and divergence; destructive changes require explicit approval. Never commit secrets.

**Next update trigger:** First verified Robot HAT identification or verified creation of our independent GitHub repository — whichever occurs first.

---

**Initial change report (2026-11-20)**  
**CHANGED:** Created an initial project-status record; no existing roadmap or decision changed.  
**PRESERVED:** Project Instructions v3.0, Roadmap v2.0, M0–M13+, all five approved pillars and the English-only policy.  
**VERIFIED:** Source files and prior approvals were reviewed for this record; no device or GitHub operations were performed.  
**UNVERIFIED:** Hardware configuration, power integrity, installations, GitHub state, test outcomes and releases.
