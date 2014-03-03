\ configurations: 
\  a = [1, 2]
\  b = [1, 3]
\  c = [1, 4]
\  d = [4, 2]

Maximize a + b + c + d

Subject To

 a + b + c     <= 6
 a         + d <= 3
     b         <= 2
         c + d <= 6

END
