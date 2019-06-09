set hlsearch
set backspace=2
set autoindent
set ruler
set showmode
set nu
set bg=dark
syntax on


" Make vim indent 2 spaces for ruby and scala files only
filetype plugin indent on
set sw=4
set ts=4
:autocmd Filetype ruby set softtabstop=2
:autocmd Filetype ruby set sw=2
:autocmd Filetype ruby set ts=2

:autocmd Filetype scala set softtabstop=2
:autocmd Filetype scala set sw=2
:autocmd Filetype scala set ts=2
