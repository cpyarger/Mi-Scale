"""Constants for integration_blueprint."""
# Base component constants
NAME = "Xiaomi Mi Scale"
DOMAIN = "mi_scale"
DOMAIN_DATA = f"{DOMAIN}_data"
VERSION = "0.0.1"
ATTRIBUTION = "Data provided by http://jsonplaceholder.typicode.com/"
ISSUE_URL = "https://github.com/cpyarger/Mi-Scale/issues"

# Icons
ICON = "mdi:format-quote-close"

# Device classes
BINARY_SENSOR_DEVICE_CLASS = "connectivity"

# Platforms
BINARY_SENSOR = "binary_sensor"
SENSOR = "sensor"
SWITCH = "switch"
PLATFORMS = [BINARY_SENSOR, SENSOR, SWITCH]


# Configuration and options
CONF_ENABLED = "enabled"
CONF_MAC_ADDDRESS = "Scale MAC Address" # Mac address of your scale
CONF_HCI_DEV="hci0"                  # Bluetooth hci device to use
CONF_MQTT_HOST="127.0.0.1"           # MQTT Server (defaults to 127.0.0.1)
CONF_MQTT_PREFIX="miscale"           # MQTT Topic Prefix. Defaults to miscale
CONF_MQTT_USERNAME=""               # Username for MQTT server (comment out if not required)
CONF_MQTT_PASSWORD=""                # Password for MQTT (comment out if not required)
CONF_MQTT_PORT="1883"                # Defaults to 1883
CONF_TIME_INTERVAL="30"              # Time in sec between each query to the scale, to allow other applications to use the Bluetooth module. Defaults to 30
CONF_MQTT_DISCOVERY="true"           # Home Assistant Discovery (true/false), defaults to true
CONF_MQTT_DISCOVERY_PREFIX=""        # Home Assistant Discovery Prefix, defaults to homeassistant
CONF_GT="70"            # If the weight is greater than this number, we'll assume that we're weighing User #1
CONF_SEX="sex"
CONF_NAME="name"          # Name of the user
CONF_HEIGHT="height"       # Height (in cm) of the user
CONF_DOB="dob"   # DOB (in yyyy-mm-dd format)

# Defaults
DEFAULT_NAME = DOMAIN


STARTUP_MESSAGE = f"""
-------------------------------------------------------------------
{NAME}
Version: {VERSION}
This is a custom integration!
If you have any issues with this you need to open an issue here:
{ISSUE_URL}
-------------------------------------------------------------------
"""
