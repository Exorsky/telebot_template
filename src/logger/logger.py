import yaml
import logging

def configure_logger():
    # Load configuration
    with open('config.yaml', 'r') as file:
        config = yaml.safe_load(file)
    
    # Get log level and format from config, defaulting to INFO and a standard format
    log_level = config.get('Logging', {}).get('level', 'INFO')
    log_format = config.get('Logging', {}).get('format', '%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    # Add custom log levels
    custom_levels = config.get('Logging', {}).get('Levels', [])
    for level in custom_levels:
        logging.addLevelName(logging.getLevelName(level.upper()), level.upper())

    # Configure logging
    logging.basicConfig(format=log_format, level=log_level)
    logger = logging.getLogger(__name__)

    return logger
