" Settings
" syntax enable
" filetype plugin indent on


" Advanced
set number
set showmatch
" set ruler
set noshowmode
" set autoindent
set undolevels=1000
" set backspace=indent,eol,start
set cmdheight=2
set textwidth=79
set wildmode=list:longest,full


let mapleader=" " 
inoremap jk <esc>
nnoremap <leader>py :!python %<cr>
nnoremap <leader>ev :e $MYVIMRC<cr>
nnoremap <leader>sv :source $MYVIMRC<cr>
nnoremap <leader>bb :buffers<CR>:buffer<space>

let g:user_emmet_leader_key=','

map <F6> :Lexplore<CR> " toggles netrw"

autocmd FileType * set tabstop=2|set shiftwidth=2|set noexpandtab
autocmd FileType python set tabstop=4|set shiftwidth=4|set expandtab

let g:netrw_banner = 0
let g:netrw_liststyle = 3
let g:netrw_browse_split = 4
let g:netrw_altv = 1
let g:netrw_winsize = 25

" Set Ultisnips triggers
" let g:UltiSnipsExpandTrigger="<tab>"
" let g:UltiSnipsJumpForwardTrigger="<c-j>"
" let g:UltiSnipsJumpBackwardTrigger="<c-k>"


colorscheme new-railscasts
highlight Comment cterm=italic

let g:UltiSnipsSnippetDirectories=['UltiSnips', $HOME.'/.local/share/UltiSnips'] 

"" For Lightline
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

packadd minpac
call minpac#init()
" minpac must have {'type': 'opt'} so that it can be loaded with `packadd`.
call minpac#add('k-takata/minpac', {'type': 'opt'})
" Add other plugins here.
call minpac#add('tpope/vim-unimpaired')
call minpac#add('jiangmiao/auto-pairs')"
" call minpac#add('raimondi/delimitmate')
call minpac#add('sirver/ultisnips')
call minpac#add('honza/vim-snippets')
call minpac#add('tpope/vim-commentary')
call minpac#add('itchyny/lightline.vim')
call minpac#add('mattn/emmet-vim')
call minpac#add('nerdpad/dracula-vim')
call minpac#add('mhartington/oceanic-next')
call minpac#add('carakan/new-railscasts-theme')
call minpac#add('klen/python-mode')

" Define user commands for updating/cleaning the plugins.
" Each of them loads minpac, reloads .vimrc to register the
" information of plugins, then performs the task.
command! PackUpdate packadd minpac | source $MYVIMRC | call minpac#update('', {'do': 'call minpac#status()'})
command! PackClean  packadd minpac | source $MYVIMRC | call minpac#clean()
command! PackStatus packadd minpac | source $MYVIMRC | call minpac#status()
