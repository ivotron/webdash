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
  args = ["up", "backend -d"]
}

action "initialize db" {
  needs = "start"
  uses = "docker://docker/compose:1.24.0"
  args = ["exec", "backend", "python", "manage.py", "loaddata"]
}

action "test" {
  needs = "initialize db"
  uses = "sh"
  args = "ls"
}
