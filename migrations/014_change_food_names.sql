UPDATE foods
SET name = CASE id
    WHEN 1 THEN 'Oatmeal - multigrain'
    WHEN 5 THEN 'Oatmeal - instant'
    WHEN 7 THEN 'Bread - whole grain'
    WHEN 8 THEN 'Bread - white'
    WHEN 9 THEN 'Bread - baguette'
    WHEN 10 THEN 'Milk - whole'
    WHEN 11 THEN 'Milk - skim'
    WHEN 12 THEN 'Yogurt - greek sweetened'
    WHEN 13 THEN 'Yogurt - greek low fat'
    WHEN 14 THEN 'Milk - chocolate'
    WHEN 15 THEN 'Milk - soy'
    WHEN 16 THEN 'Juice - tomato'
    WHEN 17 THEN 'Juice - apple'
    WHEN 18 THEN 'Juice - orange'
    WHEN 19 THEN 'Nuts - peanuts'
    WHEN 20 THEN 'Nuts - cashews'
END
WHERE id IN (1,5,7,8,9,10,11,12,13,14,15,16,17,18,19,20);