SELECT
  date_trunc('week', created) AS geotag_week,
  count(id)                   AS weekly_sum
FROM project_geotag
GROUP BY geotag_week;

SELECT
  project_geotag.photo_id,
  COUNT(id)
FROM project_geotag
GROUP BY project_geotag.photo_id;

SELECT DISTINCT ON (photo_id)
  photo_id,
  date_trunc('week', created)
FROM project_geotag
ORDER BY photo_id, created ASC;

SELECT
  date_trunc('week', created) AS week,
  COUNT(id)
FROM project_photo
WHERE rephoto_of_id IS NOT NULL
GROUP BY week
ORDER BY week;