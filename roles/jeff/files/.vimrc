"default configs
syntax enable

" tabs
set tabstop=2
set shiftwidth=2
set softtabstop=2
set expandtab
set smarttab
set autoindent

" ui stuff
set number
set cursorline
set lazyredraw
set showmatch

" search
set incsearch
set hlsearch

" movement
nnoremap j gj
nnoremap k gk

"file specific configs
autocmd FileType python setlocal shiftwidth=4 tabstop=4 softtabstop=4
