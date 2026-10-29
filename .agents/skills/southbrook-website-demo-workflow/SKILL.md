---
name: southbrook-website-demo-workflow
description: Resume Southbrook's website audit-to-demo project one page at a time, producing annotated before/proposed visuals before implementation, matching the established demo theme, verifying real links and saving published checkpoints. Use for scheduled or manual continuation, not authorization to edit the official church website or ministry forms.
---

# Southbrook Website Demo Workflow

## Start and recover
Read current main in dmcchesney96/Church-Admin-work: AGENTS.md; workflows/southbrook-website-demo/START-HERE.md; WORKFLOW.md; AUDIT-MAP.md; scope.json; and the existing Southbrook brand profile.
Read the current Sites skill. Open the existing project appgprj_6ae10560a9dc8191be01ad534c0d49dd through native source credentials/helper. Preserve its identity and audience; never create a replacement.
Read canonical runtime docs/workflow/STATE.json and RESUME.md in that Site source. Read the full audit PDF/text under docs/audit/, source captures, docs/visual-reference.md, docs/mockups/ and existing HTML/CSS/JS. Old captures are dated evidence; refresh each page before implementation.
If GitHub is unavailable use the copies in docs/workflow/ and report that limitation. If the checkout is absent recover it through Sites, not a new starter. If state is absent reconcile state-seed.json against actual source and deployments before proceeding.
Reconcile saved versions and live deployments; a local file or saved version is not proof of publication.

## Execute, one complete page at a time
1. Bootstrap /review/ as a staff review gallery if absent. Backfill original boards and real current/after screenshots for the eight existing pages; flag gaps. Preserve their latest visual design.
2. Select the highest-priority unfinished page. Record it and its exact next action in STATE.json/RESUME.md.
3. Refresh public source content and real links. Save source URL/date, a genuine current-site screenshot and relevant audit findings.
4. Generate a proposed visual with imagegen, using the existing demo and reference boards as the style baseline. Produce a numbered comparison board with genuine current screenshot, proposed design, arrows and short audit-backed reasons. Never label a generated reconstruction as a current screenshot. Use precise code-native annotation layout when appropriate.
5. Save/push the mockup and board BEFORE coding. Add them to the review gallery; publish a gallery-only checkpoint when practical so partial work is visible.
6. Implement semantic working HTML/CSS/JS to match that visual; do not substitute a bitmap with hotspots. Reuse shared components/theme. Replace in-demo navigation with the new internal route where appropriate. Preserve real external forms, registration, giving and media links.
7. Check desktop and phone-width layouts, actual links/anchors, relevant interactions, accessible names, focus/keyboard and contrast. Capture the actual result; compare visually and fix substantial drift. Never report unperformed checks as passed. Do not submit real forms.
8. Push/package the exact source through the Sites helper, save the version and deploy the existing demo. Retain exact returned commit/version/deployment/URL; poll only nonterminal deployments.
9. Persist artifacts, tests, actual publication proof and next action. Push post-deployment state. If interrupted between deployment and state write, reconcile native versions/deployments instead of blindly redeploying.
10. Validate state with scripts/validate_checkpoint.py. Update /review/ with current/proposed/after visuals, reasons, demo links, progress and unresolved questions. Only then select another page.
Continue the loop through audit core pages and then remaining public sitemap pages while resources permit. Do not stop at an arbitrary one-page limit.

## Checkpoint and delivery
Save after source capture, mockup, implementation and publication, not just run end. Keep the last working deployment accessible.
Keep public review assets in dist/review/assets/<page-id>/ and private/internal audit material outside dist. Store requested exported photo packs/PDFs in Library.
Begin each run with usable progress links. Maintain the gallery after each page; hard quota exhaustion may prevent a final message.
At completion or graceful stop return demo and gallery links, completed/pending/blocked pages, exact resume instructions, and the saved photo pack/compiled visual booklet when available. Do not claim an export exists until saved.
Do not promise unlimited credits, guaranteed quota detection, endless runtime, automatic restarts or a final notification after a hard cutoff. Do not schedule more runs without user instruction.

## Content and visual constraints
Preserve exactly in the homepage hero: “We exist to glorify God by making disciples who make a big deal of Jesus where we live, learn, work, and play.”
Match the latest demo: cyan #00AEEF, navy #002A40, white, Metropolis web typography, real logos, compact centered headers, original texture/photo backgrounds, wave dividers, rounded pale-blue panels, pill buttons, consistent icons and white footer. This explicit website design direction overrides older printed-document preferences for square cards/Arial.
Preserve Abide/Gather/Connect/Multiply, the four group environments and doctrinal substance. No pre-visit contact invitation on New Here.
Never invent ministry programs, dates, enrollment, capacity, staff ownership, response windows, care guarantees, testimonials or operating processes. Put uncertainties in staff review rather than public promises.
Use existing public Southbrook imagery. Do not expose internal Drive research, private records or raw form submissions on the public demo.
Retain real Typeforms, giving and registrations; do not submit prayers, enrollments, donations or personal data.
Do not modify southbrookchurch.com, its CMS, DNS, live forms, analytics or database. This task authorizes the separate demo/workflow only.
Do not fabricate current screenshots, performance scores, compliance certification, successful form submissions or staff approval.
