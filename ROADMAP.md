# PiCar-X V4 + Raspberry Pi 5 — Master Roadmap

**Version:** 2.0 · **Established:** 2026-11-19 · **Last reviewed:** 2026-11-19  
**Project:** Open-ended robotics and Physical AI engineering · **Language:** English for all communication, code, devices, and project artifacts  
**Status:** M0 hardware audit and M1 GitHub foundation are the starting workstreams; completion is **not verified**.

> **Purpose:** Build → Understand → Test → Measure → Document → Improve → Repeat.  
> This roadmap records **approved plans**, not completed work. GitHub will hold the lasting engineering history; measured evidence and explicit confirmation establish what has actually been done.

## 1. Established baseline and decision status

| Item | Status | Evidence boundary |
|---|---|---|
| SunFounder **PiCar-X V4** | **CONFIRMED** | Kit version reported and shown by the user; individual PCB revision not yet identified. |
| **Raspberry Pi 5** as main computer | **APPROVED / PLANNED** | Specific board, RAM, accessories, and acquisition not verified. |
| Development workflow | **APPROVED** | Linux Mint workstation, VS Code, Git/GitHub; Raspberry Pi OS **64-bit** for the Pi 5; Python primary. |
| Detailed inventory and physical build | **NOT VERIFIED** | Battery, charger, power supply, Robot HAT revision, microSD, cooler, assembly, wiring, and installation require inspection. |
| Five engineering pillars (D1–D5) | **APPROVED** | Implementation, testing, and purchases require separate evidence/authorization. |

**Approved pillars — none may be silently removed or downgraded:**

- **D1 — GitHub engineering journal:** independent repository; versioned BOM, assembly photos, wiring, code, configurations, Architecture Decision Records (ADRs), experiments, benchmarks, Issues, Pull Requests, tags, and Releases.
- **D2 — Telemetry:** battery/power where instrumented, CPU/RAM, temperatures, sensor readings, control-response times, network latency, and errors; include units, methods, and test conditions.
- **D3 — Safety Controller:** command validation, speed/motion limits, watchdog, timeouts, emergency-stop behavior, and safe response to lost communications; software stopping is **not** independent physical drive-power isolation.
- **D4 — Hybrid AI:** Pi 5 retains local control and safety enforcement; PC/CUDA, local LLM/VLM servers, or API services may handle heavier computation. External AI cannot bypass the safety layer.
- **D5 — Pico 2 W:** future supplementary embedded controller for sensors/timing only if it offers a demonstrated benefit over the Robot HAT's existing MCU and passes compatibility checks.

## 2. Engineering rules and evidence

1. **Evidence before action.** Match each instruction to the exact physical revision, included assembly booklet, applicable manufacturer documentation, and measured behavior. Label **FACT / MEASUREMENT / INDICATION / ESTIMATE / HYPOTHESIS / PROPOSAL**. Resolve disagreements rather than guessing.
2. **Controlled steps.** For hands-on work use **STEP → REQUIRED → PROCEDURE (diagram/orientation) → CHECK → RISK → STATUS → NEXT**. Stop for confirmation before the next dependent or risky action. Diagnose **symptom → cause/test → correction → retest**.
3. **Status and communication.** Use **APPROVED / PLANNED / IN PROGRESS / COMPLETED / VERIFIED / BLOCKED**. Neither a simulation nor an attempted test proves physical operation. Keep failed and unrun results visible. All project communication and artifacts are in **English**. Label commands **PC / Raspberry Pi / Pico**, including purpose, risk and result check.
4. **Safety before motion.** Identify supply and battery interfaces; verify battery chemistry, voltage, polarity, charging/protection behavior, current limits, cooling, and Pi 5 power headroom. Zero every servo **before fixing its horn**; perform first motor tests with wheels safely raised. Establish immediate stopping before driving and tested loss-of-control behavior before autonomy.
5. **Reproducibility.** Record OS, hardware/firmware revisions, library versions, upstream branch **and commit SHA**, configurations, setup, conditions, measurements, and rollback. Validate current releases and dependencies immediately before installation; avoid assuming `latest` is reproducible.
6. **Approval and reversibility.** No unapproved purchases, major rebuilds, or destructive Git actions. Protect secrets. Separate stable baselines from prototypes. Review relevant files and source history before editing them. Product proposals should show image, exact name, price, trustworthy EU seller, link and compatibility evidence.
7. **Continuous improvement.** Each proposed upgrade must state **problem → expected value → prerequisites/cost → risks/trade-offs → measurable validation**. The project has no artificial final milestone.

