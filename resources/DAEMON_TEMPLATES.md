# Daemon Interaction Templates

## File as a Daemon
- **Poll**: `view_file` to get current state.
- **Update**: `replace_file_content` to adjust state.
- **Validation**: `run_command` (linters, tests) to verify.

## Service as a Daemon
- **Poll**: `curl` or `npm status` via `run_command`.
- **Logic**: Process JSON response to update the `Ratings` stage.
