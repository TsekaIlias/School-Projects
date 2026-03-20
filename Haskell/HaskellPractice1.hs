module Assignment where

piVal :: Double
piVal = 3.14159


circleArea :: Double -> Double
circleArea r = piVal * r * r

factorial :: Integer -> Integer
factorial x
  | x < 0     = error "Negative input not allowed"
  | x == 0    = 1
  | otherwise = x * factorial (x - 1)

myLength :: [a] -> Int
myLength [] = 0
myLength (x:xs) = 1 + myLength xs

applyToList :: (Int -> Int) -> [Int] -> [Int]
applyToList f x = map f x

addPair :: (Int, Int) -> Int
addPair (x, y) = x + y

squaredEvens :: [Int] -> [Int]
squaredEvens x = map (^2) (filter even x)

evenSquares :: Int -> [Int]
evenSquares n = [x^2 | x <- [1..n], even x]

greaterThan :: Int -> [Int] -> [Int]
greaterThan n x = filter (> n) x

gt5 :: [Int] -> [Int]
gt5 x = greaterThan 5 x

gt10 :: [Int] -> [Int]
gt10 x = greaterThan 10 x
