#lang racket
(require 2htdp/image)

(let sierpinski ([n 8])
  (if (zero? n)
      (triangle 2 'solid 'blue)
      (let ([t (sierpinski (- n 1))])
        (freeze (above t (beside t t))))))