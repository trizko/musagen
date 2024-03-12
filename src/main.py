import json
import logging
import os

import uvicorn

from dotenv import load_dotenv
from fastapi import FastAPI
from pydantic import BaseModel


load_dotenv()
logger = logging.getLogger("uvicorn")


app = FastAPI()


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
