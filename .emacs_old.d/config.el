(use-package dashboard
  :ensure t
  :config
  (dashboard-setup-startup-hook))

;; Set the title
(setq dashboard-banner-logo-title "Welcome to My Emacs Dashboard")
;; Set the banner
(setq dashboard-startup-banner 'logo)
(setq dashboard-center-content t)

;; Set y or n
(fset 'yes-or-no-p 'y-or-n-p)

(set-frame-parameter (selected-frame) 'alpha '(90 . 70))
(add-to-list 'default-frame-alist '(alpha . (90 .70)))

(setq scroll-conservatively 100)

(use-package expand-region
:ensure t
:config
(global-set-key (kbd "C-=") 'er/expand-region))

(column-number-mode 1)
(global-linum-mode t)
(setq linum-format "%4d ")
(global-hl-line-mode t)
(electric-pair-mode)
(menu-bar-mode -1)
(tool-bar-mode -1)
(show-paren-mode 1)
(scroll-bar-mode -1)
(require 'org-tempo)

(require 'ido)
(ido-mode t)
(ido-everywhere 1)

(use-package which-key
  :ensure t
  :config
  (which-key-mode))

(use-package auto-complete
:ensure t
:init
(progn
(ac-config-default)
(global-auto-complete-mode t)
))

;; (require 'dracula-theme)

(use-package spaceline
  :ensure t
  :config
  (require 'spaceline-config)
  (setq powerline-default-separator (quote arrow))
  (spaceline-emacs-theme))

(use-package elpy
  :ensure t
  :init
  (elpy-enable))

(use-package emmet-mode
  :ensure t
  :init)

(add-hook 'sgml-mode-hook 'emmet-mode)
(add-hook 'css-mode-hook 'emmet-mode)

(defun config-visit ()
(interactive)
(find-file "~/.emacs.d/config.org"))
(global-set-key (kbd "C-c e") 'config-visit)

(defun config-reload ()
(interactive)
(org-babel-load-file (expand-file-name "~/.emacs.d/config.org")))
(global-set-key (kbd "C-c r") 'config-reload)

(setq org-todo-keywords
'((sequence "TODO" "IN-PROGRESS" "WAITING" "DONE")))
