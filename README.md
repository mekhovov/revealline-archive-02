# RevealLine archive 02 — proposed expansion

This local infrastructure candidate adds **v0.29.0 and v0.29.1** to the existing archive-02 site. The already published **v0.27.0 and v0.28.0** canonical site files remain byte-identical. Historical behavior, including known defects, remains frozen. Archive-01, the primary allocation, current games, old release downloads, profiles and caches are unchanged by preparation.

- Existing repository: `mekhovov/revealline-archive-02`; this candidate contains no Git repository or remote writes.
- Canonical base: `https://mekhovov.github.io/revealline-archive-02/`.
- Exact builder/source history: `e29f2ac9207b047c07e6b72f94fa24cea9b00e1c` (v0.33.0).
- Forty semantic release records and tag objects are explicitly locked; the complete tag set is compared before and after execution as well.
- Expected artifact: **860 files / 296,702,466 bytes**, below the unchanged **800,000,000-byte** archive cap.
- Exactly five hidden files: `.nojekyll` plus the four selected sites' `.xonix-build.json`.
- Expected inventory SHA256: `c8e3247fa6e93821e87146bf5f3480091714928039a121c5bd516ef575d994a2`.

The allocation copy extends only archive-02's selected list. Its archive-01 object is exactly the committed e29 allocation. The original repository's primary `scripts/pages-archives.json` must remain unchanged until the expanded canonical archive is deployed and accepted. This candidate is preparation evidence, not a claim that v0.33 has completed public delivery or that the archive expansion is published.

## Independent inventory authority

The expected inventory is derived before assembly from two accepted, pinned inventories: the existing archive-02 inventory (`809673090505e3689579a0218e88681268570e0be05e26c03fd54450c253eac7`) supplies all v0.27/v0.28 site and release bytes, and the complete v0.33 main inventory (`477a09f75cfddfd2519c3a4ed67b3a28eac87b8d975beeb8afb1a32a04686f1c`) supplies all v0.29.0/v0.29.1 site and release bytes. Independent fixed templates derive only the five root/index/routing/marker files. No arbitrary output directory is accepted by self-hashing it.

Every current release record is compared to its exact pinned main-inventory bytes and SHA before any index derivation. The record set must exactly match the forty locked semantic tags. Full routing metadata therefore includes the actual forty-edition history, while the archive index lists only its four selected editions.

| Edition | Exact original source |
| --- | --- |
| v0.27.0 | `562fc867c7aa64ffe727f55a561a6531371f0f47` |
| v0.28.0 | `f79f3c56b0a3cd88ca4e98b7f31689398523da74` |
| v0.29.0 | `f40e1d9ecf262ba94915ddc3fc05eda074058b7a` |
| v0.29.1 | `90b974bfd733ccb11d74383e154467bd172b31d0` |

## Local verification and hosted reproduction

`tools/prepare.py` requires Node 22.22.2, an exact builder source tree, immutable tag identities, unchanged allocation and expected inventory, and a fresh output path. Each selected source is freshly archived from its exact Git commit, compared with its frozen TAR SHA and embedded commit, safely extracted and compared to every tracked Git blob.

The default hosted path rebuilds all four selected sites through their own archived CLIs. The explicit local `--reuse-frozen-sites` path instead copies existing frozen sites after verifying their source TAR against the tag. It requires `--frozen-root`; no source game rebuild is claimed for that path. Both paths apply the same complete manifest, ZIP hash/CRC/member bytes, ownership marker, checksum, loose-file and accepted-inventory validation. Reuse rejects special files, symlinks and extra empty directories. Every selected frozen tree and all tags are compared again at completion. Failed output remains intact.

Only the selected sites are materialized. All forty exact release records exist in the isolated project before the unchanged source `buildPages` runs, so its missing-release fallback cannot execute. The project owns its package, metadata and output paths and reads the original repository's Git objects only. It creates no release, tag or commit. ZIP and TAR downloads remain on their original GitHub Releases. Canonical sites contain every ordinary site file except `distribution.zip`, including the unchanged ZIP checksum.

From a directory containing this infrastructure candidate as `archive` and the exact source checkout as `source`, use:

```sh
python3 archive/tools/prepare.py --git-root source --builder-source source --out /absolute/fresh/archive02
python3 archive/tools/verify-artifact.py /absolute/fresh/archive02/artifact
```

For already verified local frozen sites, add both `--frozen-root /absolute/original/releases --reuse-frozen-sites`. Put Node 22.22.2 on PATH. The hosted workflow deliberately uses the default archived-CLI rebuild, since a source checkout does not contain ignored local frozen outputs. It checks all bytes and the finite hidden set immediately before the pinned v5 Pages upload. Existing major-tag checkout/setup/deploy actions are retained; this does not claim every action definition is immutable.

## Required publication order

1. Review this exact repository tree, source lock, independent inventory, local report and preservation evidence. Preparation authorizes no remote write.
2. After separate publication authorization, update the existing archive-02 infrastructure repository and deploy the expanded canonical artifact. Preserve all prior repositories and release refs. Root/index/routing metadata may change; existing canonical v0.27/v0.28 site bytes must not.
3. Audit all **860 public files**, five hidden paths included, with exact hashes/MIME, a fixed archive-02 prefix, no redirects, bounded concurrency and retained failures. Then test canonical v0.29.0/v0.29.1 entry, secondary pages, query/fragment, same-origin saves/writers and new-scope offline preparation separately.
4. Qualify normal cached-worker migration before changing main. Do not force activation, call `skipWaiting`/`clients.claim`, clear caches or delete player data. Running old games remain on their old worker until its ordinary lifecycle permits retirement.
5. Only after canonical acceptance, integrate the allocation into the upcoming source release. Main will replace the newly archived sites with **20 HTML forwarders and two retirement workers**, retain original release/manifest/checksum metadata and remove their old non-HTML asset bodies. Audit the complete new main artifact, redirects and migration before declaring the reallocation delivered.

At the pinned v0.33 baseline, this allocation projects main to **732,564,215 bytes**, leaving **217,435,785 bytes** below its unchanged 950,000,000-byte limit. A hypothetical additional 148,000,000-byte site leaves **69,435,785 bytes**; real future root replacement and metadata growth are not included in that illustration. The actual upcoming release's complete build remains mandatory. No installed-pack, offline or Pages budget is increased, and no automatic eviction is introduced.
