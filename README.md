# RevealLine archive 02

This expansion adds **v0.29.2, v0.30.0 and v0.31.0** to the existing archive. All canonical site and release-record bytes for **v0.27.0, v0.28.0, v0.29.0 and v0.29.1** stay identical. Each game retains its historical behavior. The archive index and routing metadata expand to include the added versions.

The current game is at [RevealLine](https://mekhovov.github.io/revealline/). This repository hosts independently playable old editions at [archive 02](https://mekhovov.github.io/revealline-archive-02/releases/). Download ZIPs remain on their original GitHub Releases.

## Exact inputs and capacity

- Builder source: accepted main `f1a5d0cb4b13bc57f65c8892b81b2a405479f1e7`, with v0.34.0 package metadata.
- Forty-one semantic release records, original tag objects and peeled commits are locked in `source-lock.json`.
- Canonical artifact: **1,538 files / 583,885,534 bytes**, within the unchanged **800,000,000-byte** archive budget.
- Eight hidden files: `.nojekyll` and each of seven sites' `.xonix-build.json`.
- Expected inventory SHA256: `c61abc7495a060696ec0bac719537cc750cdcdca14b7667bc67fc519b9124b64`.
- Source lock SHA256: `ac627ca655907fb1c3ce07dfb603c98e7a70dbba3c3ce5c57cd0501bd411b097`.

The 1 GB published-site limit is documented by [GitHub Pages](https://docs.github.com/en/pages/getting-started-with-github-pages/github-pages-limits). The existing, lower project budgets remain unchanged: 800 MB per archive and 950 MB for the main site. Old originals and downloadable distributions are preserved.

## Independent inventory authority

The expected inventory is derived before assembly from two accepted public inventories. The prior archive inventory (`c8e3247fa6e93821e87146bf5f3480091714928039a121c5bd516ef575d994a2`) supplies all existing canonical site/release bytes. The complete v0.34 main inventory (`a053211458d1c85786e533373c5e84395b2bc3459f7f1aad00ede7c13ee284c7`) supplies the three added sites and all forty-one exact release records. Independent fixed templates derive only the five root, index, routing and marker files. The expected data does not come from self-hashing the assembled output.

All records must equal the accepted public bytes and match original semantic tags. Full routing metadata describes the forty-one-edition history, while this archive's index lists only its seven editions.

| Edition | Exact original source |
| --- | --- |
| v0.27.0 | `562fc867c7aa64ffe727f55a561a6531371f0f47` |
| v0.28.0 | `f79f3c56b0a3cd88ca4e98b7f31689398523da74` |
| v0.29.0 | `f40e1d9ecf262ba94915ddc3fc05eda074058b7a` |
| v0.29.1 | `90b974bfd733ccb11d74383e154467bd172b31d0` |
| v0.29.2 | `d611f1429272ce402db6c38dde763bd3e15498cb` |
| v0.30.0 | `da573579fa10f41830e5743b4f9e7e3991e7613a` |
| v0.31.0 | `70c67e172ceb39947b442948add0d745b19f9a29` |

## Reproduction and verification

`tools/prepare.py` requires Node 22.22.2, an exact builder source tree, unchanged release tags, allocation and expected inventory, and a new output directory. It freshly archives each selected Git commit, validates the exact frozen TAR hash and embedded commit, safely extracts it and compares every source file to its Git blob.

The hosted default rebuilds seven sites with their own archived CLIs. Local `--reuse-frozen-sites` instead copies already frozen sites after verifying the exact source TAR. It requires `--frozen-root`; it does not claim a new game build. Both modes validate manifest contents and totals, ZIP hash/CRC/member bytes, ownership markers, checksums, loose files and every accepted canonical inventory entry. Reuse refuses special files, symlinks and extra empty directories. Tags and supplied frozen trees must still match at completion. Failed attempts are preserved.

All forty-one locked records are staged before `buildPages` executes, preventing its missing-release fallback from creating releases. Only seven sites are materialized. The process reads source Git objects, creates no tag or commit, and assembles a private output. Canonical sites contain every ordinary original site file except the duplicated `distribution.zip`; its unchanged checksum remains present.

With infrastructure at `archive` and the exact source checkout at `source`:

```sh
python3 archive/tools/test-verify.py
python3 archive/tools/prepare.py --git-root source --builder-source source --out /absolute/new/archive02
python3 archive/tools/verify-artifact.py /absolute/new/archive02/artifact
```

For local verified frozen outputs, append `--frozen-root /absolute/original/releases --reuse-frozen-sites`. The hosted workflow uses actual archived-CLI rebuilds because checkout does not include ignored frozen outputs. Every artifact byte and the finite hidden set are verified before the pinned v5 Pages upload with hidden files included. Existing checkout/setup/deploy action major tags are retained.

## Publication sequence

1. Review source, inventory authority, preservation checks and complete local artifact.
2. Commit the logical expansion, open and merge a PR, then verify the resulting archive workflow and deployment under the user's standing release authorization. Archive-01 and existing game refs remain intact.
3. Audit all 1,538 canonical public files for exact bodies and MIME, including hidden files, using bounded concurrency and preserving failures. Verify the new canonical entries, secondary pages, query/fragment, same-origin saves and new-scope offline operation through the browser.
4. Only after canonical acceptance, adopt this allocation in the next source release. Main then creates HTML forwarders and retirement workers for the three newly archived editions while retaining their original release/manifest/checksum metadata.
5. Verify the complete new main artifact and normal cached-worker migration. Never force service-worker takeover or clear player caches/data. Running old games retain their ordinary lifecycle.

The accepted v0.34 main artifact is **904,798,002 bytes**, leaving **45,201,998 bytes** below its existing cap. Replacing these three complete old sites with small bridges will recover most of their **287,178,671 bytes**; the exact next main artifact must still be measured before deployment. No installed-pack or offline budget changes, automatic eviction, or game completion claims follow from this infrastructure work.
