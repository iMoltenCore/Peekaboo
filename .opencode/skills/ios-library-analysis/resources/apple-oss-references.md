# Apple OSS References

Use the Apple OSS distributions to map library symbols to source.

## Recommended workflow
- Check out `apple-oss-distributions` locally.
- Find the relevant component (e.g., `Libsystem`, `dyld`, `CFNetwork`).
- Match release tags to the target iOS version.
- Use symbol or string searches to locate implementations.

## Tips
- Prefer exact tags for version accuracy.
- Record commit/tag references in notes for traceability.
