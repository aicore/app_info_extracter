## Introduction
App info extractor is a utility to extract and analyze customer reviews and critical metrics of apps from multiple sources like google play store, Apple play store, and any other sources.This utility is highly configurable to extract and give relevant information about any app in a meaningful way.

## How it works?
This utility takes config.yaml as input. Configuration for each app is self-contained in configs. Once a configuration is specified in config.yaml, the utility will iteratively go through each app, crawl the relevant information, and store the data locally as a CSV file.

## How to use it?
1. Check out the package
2. Have python 3.8 on your system . Use [pyenv](https://github.com/pyenv/pyenv) to manage multiple version of python in your machine
3. Open terminal and type  ``` cd app_info_extracter```
4. Setup python [virtual enviorment](https://uoa-eresearch.github.io/eresearch-cookbook/recipe/2014/11/26/python-virtual-env/) having this will prevent you from messing up with the system-wide python installation
5. Now type in terminal ``` cd src/crawler/```
6. Add the required configuration in config.yaml using your favorite editor
7. in terminal type ```python main.py ```
8. Results of the crawling will be stored in  separate directories for  each app in current directory 
9. In case of failure, just re-run ```python main.py ```  script will start from where its left off.

## Contributing
1.Use vim or InteliJUltimate or pycharm or visualstudio code.
### Vim

Following are the vimrc setting used to create this utility. Use it if you are fan of Vim.

```
set nu
nnoremap <C-Left> :tabprevious<CR>
nnoremap <C-Right> :tabnext<CR>

" Specify a directory for plugins
" - For Neovim: stdpath('data') . '/plugged'
" - Avoid using standard Vim directory names like 'plugin'
call plug#begin('~/.vim/plugged')

Plug 'sheerun/vim-polyglot'
Plug 'dense-analysis/ale'
Plug 'junegunn/fzf', { 'do': { -> fzf#install() } }
Plug 'junegunn/fzf.vim'
Plug 'ludovicchabant/vim-gutentags'
" Use release branch (recommend)
Plug 'neoclide/coc.nvim', {'branch': 'release'}
Plug 'kamykn/spelunker.vim'
Plug 'Raimondi/delimitMate'
Plug 'mattn/emmet-vim'
Plug 'davidhalter/jedi-vim'
"Plug 'Chiel92/vim-autoformat'
"Plug 'stephpy/vim-yaml'


call plug#end()

nmap <silent> [c <Plug>(ale_previous_wrap)
nmap <silent> ]c <Plug>(ale_next_wrap)
let g:ale_sign_error = '❌'
let g:ale_sign_warning = '⚠️'

let g:ale_linters = {
      \ 'python': ['flake8']
      \}
" Fix files automatically on save
let g:ale_fixers = {
      \   'javascript': [
      \ 'prettier',
      \ 'eslint'
      \ ],
      \ 'python' : ['yapf']
      \}
let g:ale_fix_on_save = 1
let g:ale_completion_enabled = 1
nmap <F6> <Plug>(ale_fix)

nnoremap <C-p> :Files<CR>
nnoremap <Leader>b :Buffers<CR>
nnoremap <Leader>h :History<CR>

nnoremap <Leader>t :BTags<CR>
nnoremap <Leader>T :Tags<CR>

" Use tab for trigger completion with characters ahead and navigate.
" NOTE: Use command ':verbose imap <tab>' to make sure tab is not mapped by
" other plugin before putting this into your config.
inoremap <silent><expr> <TAB>
      \ pumvisible() ? "\<C-n>" :
      \ <SID>check_back_space() ? "\<TAB>" :
      \ coc#refresh()
inoremap <expr><S-TAB> pumvisible() ? "\<C-p>" : "\<C-h>"


"let g:gutentags_trace = 1

let g:spelunker_disable_backquoted_checking = 1
let g:enable_spelunker_vim = 1

" Create own custom autogroup to enable spelunker.vim for specific filetypes.
augroup spelunker
  autocmd!
  " Setting for g:spelunker_check_type = 1:
  autocmd BufWinEnter,BufWritePost *.vim,*.js,*.jsx,*.json,*.md,*.py call spelunker#check()

  " Setting for g:spelunker_check_type = 2:
  autocmd CursorHold *.vim,*.js,*.jsx,*.json,*.md,*.py call spelunker#check_displayed_words()
augroup END

```

