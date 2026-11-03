# IAP M8 Runbook — Saved projects fail to display

## Symptom

An operator runs `list` and sees an `Error:` message instead of the saved
projects. The command exits with code 1. The tracker may also fail to create
projects that use the same data file.

## Confirm the cause

1. Open **Command Prompt** in the repository folder. Use the same data path
   and working directory as the failed command. The default is
   `projects.json` in the working directory. Replace that filename in these
   commands if the operator used a different path.
2. Reproduce the symptom with the read-only list command and capture its log.

   ```bat
   python app.py --data-file "projects.json" list 2> "%TEMP%\iap-m8-list.jsonl"
   echo %ERRORLEVEL%
   type "%TEMP%\iap-m8-list.jsonl"
   ```

3. Find the `command_started` and `command_failed` lines with the same
   `operation_id`. Check that `command` is `list` and `data_file` is the
   expected path. An `error_type` of `JSONDecodeError` indicates that Python
   could not parse the file. Confirm the syntax error and its line and column:

   ```bat
   python -m json.tool "projects.json" > NUL
   echo %ERRORLEVEL%
   ```

   This procedure applies if the validator reports a JSON syntax error.
   For another error type or a valid JSON file, keep the trace and ask the
   project maintainer to investigate.

## Recover and verify

1. Pause all `create` commands using this file. Preserve the damaged file
   before attempting recovery.

   ```bat
   set "M8_DAMAGED_COPY=projects.damaged-%RANDOM%-%RANDOM%.json"
   copy /-y "projects.json" "%M8_DAMAGED_COPY%"
   dir "%M8_DAMAGED_COPY%"
   ```

   Continue only after the copy succeeds and the file is listed. Keep this
   copy for investigation and recovery of any newer records.
2. Locate the most recent known-good backup. Check it with the tracker itself
   before restoring it. Use the real backup path in place of the example.

   ```bat
   dir "projects.backup.json"
   python app.py --data-file "projects.backup.json" list
   echo %ERRORLEVEL%
   ```

   Confirm the backup exists, the exit code is 0, and the displayed projects
   match the expected backup contents. If there is no usable backup, leave
   the original and damaged copy in place. Give the maintainer the trace ID,
   data path, and parser error location so they can recover the data.
3. Copy the verified backup over the original. Confirm the overwrite only
   after verifying the damaged copy from step 1.

   ```bat
   copy /-y "projects.backup.json" "projects.json"
   python app.py --data-file "projects.json" list
   echo %ERRORLEVEL%
   ```

4. Check for the expected projects, exit code 0, and a
   `command_succeeded` log with the same operation ID as the new start
   event. Compare the restored records with the operator's expected list
   and report any changes made since the backup. Resume writes once the
   restored contents have been confirmed.
