intToLetter :: Int -> Char
intToLetter i = toEnum (i + 96)

possibleCombinations :: Int -> [String]
possibleCombinations n = [[intToLetter i, intToLetter j, intToLetter k]
                            | i<- [1..26], j<- [1..26], k <- [1..26], i + j +k == n]


main = interact $ unlines. map (minimum . possibleCombinations) . tail . map read . words