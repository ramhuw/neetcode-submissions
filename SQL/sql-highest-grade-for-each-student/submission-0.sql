-- Write your query below
WITH m AS (
    SELECT f.student_id, f.exam_id, f.score
    FROM exam_results AS f
    WHERE f.score >= ALL (
        SELECT e.score
        FROM exam_results e
        WHERE f.student_id = e.student_id
    )
)
SELECT *
FROM m
WHERE exam_id <= ALL (
    SELECT n.exam_id
    FROM m AS n
    WHERE n.student_id = m.student_id
)
ORDER BY student_id;