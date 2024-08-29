**The guide covers installation steps for both MacOS and Windows users**

# Comprehensive Setup Guide for CURSOR IDE and Streamlit Development and Deployment

This guide will walk you through the process of setting up your development environment for working with Git, Github, Conda, Python, the CURSOR IDE (an AI-powered fork of VSCode) and Streamlit. 

## Table of Contents

1. [MacOS Setup](#macos-setup)
    1. [Installing Homebrew](#installing-homebrew)
    2. [Installing Git](#installing-git-macos)
    3. [Installing Python](#installing-python-macos)
    4. [Installing Miniconda](#installing-miniconda-macos)
    5. [Installing CURSOR IDE](#installing-cursor-ide-macos)

2. [Windows Setup](#windows-setup)
    1. [Installing Git](#installing-git-windows)
    2. [Installing Python](#installing-python-windows)
    3. [Installing Miniconda](#installing-miniconda-windows)
    4. [Installing CURSOR IDE](#installing-cursor-ide-windows)

3. [Setting Up Your Development Environment](#setting-up-your-development-environment)
    1. [Creating a Conda Environment](#creating-a-conda-environment)
    2. [Selecting the Conda Environment in CURSOR IDE](#selecting-the-conda-environment-in-cursor-ide)
    3. [Installing Required Packages](#installing-required-packages)

4. [Setting Up Your Streamlit Project](#setting-up-your-streamlit-project)
    1. [Creating a New Streamlit App](#creating-a-new-streamlit-app)
    2. [Setting Up GitHub Integration](#setting-up-github-integration)
    3. [Creating Essential Files](#creating-essential-files)

5. [Running and Deploying Your Streamlit App](#running-and-deploying-your-streamlit-app)
    1. [Running Your Streamlit App Locally](#running-your-streamlit-app-locally)
    2. [Deploying to GitHub Pages](#deploying-to-github-pages)

Let's begin with the setup process for MacOS users:

## MacOS Setup

### Installing Homebrew

Homebrew is a package manager for MacOS that makes it easy to install and manage software. To install Homebrew:

1. Open Terminal.
2. Run the following command:

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

3. Follow the prompts to complete the installation.

### Installing Git (MacOS)

Git is a version control system that you'll use to manage your code. To install Git:

1. Open Terminal.
2. Run the following command:

```bash
brew install git
```

3. Verify the installation by running:

```bash
git --version
```

### Installing Python (MacOS)

While MacOS comes with Python pre-installed, it's recommended to install a separate version for development:

1. Open Terminal.
2. Run the following command:

```bash
brew install python
```

3. Verify the installation by running:

```bash
python3 --version
```

### Installing Miniconda (MacOS)

Miniconda is a minimal installer for Conda, which we'll use to manage our Python environments:

1. Visit the Miniconda download page: https://docs.conda.io/en/latest/miniconda.html
2. Download the MacOS installer (choose the appropriate version for your system architecture).
3. Open Terminal and navigate to the directory where you downloaded the installer.
4. Run the following command to make the installer executable:

```bash
chmod +x Miniconda3-latest-MacOSX-x86_64.sh
```

5. Run the installer:

```bash
./Miniconda3-latest-MacOSX-x86_64.sh
```

6. Follow the prompts to complete the installation.
7. Close and reopen Terminal to apply the changes.

### Installing CURSOR IDE (MacOS)

CURSOR IDE is an AI-powered fork of VSCode. To install it:

1. Visit the CURSOR IDE website: https://cursor.so/
2. Click on the "Download" button for MacOS.
3. Once the download is complete, open the downloaded file.
4. Drag the CURSOR app to your Applications folder.
5. Open CURSOR from your Applications folder.

## Windows Setup

### Installing Git (Windows)

1. Visit the Git for Windows download page: https://git-scm.com/download/win
2. Download the latest version for your system architecture (32-bit or 64-bit).
3. Run the downloaded installer.
4. Follow the installation wizard, using the default options unless you have specific preferences.
5. After installation, open Command Prompt and verify the installation by running:

```
git --version
```

### Installing Python (Windows)

1. Visit the official Python website: https://www.python.org/downloads/windows/
2. Download the latest Python 3 release (64-bit version recommended).
3. Run the installer.
4. Important: Check the box that says "Add Python to PATH" before clicking "Install Now".
5. Follow the installation wizard to complete the process.
6. After installation, open Command Prompt and verify by running:

```
python --version
```

### Installing Miniconda (Windows)

1. Visit the Miniconda download page: https://docs.conda.io/en/latest/miniconda.html
2. Download the Windows installer (choose the appropriate version for your system architecture).
3. Run the downloaded installer.
4. Follow the installation wizard, using the default options unless you have specific preferences.
5. Important: During installation, make sure to check the box that says "Add Miniconda3 to my PATH environment variable".
6. After installation, open a new Command Prompt and verify by running:

```
conda --version
```

### Installing CURSOR IDE (Windows)

1. Visit the CURSOR IDE website: https://cursor.so/
2. Click on the "Download" button for Windows.
3. Once the download is complete, run the installer.
4. Follow the installation wizard to complete the process.
5. Launch CURSOR IDE from the Start menu.

## Setting Up Your Development Environment

### Creating a Conda Environment

1. Open Terminal (MacOS) or Command Prompt (Windows).
2. Create a new Conda environment with Python 3.9 (or your preferred version):

```
conda create --name streamlit-env python=3.12
```

3. Activate the new environment:

```
conda activate streamlit-env
```

### Selecting the Conda Environment in CURSOR IDE

1. Open CURSOR IDE.
2. Open the Command Palette:
   - On MacOS: Press `Cmd + Shift + P`
   - On Windows: Press `Ctrl + Shift + P`
3. Type "Python: Select Interpreter" and select it.
4. Choose the interpreter that matches your Conda environment (e.g., `streamlit-env`).

### Installing Required Packages

1. In CURSOR IDE, open a new terminal:
   - On MacOS: `Terminal > New Terminal`
   - On Windows: `View > Terminal`
2. Ensure your Conda environment is activated:

```
conda activate streamlit-env
```

3. Install the required packages:

```
pip install streamlit numpy pandas matplotlib
```

Alternatively, if you have a `requirements.txt` file:

```
pip install -r requirements.txt
```

## Setting Up Your Streamlit Project

### Creating a New Streamlit App

1. In CURSOR IDE, create a new file called `app.py`.
2. Add the following code to create a basic Streamlit app:

```python
import streamlit as st

st.title("My First Streamlit App")
st.write("Welcome to my Streamlit application!")

# Add more Streamlit components as needed
```

### Setting Up GitHub Integration

1. Create a new repository on GitHub:
   - Go to https://github.com/new
   - Give your repository a name
   - Choose whether to make it public or private
   - Don't initialize with a README, .gitignore, or license

2. In CURSOR IDE, open the Source Control view (icon in the left sidebar).
3. Click on "Initialize Repository" to create a local Git repository.
4. Stage your changes by clicking the "+" next to each file or using "Stage All Changes".
5. Commit your changes by entering a commit message and clicking the checkmark icon.
6. Click on the "..." menu in the Source Control view and select "Remote > Add Remote".
7. Enter the URL of your GitHub repository and press Enter.
8. Push your changes to GitHub by clicking on "Publish Branch" in the Source Control view.

### Creating Essential Files

1. Create a `.gitignore` file:
   - In CURSOR IDE, create a new file named `.gitignore`
   - Add the following content:

```
# Python
__pycache__/
*.py[cod]
*.so

# Environments
.env
.venv
env/
venv/
ENV/

# Streamlit
.streamlit/secrets.toml

# Miscellaneous
.DS_Store
Thumbs.db
```

2. Create a `.env` file for environment variables:
   - Create a new file named `.env`
   - Add any environment variables you need, e.g.:

```
API_KEY=your_api_key_here
DATABASE_URL=your_database_url_here
```

3. Set up Streamlit configuration:
   - Create a folder named `.streamlit`
   - Inside `.streamlit`, create two files: `config.toml` and `secrets.toml`
   - In `config.toml`, add general Streamlit configurations:

```toml
[theme]
primaryColor = "#F63366"
backgroundColor = "#FFFFFF"
secondaryBackgroundColor = "#F0F2F6"
textColor = "#262730"
font = "sans serif"

[server]
enableCORS = false
```

   - In `secrets.toml`, add any secret configurations (make sure this file is in your `.gitignore`):

```toml
# .streamlit/secrets.toml
db_username = "your_username"
db_password = "your_password"
```
## Running and Deploying Your Streamlit App

### Running Your Streamlit App Locally

1. In CURSOR IDE, open a terminal (if not already open).
2. Ensure your Conda environment is activated:

```
conda activate streamlit-env
```

3. Navigate to the directory containing your `app.py` file (if not already there).
4. Run your Streamlit app with the following command:

```
streamlit run app.py
```

5. Your default web browser should open automatically, displaying your Streamlit app. If not, copy the URL shown in the terminal and paste it into your browser.

### Deploying to GitHub Pages

While GitHub Pages doesn't directly support running Python applications, you can use it to host a static website that links to your Streamlit app deployed on a platform like Streamlit Community Cloud. Here's how to set it up:

1. Deploy your app on Streamlit Community Cloud:
   - Go to https://streamlit.io/cloud
   - Sign in with your GitHub account
   - Connect your GitHub repository
   - Select the `app.py` file and deploy

2. Create a simple HTML page to redirect to your Streamlit app:
   - In your project root, create an `index.html` file with the following content:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>My Streamlit App</title>
    <meta http-equiv="refresh" content="0; URL=https://your-app-url.streamlit.app" />
</head>
<body>
    <p>If you are not redirected, <a href="https://your-app-url.streamlit.app">click here</a>.</p>
</body>
</html>
```

Replace `https://your-app-url.streamlit.app` with the actual URL of your deployed Streamlit app.

3. Commit and push the `index.html` file to your GitHub repository:

```
git add index.html
git commit -m "Add redirect page for GitHub Pages"
git push
```

4. Set up GitHub Pages:
   - Go to your GitHub repository
   - Click on "Settings"
   - Scroll down to the "GitHub Pages" section
   - Under "Source", select the branch you want to use (usually `main` or `master`)
   - Click "Save"

5. Your GitHub Pages site will now be live at `https://your-username.github.io/your-repo-name/`

## Additional Git Commands for Managing Your Project

Here are some common Git commands you'll use to manage your project:

1. Check the status of your repository:
```
git status
```

2. Add changes to staging:
```
git add .
```

3. Commit staged changes:
```
git commit -m "Your commit message here"
```

4. Push changes to GitHub:
```
git push origin main
```

5. Pull changes from GitHub:
```
git pull origin main
```

6. Create a new branch:
```
git checkout -b new-branch-name
```

7. Switch between branches:
```
git checkout branch-name
```

8. Merge branches:
```
git merge branch-name
```

## Tips for Package Management

1. To install a new package:
```
pip install package-name
```

2. To uninstall a package:
```
pip uninstall package-name
```

3. To list installed packages:
```
pip list
```

4. To generate a `requirements.txt` file:
```
pip freeze > requirements.txt
```

5. To install packages from a `requirements.txt` file:
```
pip install -r requirements.txt
```

## Conclusion

You now have a complete setup for developing Streamlit applications using CURSOR IDE, with Git integration for version control and GitHub Pages for basic web hosting. Remember to keep your environment and dependencies up to date, and always use version control to track changes in your project.

As you continue to develop your Streamlit app, you may want to explore more advanced features such as:

- Using Streamlit's built-in caching to improve performance
- Integrating with databases or external APIs
- Creating more complex layouts and interactive visualizations
- Implementing user authentication and authorization

Happy coding, and enjoy building with Streamlit!



