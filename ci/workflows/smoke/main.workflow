workflow "smoke tests" {
  resolves = "run unit tests"
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
  args = ["up", "backend"]
}

action "initialize db" {
  needs = "start"
  uses = "docker://docker/compose:1.24.0"
  args = [
      "exec", "--rm", "backend", "python", "manage.py", "loaddata"
    ]
}

action "test" {
  needs = "initialize db"
  uses = "sh"
  args = "ls"
}
