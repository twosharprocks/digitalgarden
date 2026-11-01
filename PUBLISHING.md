# Website image copies

Publish using `sync.ps1` as before. The image-export step now creates smaller website copies automatically. Vault attachments are read only and are never resized or overwritten.

- Photographs: up to 2,560 pixels on the longest side, JPEG quality 85.
- Maps, surveys, diagrams, PNG graphics and document-like images: up to 6,000 pixels on the longest side, with JPEG quality 90 where applicable.
- Transparency is preserved. GIFs and animations are copied unchanged.
- Existing image filenames and links remain the same. An already smaller original is retained rather than enlarged.
- The ignored `.cache/web-images.json` file caches results and records source/output checksums. Changed originals are processed again on the next publish.

Install `requirements.txt` into the publishing Python environment if needed. On this laptop, the exporter can also use the Pillow installation bundled with Codex.

Website images are reading previews; use the original vault attachment for full-resolution survey details.


# Karst public-copy rules

The website now prepares effective public sources outside the vault before copying posts. Eight reduced cave summaries use the same verified public text as Karst-Database. Other previously reviewed omissions are retained; changed full originals are flagged while their approved copies remain fixed.

The private policy and summary registry are required. Missing or conflicting identities, changed approved summaries, protected file matches and unapproved attachments stop publication. Approved cave document references use their published Karst copies. General manuals and publications use publisher links where a hosted copy is inappropriate.

A local `-SkipPush` run performs the full privacy checks and build without committing or publishing. It can run during a maintenance pause. Scheduled publication respects the maintenance gate, and full generated-output and outgoing-history checks remain mandatory before uploading.
