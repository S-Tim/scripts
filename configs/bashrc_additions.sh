# easier, quicker ping that terminates
alias ping='ping -vc1'

# colorized output with slashes for folders and nicer size output
alias ls='ls -GFh'

# combine clear and ls
alias cls='clear && ls'

# use c.. n to go up n directory levels
# create the string for the cd command
# https://superuser.com/questions/449687/using-cd-to-go-up-multiple-directory-levels/449705
function cd_up() {
  cd $(printf "%0.s../" $(seq 1 $1 ));
}
alias 'cd..'='cd_up'
