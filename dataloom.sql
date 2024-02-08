



SELECT 
    user.id, user.name
FROM 
    posts post
LEFT JOIN 
    users u
    ON user.id = post.userId
WHERE 
    post.id = 2;