" Get the defaults as if no .vimrc file
unlet! skip_defaults_vim
source $VIMRUNTIME/defaults.vim

" Settings
filetype plugin on
syntax on
set laststatus=2
set cmdheight=2
set title
set wildmenu
set wildmode=list:longest,full
set number
set nobackup
set noswapfile
set incsearch
set backspace=indent,eol,start
set autoindent
set splitbelow splitright
set showbreak=...

autocmd FileType * set tabstop=2|set shiftwidth=2|set noexpandtab
autocmd FileType python set tabstop=4|set shiftwidth=4|set expandtab

set t_Co=256

" if (has("termguicolors"))
" 	set termguicolors
" endif

colorscheme new-railscasts
highlight Comment cterm=italic
let mapleader=" " 
inoremap jk <esc>
nnoremap <leader>py :!python3 %<cr>
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

" =================================================================


" Package Manager for Vim 8 
packadd minpac
call minpac#init()
call minpac#add('k-takata/minpac', {'type': 'opt'})

call minpac#add('tpope/vim-sensible')
call minpac#add('sirver/ultisnips')
call minpac#add('tpope/vim-unimpaired')
call minpac#add('honza/vim-snippets')
call minpac#add('tpope/vim-commentary')
call minpac#add('itchyny/lightline.vim')
call minpac#add('mattn/emmet-vim')
call minpac#add('nerdpad/dracula-vim')
call minpac#add('fatih/vim-go')
call minpac#add('jiangmiao/auto-pairs')
call minpac#add('carakan/new-railscasts-theme')

" Define user commands for updating/cleaning the plugins.
" Each of them loads minpac, reloads .vimrc to register the
" information of plugins, then performs the task.
command! PackUpdate packadd minpac | source $MYVIMRC | call minpac#update('', {'do': 'call minpac#status()'})
command! PackClean  packadd minpac | source $MYVIMRC | call minpac#clean()
command! PackStatus packadd minpac | source $MYVIMRC | call minpac#status()


