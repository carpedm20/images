# VTO Avatar-Proportion Regression Assets

This directory contains one synthetic, public regression pair for generated
person-geometry preservation:

- `avatar-front.png` is the existing synthetic front-avatar fixture copied
  byte-for-byte from `vto/input-validation/v1`;
- `modeled-coat.png` is an original synthetic ecommerce image generated for
  this suite on 2026-08-21. Its full-height garment model, long coat, oversized
  collar, and wide trousers reproduce the conditioning geometry that exposed
  Grok head/body-ratio drift without using a production user's image or a
  third-party product photograph.

The full generation prompt is recorded in the repository root
[`PROMPTS.md`](../../../PROMPTS.md). `manifest.json` locks every file's bytes,
SHA-256, decoded geometry, mode, and format. Consumers must pin the repository
by immutable commit SHA and verify this contract after download.
