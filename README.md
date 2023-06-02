# Pi DVD Screensaver

This project showcases a DVD screensaver animation on the Adafruit 128x64 OLED Bonnet for Raspberry Pi. The DVD logo bounces around the screen, changing direction upon pressing the corresponding buttons. The project was developed using ChatGPT, an AI language model.

![DVD Screensaver](pi-dvd-screensaver.gif)

## Features

- Bouncing DVD logo animation on the OLED display
- Button controls for changing the logo's direction
- Screen inversion toggle functionality

## Requirements

- Raspberry Pi
- Adafruit 128x64 OLED Bonnet
- Python 3.x

## Installation

1. Clone the repository:
```shell
git clone https://github.com/2wenty2wo/pi-dvd-screensaver.git
```

2. Install the required dependencies:
```shell
    pip install adafruit-circuitpython-ssd1306
    pip install RPi.GPIO
```

3. Connect the Adafruit 128x64 OLED Bonnet to your Raspberry Pi.

4. Run the script:
```shell
cd pi-dvd-screensaver
python pi-dvd-screensaver.py
```

## Usage

- The DVD logo will start bouncing around the screen automatically.
- Use the D-pad to change the DVD logos direction.

## Contributing

Contributions are welcome! If you have any suggestions, improvements, or new features, feel free to open an issue or submit a pull request.

## License

This project is licensed under the [MIT License].

## Acknowledgements

This project was developed using ChatGPT, an AI language model. ChatGPT is an advanced language model developed by OpenAI.
