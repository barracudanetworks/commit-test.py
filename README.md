# gitutils

These utilities are intended to make managing sign-offs on long branches easier.
They are executable, so one can add this directory to the PATH.

Run with `--help` for details on command line arguments.

### Requirements

* Python 3
* [pygit2](http://www.pygit2.org/)
* sed
* vim

## commit-test

Check that commits between the current branch and a stable branch have enough
commits. List any commits that don't.

This is useful as a pre-push hook; see `pre-push`.

## sign-off

Add sign-offs from reviewers to commits by name. This uses rebase, so it
modifies history. Beware the wrath of others if using it on published branches!

    # Rebasing onto upstream branch
    $ sign-off 'Reviewer <email@address.tld>'
    # Rebasing onto master
    $ sign-off --upstream master 'Reviewer <email@address.tld>'
