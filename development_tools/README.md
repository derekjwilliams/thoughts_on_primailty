# Setting up a New Development System on MacOS

* [Homebrew](#homebrew)

* [Git](#git)

## Homebrew

Many of the installs for the development system will require Homebrew.  While there are alternatives to Homebrew, it is widely used and supported.

### References

https://brew.sh/

### Installing Homebrew

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```
## Git

### References

Home page https://git-scm.com/

Great set of resources: https://github.com/dictcp/awesome-git

### Installing Git

```bash
brew install git
```

Note: XCode command line tools is another option, which is what I use. I'm not sure if XCode command line tools is needed for the brew install

### Using Git

### Common Git Commands

#### Clone an existing git repository

```bash
git clone [repo]
```

##### Example

```bash
git clone git@github.com:derekjwilliams/d3-ternary.git
```

#### Add a File or Folder

```bash
git add [myfile]
```

#### Commit Changes

```bash
git commit -a -m "[describe changes]"
```

#### Push Changes to Remote Repository

```bash
git push
```

## Python3

### Install

```bash
brew install python3
```




