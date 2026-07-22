import json
import shutil
import subprocess
from pathlib import Path

REPO_URL = "{{ cookiecutter.repo_url }}"
ON_GITHUB = "github.com" in REPO_URL
CREATE_REPO = "{{ cookiecutter.create_github_repo }}" == "yes"

RULESET = {
    "name": "require-ci",
    "target": "branch",
    "enforcement": "active",
    "conditions": {"ref_name": {"include": ["~DEFAULT_BRANCH"], "exclude": []}},
    "rules": [
        {
            "type": "required_status_checks",
            "parameters": {
                "strict_required_status_checks_policy": False,
                "required_status_checks": [
                    {"context": "Tests"},
                    {"context": "Code style"},
                    {"context": "packaging"},
                ],
            },
        }
    ],
    "bypass_actors": [
        {"actor_id": 5, "actor_type": "RepositoryRole", "bypass_mode": "always"}
    ],
}

MANUAL_STEPS = """If you use GitHub and want dependency updates to be merged automatically
once CI passes:

 1. Create and push the repository
 2. Enable "Allow auto-merge" and rebase merges in the repository settings
 3. Under Settings / Rules / Rulesets, add a ruleset for ``main`` that
    requires the checks for "Tests", "Code style" and "packaging" to pass
    (and add a bypass for admins so that you can still push directly, if
    you want to)"""


def setup_github_repo():
    slug = REPO_URL.split("github.com/", 1)[1].strip("/")
    if not shutil.which("gh"):
        print(
            "The GitHub CLI (gh) was not found, so the repository was not created."
        )
        print(MANUAL_STEPS)
        return
    try:
        subprocess.run(["gh", "repo", "create", slug, "--public"], check=True)
        subprocess.run(
            [
                "gh",
                "api",
                "--method",
                "PATCH",
                f"repos/{slug}",
                "-F",
                "allow_auto_merge=true",
                "-F",
                "allow_rebase_merge=true",
            ],
            check=True,
            capture_output=True,
        )
        subprocess.run(
            ["gh", "api", "--method", "POST", f"repos/{slug}/rulesets", "--input", "-"],
            input=json.dumps(RULESET).encode(),
            check=True,
            capture_output=True,
        )
    except subprocess.CalledProcessError as e:
        if e.stderr:
            print(e.stderr.decode())
        print("Setting up the GitHub repository failed. To finish up manually:")
        print(MANUAL_STEPS)
        return
    if not Path(".git").exists():
        subprocess.run(["git", "init", "--initial-branch=main"], check=False)
    subprocess.run(
        ["git", "remote", "add", "origin", f"git@github.com:{slug}.git"], check=False
    )
    print(
        f"The repository at https://github.com/{slug} was created. In order to "
        "support automatic merges of dependency updates, auto-merge was enabled. "
        "Nothing has been pushed yet."
    )


if not ON_GITHUB:
    shutil.rmtree(Path(".github"))

subprocess.run(["uv", "lock"], check=False)
subprocess.run(["just", "fmt"], check=False)

if ON_GITHUB:
    if CREATE_REPO:
        setup_github_repo()
    else:
        print(MANUAL_STEPS)
