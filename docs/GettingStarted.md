<!--
===-----------------------------------------------------------------------------------===
Copyright (c) 2021 Voxelcraft

For copying notice, see https://github.com/CMihai99/voxelcraft/blob/main/COPYING.
For licenses we use, see https://github.com/CMihai99/voxelcraft/tree/main/LICENSES.
===-----------------------------------------------------------------------------------===
-->

# Getting Started with Development

So you want to be a Voxelcraft developer? Welcome! While there is a lot to be learned
about Voxelcraft in a technical sense, this document's goal is to teach you everything
you need to know to achieve this by describing the process you need to go through,
and hints on how to work with the community. It will also try to explain some of
the reasons why the community works like it does, and how to setup development.

## Introduction

Voxelcraft is written in Python using the Ursina game engine.
A good understanding of game development using Python and Python
in general is required for development. Experience with Ursina is optional.

Please remember that you are trying to learn how to setup development, as well as
work with the existing development community. Try to learn as much as possible with
the community, and do not expect people to adapt to your way of doing things.

## Software requirements

1.  Operating system: The supported operating systems for developing
    and playing Voxelcraft are currently Windows Vista and newer Windows
    systems, macOS 10.6 (Snow Leopard) and newer macOS systems.

2.  Programming language: Again, Voxelcraft is written in Python using
    the Ursina game engine. Ursina needs Python 3.6 and newer versions.

3.  Disk space: Make sure that you have enough available disk space before
    starting. The source code, including full git history, requires about 6MB.

Beware that using excessively old versions of these requirements can cause indirect
errors that are very difficult to track down, so please, do not assume that you
can just update software when obvious problems arise during build or operation.

## Cloning the project

1.  Create a directory for the whole project:

    ```sh
    mkdir voxelcraft-project
    cd voxelcraft-project
    ```

