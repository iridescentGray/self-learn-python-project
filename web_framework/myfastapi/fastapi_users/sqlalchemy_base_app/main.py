import uvicorn

import os
import sys
from pathlib import Path

project_root_folder = Path(os.path.abspath(__file__)).parent.parent
sys.path.append(str(project_root_folder))

# api-doc: http://127.0.0.1:8000/openapi.json
# defualt-Swagger UI: http://127.0.0.1:8000/docs
if __name__ == "__main__":
    uvicorn.run("app:app", host="0.0.0.0", log_level="info")
