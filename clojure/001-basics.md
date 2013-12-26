# Clojure Basics

Clojure is a Lisp-based language, so you'll see lots of primitives that Lisp handles well have built-in language features:

## Basic arithmetic.

The addition, subtraction, multiplication and division operators.

```clojure
(+ 1 1)   ; => 2
(- 1 2)   ; => 1
(* 1 2 3) ; => 6
(/ 1 0)   ; => ArithmeticException Divide by zero
```

## Tests for equality.

The [equals](http://clojuredocs.org/clojure_core/clojure.core/=) function.

```clojure
(= 1 1) ; => true
```

## Logical operations.

The [and](http://clojuredocs.org/clojure_core/clojure.core/and) and [or](http://clojuredocs.org/clojure_core/clojure.core/or) operators with the special form [if](http://clojuredocs.org/clojure_core/clojure.core/if).

```clojure
(not true)       ; => false
(and true false) ; => false
(if true 1 2)    ; => 1
```

## Evaluating quoted forms.
```clojure
(eval '(+ 1 2)) ; => 3
```

## Concatenating strings.
```clojure
(str "Hello" " " "World") ; => "Hello World"
```
