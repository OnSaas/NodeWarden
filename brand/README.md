# Brand logo

This fork uses the logotype from upstream PR #195 (by entsalze) instead of
the default shield artwork.

- `source/nodewarden-logo-pr195.png` — the original high-resolution
  artwork from PR #195 (badge + wordmark, transparent background).
- `assets/` — the finished logo files, mirroring their paths in the repo.
  The SVGs are vector traces of the artwork (the wordmark is a black
  silhouette, used as a CSS mask exactly like the original wordmark);
  the PNG/ICO set is rendered from the original raster badge on the
  project's `#eef4ff` background. File names, canvas sizes and usages
  are identical to the default artwork, so no code changes are needed.

## Re-applying the logo

An upstream sync overwrites the logo files with the default artwork.
Restore the brand version either way:

- GitHub: run the **Apply brand logo** workflow (Actions tab →
  "Apply brand logo" → Run workflow). It also runs automatically on
  pushes that touch a logo file.
- Locally: `python3 scripts/apply-brand-logo.py`
  (`--check` only reports differences.)

To change the logo in the future, replace the files under `assets/`
(and the source artwork), then run the workflow.
