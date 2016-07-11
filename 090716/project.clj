(defproject dojo "0.1.0-SNAPSHOT"
  :description "Coding Dojo"
  :url "https://github.com/coding-dojo-unb/dojo-days"
  :license {:name "Beerware 42"
            :url "http://people.freebsd.org/~phk/"}
  :dependencies [[org.clojure/clojure "1.7.0"]]
  :main ^:skip-aot dojo.core
  :target-path "target/%s"
  :profiles {:uberjar {:aot :all}})
