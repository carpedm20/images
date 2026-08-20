# Public test images

Original synthetic image fixtures for open-source regression tests. These files
are test data, not product photography and not production assets.

## VTO input validation

`vto/input-validation/v1/` is a branch-oriented virtual try-on fixture suite.
It contains 24 self-contained scenario folders: eight policy families at
easy, medium, and hard difficulty. Each folder has its own generated
`case.json` and all images needed by that scenario, including multi-garment
flows.

The families cover:

- category admission and non-target scope boundaries;
- front/side subjects and zero/one/multiple-person evidence;
- BiRefNet, SAM3, unknown-route, prepared reuse, and fetch fallback;
- separates, seven-slot accessory stacks, upper-body conflict/layering, and
  one-piece mode transitions;
- explicit and promoted outfit images; and
- rigid, textile, wrong-wearer, wrong-scale, and missing-state failures.

The source scenario matrix is
[`scenarios.json`](vto/input-validation/v1/scenarios.json). The generated
[`manifest.json`](vto/input-validation/v1/manifest.json) adds SHA-256, byte,
dimension, format, mode, and alpha contracts for every image. Regenerate and
verify it with:

```bash
uv run --with pillow python scripts/build_vto_input_validation_manifest.py
uv run --with pillow python scripts/build_vto_input_validation_manifest.py --check
```

The fixtures were created with OpenAI's built-in image generation tool on
2026-08-20. No third-party source image was supplied. See [PROMPTS.md](PROMPTS.md)
for the generation prompt set.

Consumers must pin raw URLs to an immutable Git commit, for example:

```text
https://raw.githubusercontent.com/carpedm20/images/<commit>/vto/input-validation/v1/<scenario>/<file>.png
```

Do not use a branch URL in a regression manifest. The consuming repository
must also verify each downloaded file's SHA-256 digest.

## License

The fixtures are released under [CC0 1.0 Universal](LICENSE).
