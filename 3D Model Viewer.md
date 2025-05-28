# C:\code> 3D Model Viewer

A powerful 3D model viewer application that supports both web-based and OpenGL-based viewing modes. The application can handle various 3D model formats including GLB, GLTF, OBJ, and PLY files.

![image](https://github.com/Dahandla/C-code-3D-Model-Viewer/blob/b1ea6b33accc2a830e96d24fd04266ccc11112ee/resources/Image5b.png)

## Features

- Dual viewing modes:
  - Web-based viewer with advanced lighting and HDRI support
  - OpenGL-based viewer with wireframe mode
- Support for multiple 3D file formats:
  - GLB/GLTF
  - OBJ
  - PLY
  - STL
- Interactive controls:
  - Model rotation
  - Zoom
  - Pan
  - Wireframe toggle
- HDRI environment support
- File system browser
- Dark theme interface

## Installation

### 1. Create Conda Environment

```bash
# Create a new conda environment
conda create -n Ccode3DViewer python=3.10
conda activate Ccode3DViewer
```

### 2. Install Dependencies

```bash
# Install required packages
pip install -r requirementsViewer.txt
```

## Usage

### Starting the Application

```bash
# Activate the environment
conda activate Ccode3DViewer

# Run the viewer
python start_viewer.py
```


### Controls

#### Web Viewer Mode
- **Mouse Controls:**
  - Left-click + drag: Rotate model
  - Right-click + drag: Pan
  - Scroll: Zoom in/out
- **Keyboard Shortcuts:**
  - `R`: Reset view
  - `r`: Toggle auto-rotation
  - `m`: Toggle menu
  - `b`: Toggle HDRI background

#### OpenGL Viewer Mode
- **Mouse Controls:**
  - Left-click + drag: Rotate model
  - Right-click + drag: Pan
  - Scroll: Zoom in/out
- **Buttons:**
  - Wireframe: Toggle wireframe mode
  - Reset View: Reset camera position

### HDRI Environment

1. Click the gear icon (⚙️) to open the controls menu
2. Click the folder icon in the HDRI Environment section
3. Select an HDR/EXR file
4. Adjust environment intensity and background settings as needed

## File Structure

```
Ccode3DGen_v1_4_/
├── CcodeGLB_Viewer_v1_2.pyd    # Main application file
├── requirementsViewer.txt # Dependencies
├── server_files/              # Directory for model files
│   └── hdri/                  # HDRI environment maps
└── resources/                 # Application resources
```

## Troubleshooting

1. **OpenGL Context Issues:**
   - Ensure your graphics drivers are up to date
   - Try running in web viewer mode if OpenGL mode fails

2. **Model Loading Issues:**
   - Check if the model file is in a supported format
   - Verify the model file is not corrupted
   - Try converting the model to GLB format

3. **HDRI Loading Issues:**
   - Ensure the HDRI file is in HDR or EXR format
   - Check file permissions in the server_files/hdri directory

## Requirements

- Python 3.10 or higher
- Conda package manager
- Graphics card with OpenGL support
- Modern web browser (for web viewer mode)

## Dependencies

- PySide6 6.4.2
- PyOpenGL 3.1.6
- trimesh 4.0.0
- numpy 1.24.3
- numpy-stl 2.16.3
- requests 2.31.0
- scipy 1.10.1

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Author

Created by Andre' L. Dickinson
Email: saraintelai@gmail.com
Version: 1.1.0
Date: December 2024
