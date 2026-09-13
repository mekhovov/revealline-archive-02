# RevealLine archive 02 — unpublished infrastructure candidate

This repository candidate publishes exactly **v0.27.0 and v0.28.0** at their new canonical sites. It preserves their historical behavior and original bytes, including defects. It does not repair those games, move saved data, change archive-01, or alter the current game's files.

- Intended repository: `mekhovov/revealline-archive-02`.
- Canonical root: `https://mekhovov.github.io/revealline-archive-02/`.
- Original source repository and ZIP downloads: `mekhovov/revealline`.
- Frozen builder: `b37f5fc3ecbeedc06fa1fd13229a9b1864cb05af` (v0.32.0).
- Archive payload: **418 files / 136,528,268 bytes**, below the unchanged 800,000,000-byte archive limit.
- Exactly three hidden files: `.nojekyll` and each selected site's `.xonix-build.json`.
- Expected inventory SHA256: `809673090505e3689579a0218e88681268570e0be05e26c03fd54450c253eac7`.

The allocation copy appends archive-02 to the existing archive-01 map. It deliberately lives in this infrastructure repository; the original repository's primary `scripts/pages-archives.json` remains unchanged until canonical archive deployment and acceptance have passed. The source-code checkout stays pinned to b37. Infrastructure approval and its eventual Git commit are separate from frozen release identities.

## Reproduction and byte authority

`source-lock.json` pins all 39 release records/tag objects, the reviewed builder contracts, the allocation, and the expected inventory. `expected-inventory.json` was derived independently from the accepted exact v0.32 Pages inventory's two retained frozen sites and explicit metadata templates. It was not made by hashing an arbitrary output directory. The two historical source commits are:

- v0.27.0: `562fc867c7aa64ffe727f55a561a6531371f0f47`.
- v0.28.0: `f79f3c56b0a3cd88ca4e98b7f31689398523da74`.

`tools/prepare.py` requires Node 22.22.2, verifies the source tree and exact tag set, and creates a new output directory. It streams each selected Git archive, checks its frozen TAR hash and embedded commit, extracts only bounded ordinary members, compares source blobs with Git, then invokes that edition's archived CLI. The resulting manifest, ZIP/CRC/member bodies, sidecar, ownership marker, complete loose inventory and original record must agree with frozen pins and the accepted inventory. Local preparation additionally compared every loose byte and TAR with the preserved original release directories before and after.

Only the selected two sites are rebuilt. Exact pinned metadata for all editions supplies the original builder's full routing history; every metadata record exists before assembly, avoiding its missing-release fallback. The cache-only project reads Git objects/refs but owns its package/metadata/site/output paths. The unchanged source `buildPages` implementation assembles the archive. It never calls `releaseSnapshot`, creates a milestone, updates source, or changes tags during the observed preparation. Source/ref changes cause refusal, with failed output retained.

All ordinary site files except `distribution.zip` are copied to the canonical artifact. ZIP checksums remain byte-identical. ZIP payloads and source TARs remain at the original GitHub Releases; generated indexes keep their original download URLs. The output contains both exact release records plus five generated root/index/routing/marker files. Root aliases and retirement workers belong to the later main-site allocation, not this canonical archive artifact.

The workflow checks out this repository and the exact original source separately, uses the same preparation code, then performs another full inventory/hidden-file check immediately before the v5 Pages upload. There is no automatic dependency installation: the archived build tools use their committed modules and Node's standard library. A changed semantic release tag set or pinned metadata requires a reviewed infrastructure update; the workflow cannot silently broaden its allocation.

## Local command

From a directory containing this repository as `archive` and the original source checkout as `source`:

```sh
python3 archive/tools/prepare.py --git-root source --builder-source source --out /absolute/fresh/archive02
python3 archive/tools/verify-artifact.py /absolute/fresh/archive02/artifact
```

Use Node 22.22.2 on PATH. The optional `--frozen-root /absolute/original/releases` adds full comparison against already frozen local artifacts. Output must not exist. A successful preparation is local byte evidence only, not a network, browser, workflow or deployment claim.

## Publication order

1. Review the concrete repository tree, source lock, local rebuild report and expected inventory before creating/pushing this repository. Configure Pages to use GitHub Actions; preserve all previous repositories, releases and refs.
2. Deploy this canonical archive with the pinned v5 upload action and `include-hidden-files: true`. Record the infrastructure commit, run and successful deployment. Do not modify archive-01 or main routing.
3. Audit every one of the 418 public files against the pinned inventory with a fixed archive-02 prefix, no redirects, bounded concurrency and retained failures. No path, hidden file or failed hash may be excluded for a passing report.
4. Validate actual canonical gameplay, secondary entry points, query/fragment routes, same-version saved data/writer behavior and new-scope offline preparation separately. Existing old tabs must not be forced across or have caches/profile/media deleted. Same-origin paths retain data ownership; the new scope still needs its own offline cache.
5. Only after canonical byte and browser acceptance, the source owner may merge the appended main allocation and deploy the 18 new historical HTML bridges/two normal-lifecycle retirement workers. Old non-HTML asset paths will be absent. Audit the complete main artifact and migration separately before calling reallocation delivered.

At the current v0.32 baseline, this allocation projects main to 744,315,686 bytes, leaving 205,684,314 under its unchanged 950,000,000-byte limit. A hypothetical additional 148 MB site would leave about 57.7 MB, but a real next release changes root and metadata too. Its actual complete build remains mandatory. No budgets increase and no installed packs or player data are evicted.
