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

action "migrate db" {
  needs = "start"
  uses = "docker://docker/compose:1.24.0"
  args = ["exec", "-T", "backend", "python", "manage.py", "migrate"]
}

action "initialize db" {
  needs = "migrate db"
  uses = "docker://docker/compose:1.24.0"
  args = ["exec", "-T", "backend", "python", "manage.py", "loaddata", "users.json", "projects.json", "executions.json"]
}

action "test" {
  needs = "initialize db"
  uses = "docker://docker/compose:1.24.0"
  args = ["exec", "-T", "backend", "python", "manage.py", "test"]
}