2.  Clone the sources:

    -   Via SSH (recommended): If you plan on contributing regularly,
        cloning over SSH provides a better experience. After you've
        [uploaded your SSH keys to GitHub](https://help.github.com/articles/adding-a-new-ssh-key-to-your-github-account/):

        ```sh
        git clone git@github.com:CMihai99/voxelcraft.git voxelcraft
        cd voxelcraft
        ```

    -   Via HTTPS: If you want to check out the sources as read-only, or
        are not familiar with setting up SSH, you can use HTTPS instead:

        ```sh
        git clone https://github.com/CMihai99/voxelcraft.git voxelcraft
        cd voxelcraft
        ```

    If you've already forked the project on GitHub at this stage, do not clone your fork to start off.
    We describe [how to setup your fork](#setting-up-your-fork) in a subsection below.

### Troubleshooting cloning issues

-   If `update-checkout` failed, double-check that the absolute path
    to your working directory does not have non-ASCII characters.

-   If `update-checkout` failed and the absolute path to your working directory
    had spaces in it, please [file a bug report](https://github.com/CMihai99/voxelcraft/issues/new?assignees=&labels=bug&template=bug_report.md&title=%5BBug%5D)
    and change the path to work around it.

-   Before running `update-checkout`, double-check that `voxelcraft` is the only
    repository inside the `voxelcraft-project` directory. Otherwise,
    `update-checkout` may not clone the necessary dependencies.

## Installing full sources

When installing full sources, also known as stable releases, put the archive in a
directory where you have permissions and unpack it either manually, or by using
Windows Powershell v5.0+ on both systems (Powershell installation on macOS needed):

```powershell
Expand-Archive -Force v1.x.y.zip; cd v1.x.y/v1.x.y
```

Where `x` and `y` are the version numbers. See the [releases](https://github.com/CMihai99/voxelcraft/releases)
for version numbers.

## Installing dependencies

### Windows

You can install every dependency with just one command by using the requirements.txt file:

-   Via PIP:

    ```sh
    pip install -r requirements.txt
    ```

If the download fails, PIP might not be located on your PATH.
To assure that the download is successful, install the dependencies like this:

```sh
python -m pip install -r requirements.txt
```

## Editing code

Make changes to the code as appropriate. Implement a shiny new feature! Fix a
nasty bug! Update the documentation as you go! The codebase is your playground!

Now that you have made some changes, you will need to rebuild.

### Setting up your fork

If you are building the toolchain for development and
submitting patches, you will need to setup a GitHub fork.

First, fork the `CMihai99/voxelcraft` [repository](https://github.com/CMihai99/voxelcraft.git),
using the "Fork" button in the web UI, near the top-right. This will create a
repository under `username/voxelcraft` with your GitHub username. Next, add it as a remote:

```sh
# Using 'my-remote' as a placeholder name.

# If you used SSH in step 2
git remote add my-remote git@github.com:username/voxelcraft.git

# If you used HTTPS in step 2
git remote add my-remote https://github.com/username/voxelcraft.git
```

Finally, create a new branch.

```sh
# Using 'my-branch' as a placeholder name

git checkout -b my-branch
git push --set-upstream my-remote my-branch
```

## Legal issues

The Voxelcraft source code is released under MIT. The Voxelcraft licensing rules
are described in [LicenseRules.md](https://github.com/CMihai99/voxelcraft/blob/main/docs/references/LicenseRules.md).

## Bug reporting

[ReportingIssues.md](https://github.com/CMihai99/voxelcraft/blob/main/docs/how-to/maintaining/ReportingIssues.md)
describes how to report a possible bug, and specifies what kind of
information is needed by developers to help track down the problem.

## Managing bug reports

One of the best ways to put into practice your skills is by fixing bugs reported
by other people. Not only you will help to make Voxelcraft more stable, but you'll also
improve your skills, and other developers will be aware of your presence. Fixing bugs
is one of the best ways to get merits among other developers, because not many people
like wasting time fixing other people's bugs.

To work on already reported bug reports, check the [bug-labeled issues](https://github.com/CMihai99/voxelcraft/labels/bug).

## Working with the community

When you submit a patch for acceptance, it will be reviewed on its
technical merits and those alone. So, what should you be expecting?

-   Criticism
-   Comments
-   Requests for change
-   Requests for justification
-   Silence

Remember, this is part of getting your patch in. You have to be able
to take criticism and comments about your patches, evaluate them at a technical level
and either rework your patches or provide clear and concise reasoning as to
why those changes should not be made. If there are no responses to your posting,
wait a few days and try again, sometimes things get lost in the huge volume.

What should you not do?

-   Expect your patch to be accepted without question
-   Become defensive
-   Ignore comments
-   Resubmit the patch without making any of the requested changes

In a community that is looking for the best technical solution possible, there
will always be differing opinions on how beneficial a patch is. You have to be
cooperative, and willing to adapt your idea to fit within Voxelcraft. Or at least
be willing to prove your idea is worth it. Remember, being wrong is acceptable as
long as you are willing to work toward a solution that is right.

It is normal that the answers to your first patch might simply be a list of a
dozen things you should correct. This does not imply that your patch will not
be accepted. Simply correct all issues raised against your patch and resend it.

## Differences between our community and corporate structures

The Voxelcraft community works differently than most traditional corporate development
environments. Here are a list of things that you can try to do to avoid problems:

```
Good things to say regarding your proposed changes:

    - "This solves multiple problems."
    - "This deletes 200 lines of code."
    - "Here is a patch that explains what I am trying to describe."
    - "Here is a series of small patches that..."
```

```
Bad things you should avoid saying:

    - "We did it this in some way, so therefore it must be good..."
    - "I've being doing this for 10 years, so..."
    - "Here is my 100 page design document that describes my idea"
    - "I've been working on this for 6 months..."
    - "Here's a 2000 line patch that..."
    - "I rewrote all of the current mess, and here it is..."
    - "I have a deadline, and this patch needs to be applied now."
```

Another way the Voxelcraft community is different than most traditional software
engineering work environments is the faceless nature of interaction. One benefit
of using email as the primary form of communication is the lack of discrimination
based on gender or race. Our work environment is accepting of women and minorities
because all you are is an email address. The international aspect also helps to level
the playing field because you can't guess gender based on a person's name.
A man may be named Andrea and a woman may be named Pat.

The language barrier can cause problems for some people who are not comfortable
with English. A good grasp of the language can be needed so it is recommended
that you check your comments to make sure they make sense in English before sending them.

## Break up your changes

Our community does not gladly accept large chunks of code dropped on it
all at once. The changes need to be properly introduced, discussed, and broken
up into tiny, individual portions. This is almost the exact opposite of what
companies are used to doing. Your proposal should also be introduced very early
in the development process, so that you can receive feedback on what you are doing.
It also lets the community feel that you are working with them, and not simply using
them as a dumping ground for your feature. However, don't send 30 patches
at once, your patch series should be smaller than that almost all of the time.

The reasons for breaking things up are the following:

-   Small patches increase the likelihood that your patches will be applied,
    since they don't take much time or effort to verify for correctness.
    A 5 line patch can be applied by a maintainer with barely a second glance.
    However, a 500 line patch may take hours to review for correctness
    (the time it takes is exponentially proportional to the size of the patch).

    Small patches also make it very easy to debug when something goes wrong.
    It's much easier to back out patches one by one than it is to dissect
    a very large patch after it's been applied (and broken something).

-   It's important not only to send small patches, but also to rewrite
    and simplify (or simply re-order) patches before submitting them.

Think of a teacher grading homework from a math student. The teacher does not
want to see the student's trials and errors before they came up with the solution.
They want to see the cleanest, most elegant answer. A good student knows this,
and would never submit her intermediate work before the final solution.

The same is true for Voxelcraft development. The maintainers and reviewers do not want
to see the thought process behind the solution to the problem one is solving.
They want to see a simple and elegant solution.

It may be challenging to keep the balance between presenting an elegant solution and
working together with the community and discussing your unfinished work. Therefore it
is good to get early in the process to get feedback to improve your work, but also
keep your changes in small chunks that they may get already accepted, even when your
whole task is not ready for inclusion now.

Also, it is not acceptable to send patches for inclusion
that are unfinished and "will be fixed up later."

## Justify your changes

Along with breaking up your patches, it is very important for you to let the
community know why they should add this change. New features must be justified
as being needed and useful.

## Document your changes

When sending in your patches, pay special attention to what you say in the text.
This information will become the changelog information for the patch, and will
be preserved for everyone to see for ever. It should describe the patch completely:

-   why the change is necessary
-   the overall design approach in the patch
-   implementation details
-   testing results

## If anything goes wrong

-   If you have problems that seem to be due to bugs, please check the maintainers
    to see if there is a particular person associated with the part that you are having
    trouble with. If there isn't anyone listed there, the second best thing to do is
    to report the problem on [GitHub issues](https://github.com/CMihai99/voxelcraft/issues/new/choose).

    -   In all bug-reports, please:
        -   tell which version you are talking about
        -   provide steps on how to reproduce the behavior
        -   apply screenshots (if possible)
        -   specify your setup (use common sense)

        In the `Additional context` section, specify if your problem is new or
        old. If you got any error messages related to your problem, paste them
        onto the `Error message` section.
