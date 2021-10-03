# Mecha Karen - Documentation
This repo contains all the official documentation for Mecha Karen. This can be viewed online [here](https://docs.mechakaren.xyz).

## ReStructuredText (.rst) Syntax
Our documentation uses Sphinx to build our API. Sphinx uses `ReStructuredText` which is a type of markup text which is easy to read and to work with.\
Before making any changes to the documentation it is recommended to read up on how it works and have some experience in order to prevent errors.

## Compiling the documentation
In order to build the API into HTML files for testing and other reasons, follow the steps below:

### Requirements
Inorder to build our documentation you will need `Python3` installed.\
Once you have that you will also need the following libraries installed as well:

* Sphinx
* Colorama

And then your good to go.


### Step 1
Clone the repository
```sh
git clone https://github.com/Mecha-Karen/Documentation
```
Then cd into the repository using
```sh
cd Documentation
```
Keep this window open as you are going to need it for compiling the docs to HTML.

### Step 2
Make your changes in the `.rst` files. Add all resources to the `_static` folder, all your pre-made `.html` files into the `_templates` folder.\
Both these folders can be found in the `source` directory.

#### Extentions
If you are modifying or creating a new extension there is a folder called `extensions`. Create and modify all extensions in that folder then head over to the source directory and open
`conf.py`. Then scroll until you find the `extensions` array. Add the filename of your extension NOT including the file extension.

### Step 3
Head back to terminal and run 
```sh
make html && python static.py
# python may be `python3` in linux
``` 
in the dir you were in step 1. Once its finished compiling you will find a new directory called `build`.\
This folder contains the compiled HTML code. Navigate to `build/html/index.html` and open it. And thats it - you have compiled the docs!

Once you are happy with your changes, either make a pull request with the modified source dir or keep it as a memory.

**Note:** If your on linux `python` may be `python3` for you.

## Pull Requests
To make pull requests a breeze, simply fork this repo. And make some changes to step 1 of compiling the docs.\
```sh
git clone your-forked-repo
cd Documentation
# Replace `Documentation` with your repository name if you have changed it
```

Once you are happy with your changes, commit everything to your repo using:
```sh
git add -A && git commit -m "Your Changes Summarised"
# If your not in powershell replace `&&` with `;`
git push
```
If you havent modified the `.gitignore` file all the garbage from `build` wont be included.

Then travel to github and submit your PR.

## Compiling Cake
To compile the cake section successfully, you will need to first install it, you can either do it directly from the branch or from pypi

```sh
# PyPi
pip/pip3 install MathCake

# Development
git clone https://github.com/Mecha-Karen/Cake
cd Cake/cake
pip install .
```

Then compile the docs as normal
