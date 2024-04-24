-- list all bands with `Glam rock` as their main style
-- Column band_name, lifespan

SELECT band_name, (IF(split IS NULL, 2022, split) - formed) AS lifespan
FROM metal_bands
WHERE style LIKE('%Glam rock%');
