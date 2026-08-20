# Public test images

Original synthetic image fixtures for open-source regression tests. These files
are test data, not product photography and not production assets.

## VTO input validation

`vto/input-validation/v1/` covers the input shapes that exposed conflicting
virtual try-on admission classifiers:

- valid adult garments with dense graphics, text-like print, multiple models,
  close crops, and utility construction;
- obvious non-target ecommerce products;
- deliberately ambiguous animal and doll apparel kept as challenge cases.

The fixtures were created with OpenAI's built-in image generation tool on
2026-08-20. No third-party source image was supplied. See [PROMPTS.md](PROMPTS.md)
for the generation prompt set.

Consumers must pin raw URLs to an immutable Git commit, for example:

```text
https://raw.githubusercontent.com/carpedm20/images/<commit>/vto/input-validation/v1/<file>.png
```

Do not use a branch URL in a regression manifest. The consuming repository
must also verify each downloaded file's SHA-256 digest.

## License

The fixtures are released under [CC0 1.0 Universal](LICENSE).
