(ns dojo.core
  (:gen-class))

(defn precisao [ diffEst margemError ]
  (and (< diffEst margemError) (> diffEst (- 0 margemError) ))
)


(defn sqqrAux [ G X margem]
  (let [newG (/ (+ G (/ X G)) 2.0)]
    (if (precisao (- newG G) margem )
      newG
      (sqqrAux newG X margem) )))


;; Raiz quadrada, com negativo ok
(defn sqrt2 [numero margemError]
  (if (= 0.0 numero)
    0.0
    (if (< 0.0 numero)
      (sqqrAux 1.0 numero margemError)
      -1.0)))

;; definicao de funcao simples
(defn studify [x] x)

;; uso do let
(defn more-stupid [x]
  (let [u x]
    u))

;; devolve o a variavel value se ela for
;; menor que o limite, ou o limite caso contrario
(defn moses [limit value]
  (if (< limit value)
    limit
    value))

;; calcula x ao quadrado
(defn sq [x]
  (* x x))

;; DOJO


;; funcao principal
(defn -main
  "Welcome to the dojo"
  [& args]
  (println (moses 10 12)))
