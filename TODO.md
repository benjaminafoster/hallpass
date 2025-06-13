# HallPass
A Python-based CLI password manager

### State of the Project
- 06/13/2025: need to modify the way that the REPL is handling command execution to pass a configuration mechanism (that contains logged in user name) alongside the command and arguments list.

### To-do


### In-progress
- [ ] Implement configuration passthrough to commands for the sake of tracking current user
- [ ] Connect login command throughout workflow
    - [X] Create database interaction
    - [X] Connect login module to database command
    - [ ] Connect login REPL command to login module equivalent (awaiting config task; see above)

### Completed
- [X] Select user login hashing algorithm
- [X] Create REPL structure and execution
- [X] Implement command registration for use in REPL
- [X] Connect register command through workflow