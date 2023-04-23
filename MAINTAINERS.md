<!--
-----------------------------------------------------------------------------------------
Copyright (c) 2023 Voxelcraft

For copying notice, see https://github.com/CMihai99/voxelcraft/blob/main/COPYING.
For licenses we use, see https://github.com/CMihai99/voxelcraft/tree/main/LICENSES.
-----------------------------------------------------------------------------------------
-->

# List of Maintainers

Please try to follow the guidelines and entry descriptions below.
This will make things easier on the maintainers. Not all of these
guidelines matter for every trivial patch so apply some common sense.

## Tips for patch submitters

1. Always test your changes, however small, on at least 1 person, preferably more.

2. Make sure your changes compile correctly in multiple configurations.
   In particular, check that changes are both responsive and/or functional.

3. When you are happy with a change, make it generally available
   for testing and await feedback.

4. Make a patch available to the relevant maintainer in the list.
   Use `diff -u` to make the patch easy to merge. Be prepared to get
   your changes sent back with seemingly silly requests about formatting
   and naming. These aren't as silly as they seem. One job the maintainers
   (and especially Mihai) do is keep things looking the same. Sometimes
   this means that the clever hack in your code to get around a problem
   needs to become a generalized feature ready for next time.

   Try to include any credit lines you want added with the patch.
   It avoids people being missed off by mistake and makes it easier
   to know who wants adding and who doesn't.

   Document known bugs. If it doesn't work for everything or it does
   something very odd once a month, document it.

   Remember that submissions must be made under the terms of the Voxelcraft
   certificate of contribution and should include a `Signed-off-by:` line.
   The current version of the "Developer's Certificate of Origin" (DCO)
   is listed in [SubmittingPatches.md](https://github.com/CMihai99/voxelcraft/blob/main/docs/how-to/maintaining/SubmittingPatches.md).

5. Always add 2 trailing spaces at the end of each attribute (e.g. `EVERYTHING  `, `S: Maintained  `).

## Section entry descriptions and preferred order

- R: Designated Reviewer: FullName <address@domain>

- S: Status, one of the following:

  - Supported: Someone is actually paid to look after this.

  - Maintained: Someone actually looks after it.

  - Odd Fixes: It has a maintainer but they don't have time to do much
    other than throw the odd patch in.

  - Orphan: No current maintainer (but maybe you could take the role
    as you write your new code).

  - Obsolete: Old code. Something tagged obsolete generally means it has
    been replaced by a better system/version and you should be using that.

- W: Web-page with status/info

- F: Files and directories wildcard patterns.
  
  A trailing slash includes all files and subdirectory files, for example:

  - F: `drivers/net/` are all files in and below `drivers/net`.

  - F: `drivers/net/*` are all files in `drivers/net`, but not below.

  - F: `*/net/*` are all files in `"any top level directory"/net`.

  One pattern per line. Multiple `F:` lines are acceptable.

- X: Excluded files and directories that are NOT maintained,
  same rules as `F: Files`. Exclusions are tested before file matches.
  Can be useful for excluding a specific subdirectory, for example:

  - F: `net/`

  - X: `net/ipv6/`

  matches all files in and below `net`, excluding `net/ipv6/`.

## Maintainers list

When reading this list, please look for the most precise areas first.
When adding to this list, please keep the entries in alphabetical order.

EVERYTHING  
R: Mihai Calinescu <mihaimihaia431@gmail.com>  
S: Maintained  
W: <https://github.com/CMihai99/voxelcraft>  
F: *  
