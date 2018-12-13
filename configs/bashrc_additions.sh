# bash completion
[ -f /usr/local/etc/bash_completion ] && . /usr/local/etc/bash_completion

# easier, quicker ping that terminates
alias ping='ping -vc1'

# colorized output with slashes for folders and nicer size output
alias ls='ls -GFh'

# combine clear and ls
alias cls='clear && ls'

# Change command line prompt
export PS1="[\t \u \W]\$ "

# use c.. n to go up n directory levels
# create the string for the cd command
# https://superuser.com/questions/449687/using-cd-to-go-up-multiple-directory-levels/449705
function cd_up() {
  cd $(printf "%0.s../" $(seq 1 $1 ));
}
alias 'cd..'='cd_up'

# vi mode
set -o vi

# jenv
export PATH="$HOME/.jenv/bin:$PATH"
eval "$(jenv init -)"
export JAVA_HOME="$HOME/.jenv/versions/`jenv version-name`"
alias jenv_set_java_home='export JAVA_HOME="$HOME/.jenv/versions/`jenv version-name`"'

# nvm
export NVM_DIR="$HOME/.nvm"
[ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"  # This loads nvm
[ -s "$NVM_DIR/bash_completion" ] && \. "$NVM_DIR/bash_completion"  # This loads nvm bash_completion

