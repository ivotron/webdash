workflow "smoke tests" {
  resolves = "test"
}

action "print things" {
  uses = "sh"
  args = "ls"
}

action "teardown previous" {
  uses = "docker://docker/compose:1.24.0"
  args = "down"
  needs = "print things"
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
  args = ["exec", "-it", "backend", "python", "manage.py", "loaddata"]
}

action "test" {
  needs = "initialize db"
  uses = "sh"
  args = "ls"
}
