# Mecha Karen - Documentation
This repo contains all the official documentation for Mecha Karen. This can be viewed online [here](https://docs.mechakaren.xyz).

## ReStructuredText (.rst) Syntax
Our documentation uses sphinx to build our API. Sphinx uses `ReStructuredText` which is a type of markup text which is easy to read and to work with.\
Before making any changes to the documentation it is recomended to read up on how it works and have some decent practise inorder to prevent errors.

## Compiling the documentation
Inorder to build the API into HTML files for testing and other reasons, follow the steps below:

### 1
Clone the repository
```sh
git clone https://github.com/Mecha-Karen/Documentation
```
Then cd into the repository using
```sh
cd Documentation
```
Keep this window open as your going to need it for compiling the docs to HTML.

### 2
Make your changes in the `.rst` files. Add all recourses to the `_static` folder, all your pre-made `.html` files into the `_templates` folder.\
Both these folders can be found in the `source` directory.

#### Extentions
If your modifying or creating a new extention there is a folder called `extensions`. Create and modify all extentions in that folder then head over to the source directory and open
`conf.py`. Then scroll till you find the `extensions` array. Add the filename of your extention NOT including the file extension.

### 3
Head back to terminal and run `make html` in the dir you were in step 1. Once its finished compiling you will find a new directory called `build`.\
This folder contains the compiled HTML code. Navigate to `build/html/index.html` and open it. And thats it - you have compiled the docs!

Once your happy with your changes, either make a pull request with the modified source dir or keep it as a memory.

## Pull Requests
To make pull requests a breeze, simply fork this repo. And make some changes to step 1 of compiling the docs.\
```sh
git clone your-forked-repo
cd Documentation
# Replace `Documentation` with your repository name if you have changed it
```

Once your happy with your changes, commit everything to your repo using:
```sh
git add -A && git commit -m "Your Changes Summarised"
# If your in powershell replace `&&` with `;`
git push
```
If you havent modified the `.gitignore` file all the garbage from `build` wont be included.

Then travel to github and submit your PR.
