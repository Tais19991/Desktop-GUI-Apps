# Watermark Creator

Watermark Creator is a desktop application built with Python and Tkinter that allows users to add watermarks to images. The application supports resizing, rotating, and changing the opacity of the watermark. Users can also add text as a watermark and adjust the spacing of multiple watermark instances on the main image.

## Features

- Load main images and overlay images (logos, watermarks)
- Resize, rotate, and change the opacity of the overlay images
- Add text as a watermark
- Adjust the spacing between multiple instances of the watermark
- Save the final image with the applied watermarks

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/Tais19991/GUI-Projects.git
    ```

2. Navigate to the project directory:
    ```bash
    cd GUI-Projects/Watermark_Creator
    ```

3. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Run the application:
    ```bash
    python main.py
    ```

## Usage

1. Load a main image using the "Add main img" button.
2. Add a logo or text watermark using the respective buttons.
3. Use the sliders to adjust the size, angle, opacity, and spacing of the watermark.
4. Save the final image using the "Save result" button.

## Current State

The project is functional but requires refactoring and bug fixing. Known issues include:
- Potential crashes when invalid files are loaded
- UI responsiveness issues on smaller screens
- Occasional incorrect application of transformations (resize, rotate, opacity) on watermarks

## Contributing

Contributions are welcome! Here are some areas that need attention:
- **Refactoring**: Improve the structure and readability of the code.
- **Bug Fixing**: Identify and fix bugs, especially those related to image transformations and file handling.
- **New Features**: Suggest and implement new features to enhance the application's functionality.
- **Exception Handling**: Add robust exception handling to prevent crashes and provide meaningful error messages.

To contribute, please fork the repository, create a new branch for your changes, and submit a pull request. Ensure your code follows the project's coding standards and includes appropriate tests.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgements

Thanks to all contributors and users for their support and feedback. Your suggestions and contributions help make this project better.