### Open, safety-critical verification items

- **Robot HAT identification:** PiCar-X **V4 kit** does not establish the exact Robot HAT PCB revision. Verify markings and the presence/absence of a **ZERO** control before choosing the zeroing procedure.
- **Power-source ambiguity:** The general PiCar-X hardware page describes a **7–12 V** input, whereas the Robot HAT V4 electrical specification lists **6.0–8.4 V battery input**. These may refer to different interfaces/revisions. **Do not treat either as permission to wire an unidentified board.** Determine the actual connector, board and permitted supply first. [General page](https://docs.sunfounder.com/projects/picar-x-v20/en/latest/hardware/cpn_robot_hat.html) · [V4 specifications](https://docs.sunfounder.com/projects/robot-hat-v4/en/latest/robot_hat_v4/features.html).
- **Pi 5 power budget:** Robot HAT V4 documentation lists **5 V/3 A output**; Raspberry Pi recommends a **5 A-capable supply** for full Pi 5 peripheral power headroom. A 3 A supply can boot a Pi 5 with reduced USB power limits; neither specification alone proves the assembled robot's suitability. Record actual topology, limits, startup/transient behavior, and measurements before added load. [Robot HAT](https://docs.sunfounder.com/projects/robot-hat-v4/en/latest/robot_hat_v4/features.html) · [Raspberry Pi power](https://www.raspberrypi.com/documentation/computers/raspberry-pi.html#power-supply).
- **Servo sequencing:** SunFounder instructs users to prioritize the **printed booklet** if it differs from the assembly video, and to zero servos before installing their arms. Some revisions use an onboard ZERO button; others use a software procedure. **M2 must provide the required software before M3 reaches servo-horn installation**, and any temporary powered setup must first pass M0 electrical checks. [Assembly](https://docs.sunfounder.com/projects/picar-x-v20/en/latest/assemble.html) · [Servo zeroing](https://docs.sunfounder.com/projects/picar-x-v20/en/latest/python/py_servo_adjust.html).

## 3. Development milestones and Exit Gates

**Sequence:** M0 and M1 may start together. Other stages are dependency-driven, not calendar-driven. A milestone is **VERIFIED** only with dated results, not just a checked box. Proposed Release tags become real only after the associated Exit Gate passes.

### M0 — Inventory, revisions, BOM and safety audit | START HERE
**Work:** Photograph kit, PCB markings, booklet, connectors and layout; count parts and inspect damage. Inventory Pi 5/RAM, battery/charger, microSD, cooling, tools and power. Build a BOM with **In kit / Must have / Nice to have / Future upgrades**, listing quantity, exact model/revision, status, cost/currency, supplier, availability, compatibility evidence and notes. Resolve power and servo-zeroing prerequisites.

**Deliverables:** `hardware/BOM.csv`, `hardware/photos/`, `docs/power-review.md`, initial open-issues register.  
**Exit Gate:** Parts and exact critical revisions identified; no unresolved electrical hazard before any powered test.

### M1 — GitHub foundation and engineering journal | PARALLEL WITH M0
**Work:** Set up an independent repo (proposed name: `PiCar-X-Raspberry-Pi5`) and VS Code workflow. Add `README.md`, this `ROADMAP.md`, `CHANGELOG.md`, `.gitignore`, BOM and reference links. Establish Issues, milestone labels, branch/PR conventions and decision documentation; preserve SunFounder as a **separate upstream**, not a replacement for local work.

**Deliverables:** Accessible repository, initial reviewed commit, M0 Issue, milestone backlog, basic directory structure.  
**Exit Gate:** Clone and history verified; local work protected; secrets excluded; documentation tracked. **Do not mark complete merely because the file exists here.**

### M2 — Raspberry Pi 5, Linux and Python foundation
**Work:** Confirm board and power; install Raspberry Pi OS **64-bit**, SSH/network access, backups, Python, and revision-compatible SunFounder `robot-hat`, `picar-x` and `vilib` dependencies. Capture installed versions/SHAs and repeatable setup steps. Keep PC (Linux Mint) commands distinct from Pi commands.

**Deliverables:** `docs/setup.md`, `configs/software-versions.md`, backup/recovery procedure, boot/network/import test evidence.  
**Exit Gate:** Reliable boot, SSH access, verified library imports, documented recovery path; prerequisites for servo zeroing ready.

### M3 — Mechanical assembly and servo alignment
**Work:** Follow the **matching printed assembly booklet**, step by step, with verified images, hardware orientation, screws and cable routing. Before fixing each servo horn: confirm M0 electrical check and required M2 setup; execute the **revision-specific zeroing** procedure. Check steering, camera pan/tilt travel and wheel clearance without forcing mechanisms.

**Deliverables:** `hardware/assembly/` photos, step checklist, alignment records and exceptions.  
**Exit Gate:** Mechanism correctly aligned, servos zeroed, no interference or pinched wiring.

### M4 — Wiring, power, calibration and controlled actuator tests
**Work:** Verify actual pinout/connectors, battery polarity/charging, regulated rails, and Pi 5 load capacity. Connect motors, servos, ultrasonic and grayscale sensors per identified revision; calibrate steering, pan/tilt, motor direction and grayscale values. Test actuator motion **with wheels lifted** and a reliable stop method available.

**Deliverables:** `hardware/wiring/`, electrical inspection and measurements, `docs/calibration.md`, test logs.  
**Exit Gate:** Correct connections, saved calibration, repeatable controlled motor/servo checks, no unexplained power faults.

### M5 — First functional robot and tested baseline
**Work:** Controlled startup/shutdown, forward/reverse/steering/stop, camera, ultrasonic and grayscale checks; capture expected versus observed behavior. Resolve blocking failures and document hardware/software baseline.

**Deliverables:** Functional checklist, logs and known-good configuration.  
**Exit Gate:** All essential tests pass repeatedly under specified conditions. **Planned release:** `v0.1.0` — Functional Robot Baseline.

### M6 — Modular Python control
**Work:** Build our own drive, sensor and control APIs with error handling, manual control and optional remote UI. Keep actuator access behind validated interfaces; add unit tests with mocks and integration tests without replacing physical validation.

**Deliverables:** `software/control/`, `software/sensors/`, `tests/`, `docs/software-architecture.md`.  
**Exit Gate:** Documented control API, repeatable manual operation and hardware-independent automated tests.

### M7 — Telemetry and Safety Controller
**Work:** Instrument available power/battery telemetry, CPU/RAM, temperatures, sensor/control timing, network and errors; implement command validation, motion limits, heartbeat/watchdog, timeouts, stop modes and safe recovery. Distinguish **normal stop**, **software emergency stop** and **physical drive-power isolation**; design and evaluate a physical solution separately.

**Deliverables:** `software/telemetry/`, `software/safety/`, measured dashboards/logs and fault-injection report.  
**Exit Gate:** Tested safe state on invalid/expired commands and lost link, with documented limitations. **Planned release:** `v0.2.0` — Safe & Observable Robot.

### M8 — Sensors and basic autonomy
**Work:** Line following, obstacle detection/avoidance, calibrated thresholds and rule-based motion; manual override and safety enforcement remain active. Test in a controlled environment and record success/failure and response times.

**Deliverables:** `software/autonomy/`, scenario descriptions, result tables and logs.  
**Exit Gate:** Reproducible operation with documented failure cases and safe recovery.

### M9 — Computer vision and local AI
**Work:** Camera streaming, OpenCV/`vilib`, detection/tracking and feasible local inference; benchmark frame rate, latency, CPU/RAM, thermals and energy. Evaluate AI acceleration only after mechanical, electrical, PCIe and software checks.

**Deliverables:** `software/vision/`, comparable benchmarks and local-versus-offload findings.  
**Exit Gate:** Stable measured perception pipeline for specified tasks. **Planned release after M8+M9:** `v0.3.0` — Perception & Basic Autonomy.

### M10 — Hybrid AI: Pi 5 + PC / LLM / VLM / API
**Work:** Define authenticated, bounded network/API messages. The Pi 5 accepts **requests**, validates them through local safety, and executes motion locally. Compare on-Pi inference with PC/CUDA, local LLM/VLM and optional cloud/API offload using task success, latency, bandwidth, reliability and cost. Test disconnection and stale responses.

**Deliverables:** `software/ai/`, interface contract, experiment logs and comparative benchmarks.  
**Exit Gate:** Useful AI-assisted task demonstrated; remote failure cannot bypass local safety or cause uncontrolled motion.

### M11 — Pico 2 W and embedded integration
**Work:** Prototype optional real-time/sensor functions using MicroPython or C/C++; verify interface voltage levels, power, GPIO/UART/I²C/USB and communication failure behavior. Benchmark against the Robot HAT's onboard MCU before keeping additional hardware.

**Deliverables:** Embedded prototype, protocol specification and benefit/cost comparison.  
**Exit Gate:** Verified compatibility and measurable value; otherwise keep existing architecture.

### M12 — Advanced robotics and ROS 2
**Work:** Evaluate ROS 2, odometry/encoders, sensor fusion, localization, mapping/SLAM, navigation and simulation. Identify missing sensors and mechanical/compute constraints rather than claiming the base kit supports every feature.

**Deliverables:** Research ADRs, prototype packages/simulations, test reports and compatibility decisions.  
**Exit Gate:** Reproducible, measurable demonstration against an explicit objective.

### M13+ — Ongoing R&D, upgrades and new platforms
**Scope:** Digital twins, multi-agent robotics, advanced vision-language behavior, learning from feedback, custom sensors/PCBs, distributed compute, alternative chassis and other research directions. Preserve stable releases while testing experiments on isolated branches and controlled hardware.

**Deliverables:** Approved experiment proposals, prototypes, evidence, ADRs and lessons learned.  
**Exit Gate:** No project endpoint; each experiment has its own acceptance test, cost/risk review and decision to adopt, iterate or reject.

## 4. GitHub repository and delivery workflow

**Proposed layout** (create as work begins; directories are not evidence of implementation):

```text
PiCar-X-Raspberry-Pi5/
├── README.md                  # Project overview and actual status
├── ROADMAP.md                 # This milestone plan
├── CHANGELOG.md               # Verified changes/releases
├── .gitignore
├── hardware/
│   ├── BOM.csv
│   ├── assembly/
│   ├── wiring/
│   └── photos/
├── docs/
│   ├── setup.md
│   ├── calibration.md
│   ├── power-review.md
│   ├── architecture/
│   ├── decisions/
│   ├── experiments/
│   └── measurements/
├── software/
│   ├── control/
│   ├── sensors/
│   ├── safety/
│   ├── telemetry/
│   ├── autonomy/
│   ├── vision/
│   └── ai/
├── tests/
├── configs/
└── scripts/
```

- **Normal workflow:** Issue → branch → implementation → test → Pull Request → review → merge → tag/Release **when justified**. Example branches: `docs/m0-inventory`, `feat/telemetry`, `fix/servo-calibration`.
- **Protect local work:** Before pull, sync, merge, rebase or reset inspect current branch, dirty/untracked files, unpublished commits and remote divergence. Never assume remote supersedes local. Obtain explicit approval before hard reset, force push, overwrite, deletion or history rewrite; back up and preview first.
- **Reproducibility:** Record upstream URL, branch, exact SHA and verification date; preserve configuration and test evidence. Do not commit passwords, Wi-Fi secrets, tokens, API keys, private photos or uncontrolled large media.
- **Release discipline:** Promote a baseline only after Exit Gate evidence. Use Issues for defects, ADRs for consequential design choices, `CHANGELOG.md` for accepted changes and a documented rollback to the previous working tag.
- **Suggested labels:** `hardware`, `software`, `safety`, `docs`, `experiment`, `bug`, `blocked`, plus milestone tags `M0`–`M13+` as appropriate.

## 5. Verification, measurements and change control

Every meaningful milestone/experiment records **test ID + date; objective; hardware PCB revision; OS, firmware and exact code SHA; wiring/setup; procedure; expected and observed results with units; conditions; PASS / FAIL / BLOCKED / NOT RUN; logs/photos; issue and corrective action**. Prefer baseline-versus-change comparisons under comparable conditions. A feature is **VERIFIED** only after its relevant test passes.

**Document workflow:** Draft → audit against requirements and prior decisions → Improvement Gate (accept/reject proposed changes) → final → applicable Markdown/link/render checks → change report. Record **CHANGED / PRESERVED / VERIFIED / UNVERIFIED**. Never silently modify approved decisions, dates, metrics, stage names, or test status.

**Candidate improvements — PROPOSED, not yet approved:** hardware-independent CI (lint and unit tests); `docs/verification-matrix.md` linking Exit Gates to evidence; a revision-specific measured power budget; an ADR index; controlled hardware-in-the-loop testing; simulation/digital twin. **Conditional hardware backlog:** USB microphone/voice, M.2 HAT+ and NVMe, AI HAT+ 2, upgraded sensing, and offboard CUDA hardware; each requires a mechanical/electrical/software/thermal/power and cost-benefit review. Evaluate separately rather than treating these as installed features or authorized purchases.

## 6. Immediate next actions

- [ ] **M0 / Step 1:** Capture readable photos of the Robot HAT board and marking, the supplied assembly booklet, and all kit parts; identify critical revisions and battery/power interfaces before any electrical step.
- [ ] **M1 / Step 1:** Create the dedicated GitHub repository only after checking for existing local or remote project content that must be preserved; add `README.md` and this English `ROADMAP.md`, then review the initial commit.
- [ ] Create an Issue: **`M0 — Identify PiCar-X V4 PCB revision, verify BOM and power safety`**; log findings and blockers.
- [ ] Prepare the confirmed Pi 5 hardware and software prerequisites for servo zeroing; do **not** mechanically attach servo horns before the revision-correct zeroing gate.
- [ ] Advance to powered tests and final assembly only when the required safety checks have evidence.

## 7. Primary technical sources

1. [SunFounder PiCar-X documentation](https://docs.sunfounder.com/projects/picar-x-v20/en/latest/) · [Assembly](https://docs.sunfounder.com/projects/picar-x-v20/en/latest/assemble.html) · [Servo zeroing](https://docs.sunfounder.com/projects/picar-x-v20/en/latest/python/py_servo_adjust.html) · [Calibration](https://docs.sunfounder.com/projects/picar-x-v20/en/latest/python/python_calibrate.html) · [Install modules](https://docs.sunfounder.com/projects/picar-x-v20/en/latest/python/install_all_modules.html)
2. [SunFounder PiCar-X source](https://github.com/sunfounder/picar-x) · [Robot HAT source](https://github.com/sunfounder/robot-hat) · [`vilib`](https://github.com/sunfounder/vilib)
3. [Robot HAT series docs](https://docs.sunfounder.com/projects/robot-hat-v4/en/latest/) · [V4 electrical specifications](https://docs.sunfounder.com/projects/robot-hat-v4/en/latest/robot_hat_v4/features.html)
4. [Raspberry Pi hardware and power documentation](https://www.raspberrypi.com/documentation/computers/raspberry-pi.html#power-supply)

**Source policy:** The user's actual PCB/manual revision and safe measurements determine applicability. Documentation may describe other versions; verify current code/dependencies before use. This file does not attest to successful device tests, a configured repository or completed purchases.
