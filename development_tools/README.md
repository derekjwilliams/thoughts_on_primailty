# Setting up a New Development System on MacOS

* [Homebrew](#homebrew)

* [VSCodium](#vscodium)

* [VSCodium Extensions](#vscodium-extensions)

* [Git](#git)

* [Setting up SSH with GitHub on macOS](#setting-up-ssh-with-github-on-macos)

* [Python3](#python3)

## Homebrew

Many of the installs for the development system will require Homebrew.  While there are alternatives to Homebrew, it is widely used and supported.

### References

https://brew.sh/

### Installing Homebrew

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

## VSCodium

VSCode is very similar, I prefer VSCodium because there are fewer restrictions

### References

https://vscodium.com/

### Installing Using Homebrew

```bash
brew install --cask vscodium
```

If you want to use VSCode, `brew install visual-studio-code`

You can now launch VSCodium by **⌘** + **Spacebar** and then typing `vsC`..., which will autocomplete to **VSCodium**.

### Launcing from Terminal

In VSCodium, Open the Command Palette ( **⌘** + **Shift** + **P**), type 'shell command', and run the Shell Command: Install 'code' command in PATH command.

*Note: **⌘** is the **Cmd(command)** key*

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


### Setting up SSH with GitHub on macOS

Doing this can very intimidating, take it one step at a time.

[This](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/checking-for-existing-ssh-keys) descibes checking for ssh keys

[This](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent) describes generating a new key are the official GitHub instructions



[This](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account) describes adding a new SSH key to your GitHub account

Abbreviated instructions based on those pages are shown below, see links above for full instructions

#### Check for Existing SSH key

From [here](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/checking-for-existing-ssh-keys)

Open Terminal and run:

```bash
ls -al ~/.ssh
```

Check the directory listing to see if you already have a public SSH key.  If you see files like `config`          `id_ed25519`      `id_ed25519.pub`  `known_hosts` then you don't need to Generate a new SSH key, and can skip to [Adding a new SSH key to your GitHub account](#adding_a_new_SSH_key_to_your_github_account)

#### Generating a new SSH key


Open Terminal.

Paste the text below, replacing the email used in the example with your GitHub email address.

```bash
ssh-keygen -t ed25519 -C "your_email@example.com"
```

When you're prompted to "Enter a file in which to save the key", you can press Enter to accept the default file location. Please note that if you created SSH keys previously, ssh-keygen may ask you to rewrite another key, in which case we recommend creating a custom-named SSH key. To do so, type the default file location and replace id_ALGORITHM with your custom key name.

```bash
Enter a file in which to save the key (/Users/YOU/.ssh/id_ALGORITHM): [Press enter]
```
At the prompt, type a secure passphrase. For more information, see Working with SSH key passphrases.

```bash
> Enter passphrase (empty for no passphrase): [Type a passphrase]
> Enter same passphrase again: [Type passphrase again]
```

#### Adding your SSH key to the ssh-agent

```bash
eval "$(ssh-agent -s)"
```

If you're using macOS Sierra 10.12.2 or later, you will need to modify your ~/.ssh/config file to automatically load keys into the ssh-agent and store passphrases in your keychain.

* First, check to see if your ~/.ssh/config file exists in the default location.

```bash
open ~/.ssh/config
> The file /Users/YOU/.ssh/config does not exist.
```

If the file doesn't exist, create the file.

```bash
touch ~/.ssh/config
```

Open your ~/.ssh/config file, then modify the file to contain the following lines. If your SSH key file has a different name or path than the example code, modify the filename or path to match your current setup.

```bash
Host github.com
  AddKeysToAgent yes
  UseKeychain yes
  IdentityFile ~/.ssh/id_ed25519
```

Add your SSH private key to the ssh-agent and store your passphrase in the keychain. If you created your key with a different name, or if you are adding an existing key that has a different name, replace id_ed25519 in the command with the name of your private key file.

```bash
ssh-add --apple-use-keychain ~/.ssh/id_ed25519
```

#### Adding a new SSH key to your GitHub account

See [here](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account) for full instructions

1. Copy the SSH public key to your clipboard.
`
pbcopy < ~/.ssh/id_ed25519.pub
`
1. In the upper-right corner of any page on GitHub, click your profile photo, then click **Settings**.

1. In the "Access" section of the sidebar, click  SSH and GPG keys.

1. Click **New SSH key** or **Add SSH key**.
1. In the "Title" field, add a descriptive label for the new key. For example, if you're using a personal laptop, you might call this key "Personal laptop".
1. Select the type of key, either authentication or signing.
1. In the "Key" field, paste your public key.
1. Click **Add SSH key**.
1. If prompted, confirm access to your account on GitHub. For more information, see Sudo mode.

### (Alternative) ChatGPT Instructions for Setting up SSH with GitHub on macOS

Note, these instructions are from ChatGPT.

#### Steps

1. Check for existing SSH keys
1. Generate a new SSH key (if needed)
1. Add your SSH key to the ssh-agent
1. Add the public key to GitHub
1. Test the connection
1. Use the SSH URL when cloning


#### 1. Check for existing SSH keys
Open Terminal and run:

```bash
ls -al ~/.ssh
```

Look for files like `id_ed25519` and `id_ed25519.pub` (or `id_rsa` / `id_rsa.pub`).

#### 2. Generate a new SSH key (if needed)
If you don’t have one, generate an Ed25519 key (recommended over RSA):

```bash
ssh-keygen -t ed25519 -C "your_email@example.com"
```

- Press Enter to accept the default location (`~/.ssh/id_ed25519`)
- Add a passphrase when prompted (recommended for security)

#### 3. Add your SSH key to the ssh-agent
Start the agent and add your key:

```bash
eval "$(ssh-agent -s)"
ssh-add --apple-use-keychain ~/.ssh/id_ed25519
```

Ensure macOS adds your key automatically:

```bash
touch ~/.ssh/config
```

Add this to `~/.ssh/config`:

```
Host github.com
  HostName github.com
  User git
  IdentityFile ~/.ssh/id_ed25519
  AddKeysToAgent yes
  UseKeychain yes
```

#### 4. Add the public key to GitHub
Copy your public key:

```bash
pbcopy < ~/.ssh/id_ed25519.pub
```

Then go to [GitHub SSH settings](https://github.com/settings/keys) and click **"New SSH key"**. Paste the key and give it a recognizable name.

#### 5. Test the connection
Run:

```
ssh -T git@github.com
```

Expected output:

```
Hi your-username! You've successfully authenticated...
```

#### 6. Use the SSH URL when cloning
Example:

```
git clone git@github.com:your-username/your-repo.git
```


## Python3

### Install

```bash
brew install python3
```

### Add Symbolic Links

```bash
ln -s /opt/homebrew/bin/python3 /opt/homebrew/bin/python
```

```bash
ln -s /opt/homebrew/bin/pip3 /opt/homebrew/bin/pip
```

## Python Math and Science Libraries

### NumPy

https://numpy.org/

#### Install

```bash
pip3 install numpy
```

### PyTorch

https://pytorch.org/

#### Install

```bash
pip3 install torch torchvision
```

### Sagemath

https://www.sagemath.org/

#### Install

Download the dmg by following the links here https://github.com/3-manifolds/Sage_macOS/releases

The file to download will be `SageMath-10.6_arm64.dmg`, or similar.  After the download is complete double click on the file in the Downloads folder, this will open a dialog, in the dialog drag SageMath-10-6 icon to Applications folder icon in the dialog.  You can now launch SageMath by **⌘** + **Spacebar** and then typing `Sag`... which will autocomplete to **SageMath-10-6**.  SageMath will be launch a dialog, select a location for JupyterLab or Jupyter Notebook, then SageMath will launch in a browser window.

### venv


Included with current version of Python 3.

This looks like a nice resource for using venv https://realpython.com/python-virtual-environments-a-primer/.  Using venv is optional, but can be very helpful.

Typically the steps would be

```bash
python3 -m venv ~/development/some-cool-environment
```

```bash
source ~/development/some-cool-environment/bin/activate
```

```bash
pip3 install numpy
```
Code away here, when complete:

```bash
deactivate
```

### Ruff

Linter and formatter for Python

#### Reference

https://docs.astral.sh/ruff/

#### Installing

```bash
pip3 install ruff
```

### uv

Alternative to pip

#### Reference

https://docs.astral.sh/uv/

#### Installing

```bash
pip3 install uv
```

## VSCodium Extensions

Also works with VSCode.

Ordered by usefulness (IMHO)

[Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python) - Python language support with extension access points for IntelliSense (Pylance), Debugging (Python Debugger), linting, formatting, refactoring, unit tests, and more.

[Python Indent](https://marketplace.visualstudio.com/items?itemName=KevinRose.vsc-python-indent) - Correct Python indentation

[Ruff](https://marketplace.visualstudio.com/items?itemName=charliermarsh.ruff) - support for the Ruff linter and formatter

[autoDocstring](https://marketplace.visualstudio.com/items?itemName=njpwerner.autodocstring) - Generates python docstrings automatically


[Jupyter](https://marketplace.visualstudio.com/items?itemName=ms-toolsai.jupyter) - Jupyter notebook support, interactive programming and computing that supports Intellisense, debugging and more.

[Pylance](https://marketplace.visualstudio.com/items?itemName=ms-python.vscode-pylance) - A performant, feature-rich language server for Python in VS Code






