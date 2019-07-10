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

action "sleep" {
  needs = "start"
  uses = "maddox/actions/sleep@master"
  args = "15"
}

action "test" {
  needs = "sleep"
  uses = "docker://docker/compose:1.24.0"
  args = ["exec", "-T", "backend", "python", "manage.py", "test"]
}
