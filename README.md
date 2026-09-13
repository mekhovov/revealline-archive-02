# RevealLine archive 02

This additive expansion adds **v0.32.0**. All canonical game, manifest, checksum, ownership and release-record bytes for the seven existing editions remain identical: v0.27.0, v0.28.0, v0.29.0, v0.29.1, v0.29.2, v0.30.0 and v0.31.0. Only the archive indexes and routing metadata change for those editions. Historical gameplay is preserved.

The current game is at [RevealLine](https://mekhovov.github.io/revealline/); old editions remain independently playable at [archive 02](https://mekhovov.github.io/revealline-archive-02/releases/). ZIPs remain on their original GitHub Releases.

## Exact authority and capacity

- Original accepted infrastructure: `3af0d6b38060b7495085e0d4309370973e8ecb56`, whose tree equals reviewed `ca5c0e75bcad5766e449e20cba9b3d1a36803fdf`.
- Current builder source: published v0.35 source `9747b3e86e43d4e66b1c7b4aea6e05b220bf3ad5`; all 42 semantic release records, tag objects and peeled commits are locked.
- Canonical artifact: **1,777 files / 731,963,905 bytes**, leaving **68,036,095 bytes** below the unchanged **800,000,000-byte** archive budget.
- Nine hidden files: `.nojekyll` and eight `.xonix-build.json` ownership files.
- Expected inventory SHA256: `f56f2f1188a2bf62a2ec2d239236f7541c10f06c89297c0effd75f6f04a508ed`.
- Source lock SHA256: `b69e05f36dab6f631e55f62eca46d81928262a2bf6eb8d913678b86d48bed0b4`.
- Added edition source: `b37f5fc3ecbeedc06fa1fd13229a9b1864cb05af`, unchanged v0.32.0.

The independent inventory is derived before assembly. Accepted archive inventory `c61abc7495a060696ec0bac719537cc750cdcdca14b7667bc67fc519b9124b64` supplies all seven old canonical site/record bodies. Accepted v0.35 main inventory `22f22b40196f1715bbe27de4165cbbdb45025af4c33eb01371583bc206a4ec0b` supplies v0.32 and the exact 42 release records. Fixed independent templates derive only five root, index, routing and marker files; the root HTML and marker remain identical. Exactly 1,535 existing bodies remain unchanged. Routing describes the full 42-edition history; the archive index lists eight editions.

## Reproduction and local verification

`tools/prepare.py` requires Node 22.22.2, exact builder Git blobs, unchanged release tags, the pinned allocation/inventory and a fresh output directory. The hosted default is unchanged: freshly archive every selected commit, check the frozen TAR digest and embedded commit, safely extract and validate every Git blob, then run each edition's own archived CLI. All eight manifest and ZIP hashes, full ZIP CRC/member bodies, loose bytes, checksums, ownership markers and finite public inventory must match before assembly.

Local `--reuse-frozen-sites` requires `--frozen-root`. To avoid redundant large TAR/source copies, it compares each existing frozen TAR byte for byte with a fresh `git archive` stream, checks its frozen SHA256, and reads every bounded TAR member against its exact Git blob and executable mode without extracting another source tree. It then copies the existing site and performs all the same manifest, ZIP, loose-byte and canonical-inventory checks. This mode verifies frozen outputs; it does not claim a new CLI build. It refuses links, special files, extra empty directories, changed source bodies and missing/extra inventory. Tags and supplied frozen trees must remain identical after completion. Failed attempts are retained.

All 42 locked records are staged before the actual `buildPages` helper runs, preventing missing-record fallback. Only eight selected sites are materialized. Every original ordinary site file except the redundant `distribution.zip` is published; its exact checksum remains present. This preparation creates no game release or tag.

```sh
python3 archive/tools/test-verify.py
python3 archive/tools/prepare.py --git-root source --builder-source source --out /absolute/new/archive02
python3 archive/tools/verify-artifact.py /absolute/new/archive02/artifact
```

For local reuse, append `--frozen-root /absolute/original/releases --reuse-frozen-sites`. The hosted workflow retains the default archived CLI builds, pinned upload-pages-artifact v5 SHA, explicit hidden-file inclusion and existing checkout/setup/deploy action major tags. The source checkout uses the exact full SHA above.

## Acceptance and publication boundaries

1. Review this infrastructure delta, independent inventory and complete verified local artifact.
2. Deliver the additive archive change through a reviewed commit/PR and successful workflow/deployment. Preserve the existing archive ancestry and game tags.
3. Audit all 1,777 canonical public paths, including nine hidden files, and reconcile all 1,535 preserved old bodies. Retain failed requests. Root separately checks the new canonical browser entry, query/fragment, ordinary saved context and actual offline outcome.
4. Only after that explicit canonical acceptance may a successor main release adopt this allocation. Main bridge/retirement-worker regressions, normal cached-worker migration and full exact final artifact admission remain mandatory. Do not force service-worker takeover or clear caches/player data.

The prior archive expansion was accepted for **online preservation**, including v0.31 ordinary win and retained Collection. Root reported v0.31 offline preparation timed out and a legacy music v1-versus-existing-v3 warning; tabs were subsequently closed externally. Public offline/cold operation was not qualified and the cause was not established. Those historical limitations remain; this expansion does not change archived code or imply repaired offline behavior. Local byte checks alone do not qualify public browser, offline, physical controller or phone behavior.

The accepted v0.35 main site is 780,633,089 bytes. This allocation is projected to free 148,029,207 main-site bytes while preserving old originals. The unchanged main cap is 950,000,000 bytes; the actual successor artifact must be measured. Installed-pack, managed-media and offline caps remain unchanged. No main allocation or public game integration is authorized by this preparation alone.
