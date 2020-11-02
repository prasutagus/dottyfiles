call plug#begin('~/.config/nvim/plugged')

Plug 'sirver/ultisnips'
Plug 'tpope/vim-unimpaired'
Plug 'honza/vim-snippets'
Plug 'itchyny/lightline.vim'
Plug 'mattn/emmet-vim'
Plug 'tpope/vim-commentary'
Plug 'jiangmiao/auto-pairs'
Plug 'carakan/new-railscasts-theme'
Plug 'dracula/vim', { 'as': 'dracula' }

call plug#end()


" Settings
"filetype plugin on
syntax on
syntax enable
set laststatus=2
set cmdheight=2
set title
set wildmenu
set wildmode=list:longest,full
set number
set nobackup
set noswapfile
set nowritebackup
set incsearch
set backspace=indent,eol,start
set autoindent
set splitbelow splitright
set showbreak=...

" True Color Support if it's avaiable in terminal
if has("termguicolors")
set termguicolors
endif

colorscheme dracula

autocmd FileType * set tabstop=2|set shiftwidth=2|set noexpandtab
autocmd FileType python set tabstop=4|set shiftwidth=4|set expandtab

highlight Comment cterm=italic gui=italic

" highlight Normal guibg=none
" highlight NonText guibg=none

let mapleader=" " 
inoremap jk <esc>
nnoremap <leader>py :term python %<cr>
nnoremap <leader>ev :e $MYVIMRC<cr>
nnoremap <leader>sv :source $MYVIMRC<cr>
nnoremap <leader>bb :buffers<CR>:buffer<space>

let g:netrw_banner = 0
let g:netrw_liststyle = 3
let g:netrw_browse_split = 4
let g:netrw_altv = 1
let g:netrw_winsize = 20

map <F6> :Lexplore<CR>

let g:UltiSnipsSnippetDirectories=['UltiSnips', $HOME.'/.local/share/UltiSnips'] 

let g:lightline = {
    \ 'colorscheme': 'darcula',
    \ 'active': {
    \   'left': [ [ 'mode'],
    \             [ 'buf', 'filename', 'modified' ] ],
    \'right':[['lineinfo', 'lines'], ['filetype']]
    \ },
    \ 'component': {
    \   'buf': 'Bufr: %n', 'lines': 'Total Ln: %L'
    \ },
    \ }
