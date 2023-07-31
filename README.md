# Auto Mouse
This is a simple Python script that keeps the mouse moving automatically to prevent the system from becoming idle (Windows OS only)

## Prerequisites

Ensure that you have installed Python 3.8 or later. You can check your current version using:

```
python --version
```

## Installation
Follow these steps to install the necessary libraries and run the project:

1. Clone the repository:
```
git clone https://github.com/your-username/auto-mouse.git
```
2. Navigate to the auto-mouse directory:
```
cd auto-mouse
```
3. Create a virtual environment (optional, but recommended):
- Using Python:
```
python -m venv venv
```
- Using Conda:
```
conda create --name auto-mouse-env python=3.11
```
4. Activate the virtual environment:
- Using Python:
```
venv\Scripts\activate
```
- Using Conda:
```
conda activate auto-mouse-env
```
5. Install the necessary libraries from the **requirements.txt** file:
```
pip install -r requirements.txt
```
6. Run the **run_mouse.py** script:
```
python run_mouse.py
```
That's it! The script should now be moving your mouse around the screen every second.
