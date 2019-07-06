workflow "smoke tests" {
  resolves = "test"
}

action "teardown previous" {
  uses = "docker://docker/compose:1.24.0"
  args = "down"
}

action "build" {
  needs = "teardown previous"
  uses = "docker://docker/compose:1.24.0"
  args = ["build", "backend"]
}

action "start" {
  needs = "build"
  uses = "docker://docker/compose:1.24.0"
  args = ["up", "-d", "backend"]
}

action "initialize db" {
  needs = "start"
  uses = "docker://docker/compose:1.24.0"
  args = ["exec", "-T", "backend", "python", "manage.py", "makemigrations"]
}

action "migrate" {
  needs = "initialize db"
  uses = "docker://docker/compose:1.24.0"
  args = ["exec", "-T", "backend", "python", "manage.py", "migrate"]
}

action "fixtures" {
  needs = "migrate"
  uses = "docker://docker/compose:1.24.0"
  args = ["exec", "-T", "backend", "python", "manage.py", "loaddata", "users.json", "projects.json", "executions.json"]
}

action "test" {
  needs = "fixtures"
  uses = "docker://docker/compose:1.24.0"
  args = ["exec", "-T", "backend", "python", "manage.py", "test"]
}
