from pathlib import Path

CACHE_DIR = Path("~/.cache/pier").expanduser()
TASK_CACHE_DIR = CACHE_DIR / "tasks"
PACKAGE_CACHE_DIR = CACHE_DIR / "tasks" / "packages"
ORG_NAME_PATTERN = r"^[a-zA-Z0-9][a-zA-Z0-9._-]*/[a-zA-Z0-9][a-zA-Z0-9._-]*$"
PIER_REGISTRY_WEBSITE_URL = "https://hub.harborframework.com"
PIER_VIEWER_WEBSITE_URL = PIER_REGISTRY_WEBSITE_URL
PIER_VIEWER_JOBS_URL = f"{PIER_VIEWER_WEBSITE_URL}/jobs"
