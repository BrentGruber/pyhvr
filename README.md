# pyhvr

Python client library for the Fivetran HVR REST API.

## Installation

```
uv add pyhvr
```

## Usage

```python
from pyhvr import HvrClient, AsyncHvrClient

# Sync
with HvrClient(base_url="http://localhost:4340", username="admin", password="secret") as client:
    hubs = client.list_hubs()

# Async
async with AsyncHvrClient(base_url="http://localhost:4340", username="admin", password="secret") as client:
    hubs = await client.list_hubs()
```
