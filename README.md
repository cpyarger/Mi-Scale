
# Home Assistant Add-on: Xiaomi Mi Scale

[![GitHub Release][releases-shield]][releases]
[![GitHub Activity][commits-shield]][commits]
[![License][license-shield]](LICENSE)

[![hacs][hacsbadge]][hacs]




**This component will set up the following platforms.**

Platform | Description
-- | --
`binary_sensor` | Show something `True` or `False`.
`sensor` | Show info from blueprint API.
`switch` | Switch something `True` or `False`.

![Xiaomi Mi Scale][mi_scale]

## Installation

1. Using the tool of choice open the directory (folder) for your HA configuration (where you find `configuration.yaml`).
2. If you do not have a `custom_components` directory (folder) there, you need to create it.
3. In the `custom_components` directory (folder) create a new folder called `mi_scale`.
4. Download _all_ the files from the `custom_components/mi_scale/` directory (folder) in this repository.
5. Place the files you downloaded in the new directory (folder) you created.
6. Restart Home Assistant
7. In the HA UI go to "Configuration" -> "Integrations" click "+" and search for "Blueprint"

Using your HA configuration directory (folder) as a starting point you should now also have this:

```text
custom_components/mi_scale/translations/en.json
custom_components/mi_scale/translations/nb.json
custom_components/mi_scale/translations/sensor.nb.json
custom_components/mi_scale/__init__.py
custom_components/mi_scale/api.py
custom_components/mi_scale/binary_sensor.py
custom_components/mi_scale/config_flow.py
custom_components/mi_scale/const.py
custom_components/mi_scale/manifest.json
custom_components/mi_scale/sensor.py
custom_components/mi_scale/switch.py
```

## Configuration is done in the UI

<!---->

## Contributions are welcome!

If you want to contribute to this please read the [Contribution guidelines](CONTRIBUTING.md)

***

[mi_scale]: https://github.com/cpyarger/Mi-Scale/blob/master/logo.png?raw=true
[releases-shield]: https://img.shields.io/github/v/release/cpyarger/Mi-Scale?style=for-the-badge
[releases]: https://github.com/cpyarger/Mi-Scale/releases/latest
[commits-shield]: https://img.shields.io/github/commit-activity/y/cpyarger/Mi-Scale?style=for-the-badge
[commits]: https://github.com/custom-components/mi_scale/commits/master
[hacs]: https://github.com/custom-components/hacs
[hacsbadge]: https://img.shields.io/badge/HACS-Custom-orange.svg?style=for-the-badge
[exampleimg]: example.png
[forum-shield]: https://img.shields.io/badge/community-forum-brightgreen.svg?style=for-the-badge
[forum]: https://community.home-assistant.io/
[license-shield]: https://img.shields.io/github/license/custom-components/blueprint.svg?style=for-the-badge
