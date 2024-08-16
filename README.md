# brixy

brixy is a package with many utilities for developing on Databricks and PySpark.

## Features

### Logging
log the steps of a workflow using the decorator `@brixy.log_step`.

```py
import brixy

@brixy.log_step
def step1():
        return 1+2
```

This will log:
```sh
2024-08-16 11:50:23.168 | INFO     | 🏃‍♀️ | JobStep:step1 - Running step1
2024-08-16 11:50:27.599 | INFO     | ✅ | JobStep:step1 - Completed running step1
```

