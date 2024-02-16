import Control.Monad
import Data.List

beautifulPairs :: Int -> Int -> [Int] -> Int
beautifulPairs x y arr = length [(i, j) | i <- [0..n-1], j <- [i+1..n-1], ((arr !! i + arr !! j) `mod` x == 0) && ((arr !! i - arr !! j) `mod` y == 0)]
    where n = length arr

main :: IO ()
main = do
    t <- readLn :: IO Int
    replicateM_ t $ do
        [n, x, y] <- map read . words <$> getLine :: IO [Int]
        arr <- map read . words <$> getLine :: IO [Int]
        print $ beautifulPairs x y arr




