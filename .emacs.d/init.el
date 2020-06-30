(require 'package)

(setq package-enable-at-startup nil)
(add-to-list 'package-archives
	     '("melpa" . "https://melpa.org/packages/"))

(package-initialize)

;; For use-package
(unless (package-installed-p 'use-package)
  (package-refresh-contents)
  (package-install 'use-package))


(org-babel-load-file (expand-file-name ".emacs.d/config.org"))
(custom-set-variables
 ;; custom-set-variables was added by Custom.
 ;; If you edit it by hand, you could mess it up, so be careful.
 ;; Your init file should contain only one such instance.
 ;; If there is more than one, they won't work right.
 '(ansi-color-faces-vector
   [default default default italic underline success warning error])
 '(ansi-color-names-vector
   ["#212526" "#ff4b4b" "#b4fa70" "#fce94f" "#729fcf" "#e090d7" "#8cc4ff" "#eeeeec"])
 '(custom-enabled-themes (quote (spacegray)))
 '(custom-safe-themes
   (quote
    ("c560237b7505f67a271def31c706151afd7aa6eba9f69af77ec05bde5408dbcd" "dd4045f095288cdd2ff9ba043e1a6def457e51af762aee7ecdafdbba0877e7c3" "a30c136e90c6d902695599723515e61c7debc3eb13f830e2432e6e2f321858e1" "b7133876a11eb2ded01b4b144b45d9e7457f80dd5900c332241881ab261c50f4" "dcdd1471fde79899ae47152d090e3551b889edf4b46f00df36d653adc2bf550d" "bf387180109d222aee6bb089db48ed38403a1e330c9ec69fe1f52460a8936b66" "912cac216b96560654f4f15a3a4d8ba47d9c604cbc3b04801e465fb67a0234f0" default)))
 '(fci-rule-color "#4C566A")
 '(jdee-db-active-breakpoint-face-colors (cons "#191C25" "#81A1C1"))
 '(jdee-db-requested-breakpoint-face-colors (cons "#191C25" "#A3BE8C"))
 '(jdee-db-spec-breakpoint-face-colors (cons "#191C25" "#434C5E"))
 '(objed-cursor-color "#BF616A")
 '(package-selected-packages
   (quote
    (expand-region spacegray-theme subatomic-theme immaterial-theme emmet-mode spaceline dashboard which-key use-package smartparens railscasts-reloaded-theme flycheck elpy dracula-theme better-defaults autopair auto-complete)))
 '(pdf-view-midnight-colors (cons "#ECEFF4" "#2E3440"))
 '(rustic-ansi-faces
   ["#2E3440" "#BF616A" "#A3BE8C" "#EBCB8B" "#81A1C1" "#B48EAD" "#88C0D0" "#ECEFF4"])
 '(vc-annotate-background "#2E3440")
 '(vc-annotate-color-map
   (list
    (cons 20 "#A3BE8C")
    (cons 40 "#bbc28b")
    (cons 60 "#d3c68b")
    (cons 80 "#EBCB8B")
    (cons 100 "#e2b482")
    (cons 120 "#d99d79")
    (cons 140 "#D08770")
    (cons 160 "#c68984")
    (cons 180 "#bd8b98")
    (cons 200 "#B48EAD")
    (cons 220 "#b77f96")
    (cons 240 "#bb7080")
    (cons 260 "#BF616A")
    (cons 280 "#a05b67")
    (cons 300 "#815664")
    (cons 320 "#625161")
    (cons 340 "#4C566A")
    (cons 360 "#4C566A")))
 '(vc-annotate-very-old-color nil))
(custom-set-faces
 ;; custom-set-faces was added by Custom.
 ;; If you edit it by hand, you could mess it up, so be careful.
 ;; Your init file should contain only one such instance.
 ;; If there is more than one, they won't work right.
 '(custom-comment ((t (:background "dim gray" :slant italic))))
 '(font-lock-comment-face ((t (:foreground "#73d216" :slant italic)))))
