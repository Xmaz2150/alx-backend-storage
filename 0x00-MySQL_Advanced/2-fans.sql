-- ranks country origins of bands, ordered by the number of (non-unique) fans
-- SELECT: cols to display
-- GROUP BY: combines all rows with same origin/ aggregate by origin
-- ORDER BY: res in asc order
SELECT origin, SUM(fans) AS nb_fans
FROM metal_bands
GROUP BY origin
ORDER BY nb_fans DESC;
