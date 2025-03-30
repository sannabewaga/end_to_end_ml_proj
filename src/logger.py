import logging
import os
from datetime import datetime

# Create logs directory if not exists
LOG_DIR = "logs"
os.makedirs(LOG_DIR, exist_ok=True)

# Generate log file name with timestamp
LOG_FILE = f"{LOG_DIR}/{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.log"

# Configure logging
logging.basicConfig(
    filename=LOG_FILE,
    format="%(asctime)s - %(levelname)s - %(message)s",
    level=logging.INFO,
    force=True  # Ensures any previous logging settings are overridden
)

# Get logger instance
logger = logging.getLogger(__name__)

# Log the start of logging
logger.info("Logging has started.")
