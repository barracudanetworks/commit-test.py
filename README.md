# gitutils

These utilities are intended to make managing sign-offs on long branches easier.
This is helpful when using revisable feature branches as a series of patches
under review before merging it into a more stable branch.

They are executable, so one can add this directory to the PATH.

Run with `--help` for details on command line arguments.

### Requirements

* Python 3
* [pygit2](http://www.pygit2.org/)

`sign-off` also requires:

* sed
* vim

## commit-test

Check that commits between the current branch and a stable branch have enough
sign-offs. List commits that do not under reviewers who have not already signed.

This can be used in a pre-push hook; see `pre-push`.

Example output:

    Expecting sign-offs from
      Reviewer One <one@example.com> on:
        8191ecc server: fix flux capacitor thermal leak
      1 commits.
      Reviewer Two <two@example.com> on:
        36a86ee doc: fix typo in user guide
        d3cae49 server: initialize buffer before writing to disk
      2 commits.
    3 commits.

## sign-off

Add sign-offs from reviewers to commits by name. This uses rebase, so it
modifies history. Beware the wrath of others if using it on published branches!

    # Rebasing onto upstream branch
    $ sign-off 'Reviewer <review@example.com>'
    # Rebasing onto master
    $ sign-off --upstream master 'Reviewer <review@example.com>'
