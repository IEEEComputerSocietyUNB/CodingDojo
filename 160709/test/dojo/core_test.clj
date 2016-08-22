(ns dojo.core-test
  (:require [clojure.test :refer :all]
            [dojo.core :refer :all]))

;(deftest nome-do-test
;  (testing "comentario de teste"
;    (is teste)))


;; negative ok
(deftest radi-negativo
  (testing "Entrada de radicando negativo"
    (is (= (sqrt2 -2.0 0.000001) -1.0)))
)

(deftest radi-zero
  (testing "Entrada de radicando zero"
    (is (= (sqrt2 0.0 0.000001) 0.0)))
)


;; raiz quadrada de 1 ok
(deftest radi-one
  (testing "Raiz quadrada de 1"
    (is (= (sqrt2 1.0 0.000001) 1.0))))

;; raiz quadrada de 4 ok
(deftest radi-four
  (testing "Raiz quadrada de 4"
    (is (and (< (sqrt2 4.0 0.000001) 2.1) (> (sqrt2 4.0 0.000001) 1.9)))))

;; raiz quadrada de 5 ok
(deftest rad-five
  (testing "raiz quadrada de 5"
   (is (precisao (- (sqrt2 5.0 0.000001) 2.3) 0.1))))

(deftest rad-seven
  (testing "raiz quadrada com alta precisao"
    (is (precisao (- (sqrt2 7.0 0.000001) 2.645751) 0.00001))))

(deftest rad-small-neg
  (testing "raiz quadrada de negativo pequeno"
    (is (precisao (- (sqrt2 -0.5 0.000001) -1.0) 0.00001))))



(deftest sqrt-java
  (testing "raiz quadrada nativa de java"
    (is (precisao (- (sqrt2 12.0 0.000001) (java.lang.Math/sqrt 12.0)) 0.00001)))
  )



(deftest precisao-1
  (testing "Teste dentro da margem de erro"
    (is (and
          (precisao -0.01 0.1)
          (not (precisao 0.2 0.1))))))

;(deftest neg-sqrt-test
;  (testing "Negative square root test"
;    (is (< (sqrt -1.0) 0))))
;
;(deftest one-sqrt-test
;  (testing "Square root of 1")
;    (is (= (sqrt 1) 1.0)))
;
;(deftest real-case-sqrt
;  (testing "Comparing to real square root implementation")
;    (is (< 0.000001 (- (sqrt 2.0) (java.lang.Math/sqrt 2.0)))))
;
;(deftest power-zero
;  (testing "Powering something to zero"
;    (is (= (power 25 0) 1))))
;
;(deftest power-negative
;  (testing "Powering something negative"
;    (is (< (power 25 (neg 1)) 0))))
;
;(deftest neg-zero
;  (testing "Negative zero"
;    (is (= 0.0 (neg 0.0)))))
;
