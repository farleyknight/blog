# Clojure Basics

Clojure is a Lisp-based language, so you'll see lots of primitives that Lisp handles well have built-in language features:

Basic arithmetic.
```clojure
(+ 1 1) ; => 2
```

Equality.
```clojure
(= 1 1) ; => true
```

Logical operators.
```clojure
(not true) ; => false
```

Evaluating quoted forms.
```clojure
(eval '(+ 1 2)) ; => 3
```

Concatenating strings.
```clojure
(str "Hello" " " "World") ; => "Hello World"
```
