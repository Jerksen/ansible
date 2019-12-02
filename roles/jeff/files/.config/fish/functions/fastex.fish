function fastex -a fname -d "auto detect the right unzipper"
  echo "going to try extracting $fname"
  if test -f $fname
    switch $fname
    case '*.tar.bz2'
      tar xjf $fname
    case '*.tar.gz'
      tar xzf $fname
    case '*.bz2'
      bunzip2 $fname
    case '*.rar'
      unrar x $fname
    case '*.gz'
      gunzip $fname
    case '*.tar'
      tar xf $fname
    case '*.tbz2'
      tar xjf $fname
    case '*.tgz'
      tar xzf $fname
    case '*.zip'
      unzip $fname
    case '*.Z'
      uncompress $fname
    case '*.7z'
      7z x $fname
    case '*'
      echo "'$fname' cannot be extracted with ex()"
    end
  else
    echo "'$fname' is not a valid file for ex()"
  end
end
