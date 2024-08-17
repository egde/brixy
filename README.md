# brixy

brixy is a package with many utilities for developing on Databricks and PySpark.

## Features

### Logging
log the steps of a workflow using the decorator `@log_step`.

```py
from brixy import log_step

@log_step()
def step1():
        return 1+2
```

This will log:
```sh
2024-08-17 20:58:50.f | INFO     | RUNNING   | test_logstep.<locals>.step1                        | 🏃‍♀️ Running step1
2024-08-17 20:58:50.f | INFO     | COMPLETED | test_logstep.<locals>.step1                        | ✅ Completed running step1
```

Logs are indented to show nested calls nicely:
```sh
2024-08-17 20:59:55.f | INFO     | RUNNING   | test_logstep_indenting.<locals>.step_a             | 🏃‍♀️ Running step_a
2024-08-17 20:59:55.f | INFO     | RUNNING   | test_logstep_indenting.<locals>.step1              |     🏃‍♀️ Running step1
2024-08-17 20:59:55.f | INFO     | RUNNING   | step2                                              |         🏃‍♀️ Running step2
2024-08-17 20:59:55.f | INFO     | COMPLETED | step2                                              |         ✅ Completed running step2
2024-08-17 20:59:55.f | INFO     | RUNNING   | step2                                              |         🏃‍♀️ Running step2
2024-08-17 20:59:55.f | INFO     | COMPLETED | step2                                              |         ✅ Completed running step2
2024-08-17 20:59:55.f | INFO     | COMPLETED | test_logstep_indenting.<locals>.step1              |     ✅ Completed running step1
2024-08-17 20:59:55.f | INFO     | RUNNING   | test_logstep_indenting.<locals>.step1              |     🏃‍♀️ Running step1
2024-08-17 20:59:55.f | INFO     | RUNNING   | step2                                              |         🏃‍♀️ Running step2
2024-08-17 20:59:55.f | INFO     | COMPLETED | step2                                              |         ✅ Completed running step2
2024-08-17 20:59:55.f | INFO     | RUNNING   | step2                                              |         🏃‍♀️ Running step2
2024-08-17 20:59:55.f | INFO     | COMPLETED | step2                                              |         ✅ Completed running step2
2024-08-17 20:59:55.f | INFO     | COMPLETED | test_logstep_indenting.<locals>.step1              |     ✅ Completed running step1
2024-08-17 20:59:55.f | INFO     | COMPLETED | test_logstep_indenting.<locals>.step_a             | ✅ Completed running step_a
```


