# El Niño V2 — quarterback

Goal: publish a **three-slide iPhone Safari preview** using the owner's original uploaded illustrations and explanations, then obtain owner feedback before building slides 4–18.

## Branch roles
- `el-nino-v2/quarterback`: coordinate integration, ensure only original illustrations are used, review and publish preview.
- `el-nino-v2/runner-content`: preserve original slide images and explanatory material, slides 1–3 only.
- `el-nino-v2/runner-preview`: implement minimal mobile viewer and a direct Safari preview, no generic substitutes.

## Non-negotiable lessons
- Show a usable preview after the first three slides.
- No generic replacements, invented explanations, or premature 18-slide build.
- No HTML download requirement or second device for the owner.
- Reuse existing orange DEV Pages hosting; preserve V1 and V2 production.
- Minimal smoke checks; do not bypass required release protections.

## Release gate
A live iPhone preview must actually contain all three original slide images and explanations. Confirm the public URL before reporting publication. Never claim branch creation alone means worker execution or publication.

## Current blocker
The original 18-slide package is available in conversation artifacts but the GitHub connector cannot read local binary files. Do not publish the old generic module. Find a supported transfer route before deployment.
