
[2024-02-05 08:23:05.805600] : Dataloom[postgres]: DROP TABLE IF EXISTS "posts" CASCADE;
[2024-02-05 08:23:05.859303] : Dataloom[postgres]: CREATE TABLE IF NOT EXISTS "posts" ("completed" BOOLEAN DEFAULT False, "id" BIGSERIAL PRIMARY KEY UNIQUE NOT NULL, "title" VARCHAR(255) NOT NULL, "createdAt" TIMESTAMP DEFAULT CURRENT_TIMESTAMP, "updatedAt" TIMESTAMP DEFAULT CURRENT_TIMESTAMP, "userId" BIGSERIAL NOT NULL REFERENCES "users"("id") ON DELETE CASCADE ON UPDATE CASCADE);
[2024-02-05 08:23:05.917871] : Dataloom[postgres]: DROP TABLE IF EXISTS "users" CASCADE;
[2024-02-05 08:23:05.950865] : Dataloom[postgres]: CREATE TABLE IF NOT EXISTS "users" ("id" BIGSERIAL PRIMARY KEY UNIQUE NOT NULL, "name" TEXT NOT NULL DEFAULT 'Bob', "username" VARCHAR(255) UNIQUE);
[2024-02-05 08:23:05.988127] : Dataloom[postgres]: SELECT tablename FROM pg_catalog.pg_tables WHERE schemaname='public';
[2024-02-05 08:23:06.031117] : Dataloom[postgres]: INSERT INTO "users" ("username") VALUES (%s) RETURNING "id";
[2024-02-05 08:23:06.059674] : Dataloom[postgres]: INSERT INTO "posts" ("title", "userId") VALUES (%s, %s) RETURNING *;
[2024-02-05 08:23:06.093643] : Dataloom[postgres]: 
        SELECT 
            parent.id AS "posts_id", parent.completed AS "posts_completed"
            user.id AS "users_id"
        FROM 
            posts parent
        JOIN users user ON parent.userId = user.id 
        WHERE 
            parent."id" = %s;
    
[2024-02-05 08:26:55.146964] : Dataloom[postgres]: DROP TABLE IF EXISTS "posts" CASCADE;
[2024-02-05 08:26:55.184905] : Dataloom[postgres]: CREATE TABLE IF NOT EXISTS "posts" ("completed" BOOLEAN DEFAULT False, "id" BIGSERIAL PRIMARY KEY UNIQUE NOT NULL, "title" VARCHAR(255) NOT NULL, "createdAt" TIMESTAMP DEFAULT CURRENT_TIMESTAMP, "updatedAt" TIMESTAMP DEFAULT CURRENT_TIMESTAMP, "userId" BIGSERIAL NOT NULL REFERENCES "users"("id") ON DELETE CASCADE ON UPDATE CASCADE);
[2024-02-05 08:26:55.231541] : Dataloom[postgres]: DROP TABLE IF EXISTS "users" CASCADE;
[2024-02-05 08:26:55.267539] : Dataloom[postgres]: CREATE TABLE IF NOT EXISTS "users" ("id" BIGSERIAL PRIMARY KEY UNIQUE NOT NULL, "name" TEXT NOT NULL DEFAULT 'Bob', "username" VARCHAR(255) UNIQUE);
[2024-02-05 08:26:55.306759] : Dataloom[postgres]: SELECT tablename FROM pg_catalog.pg_tables WHERE schemaname='public';
[2024-02-05 08:26:55.342756] : Dataloom[postgres]: INSERT INTO "users" ("username") VALUES (%s) RETURNING "id";
[2024-02-05 08:26:55.368874] : Dataloom[postgres]: INSERT INTO "posts" ("title", "userId") VALUES (%s, %s) RETURNING *;
[2024-02-05 08:26:55.397764] : Dataloom[postgres]: 
        SELECT 
            parent.id AS "posts_id", parent.completed AS "posts_completed",
            user.id AS "users_id"
        FROM 
            posts parent
        JOIN users user ON parent.userId = user.id 
        WHERE 
            parent."id" = %s;
    
[2024-02-05 08:30:52.016967] : Dataloom[postgres]: DROP TABLE IF EXISTS "posts" CASCADE;
[2024-02-05 08:30:52.083917] : Dataloom[postgres]: CREATE TABLE IF NOT EXISTS "posts" ("completed" BOOLEAN DEFAULT False, "id" BIGSERIAL PRIMARY KEY UNIQUE NOT NULL, "title" VARCHAR(255) NOT NULL, "createdAt" TIMESTAMP DEFAULT CURRENT_TIMESTAMP, "updatedAt" TIMESTAMP DEFAULT CURRENT_TIMESTAMP, "userId" BIGSERIAL NOT NULL REFERENCES "users"("id") ON DELETE CASCADE ON UPDATE CASCADE);
[2024-02-05 08:30:52.157670] : Dataloom[postgres]: DROP TABLE IF EXISTS "users" CASCADE;
[2024-02-05 08:30:52.217984] : Dataloom[postgres]: CREATE TABLE IF NOT EXISTS "users" ("id" BIGSERIAL PRIMARY KEY UNIQUE NOT NULL, "name" TEXT NOT NULL DEFAULT 'Bob', "username" VARCHAR(255) UNIQUE);
[2024-02-05 08:30:52.283663] : Dataloom[postgres]: SELECT tablename FROM pg_catalog.pg_tables WHERE schemaname='public';
[2024-02-05 08:30:52.345516] : Dataloom[postgres]: INSERT INTO "users" ("username") VALUES (%s) RETURNING "id";
[2024-02-05 08:30:52.392524] : Dataloom[postgres]: INSERT INTO "posts" ("title", "userId") VALUES (%s, %s) RETURNING *;
[2024-02-05 08:30:52.437507] : Dataloom[postgres]: 
        SELECT 
            parent.id AS "posts_id", parent.completed AS "posts_completed",
            user_alias.id AS "users_id"
        FROM 
            posts parent
        JOIN users user_alias ON parent.userId = user_alias.id 
        WHERE 
            parent."id" = %s;
    
[2024-02-05 08:34:29.648321] : Dataloom[postgres]: DROP TABLE IF EXISTS "posts" CASCADE;
[2024-02-05 08:34:29.691306] : Dataloom[postgres]: CREATE TABLE IF NOT EXISTS "posts" ("completed" BOOLEAN DEFAULT False, "id" BIGSERIAL PRIMARY KEY UNIQUE NOT NULL, "title" VARCHAR(255) NOT NULL, "createdAt" TIMESTAMP DEFAULT CURRENT_TIMESTAMP, "updatedAt" TIMESTAMP DEFAULT CURRENT_TIMESTAMP, "userId" BIGSERIAL NOT NULL REFERENCES "users"("id") ON DELETE CASCADE ON UPDATE CASCADE);
[2024-02-05 08:34:29.739025] : Dataloom[postgres]: DROP TABLE IF EXISTS "users" CASCADE;
[2024-02-05 08:34:29.775053] : Dataloom[postgres]: CREATE TABLE IF NOT EXISTS "users" ("id" BIGSERIAL PRIMARY KEY UNIQUE NOT NULL, "name" TEXT NOT NULL DEFAULT 'Bob', "username" VARCHAR(255) UNIQUE);
[2024-02-05 08:34:29.812051] : Dataloom[postgres]: SELECT tablename FROM pg_catalog.pg_tables WHERE schemaname='public';
[2024-02-05 08:34:29.849037] : Dataloom[postgres]: INSERT INTO "users" ("username") VALUES (%s) RETURNING "id";
[2024-02-05 08:34:29.877008] : Dataloom[postgres]: INSERT INTO "posts" ("title", "userId") VALUES (%s, %s) RETURNING *;
[2024-02-05 08:34:29.908998] : Dataloom[postgres]: 
        SELECT 
            parent.id AS "posts_id", parent.completed AS "posts_completed",
            child_user.id AS "users_id"
        FROM 
            posts parent
        JOIN users child_user ON parent."userId" = child_user.id 
        WHERE 
            parent."id" = %s;
    
[2024-02-05 09:32:12.010664] : Dataloom[mysql]: DROP TABLE IF EXISTS `users`;
[2024-02-05 09:32:12.058657] : Dataloom[mysql]: DROP TABLE IF EXISTS `users`;
[2024-02-05 09:32:12.094142] : Dataloom[mysql]: DROP TABLE IF EXISTS `users`;
[2024-02-05 09:32:12.104213] : Dataloom[mysql]: CREATE TABLE IF NOT EXISTS `users` (`id` INT PRIMARY KEY AUTO_INCREMENT UNIQUE NOT NULL, `name` VARCHAR(255), `username` TEXT NOT NULL);
[2024-02-05 09:32:12.149374] : Dataloom[mysql]: DROP TABLE IF EXISTS `posts`;
[2024-02-05 09:32:12.172721] : Dataloom[mysql]: CREATE TABLE IF NOT EXISTS `posts` (`id` INT PRIMARY KEY AUTO_INCREMENT UNIQUE NOT NULL, `title` TEXT NOT NULL);
[2024-02-05 09:32:12.209014] : Dataloom[mysql]: SHOW TABLES;
[2024-02-05 09:32:12.226290] : Dataloom[mysql]: DROP TABLE IF EXISTS `users`;
[2024-02-05 09:32:12.268988] : Dataloom[mysql]: CREATE TABLE IF NOT EXISTS `users` (`id` INT PRIMARY KEY AUTO_INCREMENT UNIQUE NOT NULL, `name` VARCHAR(255) UNIQUE, `username` VARCHAR(255) NOT NULL DEFAULT 'Hello there!!');
[2024-02-05 09:32:12.311930] : Dataloom[mysql]: DROP TABLE IF EXISTS `posts`;
[2024-02-05 09:32:12.338287] : Dataloom[mysql]: CREATE TABLE IF NOT EXISTS `posts` (`completed` BOOLEAN DEFAULT False, `id` INT PRIMARY KEY AUTO_INCREMENT UNIQUE NOT NULL, `title` VARCHAR(255) NOT NULL);
[2024-02-05 09:32:12.410967] : Dataloom[mysql]: SHOW TABLES;
[2024-02-05 09:32:12.433340] : Dataloom[mysql]: DROP TABLE IF EXISTS `posts`;
[2024-02-05 09:32:12.509835] : Dataloom[mysql]: CREATE TABLE IF NOT EXISTS `posts` (`completed` BOOLEAN DEFAULT False, `id` INT PRIMARY KEY AUTO_INCREMENT UNIQUE NOT NULL, `title` VARCHAR(255) NOT NULL, `createdAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP, `updatedAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP, `userId` INT NOT NULL REFERENCES `users`(`id`) ON DELETE CASCADE ON UPDATE CASCADE);
[2024-02-05 09:32:12.545060] : Dataloom[mysql]: DROP TABLE IF EXISTS `users`;
[2024-02-05 09:32:12.575171] : Dataloom[mysql]: CREATE TABLE IF NOT EXISTS `users` (`id` INT PRIMARY KEY AUTO_INCREMENT UNIQUE NOT NULL, `name` VARCHAR(255) NOT NULL DEFAULT 'Bob', `username` VARCHAR(255) UNIQUE, `createdAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP, `updatedAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP);
[2024-02-05 09:32:12.612805] : Dataloom[mysql]: SHOW TABLES;
[2024-02-05 09:32:12.622412] : Dataloom[mysql]: INSERT INTO `users` (`name`, `username`) VALUES (%s, %s);
[2024-02-05 09:32:12.632562] : Dataloom[mysql]: DELETE FROM `users` WHERE `id` = %s;
[2024-02-05 09:32:12.645561] : Dataloom[mysql]: DELETE FROM `users` WHERE `id` = %s;
[2024-02-05 09:32:12.669557] : Dataloom[mysql]: DROP TABLE IF EXISTS `posts`;
[2024-02-05 09:32:12.710874] : Dataloom[mysql]: CREATE TABLE IF NOT EXISTS `posts` (`completed` BOOLEAN DEFAULT False, `id` INT PRIMARY KEY AUTO_INCREMENT UNIQUE NOT NULL, `title` VARCHAR(255) NOT NULL, `createdAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP, `updatedAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP, `userId` INT NOT NULL REFERENCES `users`(`id`) ON DELETE CASCADE ON UPDATE CASCADE);
[2024-02-05 09:32:12.746619] : Dataloom[mysql]: DROP TABLE IF EXISTS `users`;
[2024-02-05 09:32:12.782673] : Dataloom[mysql]: CREATE TABLE IF NOT EXISTS `users` (`id` INT PRIMARY KEY AUTO_INCREMENT UNIQUE NOT NULL, `name` VARCHAR(255) NOT NULL DEFAULT 'Bob', `username` VARCHAR(255) UNIQUE, `createdAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP, `updatedAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP);
[2024-02-05 09:32:12.817779] : Dataloom[mysql]: SHOW TABLES;
[2024-02-05 09:32:12.826817] : Dataloom[mysql]: INSERT INTO `users` (`name`, `username`) VALUES (%s, %s);
[2024-02-05 09:32:12.837360] : Dataloom[mysql]: 
    DELETE FROM `users` WHERE `id` IN (
       SELECT `id` FROM  (
                SELECT `id` FROM `users` WHERE `name` = %s LIMIT 1
        ) AS subquery
    );
    
[2024-02-05 09:32:12.847450] : Dataloom[mysql]: SELECT `createdAt`, `id`, `name`, `updatedAt`, `username` FROM `users` WHERE `name` = %s   ;
[2024-02-05 09:32:12.856097] : Dataloom[mysql]: 
    DELETE FROM `users` WHERE `id` IN (
       SELECT `id` FROM  (
                SELECT `id` FROM `users` WHERE `name` = %s AND `id` = %s LIMIT 1
        ) AS subquery
    );
    
[2024-02-05 09:32:12.864064] : Dataloom[mysql]: SELECT `createdAt`, `id`, `name`, `updatedAt`, `username` FROM `users` WHERE `name` = %s   ;
[2024-02-05 09:32:12.872064] : Dataloom[mysql]: 
    DELETE FROM `users` WHERE `id` IN (
       SELECT `id` FROM  (
                SELECT `id` FROM `users` WHERE `name` = %s AND `id` = %s LIMIT 1
        ) AS subquery
    );
    
[2024-02-05 09:32:12.882369] : Dataloom[mysql]: SELECT `createdAt`, `id`, `name`, `updatedAt`, `username` FROM `users` WHERE `name` = %s   ;
[2024-02-05 09:32:12.905371] : Dataloom[mysql]: DROP TABLE IF EXISTS `posts`;
[2024-02-05 09:32:12.941893] : Dataloom[mysql]: CREATE TABLE IF NOT EXISTS `posts` (`completed` BOOLEAN DEFAULT False, `id` INT PRIMARY KEY AUTO_INCREMENT UNIQUE NOT NULL, `title` VARCHAR(255) NOT NULL, `createdAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP, `updatedAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP, `userId` INT NOT NULL REFERENCES `users`(`id`) ON DELETE CASCADE ON UPDATE CASCADE);
[2024-02-05 09:32:12.976607] : Dataloom[mysql]: DROP TABLE IF EXISTS `users`;
[2024-02-05 09:32:13.006703] : Dataloom[mysql]: CREATE TABLE IF NOT EXISTS `users` (`id` INT PRIMARY KEY AUTO_INCREMENT UNIQUE NOT NULL, `name` VARCHAR(255) NOT NULL DEFAULT 'Bob', `username` VARCHAR(255) UNIQUE, `createdAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP, `updatedAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP);
[2024-02-05 09:32:13.044096] : Dataloom[mysql]: SHOW TABLES;
[2024-02-05 09:32:13.054186] : Dataloom[mysql]: INSERT INTO `users` (`name`, `username`) VALUES (%s, %s);
[2024-02-05 09:32:13.064985] : Dataloom[mysql]: DELETE FROM `users` WHERE `name` = %s;
[2024-02-05 09:32:13.073984] : Dataloom[mysql]: SELECT `createdAt`, `id`, `name`, `updatedAt`, `username` FROM `users` WHERE `name` = %s   ;
[2024-02-05 09:32:13.082148] : Dataloom[mysql]: INSERT INTO `users` (`name`, `username`) VALUES (%s, %s);
[2024-02-05 09:32:13.092135] : Dataloom[mysql]: DELETE FROM `users` WHERE `name` = %s AND `id` = %s;
[2024-02-05 09:32:13.100141] : Dataloom[mysql]: SELECT `createdAt`, `id`, `name`, `updatedAt`, `username` FROM `users` WHERE `name` = %s   ;
[2024-02-05 09:32:13.108749] : Dataloom[mysql]: DELETE FROM `users` WHERE `name` = %s AND `id` = %s;
[2024-02-05 09:32:13.117749] : Dataloom[mysql]: SELECT `createdAt`, `id`, `name`, `updatedAt`, `username` FROM `users` WHERE `name` = %s   ;
[2024-02-05 09:32:13.136478] : Dataloom[mysql]: DROP TABLE IF EXISTS `posts`;
[2024-02-05 09:32:13.203213] : Dataloom[mysql]: CREATE TABLE IF NOT EXISTS `posts` (`completed` BOOLEAN DEFAULT False, `id` INT PRIMARY KEY AUTO_INCREMENT UNIQUE NOT NULL, `title` VARCHAR(255) NOT NULL, `createdAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP, `updatedAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP, `userId` INT NOT NULL REFERENCES `users`(`id`) ON DELETE CASCADE ON UPDATE CASCADE);
[2024-02-05 09:32:13.260210] : Dataloom[mysql]: DROP TABLE IF EXISTS `users`;
[2024-02-05 09:32:13.293210] : Dataloom[mysql]: CREATE TABLE IF NOT EXISTS `users` (`id` INT PRIMARY KEY AUTO_INCREMENT UNIQUE NOT NULL, `name` VARCHAR(255) NOT NULL DEFAULT 'Bob', `username` VARCHAR(255) UNIQUE, `createdAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP, `updatedAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP);
[2024-02-05 09:32:13.327210] : Dataloom[mysql]: SHOW TABLES;
[2024-02-05 09:32:13.336209] : Dataloom[mysql]: INSERT INTO `users` (`username`) VALUES (%s);
[2024-02-05 09:32:13.345209] : Dataloom[mysql]: INSERT INTO `posts` (`title`, `userId`) VALUES (%s, %s);
[2024-02-05 09:32:13.363211] : Dataloom[mysql]: DROP TABLE IF EXISTS `posts`;
[2024-02-05 09:32:13.399243] : Dataloom[mysql]: CREATE TABLE IF NOT EXISTS `posts` (`completed` BOOLEAN DEFAULT False, `id` INT PRIMARY KEY AUTO_INCREMENT UNIQUE NOT NULL, `title` VARCHAR(255) NOT NULL, `createdAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP, `updatedAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP, `userId` INT NOT NULL REFERENCES `users`(`id`) ON DELETE CASCADE ON UPDATE CASCADE);
[2024-02-05 09:32:13.437241] : Dataloom[mysql]: DROP TABLE IF EXISTS `users`;
[2024-02-05 09:32:13.469241] : Dataloom[mysql]: CREATE TABLE IF NOT EXISTS `users` (`id` INT PRIMARY KEY AUTO_INCREMENT UNIQUE NOT NULL, `name` VARCHAR(255) NOT NULL DEFAULT 'Bob', `username` VARCHAR(255) UNIQUE, `createdAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP, `updatedAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP);
[2024-02-05 09:32:13.503508] : Dataloom[mysql]: SHOW TABLES;
[2024-02-05 09:32:13.512508] : Dataloom[mysql]: INSERT INTO `users` (`username`) VALUES (%s);
[2024-02-05 09:32:13.522728] : Dataloom[mysql]: INSERT INTO `posts` (`title`, `userId`) VALUES (%s, %s);
[2024-02-05 09:32:13.546724] : Dataloom[mysql]: DROP TABLE IF EXISTS `posts`;
[2024-02-05 09:32:13.584649] : Dataloom[mysql]: CREATE TABLE IF NOT EXISTS `posts` (`completed` BOOLEAN DEFAULT False, `id` INT PRIMARY KEY AUTO_INCREMENT UNIQUE NOT NULL, `title` VARCHAR(255) NOT NULL, `createdAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP, `updatedAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP, `userId` INT NOT NULL REFERENCES `users`(`id`) ON DELETE CASCADE ON UPDATE CASCADE);
[2024-02-05 09:32:13.620989] : Dataloom[mysql]: DROP TABLE IF EXISTS `users`;
[2024-02-05 09:32:13.652505] : Dataloom[mysql]: CREATE TABLE IF NOT EXISTS `users` (`id` INT PRIMARY KEY AUTO_INCREMENT UNIQUE NOT NULL, `name` VARCHAR(255) NOT NULL DEFAULT 'Bob', `username` VARCHAR(255) UNIQUE);
[2024-02-05 09:32:13.681139] : Dataloom[mysql]: SHOW TABLES;
[2024-02-05 09:32:13.691162] : Dataloom[mysql]: INSERT INTO `users` (`username`) VALUES (%s);
[2024-02-05 09:32:13.701252] : Dataloom[mysql]: INSERT INTO `posts` (`title`, `userId`) VALUES (%s, %s);
[2024-02-05 09:32:13.712252] : Dataloom[mysql]: SELECT `id`, `name`, `username` FROM `users` WHERE `id` = %s;
[2024-02-05 09:32:13.723217] : Dataloom[mysql]: SELECT `id`, `name`, `username` FROM `users` WHERE `id` = %s;
[2024-02-05 09:32:13.732217] : Dataloom[mysql]: SELECT `id`, `completed` FROM `posts` WHERE `id` = %s;
[2024-02-05 09:32:13.749963] : Dataloom[mysql]: DROP TABLE IF EXISTS `posts`;
[2024-02-05 09:32:13.786840] : Dataloom[mysql]: CREATE TABLE IF NOT EXISTS `posts` (`completed` BOOLEAN DEFAULT False, `id` INT PRIMARY KEY AUTO_INCREMENT UNIQUE NOT NULL, `title` VARCHAR(255) NOT NULL, `createdAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP, `updatedAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP, `userId` INT NOT NULL REFERENCES `users`(`id`) ON DELETE CASCADE ON UPDATE CASCADE);
[2024-02-05 09:32:13.822272] : Dataloom[mysql]: DROP TABLE IF EXISTS `users`;
[2024-02-05 09:32:13.845669] : Dataloom[mysql]: CREATE TABLE IF NOT EXISTS `users` (`id` INT PRIMARY KEY AUTO_INCREMENT UNIQUE NOT NULL, `name` VARCHAR(255) NOT NULL DEFAULT 'Bob', `username` VARCHAR(255) UNIQUE);
[2024-02-05 09:32:13.881472] : Dataloom[mysql]: SHOW TABLES;
[2024-02-05 09:32:13.890355] : Dataloom[mysql]: INSERT INTO `users` (`username`) VALUES (%s);
[2024-02-05 09:32:13.899703] : Dataloom[mysql]: INSERT INTO `posts` (`title`, `userId`) VALUES (%s, %s);
[2024-02-05 09:32:13.910706] : Dataloom[mysql]: SELECT `id`, `name`, `username` FROM `users`   ;
[2024-02-05 09:32:13.920169] : Dataloom[mysql]: SELECT `completed`, `createdAt`, `id`, `title`, `updatedAt`, `userId` FROM `posts`   ;
[2024-02-05 09:32:13.928169] : Dataloom[mysql]: SELECT `id`, `completed` FROM `posts`  LIMIT 3 OFFSET 3;
[2024-02-05 09:32:13.952389] : Dataloom[mysql]: DROP TABLE IF EXISTS `posts`;
[2024-02-05 09:32:13.989504] : Dataloom[mysql]: CREATE TABLE IF NOT EXISTS `posts` (`completed` BOOLEAN DEFAULT False, `id` INT PRIMARY KEY AUTO_INCREMENT UNIQUE NOT NULL, `title` VARCHAR(255) NOT NULL, `createdAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP, `updatedAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP, `userId` INT NOT NULL REFERENCES `users`(`id`) ON DELETE CASCADE ON UPDATE CASCADE);
[2024-02-05 09:32:14.023560] : Dataloom[mysql]: DROP TABLE IF EXISTS `users`;
[2024-02-05 09:32:14.055111] : Dataloom[mysql]: CREATE TABLE IF NOT EXISTS `users` (`id` INT PRIMARY KEY AUTO_INCREMENT UNIQUE NOT NULL, `name` VARCHAR(255) NOT NULL DEFAULT 'Bob', `username` VARCHAR(255) UNIQUE);
[2024-02-05 09:32:14.088568] : Dataloom[mysql]: SHOW TABLES;
[2024-02-05 09:32:14.097250] : Dataloom[mysql]: INSERT INTO `users` (`username`) VALUES (%s);
[2024-02-05 09:32:14.107254] : Dataloom[mysql]: INSERT INTO `posts` (`title`, `userId`) VALUES (%s, %s);
[2024-02-05 09:32:14.119087] : Dataloom[mysql]: SELECT `id`, `name`, `username` FROM `users` WHERE `id` = %s   ;
[2024-02-05 09:32:14.127022] : Dataloom[mysql]: SELECT `id`, `name`, `username` FROM `users` WHERE `id` = %s   ;
[2024-02-05 09:32:14.135430] : Dataloom[mysql]: SELECT `id`, `name`, `username` FROM `users` WHERE `id` = %s AND `name` = %s   ;
[2024-02-05 09:32:14.143430] : Dataloom[mysql]: SELECT `id`, `name`, `username` FROM `users` WHERE `id` = %s AND `username` = %s   ;
[2024-02-05 09:32:14.153432] : Dataloom[mysql]: SELECT `id`, `name`, `username` FROM `users` WHERE `name` = %s AND `username` = %s   ;
[2024-02-05 09:32:14.161827] : Dataloom[mysql]: SELECT `id`, `completed` FROM `posts`   ;
[2024-02-05 09:32:14.179798] : Dataloom[mysql]: DROP TABLE IF EXISTS `posts`;
[2024-02-05 09:32:14.220245] : Dataloom[mysql]: CREATE TABLE IF NOT EXISTS `posts` (`completed` BOOLEAN DEFAULT False, `id` INT PRIMARY KEY AUTO_INCREMENT UNIQUE NOT NULL, `title` VARCHAR(255) NOT NULL, `createdAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP, `updatedAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP, `userId` INT NOT NULL REFERENCES `users`(`id`) ON DELETE CASCADE ON UPDATE CASCADE);
[2024-02-05 09:32:14.250406] : Dataloom[mysql]: DROP TABLE IF EXISTS `users`;
[2024-02-05 09:32:14.282957] : Dataloom[mysql]: CREATE TABLE IF NOT EXISTS `users` (`id` INT PRIMARY KEY AUTO_INCREMENT UNIQUE NOT NULL, `name` VARCHAR(255) NOT NULL DEFAULT 'Bob', `username` VARCHAR(255) UNIQUE);
[2024-02-05 09:32:14.323384] : Dataloom[mysql]: SHOW TABLES;
[2024-02-05 09:32:14.332698] : Dataloom[mysql]: INSERT INTO `users` (`username`) VALUES (%s);
[2024-02-05 09:32:14.341821] : Dataloom[mysql]: INSERT INTO `posts` (`title`, `userId`) VALUES (%s, %s);
[2024-02-05 09:32:14.352820] : Dataloom[mysql]: SELECT `completed`, `createdAt`, `id`, `title`, `updatedAt`, `userId` FROM `posts` WHERE `id` = %s AND `userId` = %s   ;
[2024-02-05 09:32:14.360885] : Dataloom[mysql]: SELECT `id`, `name`, `username` FROM `users`   ;
[2024-02-05 09:32:14.368884] : Dataloom[mysql]: SELECT `id`, `name`, `username` FROM `users` WHERE `id` = %s   ;
[2024-02-05 09:32:14.377710] : Dataloom[mysql]: SELECT `id`, `name`, `username` FROM `users` WHERE `id` = %s   ;
[2024-02-05 09:32:14.385676] : Dataloom[mysql]: SELECT `id`, `name`, `username` FROM `users` WHERE `id` = %s AND `name` = %s   ;
[2024-02-05 09:32:14.394679] : Dataloom[mysql]: SELECT `id`, `name`, `username` FROM `users` WHERE `id` = %s AND `username` = %s   ;
[2024-02-05 09:32:14.402554] : Dataloom[mysql]: SELECT `id`, `name`, `username` FROM `users` WHERE `name` = %s AND `username` = %s   ;
[2024-02-05 09:32:14.410589] : Dataloom[mysql]: SELECT `id`, `completed` FROM `posts` WHERE `userId` = %s  LIMIT 3 OFFSET 3;
[2024-02-05 09:32:14.419357] : Dataloom[mysql]: SELECT `completed`, `createdAt`, `id`, `title`, `updatedAt`, `userId` FROM `posts`   ;
[2024-02-05 09:32:14.435793] : Dataloom[mysql]: DROP TABLE IF EXISTS `posts`;
[2024-02-05 09:32:14.467792] : Dataloom[mysql]: CREATE TABLE IF NOT EXISTS `posts` (`completed` BOOLEAN DEFAULT False, `id` INT PRIMARY KEY AUTO_INCREMENT UNIQUE NOT NULL, `title` VARCHAR(255) NOT NULL, `createdAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP, `updatedAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP, `userId` INT NOT NULL REFERENCES `users`(`id`) ON DELETE CASCADE ON UPDATE CASCADE);
[2024-02-05 09:32:14.508815] : Dataloom[mysql]: DROP TABLE IF EXISTS `users`;
[2024-02-05 09:32:14.537496] : Dataloom[mysql]: CREATE TABLE IF NOT EXISTS `users` (`id` INT PRIMARY KEY AUTO_INCREMENT UNIQUE NOT NULL, `name` VARCHAR(255) NOT NULL DEFAULT 'Bob', `username` VARCHAR(255) UNIQUE, `createdAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP, `updatedAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP);
[2024-02-05 09:32:14.572649] : Dataloom[mysql]: SHOW TABLES;
[2024-02-05 09:32:14.584641] : Dataloom[mysql]: INSERT INTO `users` (`username`) VALUES (%s);
[2024-02-05 09:32:14.594561] : Dataloom[mysql]: INSERT INTO `posts` (`title`, `userId`) VALUES (%s, %s);
[2024-02-05 09:32:14.657448] : Dataloom[mysql]: UPDATE `users` SET `updatedAt` = %s WHERE `id` = %s;
[2024-02-05 09:32:14.667487] : Dataloom[mysql]: UPDATE `users` SET `updatedAt` = %s WHERE `id` = %s;
[2024-02-05 09:32:14.676752] : Dataloom[mysql]: SELECT `createdAt`, `id`, `name`, `updatedAt`, `username` FROM `users` WHERE `id` = %s;
[2024-02-05 09:32:14.684796] : Dataloom[mysql]: UPDATE `users` SET `id` = %s, `updatedAt` = %s WHERE `id` = %s;
[2024-02-05 09:32:14.703794] : Dataloom[mysql]: DROP TABLE IF EXISTS `posts`;
[2024-02-05 09:32:14.743616] : Dataloom[mysql]: CREATE TABLE IF NOT EXISTS `posts` (`completed` BOOLEAN DEFAULT False, `id` INT PRIMARY KEY AUTO_INCREMENT UNIQUE NOT NULL, `title` VARCHAR(255) NOT NULL, `createdAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP, `userId` INT NOT NULL REFERENCES `users`(`id`) ON DELETE CASCADE ON UPDATE CASCADE);
[2024-02-05 09:32:14.777109] : Dataloom[mysql]: DROP TABLE IF EXISTS `users`;
[2024-02-05 09:32:14.810423] : Dataloom[mysql]: CREATE TABLE IF NOT EXISTS `users` (`id` INT PRIMARY KEY AUTO_INCREMENT UNIQUE NOT NULL, `name` VARCHAR(255) NOT NULL DEFAULT 'Bob', `username` VARCHAR(255) UNIQUE, `createdAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP, `updatedAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP);
[2024-02-05 09:32:14.845095] : Dataloom[mysql]: SHOW TABLES;
[2024-02-05 09:32:14.856097] : Dataloom[mysql]: INSERT INTO `users` (`username`) VALUES (%s);
[2024-02-05 09:32:14.866572] : Dataloom[mysql]: INSERT INTO `posts` (`title`, `userId`) VALUES (%s, %s);
[2024-02-05 09:32:14.929541] : Dataloom[mysql]: 
        UPDATE `posts` SET `title` = %s WHERE `id` IN (
            SELECT `id` FROM  (
                SELECT `id` FROM `posts` WHERE `userId` = %s LIMIT 1
            ) AS subquery
        );
        
[2024-02-05 09:32:14.941140] : Dataloom[mysql]: 
        UPDATE `posts` SET `title` = %s WHERE `id` IN (
            SELECT `id` FROM  (
                SELECT `id` FROM `posts` WHERE `userId` = %s LIMIT 1
            ) AS subquery
        );
        
[2024-02-05 09:32:14.950136] : Dataloom[mysql]: SELECT `completed`, `createdAt`, `id`, `title`, `userId` FROM `posts` WHERE `id` = %s;
[2024-02-05 09:32:14.959548] : Dataloom[mysql]: 
        UPDATE `posts` SET `userId` = %s WHERE `id` IN (
            SELECT `id` FROM  (
                SELECT `id` FROM `posts` WHERE `userId` = %s LIMIT 1
            ) AS subquery
        );
        
[2024-02-05 09:32:14.976936] : Dataloom[mysql]: DROP TABLE IF EXISTS `posts`;
[2024-02-05 09:32:15.017724] : Dataloom[mysql]: CREATE TABLE IF NOT EXISTS `posts` (`completed` BOOLEAN DEFAULT False, `id` INT PRIMARY KEY AUTO_INCREMENT UNIQUE NOT NULL, `title` VARCHAR(255) NOT NULL, `createdAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP, `userId` INT NOT NULL REFERENCES `users`(`id`) ON DELETE CASCADE ON UPDATE CASCADE);
[2024-02-05 09:32:15.045557] : Dataloom[mysql]: DROP TABLE IF EXISTS `users`;
[2024-02-05 09:32:15.080066] : Dataloom[mysql]: CREATE TABLE IF NOT EXISTS `users` (`id` INT PRIMARY KEY AUTO_INCREMENT UNIQUE NOT NULL, `name` VARCHAR(255) NOT NULL DEFAULT 'Bob', `username` VARCHAR(255) UNIQUE, `createdAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP, `updatedAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP);
[2024-02-05 09:32:15.116111] : Dataloom[mysql]: SHOW TABLES;
[2024-02-05 09:32:15.125109] : Dataloom[mysql]: INSERT INTO `users` (`username`) VALUES (%s);
[2024-02-05 09:32:15.135109] : Dataloom[mysql]: INSERT INTO `posts` (`title`, `userId`) VALUES (%s, %s);
[2024-02-05 09:32:15.199923] : Dataloom[mysql]: UPDATE `posts` SET `title` = %s WHERE `userId` = %s;
[2024-02-05 09:32:15.210921] : Dataloom[mysql]: UPDATE `posts` SET `title` = %s WHERE `userId` = %s;
[2024-02-05 09:32:15.218921] : Dataloom[mysql]: SELECT `completed`, `createdAt`, `id`, `title`, `userId` FROM `posts` WHERE `id` = %s;
[2024-02-05 09:32:15.227920] : Dataloom[mysql]: UPDATE `posts` SET `userId` = %s WHERE `userId` = %s;
[2024-02-05 09:32:15.716204] : Dataloom[postgres]: DROP TABLE IF EXISTS "users" CASCADE;
[2024-02-05 09:32:15.802842] : Dataloom[postgres]: DROP TABLE IF EXISTS "users" CASCADE;
[2024-02-05 09:32:15.919845] : Dataloom[postgres]: DROP TABLE IF EXISTS "users" CASCADE;
[2024-02-05 09:32:15.928845] : Dataloom[postgres]: CREATE TABLE IF NOT EXISTS "users" ("id" BIGSERIAL PRIMARY KEY UNIQUE NOT NULL, "name" VARCHAR(255), "username" TEXT NOT NULL);
[2024-02-05 09:32:15.951451] : Dataloom[postgres]: DROP TABLE IF EXISTS "posts" CASCADE;
[2024-02-05 09:32:15.967042] : Dataloom[postgres]: CREATE TABLE IF NOT EXISTS "posts" ("id" BIGSERIAL PRIMARY KEY UNIQUE NOT NULL, "title" TEXT NOT NULL DEFAULT 'Hello there!!');
[2024-02-05 09:32:15.980042] : Dataloom[postgres]: SELECT tablename FROM pg_catalog.pg_tables WHERE schemaname='public';
[2024-02-05 09:32:16.143413] : Dataloom[postgres]: DROP TABLE IF EXISTS "users" CASCADE;
[2024-02-05 09:32:16.162415] : Dataloom[postgres]: CREATE TABLE IF NOT EXISTS "users" ("id" BIGSERIAL PRIMARY KEY UNIQUE NOT NULL, "name" VARCHAR(255) UNIQUE, "username" TEXT NOT NULL DEFAULT 'Hello there!!');
[2024-02-05 09:32:16.182574] : Dataloom[postgres]: DROP TABLE IF EXISTS "posts" CASCADE;
[2024-02-05 09:32:16.193736] : Dataloom[postgres]: CREATE TABLE IF NOT EXISTS "posts" ("completed" BOOLEAN DEFAULT False, "id" BIGSERIAL PRIMARY KEY UNIQUE NOT NULL, "title" VARCHAR(255) NOT NULL);
[2024-02-05 09:32:16.206737] : Dataloom[postgres]: SELECT tablename FROM pg_catalog.pg_tables WHERE schemaname='public';
[2024-02-05 09:32:16.282030] : Dataloom[postgres]: DROP TABLE IF EXISTS "posts" CASCADE;
[2024-02-05 09:32:16.298119] : Dataloom[postgres]: CREATE TABLE IF NOT EXISTS "posts" ("completed" BOOLEAN DEFAULT False, "id" BIGSERIAL PRIMARY KEY UNIQUE NOT NULL, "title" VARCHAR(255) NOT NULL, "createdAt" TIMESTAMP DEFAULT CURRENT_TIMESTAMP, "updatedAt" TIMESTAMP DEFAULT CURRENT_TIMESTAMP, "userId" BIGSERIAL NOT NULL REFERENCES "users"("id") ON DELETE CASCADE ON UPDATE CASCADE);
[2024-02-05 09:32:16.324551] : Dataloom[postgres]: DROP TABLE IF EXISTS "users" CASCADE;
[2024-02-05 09:32:16.339355] : Dataloom[postgres]: CREATE TABLE IF NOT EXISTS "users" ("id" BIGSERIAL PRIMARY KEY UNIQUE NOT NULL, "name" TEXT NOT NULL DEFAULT 'Bob', "username" VARCHAR(255) UNIQUE, "createdAt" TIMESTAMP DEFAULT CURRENT_TIMESTAMP, "updatedAt" TIMESTAMP DEFAULT CURRENT_TIMESTAMP);
[2024-02-05 09:32:16.353822] : Dataloom[postgres]: SELECT tablename FROM pg_catalog.pg_tables WHERE schemaname='public';
[2024-02-05 09:32:16.368271] : Dataloom[postgres]: INSERT INTO "users" ("name", "username") VALUES (%s, %s) RETURNING "id";
[2024-02-05 09:32:16.378119] : Dataloom[postgres]: DELETE FROM "users" WHERE "id" = %s;
[2024-02-05 09:32:16.388917] : Dataloom[postgres]: DELETE FROM "users" WHERE "id" = %s;
[2024-02-05 09:32:16.449745] : Dataloom[postgres]: DROP TABLE IF EXISTS "posts" CASCADE;
[2024-02-05 09:32:16.465744] : Dataloom[postgres]: CREATE TABLE IF NOT EXISTS "posts" ("completed" BOOLEAN DEFAULT False, "id" BIGSERIAL PRIMARY KEY UNIQUE NOT NULL, "title" VARCHAR(255) NOT NULL, "createdAt" TIMESTAMP DEFAULT CURRENT_TIMESTAMP, "updatedAt" TIMESTAMP DEFAULT CURRENT_TIMESTAMP, "userId" BIGSERIAL NOT NULL REFERENCES "users"("id") ON DELETE CASCADE ON UPDATE CASCADE);
[2024-02-05 09:32:16.483745] : Dataloom[postgres]: DROP TABLE IF EXISTS "users" CASCADE;
[2024-02-05 09:32:16.503746] : Dataloom[postgres]: CREATE TABLE IF NOT EXISTS "users" ("id" BIGSERIAL PRIMARY KEY UNIQUE NOT NULL, "name" TEXT NOT NULL DEFAULT 'Bob', "username" VARCHAR(255) UNIQUE, "createdAt" TIMESTAMP DEFAULT CURRENT_TIMESTAMP, "updatedAt" TIMESTAMP DEFAULT CURRENT_TIMESTAMP);
[2024-02-05 09:32:16.518784] : Dataloom[postgres]: SELECT tablename FROM pg_catalog.pg_tables WHERE schemaname='public';
[2024-02-05 09:32:16.532745] : Dataloom[postgres]: INSERT INTO "users" ("name", "username") VALUES (%s, %s) RETURNING *;
[2024-02-05 09:32:16.542779] : Dataloom[postgres]: 
    DELETE FROM "users" WHERE "id" = (
        SELECT "id" FROM  "users" WHERE "name" = %s LIMIT 1
    );
    
[2024-02-05 09:32:16.551785] : Dataloom[postgres]: SELECT "createdAt", "id", "name", "updatedAt", "username" FROM "users" WHERE "name" = %s   ;
[2024-02-05 09:32:16.559745] : Dataloom[postgres]: 
    DELETE FROM "users" WHERE "id" = (
        SELECT "id" FROM  "users" WHERE "name" = %s AND "id" = %s LIMIT 1
    );
    
[2024-02-05 09:32:16.567779] : Dataloom[postgres]: SELECT "createdAt", "id", "name", "updatedAt", "username" FROM "users" WHERE "name" = %s   ;
[2024-02-05 09:32:16.575778] : Dataloom[postgres]: 
    DELETE FROM "users" WHERE "id" = (
        SELECT "id" FROM  "users" WHERE "name" = %s AND "id" = %s LIMIT 1
    );
    
[2024-02-05 09:32:16.583779] : Dataloom[postgres]: SELECT "createdAt", "id", "name", "updatedAt", "username" FROM "users" WHERE "name" = %s   ;
[2024-02-05 09:32:16.746895] : Dataloom[postgres]: DROP TABLE IF EXISTS "posts" CASCADE;
[2024-02-05 09:32:16.761025] : Dataloom[postgres]: CREATE TABLE IF NOT EXISTS "posts" ("completed" BOOLEAN DEFAULT False, "id" BIGSERIAL PRIMARY KEY UNIQUE NOT NULL, "title" VARCHAR(255) NOT NULL, "createdAt" TIMESTAMP DEFAULT CURRENT_TIMESTAMP, "updatedAt" TIMESTAMP DEFAULT CURRENT_TIMESTAMP, "userId" BIGSERIAL NOT NULL REFERENCES "users"("id") ON DELETE CASCADE ON UPDATE CASCADE);
[2024-02-05 09:32:16.782615] : Dataloom[postgres]: DROP TABLE IF EXISTS "users" CASCADE;
[2024-02-05 09:32:16.796608] : Dataloom[postgres]: CREATE TABLE IF NOT EXISTS "users" ("id" BIGSERIAL PRIMARY KEY UNIQUE NOT NULL, "name" TEXT NOT NULL DEFAULT 'Bob', "username" VARCHAR(255) UNIQUE, "createdAt" TIMESTAMP DEFAULT CURRENT_TIMESTAMP, "updatedAt" TIMESTAMP DEFAULT CURRENT_TIMESTAMP);
[2024-02-05 09:32:16.811192] : Dataloom[postgres]: SELECT tablename FROM pg_catalog.pg_tables WHERE schemaname='public';
[2024-02-05 09:32:16.823201] : Dataloom[postgres]: INSERT INTO "users" ("name", "username") VALUES (%s, %s) RETURNING *;
[2024-02-05 09:32:16.835477] : Dataloom[postgres]: DELETE FROM "users" WHERE "name" = %s;
[2024-02-05 09:32:16.844010] : Dataloom[postgres]: SELECT "createdAt", "id", "name", "updatedAt", "username" FROM "users" WHERE "name" = %s   ;
[2024-02-05 09:32:16.852015] : Dataloom[postgres]: INSERT INTO "users" ("name", "username") VALUES (%s, %s) RETURNING *;
[2024-02-05 09:32:16.861017] : Dataloom[postgres]: DELETE FROM "users" WHERE "name" = %s AND "id" = %s;
[2024-02-05 09:32:16.868015] : Dataloom[postgres]: SELECT "createdAt", "id", "name", "updatedAt", "username" FROM "users" WHERE "name" = %s   ;
[2024-02-05 09:32:16.876982] : Dataloom[postgres]: DELETE FROM "users" WHERE "name" = %s AND "id" = %s;
[2024-02-05 09:32:16.884459] : Dataloom[postgres]: SELECT "createdAt", "id", "name", "updatedAt", "username" FROM "users" WHERE "name" = %s   ;
[2024-02-05 09:32:17.050613] : Dataloom[postgres]: DROP TABLE IF EXISTS "posts" CASCADE;
[2024-02-05 09:32:17.067309] : Dataloom[postgres]: CREATE TABLE IF NOT EXISTS "posts" ("completed" BOOLEAN DEFAULT False, "id" BIGSERIAL PRIMARY KEY UNIQUE NOT NULL, "title" VARCHAR(255) NOT NULL, "createdAt" TIMESTAMP DEFAULT CURRENT_TIMESTAMP, "updatedAt" TIMESTAMP DEFAULT CURRENT_TIMESTAMP, "userId" BIGSERIAL NOT NULL REFERENCES "users"("id") ON DELETE CASCADE ON UPDATE CASCADE);
[2024-02-05 09:32:17.085530] : Dataloom[postgres]: DROP TABLE IF EXISTS "users" CASCADE;
[2024-02-05 09:32:17.100537] : Dataloom[postgres]: CREATE TABLE IF NOT EXISTS "users" ("id" BIGSERIAL PRIMARY KEY UNIQUE NOT NULL, "name" TEXT NOT NULL DEFAULT 'Bob', "username" VARCHAR(255) UNIQUE, "createdAt" TIMESTAMP DEFAULT CURRENT_TIMESTAMP, "updatedAt" TIMESTAMP DEFAULT CURRENT_TIMESTAMP);
[2024-02-05 09:32:17.118134] : Dataloom[postgres]: SELECT tablename FROM pg_catalog.pg_tables WHERE schemaname='public';
[2024-02-05 09:32:17.132456] : Dataloom[postgres]: INSERT INTO "users" ("username") VALUES (%s) RETURNING "id";
[2024-02-05 09:32:17.142844] : Dataloom[postgres]: INSERT INTO "posts" ("title", "userId") VALUES (%s, %s) RETURNING "id";
[2024-02-05 09:32:17.213534] : Dataloom[postgres]: DROP TABLE IF EXISTS "posts" CASCADE;
[2024-02-05 09:32:17.232204] : Dataloom[postgres]: CREATE TABLE IF NOT EXISTS "posts" ("completed" BOOLEAN DEFAULT False, "id" BIGSERIAL PRIMARY KEY UNIQUE NOT NULL, "title" VARCHAR(255) NOT NULL, "createdAt" TIMESTAMP DEFAULT CURRENT_TIMESTAMP, "updatedAt" TIMESTAMP DEFAULT CURRENT_TIMESTAMP, "userId" BIGSERIAL NOT NULL REFERENCES "users"("id") ON DELETE CASCADE ON UPDATE CASCADE);
[2024-02-05 09:32:17.252174] : Dataloom[postgres]: DROP TABLE IF EXISTS "users" CASCADE;
[2024-02-05 09:32:17.267009] : Dataloom[postgres]: CREATE TABLE IF NOT EXISTS "users" ("id" BIGSERIAL PRIMARY KEY UNIQUE NOT NULL, "name" TEXT NOT NULL DEFAULT 'Bob', "username" VARCHAR(255) UNIQUE, "createdAt" TIMESTAMP DEFAULT CURRENT_TIMESTAMP, "updatedAt" TIMESTAMP DEFAULT CURRENT_TIMESTAMP);
[2024-02-05 09:32:17.289027] : Dataloom[postgres]: SELECT tablename FROM pg_catalog.pg_tables WHERE schemaname='public';
[2024-02-05 09:32:17.306291] : Dataloom[postgres]: INSERT INTO "users" ("username") VALUES (%s) RETURNING "id";
[2024-02-05 09:32:17.318110] : Dataloom[postgres]: INSERT INTO "posts" ("title", "userId") VALUES (%s, %s) RETURNING *;
[2024-02-05 09:32:17.475388] : Dataloom[postgres]: DROP TABLE IF EXISTS "posts" CASCADE;
[2024-02-05 09:32:17.492299] : Dataloom[postgres]: CREATE TABLE IF NOT EXISTS "posts" ("completed" BOOLEAN DEFAULT False, "id" BIGSERIAL PRIMARY KEY UNIQUE NOT NULL, "title" VARCHAR(255) NOT NULL, "createdAt" TIMESTAMP DEFAULT CURRENT_TIMESTAMP, "updatedAt" TIMESTAMP DEFAULT CURRENT_TIMESTAMP, "userId" BIGSERIAL NOT NULL REFERENCES "users"("id") ON DELETE CASCADE ON UPDATE CASCADE);
[2024-02-05 09:32:17.513361] : Dataloom[postgres]: DROP TABLE IF EXISTS "users" CASCADE;
[2024-02-05 09:32:17.528130] : Dataloom[postgres]: CREATE TABLE IF NOT EXISTS "users" ("id" BIGSERIAL PRIMARY KEY UNIQUE NOT NULL, "name" TEXT NOT NULL DEFAULT 'Bob', "username" VARCHAR(255) UNIQUE);
[2024-02-05 09:32:17.550131] : Dataloom[postgres]: SELECT tablename FROM pg_catalog.pg_tables WHERE schemaname='public';
[2024-02-05 09:32:17.566730] : Dataloom[postgres]: INSERT INTO "users" ("username") VALUES (%s) RETURNING "id";
[2024-02-05 09:32:17.576699] : Dataloom[postgres]: INSERT INTO "posts" ("title", "userId") VALUES (%s, %s) RETURNING *;
[2024-02-05 09:32:17.586734] : Dataloom[postgres]: SELECT "id", "name", "username" FROM "users" WHERE "id" = %s;
[2024-02-05 09:32:17.594734] : Dataloom[postgres]: SELECT "id", "name", "username" FROM "users" WHERE "id" = %s;
[2024-02-05 09:32:17.603308] : Dataloom[postgres]: SELECT "id", "completed" FROM "posts" WHERE "id" = %s;
[2024-02-05 09:32:17.666425] : Dataloom[postgres]: DROP TABLE IF EXISTS "posts" CASCADE;
[2024-02-05 09:32:17.687805] : Dataloom[postgres]: CREATE TABLE IF NOT EXISTS "posts" ("completed" BOOLEAN DEFAULT False, "id" BIGSERIAL PRIMARY KEY UNIQUE NOT NULL, "title" VARCHAR(255) NOT NULL, "createdAt" TIMESTAMP DEFAULT CURRENT_TIMESTAMP, "updatedAt" TIMESTAMP DEFAULT CURRENT_TIMESTAMP, "userId" BIGSERIAL NOT NULL REFERENCES "users"("id") ON DELETE CASCADE ON UPDATE CASCADE);
[2024-02-05 09:32:17.708707] : Dataloom[postgres]: DROP TABLE IF EXISTS "users" CASCADE;
[2024-02-05 09:32:17.729673] : Dataloom[postgres]: CREATE TABLE IF NOT EXISTS "users" ("id" BIGSERIAL PRIMARY KEY UNIQUE NOT NULL, "name" TEXT NOT NULL DEFAULT 'Bob', "username" VARCHAR(255) UNIQUE);
[2024-02-05 09:32:17.747707] : Dataloom[postgres]: SELECT tablename FROM pg_catalog.pg_tables WHERE schemaname='public';
[2024-02-05 09:32:17.761986] : Dataloom[postgres]: INSERT INTO "users" ("username") VALUES (%s) RETURNING "id";
[2024-02-05 09:32:17.773019] : Dataloom[postgres]: INSERT INTO "posts" ("title", "userId") VALUES (%s, %s) RETURNING *;
[2024-02-05 09:32:17.783428] : Dataloom[postgres]: SELECT "id", "name", "username" FROM "users"   ;
[2024-02-05 09:32:17.791421] : Dataloom[postgres]: SELECT "completed", "createdAt", "id", "title", "updatedAt", "userId" FROM "posts"   ;
[2024-02-05 09:32:17.799947] : Dataloom[postgres]: SELECT "id", "completed" FROM "posts"  LIMIT 3 OFFSET 3;
[2024-02-05 09:32:17.864860] : Dataloom[postgres]: DROP TABLE IF EXISTS "posts" CASCADE;
[2024-02-05 09:32:17.883398] : Dataloom[postgres]: CREATE TABLE IF NOT EXISTS "posts" ("completed" BOOLEAN DEFAULT False, "id" BIGSERIAL PRIMARY KEY UNIQUE NOT NULL, "title" VARCHAR(255) NOT NULL, "createdAt" TIMESTAMP DEFAULT CURRENT_TIMESTAMP, "updatedAt" TIMESTAMP DEFAULT CURRENT_TIMESTAMP, "userId" BIGSERIAL NOT NULL REFERENCES "users"("id") ON DELETE CASCADE ON UPDATE CASCADE);
[2024-02-05 09:32:17.904431] : Dataloom[postgres]: DROP TABLE IF EXISTS "users" CASCADE;
[2024-02-05 09:32:17.918456] : Dataloom[postgres]: CREATE TABLE IF NOT EXISTS "users" ("id" BIGSERIAL PRIMARY KEY UNIQUE NOT NULL, "name" TEXT NOT NULL DEFAULT 'Bob', "username" VARCHAR(255) UNIQUE);
[2024-02-05 09:32:17.936421] : Dataloom[postgres]: SELECT tablename FROM pg_catalog.pg_tables WHERE schemaname='public';
[2024-02-05 09:32:17.951429] : Dataloom[postgres]: INSERT INTO "users" ("username") VALUES (%s) RETURNING "id";
[2024-02-05 09:32:17.962462] : Dataloom[postgres]: INSERT INTO "posts" ("title", "userId") VALUES (%s, %s) RETURNING *;
[2024-02-05 09:32:17.973626] : Dataloom[postgres]: SELECT "id", "name", "username" FROM "users" WHERE "id" = %s   ;
[2024-02-05 09:32:17.981624] : Dataloom[postgres]: SELECT "id", "name", "username" FROM "users" WHERE "id" = %s   ;
[2024-02-05 09:32:17.990417] : Dataloom[postgres]: SELECT "id", "name", "username" FROM "users" WHERE "id" = %s AND "name" = %s   ;
[2024-02-05 09:32:17.998426] : Dataloom[postgres]: SELECT "id", "name", "username" FROM "users" WHERE "id" = %s AND "username" = %s   ;
[2024-02-05 09:32:18.008459] : Dataloom[postgres]: SELECT "id", "name", "username" FROM "users" WHERE "name" = %s AND "username" = %s   ;
[2024-02-05 09:32:18.016462] : Dataloom[postgres]: SELECT "id", "completed" FROM "posts"   ;
[2024-02-05 09:32:18.083802] : Dataloom[postgres]: DROP TABLE IF EXISTS "posts" CASCADE;
[2024-02-05 09:32:18.103934] : Dataloom[postgres]: CREATE TABLE IF NOT EXISTS "posts" ("completed" BOOLEAN DEFAULT False, "id" BIGSERIAL PRIMARY KEY UNIQUE NOT NULL, "title" VARCHAR(255) NOT NULL, "createdAt" TIMESTAMP DEFAULT CURRENT_TIMESTAMP, "updatedAt" TIMESTAMP DEFAULT CURRENT_TIMESTAMP, "userId" BIGSERIAL NOT NULL REFERENCES "users"("id") ON DELETE CASCADE ON UPDATE CASCADE);
[2024-02-05 09:32:18.123344] : Dataloom[postgres]: DROP TABLE IF EXISTS "users" CASCADE;
[2024-02-05 09:32:18.136879] : Dataloom[postgres]: CREATE TABLE IF NOT EXISTS "users" ("id" BIGSERIAL PRIMARY KEY UNIQUE NOT NULL, "name" TEXT NOT NULL DEFAULT 'Bob', "username" VARCHAR(255) UNIQUE);
[2024-02-05 09:32:18.154759] : Dataloom[postgres]: SELECT tablename FROM pg_catalog.pg_tables WHERE schemaname='public';
[2024-02-05 09:32:18.167803] : Dataloom[postgres]: INSERT INTO "users" ("username") VALUES (%s) RETURNING "id";
[2024-02-05 09:32:18.178771] : Dataloom[postgres]: INSERT INTO "posts" ("title", "userId") VALUES (%s, %s) RETURNING *;
[2024-02-05 09:32:18.188808] : Dataloom[postgres]: SELECT "completed", "createdAt", "id", "title", "updatedAt", "userId" FROM "posts" WHERE "id" = %s AND "userId" = %s   ;
[2024-02-05 09:32:18.196801] : Dataloom[postgres]: SELECT "id", "name", "username" FROM "users"   ;
[2024-02-05 09:32:18.204768] : Dataloom[postgres]: SELECT "id", "name", "username" FROM "users" WHERE "id" = %s   ;
[2024-02-05 09:32:18.214768] : Dataloom[postgres]: SELECT "id", "name", "username" FROM "users" WHERE "id" = %s   ;
[2024-02-05 09:32:18.223801] : Dataloom[postgres]: SELECT "id", "name", "username" FROM "users" WHERE "id" = %s AND "name" = %s   ;
[2024-02-05 09:32:18.231767] : Dataloom[postgres]: SELECT "id", "name", "username" FROM "users" WHERE "id" = %s AND "username" = %s   ;
[2024-02-05 09:32:18.239768] : Dataloom[postgres]: SELECT "id", "name", "username" FROM "users" WHERE "name" = %s AND "username" = %s   ;
[2024-02-05 09:32:18.247768] : Dataloom[postgres]: SELECT "id", "completed" FROM "posts" WHERE "userId" = %s  LIMIT 3 OFFSET 3;
[2024-02-05 09:32:18.258800] : Dataloom[postgres]: SELECT "completed", "createdAt", "id", "title", "updatedAt", "userId" FROM "posts"   ;
[2024-02-05 09:32:18.437767] : Dataloom[postgres]: DROP TABLE IF EXISTS "posts" CASCADE;
[2024-02-05 09:32:18.457770] : Dataloom[postgres]: CREATE TABLE IF NOT EXISTS "posts" ("completed" BOOLEAN DEFAULT False, "id" BIGSERIAL PRIMARY KEY UNIQUE NOT NULL, "title" VARCHAR(255) NOT NULL, "createdAt" TIMESTAMP DEFAULT CURRENT_TIMESTAMP, "updatedAt" TIMESTAMP DEFAULT CURRENT_TIMESTAMP, "userId" BIGSERIAL NOT NULL REFERENCES "users"("id") ON DELETE CASCADE ON UPDATE CASCADE);
[2024-02-05 09:32:18.475768] : Dataloom[postgres]: DROP TABLE IF EXISTS "users" CASCADE;
[2024-02-05 09:32:18.490769] : Dataloom[postgres]: CREATE TABLE IF NOT EXISTS "users" ("id" BIGSERIAL PRIMARY KEY UNIQUE NOT NULL, "name" TEXT NOT NULL DEFAULT 'Bob', "username" VARCHAR(255) UNIQUE, "createdAt" TIMESTAMP DEFAULT CURRENT_TIMESTAMP, "updatedAt" TIMESTAMP DEFAULT CURRENT_TIMESTAMP);
[2024-02-05 09:32:18.505231] : Dataloom[postgres]: SELECT tablename FROM pg_catalog.pg_tables WHERE schemaname='public';
[2024-02-05 09:32:18.518445] : Dataloom[postgres]: INSERT INTO "users" ("username") VALUES (%s) RETURNING "id";
[2024-02-05 09:32:18.529445] : Dataloom[postgres]: INSERT INTO "posts" ("title", "userId") VALUES (%s, %s) RETURNING *;
[2024-02-05 09:32:18.590117] : Dataloom[postgres]: UPDATE "users" SET "updatedAt" = %s WHERE "id" = %s;
[2024-02-05 09:32:18.601310] : Dataloom[postgres]: UPDATE "users" SET "updatedAt" = %s WHERE "id" = %s;
[2024-02-05 09:32:18.609309] : Dataloom[postgres]: SELECT "createdAt", "id", "name", "updatedAt", "username" FROM "users" WHERE "id" = %s;
[2024-02-05 09:32:18.618378] : Dataloom[postgres]: UPDATE "users" SET "id" = %s, "updatedAt" = %s WHERE "id" = %s;
[2024-02-05 09:32:18.690932] : Dataloom[postgres]: DROP TABLE IF EXISTS "posts" CASCADE;
[2024-02-05 09:32:18.707203] : Dataloom[postgres]: CREATE TABLE IF NOT EXISTS "posts" ("completed" BOOLEAN DEFAULT False, "id" BIGSERIAL PRIMARY KEY UNIQUE NOT NULL, "title" VARCHAR(255) NOT NULL, "createdAt" TIMESTAMP DEFAULT CURRENT_TIMESTAMP, "userId" BIGSERIAL NOT NULL REFERENCES "users"("id") ON DELETE CASCADE ON UPDATE CASCADE);
[2024-02-05 09:32:18.730807] : Dataloom[postgres]: DROP TABLE IF EXISTS "users" CASCADE;
[2024-02-05 09:32:18.745777] : Dataloom[postgres]: CREATE TABLE IF NOT EXISTS "users" ("id" BIGSERIAL PRIMARY KEY UNIQUE NOT NULL, "name" TEXT NOT NULL DEFAULT 'Bob', "username" VARCHAR(255) UNIQUE, "createdAt" TIMESTAMP DEFAULT CURRENT_TIMESTAMP, "updatedAt" TIMESTAMP DEFAULT CURRENT_TIMESTAMP);
[2024-02-05 09:32:18.767782] : Dataloom[postgres]: SELECT tablename FROM pg_catalog.pg_tables WHERE schemaname='public';
[2024-02-05 09:32:18.783528] : Dataloom[postgres]: INSERT INTO "users" ("username") VALUES (%s) RETURNING "id";
[2024-02-05 09:32:18.794522] : Dataloom[postgres]: INSERT INTO "posts" ("title", "userId") VALUES (%s, %s) RETURNING *;
[2024-02-05 09:32:18.855151] : Dataloom[postgres]: 
        UPDATE "users" SET "name" = %s, "updatedAt" = %s WHERE "id" = (
            SELECT "id" FROM  "users" WHERE "username" = %s LIMIT 1
        );
        
[2024-02-05 09:32:18.864151] : Dataloom[postgres]: 
        UPDATE "users" SET "name" = %s, "updatedAt" = %s WHERE "id" = (
            SELECT "id" FROM  "users" WHERE "username" = %s LIMIT 1
        );
        
[2024-02-05 09:32:18.872295] : Dataloom[postgres]: SELECT "createdAt", "id", "name", "updatedAt", "username" FROM "users" WHERE "id" = %s;
[2024-02-05 09:32:18.882618] : Dataloom[postgres]: 
        UPDATE "users" SET "id" = %s, "updatedAt" = %s WHERE "id" = (
            SELECT "id" FROM  "users" WHERE "username" = %s LIMIT 1
        );
        
[2024-02-05 09:32:18.953829] : Dataloom[postgres]: DROP TABLE IF EXISTS "posts" CASCADE;
[2024-02-05 09:32:18.968815] : Dataloom[postgres]: CREATE TABLE IF NOT EXISTS "posts" ("completed" BOOLEAN DEFAULT False, "id" BIGSERIAL PRIMARY KEY UNIQUE NOT NULL, "title" VARCHAR(255) NOT NULL, "createdAt" TIMESTAMP DEFAULT CURRENT_TIMESTAMP, "userId" BIGSERIAL NOT NULL REFERENCES "users"("id") ON DELETE CASCADE ON UPDATE CASCADE);
[2024-02-05 09:32:18.988847] : Dataloom[postgres]: DROP TABLE IF EXISTS "users" CASCADE;
[2024-02-05 09:32:19.004561] : Dataloom[postgres]: CREATE TABLE IF NOT EXISTS "users" ("id" BIGSERIAL PRIMARY KEY UNIQUE NOT NULL, "name" TEXT NOT NULL DEFAULT 'Bob', "username" VARCHAR(255) UNIQUE, "createdAt" TIMESTAMP DEFAULT CURRENT_TIMESTAMP, "updatedAt" TIMESTAMP DEFAULT CURRENT_TIMESTAMP);
[2024-02-05 09:32:19.021533] : Dataloom[postgres]: SELECT tablename FROM pg_catalog.pg_tables WHERE schemaname='public';
[2024-02-05 09:32:19.035889] : Dataloom[postgres]: INSERT INTO "users" ("username") VALUES (%s) RETURNING "id";
[2024-02-05 09:32:19.046882] : Dataloom[postgres]: INSERT INTO "posts" ("title", "userId") VALUES (%s, %s) RETURNING *;
[2024-02-05 09:32:19.057446] : Dataloom[postgres]: UPDATE "posts" SET "title" = %s WHERE "userId" = %s;
[2024-02-05 09:32:19.065443] : Dataloom[postgres]: UPDATE "posts" SET "title" = %s WHERE "userId" = %s;
[2024-02-05 09:32:19.074443] : Dataloom[postgres]: UPDATE "posts" SET "userId" = %s WHERE "userId" = %s;
[2024-02-05 09:32:19.100444] : Dataloom[sqlite]: DROP TABLE IF EXISTS users;
[2024-02-05 09:32:19.134142] : Dataloom[sqlite]: DROP TABLE IF EXISTS users;
[2024-02-05 09:32:19.154097] : Dataloom[sqlite]: DROP TABLE IF EXISTS users;
[2024-02-05 09:32:19.166130] : Dataloom[sqlite]: CREATE TABLE IF NOT EXISTS `users` (`id` INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL, `name` VARCHAR, `username` TEXT NOT NULL);
[2024-02-05 09:32:19.183656] : Dataloom[sqlite]: DROP TABLE IF EXISTS posts;
[2024-02-05 09:32:19.197621] : Dataloom[sqlite]: CREATE TABLE IF NOT EXISTS `posts` (`id` INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL, `title` TEXT NOT NULL);
[2024-02-05 09:32:19.213622] : Dataloom[sqlite]: SELECT name FROM sqlite_master WHERE type='table';
[2024-02-05 09:32:19.226636] : Dataloom[sqlite]: DROP TABLE IF EXISTS users;
[2024-02-05 09:32:19.247622] : Dataloom[sqlite]: CREATE TABLE IF NOT EXISTS `users` (`id` INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL, `name` VARCHAR UNIQUE, `username` TEXT NOT NULL DEFAULT 'Hello there!!');
[2024-02-05 09:32:19.265651] : Dataloom[sqlite]: DROP TABLE IF EXISTS posts;
[2024-02-05 09:32:19.280519] : Dataloom[sqlite]: CREATE TABLE IF NOT EXISTS `posts` (`completed` BOOLEAN DEFAULT False, `id` INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL, `title` VARCHAR NOT NULL);
[2024-02-05 09:32:19.292463] : Dataloom[sqlite]: SELECT name FROM sqlite_master WHERE type='table';
[2024-02-05 09:32:19.305464] : Dataloom[sqlite]: DROP TABLE IF EXISTS posts;
[2024-02-05 09:32:19.323087] : Dataloom[sqlite]: CREATE TABLE IF NOT EXISTS `posts` (`completed` BOOLEAN DEFAULT False, `id` INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL, `title` VARCHAR NOT NULL, `createdAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP, `updatedAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP, `userId` INTEGER NOT NULL REFERENCES `users`(`id`) ON DELETE CASCADE ON UPDATE CASCADE);
[2024-02-05 09:32:19.338087] : Dataloom[sqlite]: DROP TABLE IF EXISTS users;
[2024-02-05 09:32:19.353125] : Dataloom[sqlite]: CREATE TABLE IF NOT EXISTS `users` (`id` INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL, `name` TEXT NOT NULL DEFAULT 'Bob', `username` VARCHAR UNIQUE, `createdAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP, `updatedAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP);
[2024-02-05 09:32:19.365654] : Dataloom[sqlite]: SELECT name FROM sqlite_master WHERE type='table';
[2024-02-05 09:32:19.373656] : Dataloom[sqlite]: INSERT INTO `users` (`name`, `username`) VALUES (?, ?);
[2024-02-05 09:32:19.385223] : Dataloom[sqlite]: DELETE FROM `users` WHERE `id` = ?;
[2024-02-05 09:32:19.395822] : Dataloom[sqlite]: DELETE FROM `users` WHERE `id` = ?;
[2024-02-05 09:32:19.406850] : Dataloom[sqlite]: DROP TABLE IF EXISTS posts;
[2024-02-05 09:32:19.422296] : Dataloom[sqlite]: CREATE TABLE IF NOT EXISTS `posts` (`completed` BOOLEAN DEFAULT False, `id` INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL, `title` VARCHAR NOT NULL, `createdAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP, `updatedAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP, `userId` INTEGER NOT NULL REFERENCES `users`(`id`) ON DELETE CASCADE ON UPDATE CASCADE);
[2024-02-05 09:32:19.434640] : Dataloom[sqlite]: DROP TABLE IF EXISTS users;
[2024-02-05 09:32:19.449642] : Dataloom[sqlite]: CREATE TABLE IF NOT EXISTS `users` (`id` INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL, `name` TEXT NOT NULL DEFAULT 'Bob', `username` VARCHAR UNIQUE, `createdAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP, `updatedAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP);
[2024-02-05 09:32:19.466745] : Dataloom[sqlite]: SELECT name FROM sqlite_master WHERE type='table';
[2024-02-05 09:32:19.476754] : Dataloom[sqlite]: INSERT INTO `users` (`name`, `username`) VALUES (?, ?);
[2024-02-05 09:32:19.487582] : Dataloom[sqlite]: 
    DELETE FROM `users` WHERE `id` = (
        SELECT `id` FROM  `users` WHERE `name` = ? LIMIT 1
    );
    
[2024-02-05 09:32:19.498994] : Dataloom[sqlite]: SELECT `createdAt`, `id`, `name`, `updatedAt`, `username` FROM `users` WHERE `name` = ?   ;
[2024-02-05 09:32:19.506994] : Dataloom[sqlite]: 
    DELETE FROM `users` WHERE `id` = (
        SELECT `id` FROM  `users` WHERE `name` = ? AND `id` = ? LIMIT 1
    );
    
[2024-02-05 09:32:19.514992] : Dataloom[sqlite]: SELECT `createdAt`, `id`, `name`, `updatedAt`, `username` FROM `users` WHERE `name` = ?   ;
[2024-02-05 09:32:19.521993] : Dataloom[sqlite]: 
    DELETE FROM `users` WHERE `id` = (
        SELECT `id` FROM  `users` WHERE `name` = ? AND `id` = ? LIMIT 1
    );
    
[2024-02-05 09:32:19.532948] : Dataloom[sqlite]: SELECT `createdAt`, `id`, `name`, `updatedAt`, `username` FROM `users` WHERE `name` = ?   ;
[2024-02-05 09:32:19.543963] : Dataloom[sqlite]: DROP TABLE IF EXISTS posts;
[2024-02-05 09:32:19.557097] : Dataloom[sqlite]: CREATE TABLE IF NOT EXISTS `posts` (`completed` BOOLEAN DEFAULT False, `id` INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL, `title` VARCHAR NOT NULL, `createdAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP, `updatedAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP, `userId` INTEGER NOT NULL REFERENCES `users`(`id`) ON DELETE CASCADE ON UPDATE CASCADE);
[2024-02-05 09:32:19.573080] : Dataloom[sqlite]: DROP TABLE IF EXISTS users;
[2024-02-05 09:32:19.584065] : Dataloom[sqlite]: CREATE TABLE IF NOT EXISTS `users` (`id` INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL, `name` TEXT NOT NULL DEFAULT 'Bob', `username` VARCHAR UNIQUE, `createdAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP, `updatedAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP);
[2024-02-05 09:32:19.596099] : Dataloom[sqlite]: SELECT name FROM sqlite_master WHERE type='table';
[2024-02-05 09:32:19.605098] : Dataloom[sqlite]: INSERT INTO `users` (`name`, `username`) VALUES (?, ?);
[2024-02-05 09:32:19.615812] : Dataloom[sqlite]: DELETE FROM `users` WHERE `name` = ?;
[2024-02-05 09:32:19.626959] : Dataloom[sqlite]: SELECT `createdAt`, `id`, `name`, `updatedAt`, `username` FROM `users` WHERE `name` = ?   ;
[2024-02-05 09:32:19.635025] : Dataloom[sqlite]: INSERT INTO `users` (`name`, `username`) VALUES (?, ?);
[2024-02-05 09:32:19.645720] : Dataloom[sqlite]: DELETE FROM `users` WHERE `name` = ? AND `id` = ?;
[2024-02-05 09:32:19.652719] : Dataloom[sqlite]: SELECT `createdAt`, `id`, `name`, `updatedAt`, `username` FROM `users` WHERE `name` = ?   ;
[2024-02-05 09:32:19.660722] : Dataloom[sqlite]: DELETE FROM `users` WHERE `name` = ? AND `id` = ?;
[2024-02-05 09:32:19.671098] : Dataloom[sqlite]: SELECT `createdAt`, `id`, `name`, `updatedAt`, `username` FROM `users` WHERE `name` = ?   ;
[2024-02-05 09:32:19.682066] : Dataloom[sqlite]: DROP TABLE IF EXISTS posts;
[2024-02-05 09:32:19.694096] : Dataloom[sqlite]: CREATE TABLE IF NOT EXISTS `posts` (`completed` BOOLEAN DEFAULT False, `id` INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL, `title` VARCHAR NOT NULL, `createdAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP, `updatedAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP, `userId` INTEGER NOT NULL REFERENCES `users`(`id`) ON DELETE CASCADE ON UPDATE CASCADE);
[2024-02-05 09:32:19.709065] : Dataloom[sqlite]: DROP TABLE IF EXISTS users;
[2024-02-05 09:32:19.723064] : Dataloom[sqlite]: CREATE TABLE IF NOT EXISTS `users` (`id` INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL, `name` TEXT NOT NULL DEFAULT 'Bob', `username` VARCHAR UNIQUE, `createdAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP, `updatedAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP);
[2024-02-05 09:32:19.737068] : Dataloom[sqlite]: SELECT name FROM sqlite_master WHERE type='table';
[2024-02-05 09:32:19.748065] : Dataloom[sqlite]: INSERT INTO `users` (`username`) VALUES (?);
[2024-02-05 09:32:19.763065] : Dataloom[sqlite]: INSERT INTO `posts` (`title`, `userId`) VALUES (?, ?);
[2024-02-05 09:32:19.779069] : Dataloom[sqlite]: DROP TABLE IF EXISTS posts;
[2024-02-05 09:32:19.801069] : Dataloom[sqlite]: CREATE TABLE IF NOT EXISTS `posts` (`completed` BOOLEAN DEFAULT False, `id` INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL, `title` VARCHAR NOT NULL, `createdAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP, `updatedAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP, `userId` INTEGER NOT NULL REFERENCES `users`(`id`) ON DELETE CASCADE ON UPDATE CASCADE);
[2024-02-05 09:32:19.817099] : Dataloom[sqlite]: DROP TABLE IF EXISTS users;
[2024-02-05 09:32:19.838072] : Dataloom[sqlite]: CREATE TABLE IF NOT EXISTS `users` (`id` INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL, `name` TEXT NOT NULL DEFAULT 'Bob', `username` VARCHAR UNIQUE, `createdAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP, `updatedAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP);
[2024-02-05 09:32:19.852085] : Dataloom[sqlite]: SELECT name FROM sqlite_master WHERE type='table';
[2024-02-05 09:32:19.861065] : Dataloom[sqlite]: INSERT INTO `users` (`username`) VALUES (?);
[2024-02-05 09:32:19.871065] : Dataloom[sqlite]: INSERT INTO `posts` (`title`, `userId`) VALUES (?, ?);
[2024-02-05 09:32:19.883970] : Dataloom[sqlite]: DROP TABLE IF EXISTS posts;
[2024-02-05 09:32:19.894820] : Dataloom[sqlite]: CREATE TABLE IF NOT EXISTS `posts` (`completed` BOOLEAN DEFAULT False, `id` INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL, `title` VARCHAR NOT NULL, `createdAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP, `updatedAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP, `userId` INTEGER NOT NULL REFERENCES `users`(`id`) ON DELETE CASCADE ON UPDATE CASCADE);
[2024-02-05 09:32:19.907820] : Dataloom[sqlite]: DROP TABLE IF EXISTS users;
[2024-02-05 09:32:19.919825] : Dataloom[sqlite]: CREATE TABLE IF NOT EXISTS `users` (`id` INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL, `name` TEXT NOT NULL DEFAULT 'Bob', `username` VARCHAR UNIQUE);
[2024-02-05 09:32:19.932818] : Dataloom[sqlite]: SELECT name FROM sqlite_master WHERE type='table';
[2024-02-05 09:32:19.943850] : Dataloom[sqlite]: INSERT INTO `users` (`username`) VALUES (?);
[2024-02-05 09:32:19.957261] : Dataloom[sqlite]: INSERT INTO `posts` (`title`, `userId`) VALUES (?, ?);
[2024-02-05 09:32:19.970844] : Dataloom[sqlite]: SELECT `id`, `name`, `username` FROM `users` WHERE `id` = ?;
[2024-02-05 09:32:19.978839] : Dataloom[sqlite]: SELECT `id`, `name`, `username` FROM `users` WHERE `id` = ?;
[2024-02-05 09:32:19.986982] : Dataloom[sqlite]: SELECT `id`, `completed` FROM `posts` WHERE `id` = ?;
[2024-02-05 09:32:19.997147] : Dataloom[sqlite]: DROP TABLE IF EXISTS posts;
[2024-02-05 09:32:20.016152] : Dataloom[sqlite]: CREATE TABLE IF NOT EXISTS `posts` (`completed` BOOLEAN DEFAULT False, `id` INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL, `title` VARCHAR NOT NULL, `createdAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP, `updatedAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP, `userId` INTEGER NOT NULL REFERENCES `users`(`id`) ON DELETE CASCADE ON UPDATE CASCADE);
[2024-02-05 09:32:20.031770] : Dataloom[sqlite]: DROP TABLE IF EXISTS users;
[2024-02-05 09:32:20.046165] : Dataloom[sqlite]: CREATE TABLE IF NOT EXISTS `users` (`id` INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL, `name` TEXT NOT NULL DEFAULT 'Bob', `username` VARCHAR UNIQUE);
[2024-02-05 09:32:20.060826] : Dataloom[sqlite]: SELECT name FROM sqlite_master WHERE type='table';
[2024-02-05 09:32:20.069860] : Dataloom[sqlite]: INSERT INTO `users` (`username`) VALUES (?);
[2024-02-05 09:32:20.082047] : Dataloom[sqlite]: INSERT INTO `posts` (`title`, `userId`) VALUES (?, ?);
[2024-02-05 09:32:20.095047] : Dataloom[sqlite]: SELECT `id`, `name`, `username` FROM `users`   ;
[2024-02-05 09:32:20.104070] : Dataloom[sqlite]: SELECT `completed`, `createdAt`, `id`, `title`, `updatedAt`, `userId` FROM `posts`   ;
[2024-02-05 09:32:20.112070] : Dataloom[sqlite]: SELECT `id`, `completed` FROM `posts`  LIMIT 3 OFFSET 3;
[2024-02-05 09:32:20.122571] : Dataloom[sqlite]: DROP TABLE IF EXISTS posts;
[2024-02-05 09:32:20.138573] : Dataloom[sqlite]: CREATE TABLE IF NOT EXISTS `posts` (`completed` BOOLEAN DEFAULT False, `id` INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL, `title` VARCHAR NOT NULL, `createdAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP, `updatedAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP, `userId` INTEGER NOT NULL REFERENCES `users`(`id`) ON DELETE CASCADE ON UPDATE CASCADE);
[2024-02-05 09:32:20.154574] : Dataloom[sqlite]: DROP TABLE IF EXISTS users;
[2024-02-05 09:32:20.166490] : Dataloom[sqlite]: CREATE TABLE IF NOT EXISTS `users` (`id` INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL, `name` TEXT NOT NULL DEFAULT 'Bob', `username` VARCHAR UNIQUE);
[2024-02-05 09:32:20.180520] : Dataloom[sqlite]: SELECT name FROM sqlite_master WHERE type='table';
[2024-02-05 09:32:20.189523] : Dataloom[sqlite]: INSERT INTO `users` (`username`) VALUES (?);
[2024-02-05 09:32:20.201628] : Dataloom[sqlite]: INSERT INTO `posts` (`title`, `userId`) VALUES (?, ?);
[2024-02-05 09:32:20.213689] : Dataloom[sqlite]: SELECT `id`, `name`, `username` FROM `users` WHERE `id` = ?   ;
[2024-02-05 09:32:20.221723] : Dataloom[sqlite]: SELECT `id`, `name`, `username` FROM `users` WHERE `id` = ?   ;
[2024-02-05 09:32:20.229692] : Dataloom[sqlite]: SELECT `id`, `name`, `username` FROM `users` WHERE `id` = ? AND `name` = ?   ;
[2024-02-05 09:32:20.237935] : Dataloom[sqlite]: SELECT `id`, `name`, `username` FROM `users` WHERE `id` = ? AND `username` = ?   ;
[2024-02-05 09:32:20.245985] : Dataloom[sqlite]: SELECT `id`, `name`, `username` FROM `users` WHERE `name` = ? AND `username` = ?   ;
[2024-02-05 09:32:20.252978] : Dataloom[sqlite]: SELECT `id`, `completed` FROM `posts`   ;
[2024-02-05 09:32:20.263954] : Dataloom[sqlite]: DROP TABLE IF EXISTS posts;
[2024-02-05 09:32:20.277662] : Dataloom[sqlite]: CREATE TABLE IF NOT EXISTS `posts` (`completed` BOOLEAN DEFAULT False, `id` INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL, `title` VARCHAR NOT NULL, `createdAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP, `updatedAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP, `userId` INTEGER NOT NULL REFERENCES `users`(`id`) ON DELETE CASCADE ON UPDATE CASCADE);
[2024-02-05 09:32:20.292691] : Dataloom[sqlite]: DROP TABLE IF EXISTS users;
[2024-02-05 09:32:20.306661] : Dataloom[sqlite]: CREATE TABLE IF NOT EXISTS `users` (`id` INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL, `name` TEXT NOT NULL DEFAULT 'Bob', `username` VARCHAR UNIQUE);
[2024-02-05 09:32:20.319659] : Dataloom[sqlite]: SELECT name FROM sqlite_master WHERE type='table';
[2024-02-05 09:32:20.328688] : Dataloom[sqlite]: INSERT INTO `users` (`username`) VALUES (?);
[2024-02-05 09:32:20.340658] : Dataloom[sqlite]: INSERT INTO `posts` (`title`, `userId`) VALUES (?, ?);
[2024-02-05 09:32:20.352674] : Dataloom[sqlite]: SELECT `completed`, `createdAt`, `id`, `title`, `updatedAt`, `userId` FROM `posts` WHERE `id` = ? AND `userId` = ?   ;
[2024-02-05 09:32:20.362665] : Dataloom[sqlite]: SELECT `id`, `name`, `username` FROM `users`   ;
[2024-02-05 09:32:20.372660] : Dataloom[sqlite]: SELECT `id`, `name`, `username` FROM `users` WHERE `id` = ?   ;
[2024-02-05 09:32:20.383660] : Dataloom[sqlite]: SELECT `id`, `name`, `username` FROM `users` WHERE `id` = ?   ;
[2024-02-05 09:32:20.393671] : Dataloom[sqlite]: SELECT `id`, `name`, `username` FROM `users` WHERE `id` = ? AND `name` = ?   ;
[2024-02-05 09:32:20.404660] : Dataloom[sqlite]: SELECT `id`, `name`, `username` FROM `users` WHERE `id` = ? AND `username` = ?   ;
[2024-02-05 09:32:20.411693] : Dataloom[sqlite]: SELECT `id`, `name`, `username` FROM `users` WHERE `name` = ? AND `username` = ?   ;
[2024-02-05 09:32:20.420659] : Dataloom[sqlite]: SELECT `id`, `completed` FROM `posts` WHERE `userId` = ?  LIMIT 3 OFFSET 3;
[2024-02-05 09:32:20.428658] : Dataloom[sqlite]: SELECT `completed`, `createdAt`, `id`, `title`, `updatedAt`, `userId` FROM `posts`   ;
[2024-02-05 09:32:20.441227] : Dataloom[sqlite]: DROP TABLE IF EXISTS posts;
[2024-02-05 09:32:20.461203] : Dataloom[sqlite]: CREATE TABLE IF NOT EXISTS `posts` (`completed` BOOLEAN DEFAULT False, `id` INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL, `title` VARCHAR NOT NULL, `createdAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP, `updatedAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP, `userId` INTEGER NOT NULL REFERENCES `users`(`id`) ON DELETE CASCADE ON UPDATE CASCADE);
[2024-02-05 09:32:20.477230] : Dataloom[sqlite]: DROP TABLE IF EXISTS users;
[2024-02-05 09:32:20.494235] : Dataloom[sqlite]: CREATE TABLE IF NOT EXISTS `users` (`id` INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL, `name` TEXT NOT NULL DEFAULT 'Bob', `username` VARCHAR UNIQUE, `createdAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP, `updatedAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP);
[2024-02-05 09:32:20.510268] : Dataloom[sqlite]: SELECT name FROM sqlite_master WHERE type='table';
[2024-02-05 09:32:20.519276] : Dataloom[sqlite]: INSERT INTO `users` (`username`) VALUES (?);
[2024-02-05 09:32:20.540070] : Dataloom[sqlite]: INSERT INTO `posts` (`title`, `userId`) VALUES (?, ?);
[2024-02-05 09:32:20.607071] : Dataloom[sqlite]: UPDATE `users` SET `updatedAt` = ? WHERE `id` = ?;
[2024-02-05 09:32:20.619110] : Dataloom[sqlite]: UPDATE `users` SET `updatedAt` = ? WHERE `id` = ?;
[2024-02-05 09:32:20.629068] : Dataloom[sqlite]: SELECT `createdAt`, `id`, `name`, `updatedAt`, `username` FROM `users` WHERE `id` = ?;
[2024-02-05 09:32:20.642071] : Dataloom[sqlite]: DROP TABLE IF EXISTS posts;
[2024-02-05 09:32:20.657076] : Dataloom[sqlite]: CREATE TABLE IF NOT EXISTS `posts` (`completed` BOOLEAN DEFAULT False, `id` INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL, `title` VARCHAR NOT NULL, `createdAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP, `userId` INTEGER NOT NULL REFERENCES `users`(`id`) ON DELETE CASCADE ON UPDATE CASCADE);
[2024-02-05 09:32:20.672989] : Dataloom[sqlite]: DROP TABLE IF EXISTS users;
[2024-02-05 09:32:20.687958] : Dataloom[sqlite]: CREATE TABLE IF NOT EXISTS `users` (`id` INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL, `name` TEXT NOT NULL DEFAULT 'Bob', `username` VARCHAR UNIQUE, `createdAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP, `updatedAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP);
[2024-02-05 09:32:20.705590] : Dataloom[sqlite]: SELECT name FROM sqlite_master WHERE type='table';
[2024-02-05 09:32:20.713600] : Dataloom[sqlite]: INSERT INTO `users` (`username`) VALUES (?);
[2024-02-05 09:32:20.726633] : Dataloom[sqlite]: INSERT INTO `posts` (`title`, `userId`) VALUES (?, ?);
[2024-02-05 09:32:20.790233] : Dataloom[sqlite]: 
        UPDATE `posts` SET `title` = ? WHERE `id` = (
            SELECT `id` FROM  `posts` WHERE `userId` = ? LIMIT 1
        );
        
[2024-02-05 09:32:20.803231] : Dataloom[sqlite]: 
        UPDATE `posts` SET `title` = ? WHERE `id` = (
            SELECT `id` FROM  `posts` WHERE `userId` = ? LIMIT 1
        );
        
[2024-02-05 09:32:20.813238] : Dataloom[sqlite]: SELECT `completed`, `createdAt`, `id`, `title`, `userId` FROM `posts` WHERE `id` = ?;
[2024-02-05 09:32:20.824709] : Dataloom[sqlite]: DROP TABLE IF EXISTS posts;
[2024-02-05 09:32:20.838641] : Dataloom[sqlite]: CREATE TABLE IF NOT EXISTS `posts` (`completed` BOOLEAN DEFAULT False, `id` INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL, `title` VARCHAR NOT NULL, `createdAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP, `userId` INTEGER NOT NULL REFERENCES `users`(`id`) ON DELETE CASCADE ON UPDATE CASCADE);
[2024-02-05 09:32:20.858611] : Dataloom[sqlite]: DROP TABLE IF EXISTS users;
[2024-02-05 09:32:20.878609] : Dataloom[sqlite]: CREATE TABLE IF NOT EXISTS `users` (`id` INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL, `name` TEXT NOT NULL DEFAULT 'Bob', `username` VARCHAR UNIQUE, `createdAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP, `updatedAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP);
[2024-02-05 09:32:20.897611] : Dataloom[sqlite]: SELECT name FROM sqlite_master WHERE type='table';
[2024-02-05 09:32:20.906633] : Dataloom[sqlite]: INSERT INTO `users` (`username`) VALUES (?);
[2024-02-05 09:32:20.920607] : Dataloom[sqlite]: INSERT INTO `posts` (`title`, `userId`) VALUES (?, ?);
[2024-02-05 09:32:20.987605] : Dataloom[sqlite]: UPDATE `posts` SET `title` = ? WHERE `userId` = ?;
[2024-02-05 09:32:20.997606] : Dataloom[sqlite]: UPDATE `posts` SET `title` = ? WHERE `userId` = ?;
[2024-02-05 09:32:21.007606] : Dataloom[sqlite]: SELECT `completed`, `createdAt`, `id`, `title`, `userId` FROM `posts` WHERE `id` = ?;
[2024-02-05 09:33:33.226947] : Dataloom[mysql]: DROP TABLE IF EXISTS `users`;
[2024-02-05 09:33:33.296688] : Dataloom[mysql]: DROP TABLE IF EXISTS `users`;
[2024-02-05 09:33:33.366923] : Dataloom[mysql]: DROP TABLE IF EXISTS `users`;
[2024-02-05 09:33:33.394771] : Dataloom[mysql]: CREATE TABLE IF NOT EXISTS `users` (`id` INT PRIMARY KEY AUTO_INCREMENT UNIQUE NOT NULL, `name` VARCHAR(255), `username` TEXT NOT NULL);
[2024-02-05 09:33:33.473827] : Dataloom[mysql]: DROP TABLE IF EXISTS `posts`;
[2024-02-05 09:33:33.547645] : Dataloom[mysql]: CREATE TABLE IF NOT EXISTS `posts` (`id` INT PRIMARY KEY AUTO_INCREMENT UNIQUE NOT NULL, `title` TEXT NOT NULL);
[2024-02-05 09:33:33.668377] : Dataloom[mysql]: SHOW TABLES;
[2024-02-05 09:33:33.748021] : Dataloom[mysql]: DROP TABLE IF EXISTS `users`;
[2024-02-05 09:33:33.879940] : Dataloom[mysql]: CREATE TABLE IF NOT EXISTS `users` (`id` INT PRIMARY KEY AUTO_INCREMENT UNIQUE NOT NULL, `name` VARCHAR(255) UNIQUE, `username` VARCHAR(255) NOT NULL DEFAULT 'Hello there!!');
[2024-02-05 09:33:34.019702] : Dataloom[mysql]: DROP TABLE IF EXISTS `posts`;
[2024-02-05 09:33:34.114468] : Dataloom[mysql]: CREATE TABLE IF NOT EXISTS `posts` (`completed` BOOLEAN DEFAULT False, `id` INT PRIMARY KEY AUTO_INCREMENT UNIQUE NOT NULL, `title` VARCHAR(255) NOT NULL);
[2024-02-05 09:33:34.230421] : Dataloom[mysql]: SHOW TABLES;
[2024-02-05 09:33:34.302425] : Dataloom[mysql]: DROP TABLE IF EXISTS `posts`;
[2024-02-05 09:33:34.403491] : Dataloom[mysql]: CREATE TABLE IF NOT EXISTS `posts` (`completed` BOOLEAN DEFAULT False, `id` INT PRIMARY KEY AUTO_INCREMENT UNIQUE NOT NULL, `title` VARCHAR(255) NOT NULL, `createdAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP, `updatedAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP, `userId` INT NOT NULL REFERENCES `users`(`id`) ON DELETE CASCADE ON UPDATE CASCADE);
[2024-02-05 09:33:34.512488] : Dataloom[mysql]: DROP TABLE IF EXISTS `users`;
[2024-02-05 09:33:34.612560] : Dataloom[mysql]: CREATE TABLE IF NOT EXISTS `users` (`id` INT PRIMARY KEY AUTO_INCREMENT UNIQUE NOT NULL, `name` VARCHAR(255) NOT NULL DEFAULT 'Bob', `username` VARCHAR(255) UNIQUE, `createdAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP, `updatedAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP);
[2024-02-05 09:33:34.800164] : Dataloom[mysql]: SHOW TABLES;
[2024-02-05 09:33:34.835521] : Dataloom[mysql]: INSERT INTO `users` (`name`, `username`) VALUES (%s, %s);
[2024-02-05 09:33:34.873337] : Dataloom[mysql]: DELETE FROM `users` WHERE `id` = %s;
[2024-02-05 09:33:34.904753] : Dataloom[mysql]: DELETE FROM `users` WHERE `id` = %s;
[2024-02-05 09:33:34.967723] : Dataloom[mysql]: DROP TABLE IF EXISTS `posts`;
[2024-02-05 09:33:35.079690] : Dataloom[mysql]: CREATE TABLE IF NOT EXISTS `posts` (`completed` BOOLEAN DEFAULT False, `id` INT PRIMARY KEY AUTO_INCREMENT UNIQUE NOT NULL, `title` VARCHAR(255) NOT NULL, `createdAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP, `updatedAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP, `userId` INT NOT NULL REFERENCES `users`(`id`) ON DELETE CASCADE ON UPDATE CASCADE);
[2024-02-05 09:33:35.176391] : Dataloom[mysql]: DROP TABLE IF EXISTS `users`;
[2024-02-05 09:33:35.270833] : Dataloom[mysql]: CREATE TABLE IF NOT EXISTS `users` (`id` INT PRIMARY KEY AUTO_INCREMENT UNIQUE NOT NULL, `name` VARCHAR(255) NOT NULL DEFAULT 'Bob', `username` VARCHAR(255) UNIQUE, `createdAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP, `updatedAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP);
[2024-02-05 09:33:35.374448] : Dataloom[mysql]: SHOW TABLES;
[2024-02-05 09:33:35.403502] : Dataloom[mysql]: INSERT INTO `users` (`name`, `username`) VALUES (%s, %s);
[2024-02-05 09:33:35.436447] : Dataloom[mysql]: 
    DELETE FROM `users` WHERE `id` IN (
       SELECT `id` FROM  (
                SELECT `id` FROM `users` WHERE `name` = %s LIMIT 1
        ) AS subquery
    );
    
[2024-02-05 09:33:35.466038] : Dataloom[mysql]: SELECT `createdAt`, `id`, `name`, `updatedAt`, `username` FROM `users` WHERE `name` = %s   ;
[2024-02-05 09:33:35.492990] : Dataloom[mysql]: 
    DELETE FROM `users` WHERE `id` IN (
       SELECT `id` FROM  (
                SELECT `id` FROM `users` WHERE `name` = %s AND `id` = %s LIMIT 1
        ) AS subquery
    );
    
[2024-02-05 09:33:35.520133] : Dataloom[mysql]: SELECT `createdAt`, `id`, `name`, `updatedAt`, `username` FROM `users` WHERE `name` = %s   ;
[2024-02-05 09:33:35.548592] : Dataloom[mysql]: 
    DELETE FROM `users` WHERE `id` IN (
       SELECT `id` FROM  (
                SELECT `id` FROM `users` WHERE `name` = %s AND `id` = %s LIMIT 1
        ) AS subquery
    );
    
[2024-02-05 09:33:35.578526] : Dataloom[mysql]: SELECT `createdAt`, `id`, `name`, `updatedAt`, `username` FROM `users` WHERE `name` = %s   ;
[2024-02-05 09:33:35.634558] : Dataloom[mysql]: DROP TABLE IF EXISTS `posts`;
[2024-02-05 09:33:35.739103] : Dataloom[mysql]: CREATE TABLE IF NOT EXISTS `posts` (`completed` BOOLEAN DEFAULT False, `id` INT PRIMARY KEY AUTO_INCREMENT UNIQUE NOT NULL, `title` VARCHAR(255) NOT NULL, `createdAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP, `updatedAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP, `userId` INT NOT NULL REFERENCES `users`(`id`) ON DELETE CASCADE ON UPDATE CASCADE);
[2024-02-05 09:33:35.819720] : Dataloom[mysql]: DROP TABLE IF EXISTS `users`;
[2024-02-05 09:33:35.889636] : Dataloom[mysql]: CREATE TABLE IF NOT EXISTS `users` (`id` INT PRIMARY KEY AUTO_INCREMENT UNIQUE NOT NULL, `name` VARCHAR(255) NOT NULL DEFAULT 'Bob', `username` VARCHAR(255) UNIQUE, `createdAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP, `updatedAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP);
[2024-02-05 09:33:35.977592] : Dataloom[mysql]: SHOW TABLES;
[2024-02-05 09:33:36.007295] : Dataloom[mysql]: INSERT INTO `users` (`name`, `username`) VALUES (%s, %s);
[2024-02-05 09:33:36.039036] : Dataloom[mysql]: DELETE FROM `users` WHERE `name` = %s;
[2024-02-05 09:33:36.067700] : Dataloom[mysql]: SELECT `createdAt`, `id`, `name`, `updatedAt`, `username` FROM `users` WHERE `name` = %s   ;
[2024-02-05 09:33:36.095703] : Dataloom[mysql]: INSERT INTO `users` (`name`, `username`) VALUES (%s, %s);
[2024-02-05 09:33:36.124701] : Dataloom[mysql]: DELETE FROM `users` WHERE `name` = %s AND `id` = %s;
[2024-02-05 09:33:36.151371] : Dataloom[mysql]: SELECT `createdAt`, `id`, `name`, `updatedAt`, `username` FROM `users` WHERE `name` = %s   ;
[2024-02-05 09:33:36.177798] : Dataloom[mysql]: DELETE FROM `users` WHERE `name` = %s AND `id` = %s;
[2024-02-05 09:33:36.208436] : Dataloom[mysql]: SELECT `createdAt`, `id`, `name`, `updatedAt`, `username` FROM `users` WHERE `name` = %s   ;
[2024-02-05 09:33:36.269694] : Dataloom[mysql]: DROP TABLE IF EXISTS `posts`;
[2024-02-05 09:33:36.402824] : Dataloom[mysql]: CREATE TABLE IF NOT EXISTS `posts` (`completed` BOOLEAN DEFAULT False, `id` INT PRIMARY KEY AUTO_INCREMENT UNIQUE NOT NULL, `title` VARCHAR(255) NOT NULL, `createdAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP, `updatedAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP, `userId` INT NOT NULL REFERENCES `users`(`id`) ON DELETE CASCADE ON UPDATE CASCADE);
[2024-02-05 09:33:36.483328] : Dataloom[mysql]: DROP TABLE IF EXISTS `users`;
[2024-02-05 09:33:36.565330] : Dataloom[mysql]: CREATE TABLE IF NOT EXISTS `users` (`id` INT PRIMARY KEY AUTO_INCREMENT UNIQUE NOT NULL, `name` VARCHAR(255) NOT NULL DEFAULT 'Bob', `username` VARCHAR(255) UNIQUE, `createdAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP, `updatedAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP);
[2024-02-05 09:33:36.642085] : Dataloom[mysql]: SHOW TABLES;
[2024-02-05 09:33:36.665700] : Dataloom[mysql]: INSERT INTO `users` (`username`) VALUES (%s);
[2024-02-05 09:33:36.695819] : Dataloom[mysql]: INSERT INTO `posts` (`title`, `userId`) VALUES (%s, %s);
[2024-02-05 09:33:36.748820] : Dataloom[mysql]: DROP TABLE IF EXISTS `posts`;
[2024-02-05 09:33:36.840480] : Dataloom[mysql]: CREATE TABLE IF NOT EXISTS `posts` (`completed` BOOLEAN DEFAULT False, `id` INT PRIMARY KEY AUTO_INCREMENT UNIQUE NOT NULL, `title` VARCHAR(255) NOT NULL, `createdAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP, `updatedAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP, `userId` INT NOT NULL REFERENCES `users`(`id`) ON DELETE CASCADE ON UPDATE CASCADE);
[2024-02-05 09:33:36.935723] : Dataloom[mysql]: DROP TABLE IF EXISTS `users`;
[2024-02-05 09:33:37.015218] : Dataloom[mysql]: CREATE TABLE IF NOT EXISTS `users` (`id` INT PRIMARY KEY AUTO_INCREMENT UNIQUE NOT NULL, `name` VARCHAR(255) NOT NULL DEFAULT 'Bob', `username` VARCHAR(255) UNIQUE, `createdAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP, `updatedAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP);
[2024-02-05 09:33:37.111431] : Dataloom[mysql]: SHOW TABLES;
[2024-02-05 09:33:37.138375] : Dataloom[mysql]: INSERT INTO `users` (`username`) VALUES (%s);
[2024-02-05 09:33:37.167937] : Dataloom[mysql]: INSERT INTO `posts` (`title`, `userId`) VALUES (%s, %s);
[2024-02-05 09:33:37.223982] : Dataloom[mysql]: DROP TABLE IF EXISTS `posts`;
[2024-02-05 09:33:37.310777] : Dataloom[mysql]: CREATE TABLE IF NOT EXISTS `posts` (`completed` BOOLEAN DEFAULT False, `id` INT PRIMARY KEY AUTO_INCREMENT UNIQUE NOT NULL, `title` VARCHAR(255) NOT NULL, `createdAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP, `updatedAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP, `userId` INT NOT NULL REFERENCES `users`(`id`) ON DELETE CASCADE ON UPDATE CASCADE);
[2024-02-05 09:33:37.378987] : Dataloom[mysql]: DROP TABLE IF EXISTS `users`;
[2024-02-05 09:33:37.461647] : Dataloom[mysql]: CREATE TABLE IF NOT EXISTS `users` (`id` INT PRIMARY KEY AUTO_INCREMENT UNIQUE NOT NULL, `name` VARCHAR(255) NOT NULL DEFAULT 'Bob', `username` VARCHAR(255) UNIQUE);
[2024-02-05 09:33:37.551721] : Dataloom[mysql]: SHOW TABLES;
[2024-02-05 09:33:37.579691] : Dataloom[mysql]: INSERT INTO `users` (`username`) VALUES (%s);
[2024-02-05 09:33:37.609955] : Dataloom[mysql]: INSERT INTO `posts` (`title`, `userId`) VALUES (%s, %s);
[2024-02-05 09:33:37.639933] : Dataloom[mysql]: SELECT `id`, `name`, `username` FROM `users` WHERE `id` = %s;
[2024-02-05 09:33:37.666934] : Dataloom[mysql]: SELECT `id`, `name`, `username` FROM `users` WHERE `id` = %s;
[2024-02-05 09:33:37.696884] : Dataloom[mysql]: SELECT `id`, `completed` FROM `posts` WHERE `id` = %s;
[2024-02-05 09:33:37.760942] : Dataloom[mysql]: DROP TABLE IF EXISTS `posts`;
[2024-02-05 09:33:37.839507] : Dataloom[mysql]: CREATE TABLE IF NOT EXISTS `posts` (`completed` BOOLEAN DEFAULT False, `id` INT PRIMARY KEY AUTO_INCREMENT UNIQUE NOT NULL, `title` VARCHAR(255) NOT NULL, `createdAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP, `updatedAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP, `userId` INT NOT NULL REFERENCES `users`(`id`) ON DELETE CASCADE ON UPDATE CASCADE);
[2024-02-05 09:33:37.951568] : Dataloom[mysql]: DROP TABLE IF EXISTS `users`;
[2024-02-05 09:33:38.035846] : Dataloom[mysql]: CREATE TABLE IF NOT EXISTS `users` (`id` INT PRIMARY KEY AUTO_INCREMENT UNIQUE NOT NULL, `name` VARCHAR(255) NOT NULL DEFAULT 'Bob', `username` VARCHAR(255) UNIQUE);
[2024-02-05 09:33:38.127557] : Dataloom[mysql]: SHOW TABLES;
[2024-02-05 09:33:38.154475] : Dataloom[mysql]: INSERT INTO `users` (`username`) VALUES (%s);
[2024-02-05 09:33:38.184177] : Dataloom[mysql]: INSERT INTO `posts` (`title`, `userId`) VALUES (%s, %s);
[2024-02-05 09:33:38.212912] : Dataloom[mysql]: SELECT `id`, `name`, `username` FROM `users`   ;
[2024-02-05 09:33:38.238076] : Dataloom[mysql]: SELECT `completed`, `createdAt`, `id`, `title`, `updatedAt`, `userId` FROM `posts`   ;
[2024-02-05 09:33:38.263279] : Dataloom[mysql]: SELECT `id`, `completed` FROM `posts`  LIMIT 3 OFFSET 3;
[2024-02-05 09:33:38.316669] : Dataloom[mysql]: DROP TABLE IF EXISTS `posts`;
[2024-02-05 09:33:38.404779] : Dataloom[mysql]: CREATE TABLE IF NOT EXISTS `posts` (`completed` BOOLEAN DEFAULT False, `id` INT PRIMARY KEY AUTO_INCREMENT UNIQUE NOT NULL, `title` VARCHAR(255) NOT NULL, `createdAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP, `updatedAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP, `userId` INT NOT NULL REFERENCES `users`(`id`) ON DELETE CASCADE ON UPDATE CASCADE);
[2024-02-05 09:33:38.494424] : Dataloom[mysql]: DROP TABLE IF EXISTS `users`;
[2024-02-05 09:33:38.573095] : Dataloom[mysql]: CREATE TABLE IF NOT EXISTS `users` (`id` INT PRIMARY KEY AUTO_INCREMENT UNIQUE NOT NULL, `name` VARCHAR(255) NOT NULL DEFAULT 'Bob', `username` VARCHAR(255) UNIQUE);
[2024-02-05 09:33:38.656314] : Dataloom[mysql]: SHOW TABLES;
[2024-02-05 09:33:38.683624] : Dataloom[mysql]: INSERT INTO `users` (`username`) VALUES (%s);
[2024-02-05 09:33:38.713651] : Dataloom[mysql]: INSERT INTO `posts` (`title`, `userId`) VALUES (%s, %s);
[2024-02-05 09:33:38.748652] : Dataloom[mysql]: SELECT `id`, `name`, `username` FROM `users` WHERE `id` = %s   ;
[2024-02-05 09:33:38.776611] : Dataloom[mysql]: SELECT `id`, `name`, `username` FROM `users` WHERE `id` = %s   ;
[2024-02-05 09:33:38.804086] : Dataloom[mysql]: SELECT `id`, `name`, `username` FROM `users` WHERE `id` = %s AND `name` = %s   ;
[2024-02-05 09:33:38.833085] : Dataloom[mysql]: SELECT `id`, `name`, `username` FROM `users` WHERE `id` = %s AND `username` = %s   ;
[2024-02-05 09:33:38.860086] : Dataloom[mysql]: SELECT `id`, `name`, `username` FROM `users` WHERE `name` = %s AND `username` = %s   ;
[2024-02-05 09:33:38.888032] : Dataloom[mysql]: SELECT `id`, `completed` FROM `posts`   ;
[2024-02-05 09:33:38.942568] : Dataloom[mysql]: DROP TABLE IF EXISTS `posts`;
[2024-02-05 09:33:39.037074] : Dataloom[mysql]: CREATE TABLE IF NOT EXISTS `posts` (`completed` BOOLEAN DEFAULT False, `id` INT PRIMARY KEY AUTO_INCREMENT UNIQUE NOT NULL, `title` VARCHAR(255) NOT NULL, `createdAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP, `updatedAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP, `userId` INT NOT NULL REFERENCES `users`(`id`) ON DELETE CASCADE ON UPDATE CASCADE);
[2024-02-05 09:33:39.114703] : Dataloom[mysql]: DROP TABLE IF EXISTS `users`;
[2024-02-05 09:33:39.199761] : Dataloom[mysql]: CREATE TABLE IF NOT EXISTS `users` (`id` INT PRIMARY KEY AUTO_INCREMENT UNIQUE NOT NULL, `name` VARCHAR(255) NOT NULL DEFAULT 'Bob', `username` VARCHAR(255) UNIQUE);
[2024-02-05 09:33:39.296377] : Dataloom[mysql]: SHOW TABLES;
[2024-02-05 09:33:39.323416] : Dataloom[mysql]: INSERT INTO `users` (`username`) VALUES (%s);
[2024-02-05 09:33:39.357385] : Dataloom[mysql]: INSERT INTO `posts` (`title`, `userId`) VALUES (%s, %s);
[2024-02-05 09:33:39.391422] : Dataloom[mysql]: SELECT `completed`, `createdAt`, `id`, `title`, `updatedAt`, `userId` FROM `posts` WHERE `id` = %s AND `userId` = %s   ;
[2024-02-05 09:33:39.421430] : Dataloom[mysql]: SELECT `id`, `name`, `username` FROM `users`   ;
[2024-02-05 09:33:39.448381] : Dataloom[mysql]: SELECT `id`, `name`, `username` FROM `users` WHERE `id` = %s   ;
[2024-02-05 09:33:39.474411] : Dataloom[mysql]: SELECT `id`, `name`, `username` FROM `users` WHERE `id` = %s   ;
[2024-02-05 09:33:39.500412] : Dataloom[mysql]: SELECT `id`, `name`, `username` FROM `users` WHERE `id` = %s AND `name` = %s   ;
[2024-02-05 09:33:39.525991] : Dataloom[mysql]: SELECT `id`, `name`, `username` FROM `users` WHERE `id` = %s AND `username` = %s   ;
[2024-02-05 09:33:39.550393] : Dataloom[mysql]: SELECT `id`, `name`, `username` FROM `users` WHERE `name` = %s AND `username` = %s   ;
[2024-02-05 09:33:39.576349] : Dataloom[mysql]: SELECT `id`, `completed` FROM `posts` WHERE `userId` = %s  LIMIT 3 OFFSET 3;
[2024-02-05 09:33:39.603035] : Dataloom[mysql]: SELECT `completed`, `createdAt`, `id`, `title`, `updatedAt`, `userId` FROM `posts`   ;
[2024-02-05 09:33:39.654511] : Dataloom[mysql]: DROP TABLE IF EXISTS `posts`;
[2024-02-05 09:33:39.726977] : Dataloom[mysql]: CREATE TABLE IF NOT EXISTS `posts` (`completed` BOOLEAN DEFAULT False, `id` INT PRIMARY KEY AUTO_INCREMENT UNIQUE NOT NULL, `title` VARCHAR(255) NOT NULL, `createdAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP, `updatedAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP, `userId` INT NOT NULL REFERENCES `users`(`id`) ON DELETE CASCADE ON UPDATE CASCADE);
[2024-02-05 09:33:39.805979] : Dataloom[mysql]: DROP TABLE IF EXISTS `users`;
[2024-02-05 09:33:39.891985] : Dataloom[mysql]: CREATE TABLE IF NOT EXISTS `users` (`id` INT PRIMARY KEY AUTO_INCREMENT UNIQUE NOT NULL, `name` VARCHAR(255) NOT NULL DEFAULT 'Bob', `username` VARCHAR(255) UNIQUE, `createdAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP, `updatedAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP);
[2024-02-05 09:33:39.982578] : Dataloom[mysql]: SHOW TABLES;
[2024-02-05 09:33:40.010585] : Dataloom[mysql]: INSERT INTO `users` (`username`) VALUES (%s);
[2024-02-05 09:33:40.042539] : Dataloom[mysql]: INSERT INTO `posts` (`title`, `userId`) VALUES (%s, %s);
[2024-02-05 09:33:40.127849] : Dataloom[mysql]: UPDATE `users` SET `updatedAt` = %s WHERE `id` = %s;
[2024-02-05 09:33:40.160647] : Dataloom[mysql]: UPDATE `users` SET `updatedAt` = %s WHERE `id` = %s;
[2024-02-05 09:33:40.190318] : Dataloom[mysql]: SELECT `createdAt`, `id`, `name`, `updatedAt`, `username` FROM `users` WHERE `id` = %s;
[2024-02-05 09:33:40.218247] : Dataloom[mysql]: UPDATE `users` SET `id` = %s, `updatedAt` = %s WHERE `id` = %s;
[2024-02-05 09:33:40.267246] : Dataloom[mysql]: DROP TABLE IF EXISTS `posts`;
[2024-02-05 09:33:40.338228] : Dataloom[mysql]: CREATE TABLE IF NOT EXISTS `posts` (`completed` BOOLEAN DEFAULT False, `id` INT PRIMARY KEY AUTO_INCREMENT UNIQUE NOT NULL, `title` VARCHAR(255) NOT NULL, `createdAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP, `userId` INT NOT NULL REFERENCES `users`(`id`) ON DELETE CASCADE ON UPDATE CASCADE);
[2024-02-05 09:33:40.429328] : Dataloom[mysql]: DROP TABLE IF EXISTS `users`;
[2024-02-05 09:33:40.510788] : Dataloom[mysql]: CREATE TABLE IF NOT EXISTS `users` (`id` INT PRIMARY KEY AUTO_INCREMENT UNIQUE NOT NULL, `name` VARCHAR(255) NOT NULL DEFAULT 'Bob', `username` VARCHAR(255) UNIQUE, `createdAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP, `updatedAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP);
[2024-02-05 09:33:40.610436] : Dataloom[mysql]: SHOW TABLES;
[2024-02-05 09:33:40.639473] : Dataloom[mysql]: INSERT INTO `users` (`username`) VALUES (%s);
[2024-02-05 09:33:40.672524] : Dataloom[mysql]: INSERT INTO `posts` (`title`, `userId`) VALUES (%s, %s);
[2024-02-05 09:33:40.759795] : Dataloom[mysql]: 
        UPDATE `posts` SET `title` = %s WHERE `id` IN (
            SELECT `id` FROM  (
                SELECT `id` FROM `posts` WHERE `userId` = %s LIMIT 1
            ) AS subquery
        );
        
[2024-02-05 09:33:40.794016] : Dataloom[mysql]: 
        UPDATE `posts` SET `title` = %s WHERE `id` IN (
            SELECT `id` FROM  (
                SELECT `id` FROM `posts` WHERE `userId` = %s LIMIT 1
            ) AS subquery
        );
        
[2024-02-05 09:33:40.830865] : Dataloom[mysql]: SELECT `completed`, `createdAt`, `id`, `title`, `userId` FROM `posts` WHERE `id` = %s;
[2024-02-05 09:33:40.861622] : Dataloom[mysql]: 
        UPDATE `posts` SET `userId` = %s WHERE `id` IN (
            SELECT `id` FROM  (
                SELECT `id` FROM `posts` WHERE `userId` = %s LIMIT 1
            ) AS subquery
        );
        
[2024-02-05 09:33:40.927641] : Dataloom[mysql]: DROP TABLE IF EXISTS `posts`;
[2024-02-05 09:33:41.025743] : Dataloom[mysql]: CREATE TABLE IF NOT EXISTS `posts` (`completed` BOOLEAN DEFAULT False, `id` INT PRIMARY KEY AUTO_INCREMENT UNIQUE NOT NULL, `title` VARCHAR(255) NOT NULL, `createdAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP, `userId` INT NOT NULL REFERENCES `users`(`id`) ON DELETE CASCADE ON UPDATE CASCADE);
[2024-02-05 09:33:41.132632] : Dataloom[mysql]: DROP TABLE IF EXISTS `users`;
[2024-02-05 09:33:41.235535] : Dataloom[mysql]: CREATE TABLE IF NOT EXISTS `users` (`id` INT PRIMARY KEY AUTO_INCREMENT UNIQUE NOT NULL, `name` VARCHAR(255) NOT NULL DEFAULT 'Bob', `username` VARCHAR(255) UNIQUE, `createdAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP, `updatedAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP);
[2024-02-05 09:33:41.338521] : Dataloom[mysql]: SHOW TABLES;
[2024-02-05 09:33:41.370485] : Dataloom[mysql]: INSERT INTO `users` (`username`) VALUES (%s);
[2024-02-05 09:33:41.406483] : Dataloom[mysql]: INSERT INTO `posts` (`title`, `userId`) VALUES (%s, %s);
[2024-02-05 09:33:41.497328] : Dataloom[mysql]: UPDATE `posts` SET `title` = %s WHERE `userId` = %s;
[2024-02-05 09:33:41.531895] : Dataloom[mysql]: UPDATE `posts` SET `title` = %s WHERE `userId` = %s;
[2024-02-05 09:33:41.564848] : Dataloom[mysql]: SELECT `completed`, `createdAt`, `id`, `title`, `userId` FROM `posts` WHERE `id` = %s;
[2024-02-05 09:33:41.603863] : Dataloom[mysql]: UPDATE `posts` SET `userId` = %s WHERE `userId` = %s;
[2024-02-05 09:33:42.413145] : Dataloom[postgres]: DROP TABLE IF EXISTS "users" CASCADE;
[2024-02-05 09:33:42.732854] : Dataloom[postgres]: DROP TABLE IF EXISTS "users" CASCADE;
[2024-02-05 09:33:43.139667] : Dataloom[postgres]: DROP TABLE IF EXISTS "users" CASCADE;
[2024-02-05 09:33:43.170916] : Dataloom[postgres]: CREATE TABLE IF NOT EXISTS "users" ("id" BIGSERIAL PRIMARY KEY UNIQUE NOT NULL, "name" VARCHAR(255), "username" TEXT NOT NULL);
[2024-02-05 09:33:43.240924] : Dataloom[postgres]: DROP TABLE IF EXISTS "posts" CASCADE;
[2024-02-05 09:33:43.285634] : Dataloom[postgres]: CREATE TABLE IF NOT EXISTS "posts" ("id" BIGSERIAL PRIMARY KEY UNIQUE NOT NULL, "title" TEXT NOT NULL DEFAULT 'Hello there!!');
[2024-02-05 09:33:43.327224] : Dataloom[postgres]: SELECT tablename FROM pg_catalog.pg_tables WHERE schemaname='public';
[2024-02-05 09:33:43.541492] : Dataloom[postgres]: DROP TABLE IF EXISTS "users" CASCADE;
[2024-02-05 09:33:43.591508] : Dataloom[postgres]: CREATE TABLE IF NOT EXISTS "users" ("id" BIGSERIAL PRIMARY KEY UNIQUE NOT NULL, "name" VARCHAR(255) UNIQUE, "username" TEXT NOT NULL DEFAULT 'Hello there!!');
[2024-02-05 09:33:43.642497] : Dataloom[postgres]: DROP TABLE IF EXISTS "posts" CASCADE;
[2024-02-05 09:33:43.671441] : Dataloom[postgres]: CREATE TABLE IF NOT EXISTS "posts" ("completed" BOOLEAN DEFAULT False, "id" BIGSERIAL PRIMARY KEY UNIQUE NOT NULL, "title" VARCHAR(255) NOT NULL);
[2024-02-05 09:33:43.699441] : Dataloom[postgres]: SELECT tablename FROM pg_catalog.pg_tables WHERE schemaname='public';
[2024-02-05 09:33:43.854054] : Dataloom[postgres]: DROP TABLE IF EXISTS "posts" CASCADE;
[2024-02-05 09:33:43.874095] : Dataloom[postgres]: CREATE TABLE IF NOT EXISTS "posts" ("completed" BOOLEAN DEFAULT False, "id" BIGSERIAL PRIMARY KEY UNIQUE NOT NULL, "title" VARCHAR(255) NOT NULL, "createdAt" TIMESTAMP DEFAULT CURRENT_TIMESTAMP, "updatedAt" TIMESTAMP DEFAULT CURRENT_TIMESTAMP, "userId" BIGSERIAL NOT NULL REFERENCES "users"("id") ON DELETE CASCADE ON UPDATE CASCADE);
[2024-02-05 09:33:43.904049] : Dataloom[postgres]: DROP TABLE IF EXISTS "users" CASCADE;
[2024-02-05 09:33:43.931127] : Dataloom[postgres]: CREATE TABLE IF NOT EXISTS "users" ("id" BIGSERIAL PRIMARY KEY UNIQUE NOT NULL, "name" TEXT NOT NULL DEFAULT 'Bob', "username" VARCHAR(255) UNIQUE, "createdAt" TIMESTAMP DEFAULT CURRENT_TIMESTAMP, "updatedAt" TIMESTAMP DEFAULT CURRENT_TIMESTAMP);
[2024-02-05 09:33:43.963057] : Dataloom[postgres]: SELECT tablename FROM pg_catalog.pg_tables WHERE schemaname='public';
[2024-02-05 09:33:44.000053] : Dataloom[postgres]: INSERT INTO "users" ("name", "username") VALUES (%s, %s) RETURNING "id";
[2024-02-05 09:33:44.031065] : Dataloom[postgres]: DELETE FROM "users" WHERE "id" = %s;
[2024-02-05 09:33:44.056607] : Dataloom[postgres]: DELETE FROM "users" WHERE "id" = %s;
[2024-02-05 09:33:44.202182] : Dataloom[postgres]: DROP TABLE IF EXISTS "posts" CASCADE;
[2024-02-05 09:33:44.237021] : Dataloom[postgres]: CREATE TABLE IF NOT EXISTS "posts" ("completed" BOOLEAN DEFAULT False, "id" BIGSERIAL PRIMARY KEY UNIQUE NOT NULL, "title" VARCHAR(255) NOT NULL, "createdAt" TIMESTAMP DEFAULT CURRENT_TIMESTAMP, "updatedAt" TIMESTAMP DEFAULT CURRENT_TIMESTAMP, "userId" BIGSERIAL NOT NULL REFERENCES "users"("id") ON DELETE CASCADE ON UPDATE CASCADE);
[2024-02-05 09:33:44.300530] : Dataloom[postgres]: DROP TABLE IF EXISTS "users" CASCADE;
[2024-02-05 09:33:44.350568] : Dataloom[postgres]: CREATE TABLE IF NOT EXISTS "users" ("id" BIGSERIAL PRIMARY KEY UNIQUE NOT NULL, "name" TEXT NOT NULL DEFAULT 'Bob', "username" VARCHAR(255) UNIQUE, "createdAt" TIMESTAMP DEFAULT CURRENT_TIMESTAMP, "updatedAt" TIMESTAMP DEFAULT CURRENT_TIMESTAMP);
[2024-02-05 09:33:44.398096] : Dataloom[postgres]: SELECT tablename FROM pg_catalog.pg_tables WHERE schemaname='public';
[2024-02-05 09:33:44.444078] : Dataloom[postgres]: INSERT INTO "users" ("name", "username") VALUES (%s, %s) RETURNING *;
[2024-02-05 09:33:44.483041] : Dataloom[postgres]: 
    DELETE FROM "users" WHERE "id" = (
        SELECT "id" FROM  "users" WHERE "name" = %s LIMIT 1
    );
    
[2024-02-05 09:33:44.514039] : Dataloom[postgres]: SELECT "createdAt", "id", "name", "updatedAt", "username" FROM "users" WHERE "name" = %s   ;
[2024-02-05 09:33:44.544121] : Dataloom[postgres]: 
    DELETE FROM "users" WHERE "id" = (
        SELECT "id" FROM  "users" WHERE "name" = %s AND "id" = %s LIMIT 1
    );
    
[2024-02-05 09:33:44.572044] : Dataloom[postgres]: SELECT "createdAt", "id", "name", "updatedAt", "username" FROM "users" WHERE "name" = %s   ;
[2024-02-05 09:33:44.598041] : Dataloom[postgres]: 
    DELETE FROM "users" WHERE "id" = (
        SELECT "id" FROM  "users" WHERE "name" = %s AND "id" = %s LIMIT 1
    );
    
[2024-02-05 09:33:44.632037] : Dataloom[postgres]: SELECT "createdAt", "id", "name", "updatedAt", "username" FROM "users" WHERE "name" = %s   ;
[2024-02-05 09:33:44.808858] : Dataloom[postgres]: DROP TABLE IF EXISTS "posts" CASCADE;
[2024-02-05 09:33:44.840855] : Dataloom[postgres]: CREATE TABLE IF NOT EXISTS "posts" ("completed" BOOLEAN DEFAULT False, "id" BIGSERIAL PRIMARY KEY UNIQUE NOT NULL, "title" VARCHAR(255) NOT NULL, "createdAt" TIMESTAMP DEFAULT CURRENT_TIMESTAMP, "updatedAt" TIMESTAMP DEFAULT CURRENT_TIMESTAMP, "userId" BIGSERIAL NOT NULL REFERENCES "users"("id") ON DELETE CASCADE ON UPDATE CASCADE);
[2024-02-05 09:33:44.884856] : Dataloom[postgres]: DROP TABLE IF EXISTS "users" CASCADE;
[2024-02-05 09:33:44.924857] : Dataloom[postgres]: CREATE TABLE IF NOT EXISTS "users" ("id" BIGSERIAL PRIMARY KEY UNIQUE NOT NULL, "name" TEXT NOT NULL DEFAULT 'Bob', "username" VARCHAR(255) UNIQUE, "createdAt" TIMESTAMP DEFAULT CURRENT_TIMESTAMP, "updatedAt" TIMESTAMP DEFAULT CURRENT_TIMESTAMP);
[2024-02-05 09:33:44.960268] : Dataloom[postgres]: SELECT tablename FROM pg_catalog.pg_tables WHERE schemaname='public';
[2024-02-05 09:33:45.002275] : Dataloom[postgres]: INSERT INTO "users" ("name", "username") VALUES (%s, %s) RETURNING *;
[2024-02-05 09:33:45.044275] : Dataloom[postgres]: DELETE FROM "users" WHERE "name" = %s;
[2024-02-05 09:33:45.075047] : Dataloom[postgres]: SELECT "createdAt", "id", "name", "updatedAt", "username" FROM "users" WHERE "name" = %s   ;
[2024-02-05 09:33:45.103250] : Dataloom[postgres]: INSERT INTO "users" ("name", "username") VALUES (%s, %s) RETURNING *;
[2024-02-05 09:33:45.130837] : Dataloom[postgres]: DELETE FROM "users" WHERE "name" = %s AND "id" = %s;
[2024-02-05 09:33:45.157867] : Dataloom[postgres]: SELECT "createdAt", "id", "name", "updatedAt", "username" FROM "users" WHERE "name" = %s   ;
[2024-02-05 09:33:45.186824] : Dataloom[postgres]: DELETE FROM "users" WHERE "name" = %s AND "id" = %s;
[2024-02-05 09:33:45.215579] : Dataloom[postgres]: SELECT "createdAt", "id", "name", "updatedAt", "username" FROM "users" WHERE "name" = %s   ;
[2024-02-05 09:33:45.406641] : Dataloom[postgres]: DROP TABLE IF EXISTS "posts" CASCADE;
[2024-02-05 09:33:45.450037] : Dataloom[postgres]: CREATE TABLE IF NOT EXISTS "posts" ("completed" BOOLEAN DEFAULT False, "id" BIGSERIAL PRIMARY KEY UNIQUE NOT NULL, "title" VARCHAR(255) NOT NULL, "createdAt" TIMESTAMP DEFAULT CURRENT_TIMESTAMP, "updatedAt" TIMESTAMP DEFAULT CURRENT_TIMESTAMP, "userId" BIGSERIAL NOT NULL REFERENCES "users"("id") ON DELETE CASCADE ON UPDATE CASCADE);
[2024-02-05 09:33:45.499482] : Dataloom[postgres]: DROP TABLE IF EXISTS "users" CASCADE;
[2024-02-05 09:33:45.546659] : Dataloom[postgres]: CREATE TABLE IF NOT EXISTS "users" ("id" BIGSERIAL PRIMARY KEY UNIQUE NOT NULL, "name" TEXT NOT NULL DEFAULT 'Bob', "username" VARCHAR(255) UNIQUE, "createdAt" TIMESTAMP DEFAULT CURRENT_TIMESTAMP, "updatedAt" TIMESTAMP DEFAULT CURRENT_TIMESTAMP);
[2024-02-05 09:33:45.594866] : Dataloom[postgres]: SELECT tablename FROM pg_catalog.pg_tables WHERE schemaname='public';
[2024-02-05 09:33:45.636925] : Dataloom[postgres]: INSERT INTO "users" ("username") VALUES (%s) RETURNING "id";
[2024-02-05 09:33:45.667468] : Dataloom[postgres]: INSERT INTO "posts" ("title", "userId") VALUES (%s, %s) RETURNING "id";
[2024-02-05 09:33:45.853601] : Dataloom[postgres]: DROP TABLE IF EXISTS "posts" CASCADE;
[2024-02-05 09:33:45.896595] : Dataloom[postgres]: CREATE TABLE IF NOT EXISTS "posts" ("completed" BOOLEAN DEFAULT False, "id" BIGSERIAL PRIMARY KEY UNIQUE NOT NULL, "title" VARCHAR(255) NOT NULL, "createdAt" TIMESTAMP DEFAULT CURRENT_TIMESTAMP, "updatedAt" TIMESTAMP DEFAULT CURRENT_TIMESTAMP, "userId" BIGSERIAL NOT NULL REFERENCES "users"("id") ON DELETE CASCADE ON UPDATE CASCADE);
[2024-02-05 09:33:45.950651] : Dataloom[postgres]: DROP TABLE IF EXISTS "users" CASCADE;
[2024-02-05 09:33:45.997722] : Dataloom[postgres]: CREATE TABLE IF NOT EXISTS "users" ("id" BIGSERIAL PRIMARY KEY UNIQUE NOT NULL, "name" TEXT NOT NULL DEFAULT 'Bob', "username" VARCHAR(255) UNIQUE, "createdAt" TIMESTAMP DEFAULT CURRENT_TIMESTAMP, "updatedAt" TIMESTAMP DEFAULT CURRENT_TIMESTAMP);
[2024-02-05 09:33:46.050188] : Dataloom[postgres]: SELECT tablename FROM pg_catalog.pg_tables WHERE schemaname='public';
[2024-02-05 09:33:46.099502] : Dataloom[postgres]: INSERT INTO "users" ("username") VALUES (%s) RETURNING "id";
[2024-02-05 09:33:46.125492] : Dataloom[postgres]: INSERT INTO "posts" ("title", "userId") VALUES (%s, %s) RETURNING *;
[2024-02-05 09:33:46.279506] : Dataloom[postgres]: DROP TABLE IF EXISTS "posts" CASCADE;
[2024-02-05 09:33:46.321325] : Dataloom[postgres]: CREATE TABLE IF NOT EXISTS "posts" ("completed" BOOLEAN DEFAULT False, "id" BIGSERIAL PRIMARY KEY UNIQUE NOT NULL, "title" VARCHAR(255) NOT NULL, "createdAt" TIMESTAMP DEFAULT CURRENT_TIMESTAMP, "updatedAt" TIMESTAMP DEFAULT CURRENT_TIMESTAMP, "userId" BIGSERIAL NOT NULL REFERENCES "users"("id") ON DELETE CASCADE ON UPDATE CASCADE);
[2024-02-05 09:33:46.371787] : Dataloom[postgres]: DROP TABLE IF EXISTS "users" CASCADE;
[2024-02-05 09:33:46.411811] : Dataloom[postgres]: CREATE TABLE IF NOT EXISTS "users" ("id" BIGSERIAL PRIMARY KEY UNIQUE NOT NULL, "name" TEXT NOT NULL DEFAULT 'Bob', "username" VARCHAR(255) UNIQUE);
[2024-02-05 09:33:46.450808] : Dataloom[postgres]: SELECT tablename FROM pg_catalog.pg_tables WHERE schemaname='public';
[2024-02-05 09:33:46.492452] : Dataloom[postgres]: INSERT INTO "users" ("username") VALUES (%s) RETURNING "id";
[2024-02-05 09:33:46.522452] : Dataloom[postgres]: INSERT INTO "posts" ("title", "userId") VALUES (%s, %s) RETURNING *;
[2024-02-05 09:33:46.558579] : Dataloom[postgres]: SELECT "id", "name", "username" FROM "users" WHERE "id" = %s;
[2024-02-05 09:33:46.585507] : Dataloom[postgres]: SELECT "id", "name", "username" FROM "users" WHERE "id" = %s;
[2024-02-05 09:33:46.612462] : Dataloom[postgres]: SELECT "id", "completed" FROM "posts" WHERE "id" = %s;
[2024-02-05 09:33:46.792354] : Dataloom[postgres]: DROP TABLE IF EXISTS "posts" CASCADE;
[2024-02-05 09:33:46.834903] : Dataloom[postgres]: CREATE TABLE IF NOT EXISTS "posts" ("completed" BOOLEAN DEFAULT False, "id" BIGSERIAL PRIMARY KEY UNIQUE NOT NULL, "title" VARCHAR(255) NOT NULL, "createdAt" TIMESTAMP DEFAULT CURRENT_TIMESTAMP, "updatedAt" TIMESTAMP DEFAULT CURRENT_TIMESTAMP, "userId" BIGSERIAL NOT NULL REFERENCES "users"("id") ON DELETE CASCADE ON UPDATE CASCADE);
[2024-02-05 09:33:46.883921] : Dataloom[postgres]: DROP TABLE IF EXISTS "users" CASCADE;
[2024-02-05 09:33:46.923806] : Dataloom[postgres]: CREATE TABLE IF NOT EXISTS "users" ("id" BIGSERIAL PRIMARY KEY UNIQUE NOT NULL, "name" TEXT NOT NULL DEFAULT 'Bob', "username" VARCHAR(255) UNIQUE);
[2024-02-05 09:33:46.972302] : Dataloom[postgres]: SELECT tablename FROM pg_catalog.pg_tables WHERE schemaname='public';
[2024-02-05 09:33:47.022735] : Dataloom[postgres]: INSERT INTO "users" ("username") VALUES (%s) RETURNING "id";
[2024-02-05 09:33:47.062730] : Dataloom[postgres]: INSERT INTO "posts" ("title", "userId") VALUES (%s, %s) RETURNING *;
[2024-02-05 09:33:47.105902] : Dataloom[postgres]: SELECT "id", "name", "username" FROM "users"   ;
[2024-02-05 09:33:47.127889] : Dataloom[postgres]: SELECT "completed", "createdAt", "id", "title", "updatedAt", "userId" FROM "posts"   ;
[2024-02-05 09:33:47.151896] : Dataloom[postgres]: SELECT "id", "completed" FROM "posts"  LIMIT 3 OFFSET 3;
[2024-02-05 09:33:47.275392] : Dataloom[postgres]: DROP TABLE IF EXISTS "posts" CASCADE;
[2024-02-05 09:33:47.314747] : Dataloom[postgres]: CREATE TABLE IF NOT EXISTS "posts" ("completed" BOOLEAN DEFAULT False, "id" BIGSERIAL PRIMARY KEY UNIQUE NOT NULL, "title" VARCHAR(255) NOT NULL, "createdAt" TIMESTAMP DEFAULT CURRENT_TIMESTAMP, "updatedAt" TIMESTAMP DEFAULT CURRENT_TIMESTAMP, "userId" BIGSERIAL NOT NULL REFERENCES "users"("id") ON DELETE CASCADE ON UPDATE CASCADE);
[2024-02-05 09:33:47.363816] : Dataloom[postgres]: DROP TABLE IF EXISTS "users" CASCADE;
[2024-02-05 09:33:47.405304] : Dataloom[postgres]: CREATE TABLE IF NOT EXISTS "users" ("id" BIGSERIAL PRIMARY KEY UNIQUE NOT NULL, "name" TEXT NOT NULL DEFAULT 'Bob', "username" VARCHAR(255) UNIQUE);
[2024-02-05 09:33:47.448333] : Dataloom[postgres]: SELECT tablename FROM pg_catalog.pg_tables WHERE schemaname='public';
[2024-02-05 09:33:47.493331] : Dataloom[postgres]: INSERT INTO "users" ("username") VALUES (%s) RETURNING "id";
[2024-02-05 09:33:47.525051] : Dataloom[postgres]: INSERT INTO "posts" ("title", "userId") VALUES (%s, %s) RETURNING *;
[2024-02-05 09:33:47.559041] : Dataloom[postgres]: SELECT "id", "name", "username" FROM "users" WHERE "id" = %s   ;
[2024-02-05 09:33:47.585400] : Dataloom[postgres]: SELECT "id", "name", "username" FROM "users" WHERE "id" = %s   ;
[2024-02-05 09:33:47.612346] : Dataloom[postgres]: SELECT "id", "name", "username" FROM "users" WHERE "id" = %s AND "name" = %s   ;
[2024-02-05 09:33:47.640347] : Dataloom[postgres]: SELECT "id", "name", "username" FROM "users" WHERE "id" = %s AND "username" = %s   ;
[2024-02-05 09:33:47.670395] : Dataloom[postgres]: SELECT "id", "name", "username" FROM "users" WHERE "name" = %s AND "username" = %s   ;
[2024-02-05 09:33:47.699439] : Dataloom[postgres]: SELECT "id", "completed" FROM "posts"   ;
[2024-02-05 09:33:47.895502] : Dataloom[postgres]: DROP TABLE IF EXISTS "posts" CASCADE;
[2024-02-05 09:33:47.937509] : Dataloom[postgres]: CREATE TABLE IF NOT EXISTS "posts" ("completed" BOOLEAN DEFAULT False, "id" BIGSERIAL PRIMARY KEY UNIQUE NOT NULL, "title" VARCHAR(255) NOT NULL, "createdAt" TIMESTAMP DEFAULT CURRENT_TIMESTAMP, "updatedAt" TIMESTAMP DEFAULT CURRENT_TIMESTAMP, "userId" BIGSERIAL NOT NULL REFERENCES "users"("id") ON DELETE CASCADE ON UPDATE CASCADE);
[2024-02-05 09:33:47.985918] : Dataloom[postgres]: DROP TABLE IF EXISTS "users" CASCADE;
[2024-02-05 09:33:48.027987] : Dataloom[postgres]: CREATE TABLE IF NOT EXISTS "users" ("id" BIGSERIAL PRIMARY KEY UNIQUE NOT NULL, "name" TEXT NOT NULL DEFAULT 'Bob', "username" VARCHAR(255) UNIQUE);
[2024-02-05 09:33:48.068758] : Dataloom[postgres]: SELECT tablename FROM pg_catalog.pg_tables WHERE schemaname='public';
[2024-02-05 09:33:48.110816] : Dataloom[postgres]: INSERT INTO "users" ("username") VALUES (%s) RETURNING "id";
[2024-02-05 09:33:48.140087] : Dataloom[postgres]: INSERT INTO "posts" ("title", "userId") VALUES (%s, %s) RETURNING *;
[2024-02-05 09:33:48.173820] : Dataloom[postgres]: SELECT "completed", "createdAt", "id", "title", "updatedAt", "userId" FROM "posts" WHERE "id" = %s AND "userId" = %s   ;
[2024-02-05 09:33:48.203222] : Dataloom[postgres]: SELECT "id", "name", "username" FROM "users"   ;
[2024-02-05 09:33:48.228958] : Dataloom[postgres]: SELECT "id", "name", "username" FROM "users" WHERE "id" = %s   ;
[2024-02-05 09:33:48.256013] : Dataloom[postgres]: SELECT "id", "name", "username" FROM "users" WHERE "id" = %s   ;
[2024-02-05 09:33:48.280966] : Dataloom[postgres]: SELECT "id", "name", "username" FROM "users" WHERE "id" = %s AND "name" = %s   ;
[2024-02-05 09:33:48.305009] : Dataloom[postgres]: SELECT "id", "name", "username" FROM "users" WHERE "id" = %s AND "username" = %s   ;
[2024-02-05 09:33:48.329018] : Dataloom[postgres]: SELECT "id", "name", "username" FROM "users" WHERE "name" = %s AND "username" = %s   ;
[2024-02-05 09:33:48.353007] : Dataloom[postgres]: SELECT "id", "completed" FROM "posts" WHERE "userId" = %s  LIMIT 3 OFFSET 3;
[2024-02-05 09:33:48.377633] : Dataloom[postgres]: SELECT "completed", "createdAt", "id", "title", "updatedAt", "userId" FROM "posts"   ;
[2024-02-05 09:33:48.585104] : Dataloom[postgres]: DROP TABLE IF EXISTS "posts" CASCADE;
[2024-02-05 09:33:48.635714] : Dataloom[postgres]: CREATE TABLE IF NOT EXISTS "posts" ("completed" BOOLEAN DEFAULT False, "id" BIGSERIAL PRIMARY KEY UNIQUE NOT NULL, "title" VARCHAR(255) NOT NULL, "createdAt" TIMESTAMP DEFAULT CURRENT_TIMESTAMP, "updatedAt" TIMESTAMP DEFAULT CURRENT_TIMESTAMP, "userId" BIGSERIAL NOT NULL REFERENCES "users"("id") ON DELETE CASCADE ON UPDATE CASCADE);
[2024-02-05 09:33:48.692704] : Dataloom[postgres]: DROP TABLE IF EXISTS "users" CASCADE;
[2024-02-05 09:33:48.742703] : Dataloom[postgres]: CREATE TABLE IF NOT EXISTS "users" ("id" BIGSERIAL PRIMARY KEY UNIQUE NOT NULL, "name" TEXT NOT NULL DEFAULT 'Bob', "username" VARCHAR(255) UNIQUE, "createdAt" TIMESTAMP DEFAULT CURRENT_TIMESTAMP, "updatedAt" TIMESTAMP DEFAULT CURRENT_TIMESTAMP);
[2024-02-05 09:33:48.797707] : Dataloom[postgres]: SELECT tablename FROM pg_catalog.pg_tables WHERE schemaname='public';
[2024-02-05 09:33:48.837702] : Dataloom[postgres]: INSERT INTO "users" ("username") VALUES (%s) RETURNING "id";
[2024-02-05 09:33:48.871756] : Dataloom[postgres]: INSERT INTO "posts" ("title", "userId") VALUES (%s, %s) RETURNING *;
[2024-02-05 09:33:48.963779] : Dataloom[postgres]: UPDATE "users" SET "updatedAt" = %s WHERE "id" = %s;
[2024-02-05 09:33:49.008965] : Dataloom[postgres]: UPDATE "users" SET "updatedAt" = %s WHERE "id" = %s;
[2024-02-05 09:33:49.056983] : Dataloom[postgres]: SELECT "createdAt", "id", "name", "updatedAt", "username" FROM "users" WHERE "id" = %s;
[2024-02-05 09:33:49.107030] : Dataloom[postgres]: UPDATE "users" SET "id" = %s, "updatedAt" = %s WHERE "id" = %s;
[2024-02-05 09:33:49.339783] : Dataloom[postgres]: DROP TABLE IF EXISTS "posts" CASCADE;
[2024-02-05 09:33:49.384822] : Dataloom[postgres]: CREATE TABLE IF NOT EXISTS "posts" ("completed" BOOLEAN DEFAULT False, "id" BIGSERIAL PRIMARY KEY UNIQUE NOT NULL, "title" VARCHAR(255) NOT NULL, "createdAt" TIMESTAMP DEFAULT CURRENT_TIMESTAMP, "userId" BIGSERIAL NOT NULL REFERENCES "users"("id") ON DELETE CASCADE ON UPDATE CASCADE);
[2024-02-05 09:33:49.445675] : Dataloom[postgres]: DROP TABLE IF EXISTS "users" CASCADE;
[2024-02-05 09:33:49.499922] : Dataloom[postgres]: CREATE TABLE IF NOT EXISTS "users" ("id" BIGSERIAL PRIMARY KEY UNIQUE NOT NULL, "name" TEXT NOT NULL DEFAULT 'Bob', "username" VARCHAR(255) UNIQUE, "createdAt" TIMESTAMP DEFAULT CURRENT_TIMESTAMP, "updatedAt" TIMESTAMP DEFAULT CURRENT_TIMESTAMP);
[2024-02-05 09:33:49.556316] : Dataloom[postgres]: SELECT tablename FROM pg_catalog.pg_tables WHERE schemaname='public';
[2024-02-05 09:33:49.613304] : Dataloom[postgres]: INSERT INTO "users" ("username") VALUES (%s) RETURNING "id";
[2024-02-05 09:33:49.654046] : Dataloom[postgres]: INSERT INTO "posts" ("title", "userId") VALUES (%s, %s) RETURNING *;
[2024-02-05 09:33:49.742458] : Dataloom[postgres]: 
        UPDATE "users" SET "name" = %s, "updatedAt" = %s WHERE "id" = (
            SELECT "id" FROM  "users" WHERE "username" = %s LIMIT 1
        );
        
[2024-02-05 09:33:49.777975] : Dataloom[postgres]: 
        UPDATE "users" SET "name" = %s, "updatedAt" = %s WHERE "id" = (
            SELECT "id" FROM  "users" WHERE "username" = %s LIMIT 1
        );
        
[2024-02-05 09:33:49.808617] : Dataloom[postgres]: SELECT "createdAt", "id", "name", "updatedAt", "username" FROM "users" WHERE "id" = %s;
[2024-02-05 09:33:49.838989] : Dataloom[postgres]: 
        UPDATE "users" SET "id" = %s, "updatedAt" = %s WHERE "id" = (
            SELECT "id" FROM  "users" WHERE "username" = %s LIMIT 1
        );
        
[2024-02-05 09:33:50.036902] : Dataloom[postgres]: DROP TABLE IF EXISTS "posts" CASCADE;
[2024-02-05 09:33:50.087481] : Dataloom[postgres]: CREATE TABLE IF NOT EXISTS "posts" ("completed" BOOLEAN DEFAULT False, "id" BIGSERIAL PRIMARY KEY UNIQUE NOT NULL, "title" VARCHAR(255) NOT NULL, "createdAt" TIMESTAMP DEFAULT CURRENT_TIMESTAMP, "userId" BIGSERIAL NOT NULL REFERENCES "users"("id") ON DELETE CASCADE ON UPDATE CASCADE);
[2024-02-05 09:33:50.151208] : Dataloom[postgres]: DROP TABLE IF EXISTS "users" CASCADE;
[2024-02-05 09:33:50.202160] : Dataloom[postgres]: CREATE TABLE IF NOT EXISTS "users" ("id" BIGSERIAL PRIMARY KEY UNIQUE NOT NULL, "name" TEXT NOT NULL DEFAULT 'Bob', "username" VARCHAR(255) UNIQUE, "createdAt" TIMESTAMP DEFAULT CURRENT_TIMESTAMP, "updatedAt" TIMESTAMP DEFAULT CURRENT_TIMESTAMP);
[2024-02-05 09:33:50.250729] : Dataloom[postgres]: SELECT tablename FROM pg_catalog.pg_tables WHERE schemaname='public';
[2024-02-05 09:33:50.287637] : Dataloom[postgres]: INSERT INTO "users" ("username") VALUES (%s) RETURNING "id";
[2024-02-05 09:33:50.313284] : Dataloom[postgres]: INSERT INTO "posts" ("title", "userId") VALUES (%s, %s) RETURNING *;
[2024-02-05 09:33:50.342234] : Dataloom[postgres]: UPDATE "posts" SET "title" = %s WHERE "userId" = %s;
[2024-02-05 09:33:50.371125] : Dataloom[postgres]: UPDATE "posts" SET "title" = %s WHERE "userId" = %s;
[2024-02-05 09:33:50.399045] : Dataloom[postgres]: UPDATE "posts" SET "userId" = %s WHERE "userId" = %s;
[2024-02-05 09:33:50.458046] : Dataloom[sqlite]: DROP TABLE IF EXISTS users;
[2024-02-05 09:33:50.514044] : Dataloom[sqlite]: DROP TABLE IF EXISTS users;
[2024-02-05 09:33:50.564052] : Dataloom[sqlite]: DROP TABLE IF EXISTS users;
[2024-02-05 09:33:50.604038] : Dataloom[sqlite]: CREATE TABLE IF NOT EXISTS `users` (`id` INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL, `name` VARCHAR, `username` TEXT NOT NULL);
[2024-02-05 09:33:50.646038] : Dataloom[sqlite]: DROP TABLE IF EXISTS posts;
[2024-02-05 09:33:50.688046] : Dataloom[sqlite]: CREATE TABLE IF NOT EXISTS `posts` (`id` INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL, `title` TEXT NOT NULL);
[2024-02-05 09:33:50.726608] : Dataloom[sqlite]: SELECT name FROM sqlite_master WHERE type='table';
[2024-02-05 09:33:50.770885] : Dataloom[sqlite]: DROP TABLE IF EXISTS users;
[2024-02-05 09:33:50.822257] : Dataloom[sqlite]: CREATE TABLE IF NOT EXISTS `users` (`id` INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL, `name` VARCHAR UNIQUE, `username` TEXT NOT NULL DEFAULT 'Hello there!!');
[2024-02-05 09:33:50.856253] : Dataloom[sqlite]: DROP TABLE IF EXISTS posts;
[2024-02-05 09:33:50.897259] : Dataloom[sqlite]: CREATE TABLE IF NOT EXISTS `posts` (`completed` BOOLEAN DEFAULT False, `id` INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL, `title` VARCHAR NOT NULL);
[2024-02-05 09:33:50.931307] : Dataloom[sqlite]: SELECT name FROM sqlite_master WHERE type='table';
[2024-02-05 09:33:50.970306] : Dataloom[sqlite]: DROP TABLE IF EXISTS posts;
[2024-02-05 09:33:51.031111] : Dataloom[sqlite]: CREATE TABLE IF NOT EXISTS `posts` (`completed` BOOLEAN DEFAULT False, `id` INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL, `title` VARCHAR NOT NULL, `createdAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP, `updatedAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP, `userId` INTEGER NOT NULL REFERENCES `users`(`id`) ON DELETE CASCADE ON UPDATE CASCADE);
[2024-02-05 09:33:51.072095] : Dataloom[sqlite]: DROP TABLE IF EXISTS users;
[2024-02-05 09:33:51.104095] : Dataloom[sqlite]: CREATE TABLE IF NOT EXISTS `users` (`id` INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL, `name` TEXT NOT NULL DEFAULT 'Bob', `username` VARCHAR UNIQUE, `createdAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP, `updatedAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP);
[2024-02-05 09:33:51.155235] : Dataloom[sqlite]: SELECT name FROM sqlite_master WHERE type='table';
[2024-02-05 09:33:51.193223] : Dataloom[sqlite]: INSERT INTO `users` (`name`, `username`) VALUES (?, ?);
[2024-02-05 09:33:51.250871] : Dataloom[sqlite]: DELETE FROM `users` WHERE `id` = ?;
[2024-02-05 09:33:51.307124] : Dataloom[sqlite]: DELETE FROM `users` WHERE `id` = ?;
[2024-02-05 09:33:51.361549] : Dataloom[sqlite]: DROP TABLE IF EXISTS posts;
[2024-02-05 09:33:51.399547] : Dataloom[sqlite]: CREATE TABLE IF NOT EXISTS `posts` (`completed` BOOLEAN DEFAULT False, `id` INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL, `title` VARCHAR NOT NULL, `createdAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP, `updatedAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP, `userId` INTEGER NOT NULL REFERENCES `users`(`id`) ON DELETE CASCADE ON UPDATE CASCADE);
[2024-02-05 09:33:51.436030] : Dataloom[sqlite]: DROP TABLE IF EXISTS users;
[2024-02-05 09:33:51.473068] : Dataloom[sqlite]: CREATE TABLE IF NOT EXISTS `users` (`id` INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL, `name` TEXT NOT NULL DEFAULT 'Bob', `username` VARCHAR UNIQUE, `createdAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP, `updatedAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP);
[2024-02-05 09:33:51.503466] : Dataloom[sqlite]: SELECT name FROM sqlite_master WHERE type='table';
[2024-02-05 09:33:51.526378] : Dataloom[sqlite]: INSERT INTO `users` (`name`, `username`) VALUES (?, ?);
[2024-02-05 09:33:51.551379] : Dataloom[sqlite]: 
    DELETE FROM `users` WHERE `id` = (
        SELECT `id` FROM  `users` WHERE `name` = ? LIMIT 1
    );
    
[2024-02-05 09:33:51.573376] : Dataloom[sqlite]: SELECT `createdAt`, `id`, `name`, `updatedAt`, `username` FROM `users` WHERE `name` = ?   ;
[2024-02-05 09:33:51.589540] : Dataloom[sqlite]: 
    DELETE FROM `users` WHERE `id` = (
        SELECT `id` FROM  `users` WHERE `name` = ? AND `id` = ? LIMIT 1
    );
    
[2024-02-05 09:33:51.609379] : Dataloom[sqlite]: SELECT `createdAt`, `id`, `name`, `updatedAt`, `username` FROM `users` WHERE `name` = ?   ;
[2024-02-05 09:33:51.630799] : Dataloom[sqlite]: 
    DELETE FROM `users` WHERE `id` = (
        SELECT `id` FROM  `users` WHERE `name` = ? AND `id` = ? LIMIT 1
    );
    
[2024-02-05 09:33:51.664933] : Dataloom[sqlite]: SELECT `createdAt`, `id`, `name`, `updatedAt`, `username` FROM `users` WHERE `name` = ?   ;
[2024-02-05 09:33:51.720797] : Dataloom[sqlite]: DROP TABLE IF EXISTS posts;
[2024-02-05 09:33:51.792806] : Dataloom[sqlite]: CREATE TABLE IF NOT EXISTS `posts` (`completed` BOOLEAN DEFAULT False, `id` INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL, `title` VARCHAR NOT NULL, `createdAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP, `updatedAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP, `userId` INTEGER NOT NULL REFERENCES `users`(`id`) ON DELETE CASCADE ON UPDATE CASCADE);
[2024-02-05 09:33:51.855791] : Dataloom[sqlite]: DROP TABLE IF EXISTS users;
[2024-02-05 09:33:51.929795] : Dataloom[sqlite]: CREATE TABLE IF NOT EXISTS `users` (`id` INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL, `name` TEXT NOT NULL DEFAULT 'Bob', `username` VARCHAR UNIQUE, `createdAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP, `updatedAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP);
[2024-02-05 09:33:51.987806] : Dataloom[sqlite]: SELECT name FROM sqlite_master WHERE type='table';
[2024-02-05 09:33:52.024844] : Dataloom[sqlite]: INSERT INTO `users` (`name`, `username`) VALUES (?, ?);
[2024-02-05 09:33:52.135363] : Dataloom[sqlite]: DELETE FROM `users` WHERE `name` = ?;
[2024-02-05 09:33:52.167364] : Dataloom[sqlite]: SELECT `createdAt`, `id`, `name`, `updatedAt`, `username` FROM `users` WHERE `name` = ?   ;
[2024-02-05 09:33:52.198365] : Dataloom[sqlite]: INSERT INTO `users` (`name`, `username`) VALUES (?, ?);
[2024-02-05 09:33:52.242360] : Dataloom[sqlite]: DELETE FROM `users` WHERE `name` = ? AND `id` = ?;
[2024-02-05 09:33:52.293530] : Dataloom[sqlite]: SELECT `createdAt`, `id`, `name`, `updatedAt`, `username` FROM `users` WHERE `name` = ?   ;
[2024-02-05 09:33:52.355536] : Dataloom[sqlite]: DELETE FROM `users` WHERE `name` = ? AND `id` = ?;
[2024-02-05 09:33:52.384532] : Dataloom[sqlite]: SELECT `createdAt`, `id`, `name`, `updatedAt`, `username` FROM `users` WHERE `name` = ?   ;
[2024-02-05 09:33:52.432529] : Dataloom[sqlite]: DROP TABLE IF EXISTS posts;
[2024-02-05 09:33:52.466422] : Dataloom[sqlite]: CREATE TABLE IF NOT EXISTS `posts` (`completed` BOOLEAN DEFAULT False, `id` INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL, `title` VARCHAR NOT NULL, `createdAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP, `updatedAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP, `userId` INTEGER NOT NULL REFERENCES `users`(`id`) ON DELETE CASCADE ON UPDATE CASCADE);
[2024-02-05 09:33:52.503379] : Dataloom[sqlite]: DROP TABLE IF EXISTS users;
[2024-02-05 09:33:52.547383] : Dataloom[sqlite]: CREATE TABLE IF NOT EXISTS `users` (`id` INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL, `name` TEXT NOT NULL DEFAULT 'Bob', `username` VARCHAR UNIQUE, `createdAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP, `updatedAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP);
[2024-02-05 09:33:52.586317] : Dataloom[sqlite]: SELECT name FROM sqlite_master WHERE type='table';
[2024-02-05 09:33:52.609313] : Dataloom[sqlite]: INSERT INTO `users` (`username`) VALUES (?);
[2024-02-05 09:33:52.633313] : Dataloom[sqlite]: INSERT INTO `posts` (`title`, `userId`) VALUES (?, ?);
[2024-02-05 09:33:52.667907] : Dataloom[sqlite]: DROP TABLE IF EXISTS posts;
[2024-02-05 09:33:52.701903] : Dataloom[sqlite]: CREATE TABLE IF NOT EXISTS `posts` (`completed` BOOLEAN DEFAULT False, `id` INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL, `title` VARCHAR NOT NULL, `createdAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP, `updatedAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP, `userId` INTEGER NOT NULL REFERENCES `users`(`id`) ON DELETE CASCADE ON UPDATE CASCADE);
[2024-02-05 09:33:52.736100] : Dataloom[sqlite]: DROP TABLE IF EXISTS users;
[2024-02-05 09:33:52.770567] : Dataloom[sqlite]: CREATE TABLE IF NOT EXISTS `users` (`id` INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL, `name` TEXT NOT NULL DEFAULT 'Bob', `username` VARCHAR UNIQUE, `createdAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP, `updatedAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP);
[2024-02-05 09:33:52.800542] : Dataloom[sqlite]: SELECT name FROM sqlite_master WHERE type='table';
[2024-02-05 09:33:52.840538] : Dataloom[sqlite]: INSERT INTO `users` (`username`) VALUES (?);
[2024-02-05 09:33:52.893545] : Dataloom[sqlite]: INSERT INTO `posts` (`title`, `userId`) VALUES (?, ?);
[2024-02-05 09:33:52.956530] : Dataloom[sqlite]: DROP TABLE IF EXISTS posts;
[2024-02-05 09:33:53.001548] : Dataloom[sqlite]: CREATE TABLE IF NOT EXISTS `posts` (`completed` BOOLEAN DEFAULT False, `id` INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL, `title` VARCHAR NOT NULL, `createdAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP, `updatedAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP, `userId` INTEGER NOT NULL REFERENCES `users`(`id`) ON DELETE CASCADE ON UPDATE CASCADE);
[2024-02-05 09:33:53.044532] : Dataloom[sqlite]: DROP TABLE IF EXISTS users;
[2024-02-05 09:33:53.088501] : Dataloom[sqlite]: CREATE TABLE IF NOT EXISTS `users` (`id` INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL, `name` TEXT NOT NULL DEFAULT 'Bob', `username` VARCHAR UNIQUE);
[2024-02-05 09:33:53.140508] : Dataloom[sqlite]: SELECT name FROM sqlite_master WHERE type='table';
[2024-02-05 09:33:53.180857] : Dataloom[sqlite]: INSERT INTO `users` (`username`) VALUES (?);
[2024-02-05 09:33:53.235562] : Dataloom[sqlite]: INSERT INTO `posts` (`title`, `userId`) VALUES (?, ?);
[2024-02-05 09:33:53.307160] : Dataloom[sqlite]: SELECT `id`, `name`, `username` FROM `users` WHERE `id` = ?;
[2024-02-05 09:33:53.360150] : Dataloom[sqlite]: SELECT `id`, `name`, `username` FROM `users` WHERE `id` = ?;
[2024-02-05 09:33:53.421971] : Dataloom[sqlite]: SELECT `id`, `completed` FROM `posts` WHERE `id` = ?;
[2024-02-05 09:33:53.492816] : Dataloom[sqlite]: DROP TABLE IF EXISTS posts;
[2024-02-05 09:33:53.577640] : Dataloom[sqlite]: CREATE TABLE IF NOT EXISTS `posts` (`completed` BOOLEAN DEFAULT False, `id` INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL, `title` VARCHAR NOT NULL, `createdAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP, `updatedAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP, `userId` INTEGER NOT NULL REFERENCES `users`(`id`) ON DELETE CASCADE ON UPDATE CASCADE);
[2024-02-05 09:33:53.647396] : Dataloom[sqlite]: DROP TABLE IF EXISTS users;
[2024-02-05 09:33:53.703967] : Dataloom[sqlite]: CREATE TABLE IF NOT EXISTS `users` (`id` INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL, `name` TEXT NOT NULL DEFAULT 'Bob', `username` VARCHAR UNIQUE);
[2024-02-05 09:33:53.748357] : Dataloom[sqlite]: SELECT name FROM sqlite_master WHERE type='table';
[2024-02-05 09:33:53.784003] : Dataloom[sqlite]: INSERT INTO `users` (`username`) VALUES (?);
[2024-02-05 09:33:53.820009] : Dataloom[sqlite]: INSERT INTO `posts` (`title`, `userId`) VALUES (?, ?);
[2024-02-05 09:33:53.857015] : Dataloom[sqlite]: SELECT `id`, `name`, `username` FROM `users`   ;
[2024-02-05 09:33:53.894977] : Dataloom[sqlite]: SELECT `completed`, `createdAt`, `id`, `title`, `updatedAt`, `userId` FROM `posts`   ;
[2024-02-05 09:33:53.935971] : Dataloom[sqlite]: SELECT `id`, `completed` FROM `posts`  LIMIT 3 OFFSET 3;
[2024-02-05 09:33:53.984970] : Dataloom[sqlite]: DROP TABLE IF EXISTS posts;
[2024-02-05 09:33:54.031969] : Dataloom[sqlite]: CREATE TABLE IF NOT EXISTS `posts` (`completed` BOOLEAN DEFAULT False, `id` INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL, `title` VARCHAR NOT NULL, `createdAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP, `updatedAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP, `userId` INTEGER NOT NULL REFERENCES `users`(`id`) ON DELETE CASCADE ON UPDATE CASCADE);
[2024-02-05 09:33:54.083970] : Dataloom[sqlite]: DROP TABLE IF EXISTS users;
[2024-02-05 09:33:54.141972] : Dataloom[sqlite]: CREATE TABLE IF NOT EXISTS `users` (`id` INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL, `name` TEXT NOT NULL DEFAULT 'Bob', `username` VARCHAR UNIQUE);
[2024-02-05 09:33:54.194947] : Dataloom[sqlite]: SELECT name FROM sqlite_master WHERE type='table';
[2024-02-05 09:33:54.237990] : Dataloom[sqlite]: INSERT INTO `users` (`username`) VALUES (?);
[2024-02-05 09:33:54.285942] : Dataloom[sqlite]: INSERT INTO `posts` (`title`, `userId`) VALUES (?, ?);
[2024-02-05 09:33:54.341894] : Dataloom[sqlite]: SELECT `id`, `name`, `username` FROM `users` WHERE `id` = ?   ;
[2024-02-05 09:33:54.383897] : Dataloom[sqlite]: SELECT `id`, `name`, `username` FROM `users` WHERE `id` = ?   ;
[2024-02-05 09:33:54.425895] : Dataloom[sqlite]: SELECT `id`, `name`, `username` FROM `users` WHERE `id` = ? AND `name` = ?   ;
[2024-02-05 09:33:54.460896] : Dataloom[sqlite]: SELECT `id`, `name`, `username` FROM `users` WHERE `id` = ? AND `username` = ?   ;
[2024-02-05 09:33:54.491667] : Dataloom[sqlite]: SELECT `id`, `name`, `username` FROM `users` WHERE `name` = ? AND `username` = ?   ;
[2024-02-05 09:33:54.519666] : Dataloom[sqlite]: SELECT `id`, `completed` FROM `posts`   ;
[2024-02-05 09:33:54.557729] : Dataloom[sqlite]: DROP TABLE IF EXISTS posts;
[2024-02-05 09:33:54.597515] : Dataloom[sqlite]: CREATE TABLE IF NOT EXISTS `posts` (`completed` BOOLEAN DEFAULT False, `id` INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL, `title` VARCHAR NOT NULL, `createdAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP, `updatedAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP, `userId` INTEGER NOT NULL REFERENCES `users`(`id`) ON DELETE CASCADE ON UPDATE CASCADE);
[2024-02-05 09:33:54.630498] : Dataloom[sqlite]: DROP TABLE IF EXISTS users;
[2024-02-05 09:33:54.666629] : Dataloom[sqlite]: CREATE TABLE IF NOT EXISTS `users` (`id` INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL, `name` TEXT NOT NULL DEFAULT 'Bob', `username` VARCHAR UNIQUE);
[2024-02-05 09:33:54.706676] : Dataloom[sqlite]: SELECT name FROM sqlite_master WHERE type='table';
[2024-02-05 09:33:54.736667] : Dataloom[sqlite]: INSERT INTO `users` (`username`) VALUES (?);
[2024-02-05 09:33:54.783329] : Dataloom[sqlite]: INSERT INTO `posts` (`title`, `userId`) VALUES (?, ?);
[2024-02-05 09:33:54.818323] : Dataloom[sqlite]: SELECT `completed`, `createdAt`, `id`, `title`, `updatedAt`, `userId` FROM `posts` WHERE `id` = ? AND `userId` = ?   ;
[2024-02-05 09:33:54.856323] : Dataloom[sqlite]: SELECT `id`, `name`, `username` FROM `users`   ;
[2024-02-05 09:33:54.892331] : Dataloom[sqlite]: SELECT `id`, `name`, `username` FROM `users` WHERE `id` = ?   ;
[2024-02-05 09:33:54.924378] : Dataloom[sqlite]: SELECT `id`, `name`, `username` FROM `users` WHERE `id` = ?   ;
[2024-02-05 09:33:54.956325] : Dataloom[sqlite]: SELECT `id`, `name`, `username` FROM `users` WHERE `id` = ? AND `name` = ?   ;
[2024-02-05 09:33:54.980332] : Dataloom[sqlite]: SELECT `id`, `name`, `username` FROM `users` WHERE `id` = ? AND `username` = ?   ;
[2024-02-05 09:33:55.001367] : Dataloom[sqlite]: SELECT `id`, `name`, `username` FROM `users` WHERE `name` = ? AND `username` = ?   ;
[2024-02-05 09:33:55.028917] : Dataloom[sqlite]: SELECT `id`, `completed` FROM `posts` WHERE `userId` = ?  LIMIT 3 OFFSET 3;
[2024-02-05 09:33:55.049994] : Dataloom[sqlite]: SELECT `completed`, `createdAt`, `id`, `title`, `updatedAt`, `userId` FROM `posts`   ;
[2024-02-05 09:33:55.079788] : Dataloom[sqlite]: DROP TABLE IF EXISTS posts;
[2024-02-05 09:33:55.109732] : Dataloom[sqlite]: CREATE TABLE IF NOT EXISTS `posts` (`completed` BOOLEAN DEFAULT False, `id` INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL, `title` VARCHAR NOT NULL, `createdAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP, `updatedAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP, `userId` INTEGER NOT NULL REFERENCES `users`(`id`) ON DELETE CASCADE ON UPDATE CASCADE);
[2024-02-05 09:33:55.133786] : Dataloom[sqlite]: DROP TABLE IF EXISTS users;
[2024-02-05 09:33:55.159790] : Dataloom[sqlite]: CREATE TABLE IF NOT EXISTS `users` (`id` INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL, `name` TEXT NOT NULL DEFAULT 'Bob', `username` VARCHAR UNIQUE, `createdAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP, `updatedAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP);
[2024-02-05 09:33:55.185780] : Dataloom[sqlite]: SELECT name FROM sqlite_master WHERE type='table';
[2024-02-05 09:33:55.211776] : Dataloom[sqlite]: INSERT INTO `users` (`username`) VALUES (?);
[2024-02-05 09:33:55.238789] : Dataloom[sqlite]: INSERT INTO `posts` (`title`, `userId`) VALUES (?, ?);
[2024-02-05 09:33:55.326121] : Dataloom[sqlite]: UPDATE `users` SET `updatedAt` = ? WHERE `id` = ?;
[2024-02-05 09:33:55.362202] : Dataloom[sqlite]: UPDATE `users` SET `updatedAt` = ? WHERE `id` = ?;
[2024-02-05 09:33:55.390150] : Dataloom[sqlite]: SELECT `createdAt`, `id`, `name`, `updatedAt`, `username` FROM `users` WHERE `id` = ?;
[2024-02-05 09:33:55.438202] : Dataloom[sqlite]: DROP TABLE IF EXISTS posts;
[2024-02-05 09:33:55.478150] : Dataloom[sqlite]: CREATE TABLE IF NOT EXISTS `posts` (`completed` BOOLEAN DEFAULT False, `id` INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL, `title` VARCHAR NOT NULL, `createdAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP, `userId` INTEGER NOT NULL REFERENCES `users`(`id`) ON DELETE CASCADE ON UPDATE CASCADE);
[2024-02-05 09:33:55.510959] : Dataloom[sqlite]: DROP TABLE IF EXISTS users;
[2024-02-05 09:33:55.545962] : Dataloom[sqlite]: CREATE TABLE IF NOT EXISTS `users` (`id` INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL, `name` TEXT NOT NULL DEFAULT 'Bob', `username` VARCHAR UNIQUE, `createdAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP, `updatedAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP);
[2024-02-05 09:33:55.581963] : Dataloom[sqlite]: SELECT name FROM sqlite_master WHERE type='table';
[2024-02-05 09:33:55.611061] : Dataloom[sqlite]: INSERT INTO `users` (`username`) VALUES (?);
[2024-02-05 09:33:55.657963] : Dataloom[sqlite]: INSERT INTO `posts` (`title`, `userId`) VALUES (?, ?);
[2024-02-05 09:33:55.737063] : Dataloom[sqlite]: 
        UPDATE `posts` SET `title` = ? WHERE `id` = (
            SELECT `id` FROM  `posts` WHERE `userId` = ? LIMIT 1
        );
        
[2024-02-05 09:33:55.761915] : Dataloom[sqlite]: 
        UPDATE `posts` SET `title` = ? WHERE `id` = (
            SELECT `id` FROM  `posts` WHERE `userId` = ? LIMIT 1
        );
        
[2024-02-05 09:33:55.779921] : Dataloom[sqlite]: SELECT `completed`, `createdAt`, `id`, `title`, `userId` FROM `posts` WHERE `id` = ?;
[2024-02-05 09:33:55.812541] : Dataloom[sqlite]: DROP TABLE IF EXISTS posts;
[2024-02-05 09:33:55.848533] : Dataloom[sqlite]: CREATE TABLE IF NOT EXISTS `posts` (`completed` BOOLEAN DEFAULT False, `id` INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL, `title` VARCHAR NOT NULL, `createdAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP, `userId` INTEGER NOT NULL REFERENCES `users`(`id`) ON DELETE CASCADE ON UPDATE CASCADE);
[2024-02-05 09:33:55.868535] : Dataloom[sqlite]: DROP TABLE IF EXISTS users;
[2024-02-05 09:33:55.889537] : Dataloom[sqlite]: CREATE TABLE IF NOT EXISTS `users` (`id` INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL, `name` TEXT NOT NULL DEFAULT 'Bob', `username` VARCHAR UNIQUE, `createdAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP, `updatedAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP);
[2024-02-05 09:33:55.908535] : Dataloom[sqlite]: SELECT name FROM sqlite_master WHERE type='table';
[2024-02-05 09:33:55.926538] : Dataloom[sqlite]: INSERT INTO `users` (`username`) VALUES (?);
[2024-02-05 09:33:56.067540] : Dataloom[sqlite]: INSERT INTO `posts` (`title`, `userId`) VALUES (?, ?);
[2024-02-05 09:33:56.199538] : Dataloom[sqlite]: UPDATE `posts` SET `title` = ? WHERE `userId` = ?;
[2024-02-05 09:33:56.295539] : Dataloom[sqlite]: UPDATE `posts` SET `title` = ? WHERE `userId` = ?;
[2024-02-05 09:33:56.393411] : Dataloom[sqlite]: SELECT `completed`, `createdAt`, `id`, `title`, `userId` FROM `posts` WHERE `id` = ?;
[2024-02-05 09:34:11.073904] : Dataloom[mysql]: DROP TABLE IF EXISTS `users`;
[2024-02-05 09:34:11.158907] : Dataloom[mysql]: DROP TABLE IF EXISTS `users`;
[2024-02-05 09:34:11.233241] : Dataloom[mysql]: DROP TABLE IF EXISTS `users`;
[2024-02-05 09:34:11.263241] : Dataloom[mysql]: CREATE TABLE IF NOT EXISTS `users` (`id` INT PRIMARY KEY AUTO_INCREMENT UNIQUE NOT NULL, `name` VARCHAR(255), `username` TEXT NOT NULL);
[2024-02-05 09:34:11.326237] : Dataloom[mysql]: DROP TABLE IF EXISTS `posts`;
[2024-02-05 09:34:11.386406] : Dataloom[mysql]: CREATE TABLE IF NOT EXISTS `posts` (`id` INT PRIMARY KEY AUTO_INCREMENT UNIQUE NOT NULL, `title` TEXT NOT NULL);
[2024-02-05 09:34:11.543402] : Dataloom[mysql]: SHOW TABLES;
[2024-02-05 09:34:11.623998] : Dataloom[mysql]: DROP TABLE IF EXISTS `users`;
[2024-02-05 09:34:11.756563] : Dataloom[mysql]: CREATE TABLE IF NOT EXISTS `users` (`id` INT PRIMARY KEY AUTO_INCREMENT UNIQUE NOT NULL, `name` VARCHAR(255) UNIQUE, `username` VARCHAR(255) NOT NULL DEFAULT 'Hello there!!');
[2024-02-05 09:34:11.910490] : Dataloom[mysql]: DROP TABLE IF EXISTS `posts`;
[2024-02-05 09:34:12.064693] : Dataloom[mysql]: CREATE TABLE IF NOT EXISTS `posts` (`completed` BOOLEAN DEFAULT False, `id` INT PRIMARY KEY AUTO_INCREMENT UNIQUE NOT NULL, `title` VARCHAR(255) NOT NULL);
[2024-02-05 09:34:12.221674] : Dataloom[mysql]: SHOW TABLES;
[2024-02-05 09:34:12.299651] : Dataloom[mysql]: DROP TABLE IF EXISTS `posts`;
[2024-02-05 09:34:12.408069] : Dataloom[mysql]: CREATE TABLE IF NOT EXISTS `posts` (`completed` BOOLEAN DEFAULT False, `id` INT PRIMARY KEY AUTO_INCREMENT UNIQUE NOT NULL, `title` VARCHAR(255) NOT NULL, `createdAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP, `updatedAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP, `userId` INT NOT NULL REFERENCES `users`(`id`) ON DELETE CASCADE ON UPDATE CASCADE);
[2024-02-05 09:34:12.521578] : Dataloom[mysql]: DROP TABLE IF EXISTS `users`;
[2024-02-05 09:34:12.584249] : Dataloom[mysql]: CREATE TABLE IF NOT EXISTS `users` (`id` INT PRIMARY KEY AUTO_INCREMENT UNIQUE NOT NULL, `name` VARCHAR(255) NOT NULL DEFAULT 'Bob', `username` VARCHAR(255) UNIQUE, `createdAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP, `updatedAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP);
[2024-02-05 09:34:12.707775] : Dataloom[mysql]: SHOW TABLES;
[2024-02-05 09:34:12.727812] : Dataloom[mysql]: INSERT INTO `users` (`name`, `username`) VALUES (%s, %s);
[2024-02-05 09:34:12.755774] : Dataloom[mysql]: DELETE FROM `users` WHERE `id` = %s;
[2024-02-05 09:34:12.778770] : Dataloom[mysql]: DELETE FROM `users` WHERE `id` = %s;
[2024-02-05 09:34:12.815902] : Dataloom[mysql]: DROP TABLE IF EXISTS `posts`;
[2024-02-05 09:34:12.880821] : Dataloom[mysql]: CREATE TABLE IF NOT EXISTS `posts` (`completed` BOOLEAN DEFAULT False, `id` INT PRIMARY KEY AUTO_INCREMENT UNIQUE NOT NULL, `title` VARCHAR(255) NOT NULL, `createdAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP, `updatedAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP, `userId` INT NOT NULL REFERENCES `users`(`id`) ON DELETE CASCADE ON UPDATE CASCADE);
[2024-02-05 09:34:12.947243] : Dataloom[mysql]: DROP TABLE IF EXISTS `users`;
[2024-02-05 09:34:13.051136] : Dataloom[mysql]: CREATE TABLE IF NOT EXISTS `users` (`id` INT PRIMARY KEY AUTO_INCREMENT UNIQUE NOT NULL, `name` VARCHAR(255) NOT NULL DEFAULT 'Bob', `username` VARCHAR(255) UNIQUE, `createdAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP, `updatedAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP);
[2024-02-05 09:34:13.110133] : Dataloom[mysql]: SHOW TABLES;
[2024-02-05 09:34:13.132702] : Dataloom[mysql]: INSERT INTO `users` (`name`, `username`) VALUES (%s, %s);
[2024-02-05 09:34:13.161869] : Dataloom[mysql]: 
    DELETE FROM `users` WHERE `id` IN (
       SELECT `id` FROM  (
                SELECT `id` FROM `users` WHERE `name` = %s LIMIT 1
        ) AS subquery
    );
    
[2024-02-05 09:34:13.191697] : Dataloom[mysql]: SELECT `createdAt`, `id`, `name`, `updatedAt`, `username` FROM `users` WHERE `name` = %s   ;
[2024-02-05 09:34:13.213704] : Dataloom[mysql]: 
    DELETE FROM `users` WHERE `id` IN (
       SELECT `id` FROM  (
                SELECT `id` FROM `users` WHERE `name` = %s AND `id` = %s LIMIT 1
        ) AS subquery
    );
    
[2024-02-05 09:34:13.236004] : Dataloom[mysql]: SELECT `createdAt`, `id`, `name`, `updatedAt`, `username` FROM `users` WHERE `name` = %s   ;
[2024-02-05 09:34:13.258934] : Dataloom[mysql]: 
    DELETE FROM `users` WHERE `id` IN (
       SELECT `id` FROM  (
                SELECT `id` FROM `users` WHERE `name` = %s AND `id` = %s LIMIT 1
        ) AS subquery
    );
    
[2024-02-05 09:34:13.282747] : Dataloom[mysql]: SELECT `createdAt`, `id`, `name`, `updatedAt`, `username` FROM `users` WHERE `name` = %s   ;
[2024-02-05 09:34:13.282747] : Dataloom[postgres]: DROP TABLE IF EXISTS "posts" CASCADE;
[2024-02-05 09:34:13.326558] : Dataloom[postgres]: CREATE TABLE IF NOT EXISTS "posts" ("completed" BOOLEAN DEFAULT False, "id" BIGSERIAL PRIMARY KEY UNIQUE NOT NULL, "title" VARCHAR(255) NOT NULL, "createdAt" TIMESTAMP DEFAULT CURRENT_TIMESTAMP, "updatedAt" TIMESTAMP DEFAULT CURRENT_TIMESTAMP, "userId" BIGSERIAL NOT NULL REFERENCES "users"("id") ON DELETE CASCADE ON UPDATE CASCADE);
[2024-02-05 09:34:13.380507] : Dataloom[postgres]: DROP TABLE IF EXISTS "users" CASCADE;
[2024-02-05 09:34:13.380507] : Dataloom[mysql]: CREATE TABLE IF NOT EXISTS `posts` (`completed` BOOLEAN DEFAULT False, `id` INT PRIMARY KEY AUTO_INCREMENT UNIQUE NOT NULL, `title` VARCHAR(255) NOT NULL, `createdAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP, `updatedAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP, `userId` INT NOT NULL REFERENCES `users`(`id`) ON DELETE CASCADE ON UPDATE CASCADE);
[2024-02-05 09:34:13.423557] : Dataloom[postgres]: CREATE TABLE IF NOT EXISTS "users" ("id" BIGSERIAL PRIMARY KEY UNIQUE NOT NULL, "name" TEXT NOT NULL DEFAULT 'Bob', "username" VARCHAR(255) UNIQUE);
[2024-02-05 09:34:13.459574] : Dataloom[mysql]: DROP TABLE IF EXISTS `users`;
alog.pg_tables WHERE schemaname='public';
[2024-02-05 09:34:13.503946] : Dataloom[postgres]: INSERT INTO "users" ("username") VALUES (%s) RETURNING "id";
REMENT UNIQUE NOT NULL, `name` VARCHAR(255) NOT NULL DEFAULT 'Bob', `username` VARCHAR(255) UNIQUE, `createdAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP, `updatedAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP);
[2024-02-05 09:34:13.536570] : Dataloom[postgres]: INSERT INTO "posts" ("title", "userId") VALUES (%s, %s) RETURNING *;
[2024-02-05 09:34:13.573644] : Dataloom[postgres]: 
        SELECT 
            parent.id AS "posts_id", parent.completed AS "posts_completed",
            child_user.id AS "users_id"
        FROM 
            posts parent
        JOIN users child_user ON parent."userId" = child_user.id 
        WHERE 
            parent."id" = %s;
    
[2024-02-05 09:34:13.616595] : Dataloom[mysql]: SHOW TABLES;
[2024-02-05 09:34:13.648110] : Dataloom[mysql]: INSERT INTO `users` (`name`, `username`) VALUES (%s, %s);
[2024-02-05 09:34:13.677110] : Dataloom[mysql]: DELETE FROM `users` WHERE `name` = %s;
[2024-02-05 09:34:13.698175] : Dataloom[mysql]: SELECT `createdAt`, `id`, `name`, `updatedAt`, `username` FROM `users` WHERE `name` = %s   ;
[2024-02-05 09:34:13.719111] : Dataloom[mysql]: INSERT INTO `users` (`name`, `username`) VALUES (%s, %s);
[2024-02-05 09:34:13.737156] : Dataloom[mysql]: DELETE FROM `users` WHERE `name` = %s AND `id` = %s;
[2024-02-05 09:34:13.756159] : Dataloom[mysql]: SELECT `createdAt`, `id`, `name`, `updatedAt`, `username` FROM `users` WHERE `name` = %s   ;
[2024-02-05 09:34:13.781321] : Dataloom[mysql]: DELETE FROM `users` WHERE `name` = %s AND `id` = %s;
[2024-02-05 09:34:13.817169] : Dataloom[mysql]: SELECT `createdAt`, `id`, `name`, `updatedAt`, `username` FROM `users` WHERE `name` = %s   ;
[2024-02-05 09:34:13.898163] : Dataloom[mysql]: DROP TABLE IF EXISTS `posts`;
[2024-02-05 09:34:13.988514] : Dataloom[mysql]: CREATE TABLE IF NOT EXISTS `posts` (`completed` BOOLEAN DEFAULT False, `id` INT PRIMARY KEY AUTO_INCREMENT UNIQUE NOT NULL, `title` VARCHAR(255) NOT NULL, `createdAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP, `updatedAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP, `userId` INT NOT NULL REFERENCES `users`(`id`) ON DELETE CASCADE ON UPDATE CASCADE);
[2024-02-05 09:34:14.071513] : Dataloom[mysql]: DROP TABLE IF EXISTS `users`;
[2024-02-05 09:34:14.126513] : Dataloom[mysql]: CREATE TABLE IF NOT EXISTS `users` (`id` INT PRIMARY KEY AUTO_INCREMENT UNIQUE NOT NULL, `name` VARCHAR(255) NOT NULL DEFAULT 'Bob', `username` VARCHAR(255) UNIQUE, `createdAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP, `updatedAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP);
[2024-02-05 09:34:14.232580] : Dataloom[mysql]: SHOW TABLES;
[2024-02-05 09:34:14.273142] : Dataloom[mysql]: INSERT INTO `users` (`username`) VALUES (%s);
[2024-02-05 09:34:14.316540] : Dataloom[mysql]: INSERT INTO `posts` (`title`, `userId`) VALUES (%s, %s);
[2024-02-05 09:34:14.396263] : Dataloom[mysql]: DROP TABLE IF EXISTS `posts`;
[2024-02-05 09:34:14.531397] : Dataloom[mysql]: CREATE TABLE IF NOT EXISTS `posts` (`completed` BOOLEAN DEFAULT False, `id` INT PRIMARY KEY AUTO_INCREMENT UNIQUE NOT NULL, `title` VARCHAR(255) NOT NULL, `createdAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP, `updatedAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP, `userId` INT NOT NULL REFERENCES `users`(`id`) ON DELETE CASCADE ON UPDATE CASCADE);
[2024-02-05 09:34:14.652517] : Dataloom[mysql]: DROP TABLE IF EXISTS `users`;
[2024-02-05 09:34:14.739055] : Dataloom[mysql]: CREATE TABLE IF NOT EXISTS `users` (`id` INT PRIMARY KEY AUTO_INCREMENT UNIQUE NOT NULL, `name` VARCHAR(255) NOT NULL DEFAULT 'Bob', `username` VARCHAR(255) UNIQUE, `createdAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP, `updatedAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP);
[2024-02-05 09:34:14.824880] : Dataloom[mysql]: SHOW TABLES;
[2024-02-05 09:34:14.842926] : Dataloom[mysql]: INSERT INTO `users` (`username`) VALUES (%s);
[2024-02-05 09:34:14.864169] : Dataloom[mysql]: INSERT INTO `posts` (`title`, `userId`) VALUES (%s, %s);
[2024-02-05 09:34:14.898921] : Dataloom[mysql]: DROP TABLE IF EXISTS `posts`;
[2024-02-05 09:34:14.968541] : Dataloom[mysql]: CREATE TABLE IF NOT EXISTS `posts` (`completed` BOOLEAN DEFAULT False, `id` INT PRIMARY KEY AUTO_INCREMENT UNIQUE NOT NULL, `title` VARCHAR(255) NOT NULL, `createdAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP, `updatedAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP, `userId` INT NOT NULL REFERENCES `users`(`id`) ON DELETE CASCADE ON UPDATE CASCADE);
[2024-02-05 09:34:15.037540] : Dataloom[mysql]: DROP TABLE IF EXISTS `users`;
[2024-02-05 09:34:15.100371] : Dataloom[mysql]: CREATE TABLE IF NOT EXISTS `users` (`id` INT PRIMARY KEY AUTO_INCREMENT UNIQUE NOT NULL, `name` VARCHAR(255) NOT NULL DEFAULT 'Bob', `username` VARCHAR(255) UNIQUE);
[2024-02-05 09:34:15.183566] : Dataloom[mysql]: SHOW TABLES;
[2024-02-05 09:34:15.207565] : Dataloom[mysql]: INSERT INTO `users` (`username`) VALUES (%s);
[2024-02-05 09:34:15.232562] : Dataloom[mysql]: INSERT INTO `posts` (`title`, `userId`) VALUES (%s, %s);
[2024-02-05 09:34:15.253196] : Dataloom[mysql]: SELECT `id`, `name`, `username` FROM `users` WHERE `id` = %s;
[2024-02-05 09:34:15.272191] : Dataloom[mysql]: SELECT `id`, `name`, `username` FROM `users` WHERE `id` = %s;
[2024-02-05 09:34:15.289195] : Dataloom[mysql]: SELECT `id`, `completed` FROM `posts` WHERE `id` = %s;
[2024-02-05 09:34:15.326191] : Dataloom[mysql]: DROP TABLE IF EXISTS `posts`;
[2024-02-05 09:34:15.403792] : Dataloom[mysql]: CREATE TABLE IF NOT EXISTS `posts` (`completed` BOOLEAN DEFAULT False, `id` INT PRIMARY KEY AUTO_INCREMENT UNIQUE NOT NULL, `title` VARCHAR(255) NOT NULL, `createdAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP, `updatedAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP, `userId` INT NOT NULL REFERENCES `users`(`id`) ON DELETE CASCADE ON UPDATE CASCADE);
[2024-02-05 09:34:15.475170] : Dataloom[mysql]: DROP TABLE IF EXISTS `users`;
[2024-02-05 09:34:15.559574] : Dataloom[mysql]: CREATE TABLE IF NOT EXISTS `users` (`id` INT PRIMARY KEY AUTO_INCREMENT UNIQUE NOT NULL, `name` VARCHAR(255) NOT NULL DEFAULT 'Bob', `username` VARCHAR(255) UNIQUE);
[2024-02-05 09:34:15.678824] : Dataloom[mysql]: SHOW TABLES;
[2024-02-05 09:34:15.705836] : Dataloom[mysql]: INSERT INTO `users` (`username`) VALUES (%s);
[2024-02-05 09:34:15.736033] : Dataloom[mysql]: INSERT INTO `posts` (`title`, `userId`) VALUES (%s, %s);
[2024-02-05 09:34:15.757832] : Dataloom[mysql]: SELECT `id`, `name`, `username` FROM `users`   ;
[2024-02-05 09:34:15.775848] : Dataloom[mysql]: SELECT `completed`, `createdAt`, `id`, `title`, `updatedAt`, `userId` FROM `posts`   ;
[2024-02-05 09:34:15.792812] : Dataloom[mysql]: SELECT `id`, `completed` FROM `posts`  LIMIT 3 OFFSET 3;
[2024-02-05 09:34:15.823814] : Dataloom[mysql]: DROP TABLE IF EXISTS `posts`;
[2024-02-05 09:34:15.866812] : Dataloom[mysql]: CREATE TABLE IF NOT EXISTS `posts` (`completed` BOOLEAN DEFAULT False, `id` INT PRIMARY KEY AUTO_INCREMENT UNIQUE NOT NULL, `title` VARCHAR(255) NOT NULL, `createdAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP, `updatedAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP, `userId` INT NOT NULL REFERENCES `users`(`id`) ON DELETE CASCADE ON UPDATE CASCADE);
[2024-02-05 09:34:15.912618] : Dataloom[mysql]: DROP TABLE IF EXISTS `users`;
[2024-02-05 09:34:15.982352] : Dataloom[mysql]: CREATE TABLE IF NOT EXISTS `users` (`id` INT PRIMARY KEY AUTO_INCREMENT UNIQUE NOT NULL, `name` VARCHAR(255) NOT NULL DEFAULT 'Bob', `username` VARCHAR(255) UNIQUE);
[2024-02-05 09:34:16.021953] : Dataloom[mysql]: SHOW TABLES;
[2024-02-05 09:34:16.038972] : Dataloom[mysql]: INSERT INTO `users` (`username`) VALUES (%s);
[2024-02-05 09:34:16.059722] : Dataloom[mysql]: INSERT INTO `posts` (`title`, `userId`) VALUES (%s, %s);
[2024-02-05 09:34:16.081350] : Dataloom[mysql]: SELECT `id`, `name`, `username` FROM `users` WHERE `id` = %s   ;
[2024-02-05 09:34:16.099353] : Dataloom[mysql]: SELECT `id`, `name`, `username` FROM `users` WHERE `id` = %s   ;
[2024-02-05 09:34:16.117087] : Dataloom[mysql]: SELECT `id`, `name`, `username` FROM `users` WHERE `id` = %s AND `name` = %s   ;
[2024-02-05 09:34:16.132359] : Dataloom[mysql]: SELECT `id`, `name`, `username` FROM `users` WHERE `id` = %s AND `username` = %s   ;
[2024-02-05 09:34:16.148354] : Dataloom[mysql]: SELECT `id`, `name`, `username` FROM `users` WHERE `name` = %s AND `username` = %s   ;
[2024-02-05 09:34:16.163957] : Dataloom[mysql]: SELECT `id`, `completed` FROM `posts`   ;
[2024-02-05 09:34:16.194986] : Dataloom[mysql]: DROP TABLE IF EXISTS `posts`;
[2024-02-05 09:34:16.241959] : Dataloom[mysql]: CREATE TABLE IF NOT EXISTS `posts` (`completed` BOOLEAN DEFAULT False, `id` INT PRIMARY KEY AUTO_INCREMENT UNIQUE NOT NULL, `title` VARCHAR(255) NOT NULL, `createdAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP, `updatedAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP, `userId` INT NOT NULL REFERENCES `users`(`id`) ON DELETE CASCADE ON UPDATE CASCADE);
[2024-02-05 09:34:16.317964] : Dataloom[mysql]: DROP TABLE IF EXISTS `users`;
[2024-02-05 09:34:16.359080] : Dataloom[mysql]: CREATE TABLE IF NOT EXISTS `users` (`id` INT PRIMARY KEY AUTO_INCREMENT UNIQUE NOT NULL, `name` VARCHAR(255) NOT NULL DEFAULT 'Bob', `username` VARCHAR(255) UNIQUE);
[2024-02-05 09:34:16.456170] : Dataloom[mysql]: SHOW TABLES;
[2024-02-05 09:34:16.478603] : Dataloom[mysql]: INSERT INTO `users` (`username`) VALUES (%s);
[2024-02-05 09:34:16.503688] : Dataloom[mysql]: INSERT INTO `posts` (`title`, `userId`) VALUES (%s, %s);
[2024-02-05 09:34:16.527677] : Dataloom[mysql]: SELECT `completed`, `createdAt`, `id`, `title`, `updatedAt`, `userId` FROM `posts` WHERE `id` = %s AND `userId` = %s   ;
[2024-02-05 09:34:16.549626] : Dataloom[mysql]: SELECT `id`, `name`, `username` FROM `users`   ;
[2024-02-05 09:34:16.571223] : Dataloom[mysql]: SELECT `id`, `name`, `username` FROM `users` WHERE `id` = %s   ;
[2024-02-05 09:34:16.593266] : Dataloom[mysql]: SELECT `id`, `name`, `username` FROM `users` WHERE `id` = %s   ;
[2024-02-05 09:34:16.616227] : Dataloom[mysql]: SELECT `id`, `name`, `username` FROM `users` WHERE `id` = %s AND `name` = %s   ;
[2024-02-05 09:34:16.637370] : Dataloom[mysql]: SELECT `id`, `name`, `username` FROM `users` WHERE `id` = %s AND `username` = %s   ;
[2024-02-05 09:34:16.658677] : Dataloom[mysql]: SELECT `id`, `name`, `username` FROM `users` WHERE `name` = %s AND `username` = %s   ;
[2024-02-05 09:34:16.680025] : Dataloom[mysql]: SELECT `id`, `completed` FROM `posts` WHERE `userId` = %s  LIMIT 3 OFFSET 3;
[2024-02-05 09:34:16.704217] : Dataloom[mysql]: SELECT `completed`, `createdAt`, `id`, `title`, `updatedAt`, `userId` FROM `posts`   ;
[2024-02-05 09:34:16.751050] : Dataloom[mysql]: DROP TABLE IF EXISTS `posts`;
[2024-02-05 09:34:16.826919] : Dataloom[mysql]: CREATE TABLE IF NOT EXISTS `posts` (`completed` BOOLEAN DEFAULT False, `id` INT PRIMARY KEY AUTO_INCREMENT UNIQUE NOT NULL, `title` VARCHAR(255) NOT NULL, `createdAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP, `updatedAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP, `userId` INT NOT NULL REFERENCES `users`(`id`) ON DELETE CASCADE ON UPDATE CASCADE);
[2024-02-05 09:34:16.887626] : Dataloom[mysql]: DROP TABLE IF EXISTS `users`;
[2024-02-05 09:34:16.978660] : Dataloom[mysql]: CREATE TABLE IF NOT EXISTS `users` (`id` INT PRIMARY KEY AUTO_INCREMENT UNIQUE NOT NULL, `name` VARCHAR(255) NOT NULL DEFAULT 'Bob', `username` VARCHAR(255) UNIQUE, `createdAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP, `updatedAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP);
[2024-02-05 09:34:17.044463] : Dataloom[mysql]: SHOW TABLES;
[2024-02-05 09:34:17.068293] : Dataloom[mysql]: INSERT INTO `users` (`username`) VALUES (%s);
[2024-02-05 09:34:17.094484] : Dataloom[mysql]: INSERT INTO `posts` (`title`, `userId`) VALUES (%s, %s);
[2024-02-05 09:34:17.188136] : Dataloom[mysql]: UPDATE `users` SET `updatedAt` = %s WHERE `id` = %s;
[2024-02-05 09:34:17.225146] : Dataloom[mysql]: UPDATE `users` SET `updatedAt` = %s WHERE `id` = %s;
[2024-02-05 09:34:17.262151] : Dataloom[mysql]: SELECT `createdAt`, `id`, `name`, `updatedAt`, `username` FROM `users` WHERE `id` = %s;
[2024-02-05 09:34:17.299196] : Dataloom[mysql]: UPDATE `users` SET `id` = %s, `updatedAt` = %s WHERE `id` = %s;
[2024-02-05 09:34:17.374861] : Dataloom[mysql]: DROP TABLE IF EXISTS `posts`;
[2024-02-05 09:34:17.465851] : Dataloom[mysql]: CREATE TABLE IF NOT EXISTS `posts` (`completed` BOOLEAN DEFAULT False, `id` INT PRIMARY KEY AUTO_INCREMENT UNIQUE NOT NULL, `title` VARCHAR(255) NOT NULL, `createdAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP, `userId` INT NOT NULL REFERENCES `users`(`id`) ON DELETE CASCADE ON UPDATE CASCADE);
[2024-02-05 09:34:17.554125] : Dataloom[mysql]: DROP TABLE IF EXISTS `users`;
[2024-02-05 09:34:17.629707] : Dataloom[mysql]: CREATE TABLE IF NOT EXISTS `users` (`id` INT PRIMARY KEY AUTO_INCREMENT UNIQUE NOT NULL, `name` VARCHAR(255) NOT NULL DEFAULT 'Bob', `username` VARCHAR(255) UNIQUE, `createdAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP, `updatedAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP);
[2024-02-05 09:34:17.751038] : Dataloom[mysql]: SHOW TABLES;
[2024-02-05 09:34:17.783087] : Dataloom[mysql]: INSERT INTO `users` (`username`) VALUES (%s);
[2024-02-05 09:34:17.818020] : Dataloom[mysql]: INSERT INTO `posts` (`title`, `userId`) VALUES (%s, %s);
[2024-02-05 09:34:17.904499] : Dataloom[mysql]: 
        UPDATE `posts` SET `title` = %s WHERE `id` IN (
            SELECT `id` FROM  (
                SELECT `id` FROM `posts` WHERE `userId` = %s LIMIT 1
            ) AS subquery
        );
        
[2024-02-05 09:34:17.939626] : Dataloom[mysql]: 
        UPDATE `posts` SET `title` = %s WHERE `id` IN (
            SELECT `id` FROM  (
                SELECT `id` FROM `posts` WHERE `userId` = %s LIMIT 1
            ) AS subquery
        );
        
[2024-02-05 09:34:17.970465] : Dataloom[mysql]: SELECT `completed`, `createdAt`, `id`, `title`, `userId` FROM `posts` WHERE `id` = %s;
[2024-02-05 09:34:18.002496] : Dataloom[mysql]: 
        UPDATE `posts` SET `userId` = %s WHERE `id` IN (
            SELECT `id` FROM  (
                SELECT `id` FROM `posts` WHERE `userId` = %s LIMIT 1
            ) AS subquery
        );
        
[2024-02-05 09:34:18.063463] : Dataloom[mysql]: DROP TABLE IF EXISTS `posts`;
[2024-02-05 09:34:18.142080] : Dataloom[mysql]: CREATE TABLE IF NOT EXISTS `posts` (`completed` BOOLEAN DEFAULT False, `id` INT PRIMARY KEY AUTO_INCREMENT UNIQUE NOT NULL, `title` VARCHAR(255) NOT NULL, `createdAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP, `userId` INT NOT NULL REFERENCES `users`(`id`) ON DELETE CASCADE ON UPDATE CASCADE);
[2024-02-05 09:34:18.236595] : Dataloom[mysql]: DROP TABLE IF EXISTS `users`;
[2024-02-05 09:34:18.342247] : Dataloom[mysql]: CREATE TABLE IF NOT EXISTS `users` (`id` INT PRIMARY KEY AUTO_INCREMENT UNIQUE NOT NULL, `name` VARCHAR(255) NOT NULL DEFAULT 'Bob', `username` VARCHAR(255) UNIQUE, `createdAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP, `updatedAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP);
[2024-02-05 09:34:18.453276] : Dataloom[mysql]: SHOW TABLES;
[2024-02-05 09:34:18.483230] : Dataloom[mysql]: INSERT INTO `users` (`username`) VALUES (%s);
[2024-02-05 09:34:18.518230] : Dataloom[mysql]: INSERT INTO `posts` (`title`, `userId`) VALUES (%s, %s);
[2024-02-05 09:34:18.601944] : Dataloom[mysql]: UPDATE `posts` SET `title` = %s WHERE `userId` = %s;
[2024-02-05 09:34:18.632892] : Dataloom[mysql]: UPDATE `posts` SET `title` = %s WHERE `userId` = %s;
[2024-02-05 09:34:18.659701] : Dataloom[mysql]: SELECT `completed`, `createdAt`, `id`, `title`, `userId` FROM `posts` WHERE `id` = %s;
[2024-02-05 09:34:18.690562] : Dataloom[mysql]: UPDATE `posts` SET `userId` = %s WHERE `userId` = %s;
[2024-02-05 09:34:19.486961] : Dataloom[postgres]: DROP TABLE IF EXISTS "users" CASCADE;
[2024-02-05 09:34:19.609770] : Dataloom[postgres]: DROP TABLE IF EXISTS "users" CASCADE;
[2024-02-05 09:34:20.016385] : Dataloom[postgres]: DROP TABLE IF EXISTS "users" CASCADE;
[2024-02-05 09:34:20.046547] : Dataloom[postgres]: CREATE TABLE IF NOT EXISTS "users" ("id" BIGSERIAL PRIMARY KEY UNIQUE NOT NULL, "name" VARCHAR(255), "username" TEXT NOT NULL);
[2024-02-05 09:34:20.110572] : Dataloom[postgres]: DROP TABLE IF EXISTS "posts" CASCADE;
[2024-02-05 09:34:20.155030] : Dataloom[postgres]: CREATE TABLE IF NOT EXISTS "posts" ("id" BIGSERIAL PRIMARY KEY UNIQUE NOT NULL, "title" TEXT NOT NULL DEFAULT 'Hello there!!');
[2024-02-05 09:34:20.200909] : Dataloom[postgres]: SELECT tablename FROM pg_catalog.pg_tables WHERE schemaname='public';
[2024-02-05 09:34:20.433289] : Dataloom[postgres]: DROP TABLE IF EXISTS "users" CASCADE;
[2024-02-05 09:34:20.480607] : Dataloom[postgres]: CREATE TABLE IF NOT EXISTS "users" ("id" BIGSERIAL PRIMARY KEY UNIQUE NOT NULL, "name" VARCHAR(255) UNIQUE, "username" TEXT NOT NULL DEFAULT 'Hello there!!');
[2024-02-05 09:34:20.547345] : Dataloom[postgres]: DROP TABLE IF EXISTS "posts" CASCADE;
[2024-02-05 09:34:20.587346] : Dataloom[postgres]: CREATE TABLE IF NOT EXISTS "posts" ("completed" BOOLEAN DEFAULT False, "id" BIGSERIAL PRIMARY KEY UNIQUE NOT NULL, "title" VARCHAR(255) NOT NULL);
[2024-02-05 09:34:20.625702] : Dataloom[postgres]: SELECT tablename FROM pg_catalog.pg_tables WHERE schemaname='public';
[2024-02-05 09:34:20.846769] : Dataloom[postgres]: DROP TABLE IF EXISTS "posts" CASCADE;
[2024-02-05 09:34:20.888768] : Dataloom[postgres]: CREATE TABLE IF NOT EXISTS "posts" ("completed" BOOLEAN DEFAULT False, "id" BIGSERIAL PRIMARY KEY UNIQUE NOT NULL, "title" VARCHAR(255) NOT NULL, "createdAt" TIMESTAMP DEFAULT CURRENT_TIMESTAMP, "updatedAt" TIMESTAMP DEFAULT CURRENT_TIMESTAMP, "userId" BIGSERIAL NOT NULL REFERENCES "users"("id") ON DELETE CASCADE ON UPDATE CASCADE);
[2024-02-05 09:34:20.948752] : Dataloom[postgres]: DROP TABLE IF EXISTS "users" CASCADE;
[2024-02-05 09:34:20.996762] : Dataloom[postgres]: CREATE TABLE IF NOT EXISTS "users" ("id" BIGSERIAL PRIMARY KEY UNIQUE NOT NULL, "name" TEXT NOT NULL DEFAULT 'Bob', "username" VARCHAR(255) UNIQUE, "createdAt" TIMESTAMP DEFAULT CURRENT_TIMESTAMP, "updatedAt" TIMESTAMP DEFAULT CURRENT_TIMESTAMP);
[2024-02-05 09:34:21.058547] : Dataloom[postgres]: SELECT tablename FROM pg_catalog.pg_tables WHERE schemaname='public';
[2024-02-05 09:34:21.113180] : Dataloom[postgres]: INSERT INTO "users" ("name", "username") VALUES (%s, %s) RETURNING "id";
[2024-02-05 09:34:21.149384] : Dataloom[postgres]: DELETE FROM "users" WHERE "id" = %s;
[2024-02-05 09:34:21.178416] : Dataloom[postgres]: DELETE FROM "users" WHERE "id" = %s;
[2024-02-05 09:34:21.384886] : Dataloom[postgres]: DROP TABLE IF EXISTS "posts" CASCADE;
[2024-02-05 09:34:21.435560] : Dataloom[postgres]: CREATE TABLE IF NOT EXISTS "posts" ("completed" BOOLEAN DEFAULT False, "id" BIGSERIAL PRIMARY KEY UNIQUE NOT NULL, "title" VARCHAR(255) NOT NULL, "createdAt" TIMESTAMP DEFAULT CURRENT_TIMESTAMP, "updatedAt" TIMESTAMP DEFAULT CURRENT_TIMESTAMP, "userId" BIGSERIAL NOT NULL REFERENCES "users"("id") ON DELETE CASCADE ON UPDATE CASCADE);
[2024-02-05 09:34:21.496009] : Dataloom[postgres]: DROP TABLE IF EXISTS "users" CASCADE;
[2024-02-05 09:34:21.545073] : Dataloom[postgres]: CREATE TABLE IF NOT EXISTS "users" ("id" BIGSERIAL PRIMARY KEY UNIQUE NOT NULL, "name" TEXT NOT NULL DEFAULT 'Bob', "username" VARCHAR(255) UNIQUE, "createdAt" TIMESTAMP DEFAULT CURRENT_TIMESTAMP, "updatedAt" TIMESTAMP DEFAULT CURRENT_TIMESTAMP);
[2024-02-05 09:34:21.594951] : Dataloom[postgres]: SELECT tablename FROM pg_catalog.pg_tables WHERE schemaname='public';
[2024-02-05 09:34:21.642380] : Dataloom[postgres]: INSERT INTO "users" ("name", "username") VALUES (%s, %s) RETURNING *;
[2024-02-05 09:34:21.678007] : Dataloom[postgres]: 
    DELETE FROM "users" WHERE "id" = (
        SELECT "id" FROM  "users" WHERE "name" = %s LIMIT 1
    );
    
[2024-02-05 09:34:21.706393] : Dataloom[postgres]: SELECT "createdAt", "id", "name", "updatedAt", "username" FROM "users" WHERE "name" = %s   ;
[2024-02-05 09:34:21.733445] : Dataloom[postgres]: 
    DELETE FROM "users" WHERE "id" = (
        SELECT "id" FROM  "users" WHERE "name" = %s AND "id" = %s LIMIT 1
    );
    
[2024-02-05 09:34:21.764383] : Dataloom[postgres]: SELECT "createdAt", "id", "name", "updatedAt", "username" FROM "users" WHERE "name" = %s   ;
[2024-02-05 09:34:21.793393] : Dataloom[postgres]: 
    DELETE FROM "users" WHERE "id" = (
        SELECT "id" FROM  "users" WHERE "name" = %s AND "id" = %s LIMIT 1
    );
    
[2024-02-05 09:34:21.823377] : Dataloom[postgres]: SELECT "createdAt", "id", "name", "updatedAt", "username" FROM "users" WHERE "name" = %s   ;
[2024-02-05 09:34:22.001287] : Dataloom[postgres]: DROP TABLE IF EXISTS "posts" CASCADE;
[2024-02-05 09:34:22.052659] : Dataloom[postgres]: CREATE TABLE IF NOT EXISTS "posts" ("completed" BOOLEAN DEFAULT False, "id" BIGSERIAL PRIMARY KEY UNIQUE NOT NULL, "title" VARCHAR(255) NOT NULL, "createdAt" TIMESTAMP DEFAULT CURRENT_TIMESTAMP, "updatedAt" TIMESTAMP DEFAULT CURRENT_TIMESTAMP, "userId" BIGSERIAL NOT NULL REFERENCES "users"("id") ON DELETE CASCADE ON UPDATE CASCADE);
[2024-02-05 09:34:22.174353] : Dataloom[postgres]: DROP TABLE IF EXISTS "users" CASCADE;
[2024-02-05 09:34:22.222925] : Dataloom[postgres]: CREATE TABLE IF NOT EXISTS "users" ("id" BIGSERIAL PRIMARY KEY UNIQUE NOT NULL, "name" TEXT NOT NULL DEFAULT 'Bob', "username" VARCHAR(255) UNIQUE, "createdAt" TIMESTAMP DEFAULT CURRENT_TIMESTAMP, "updatedAt" TIMESTAMP DEFAULT CURRENT_TIMESTAMP);
[2024-02-05 09:34:22.272458] : Dataloom[postgres]: SELECT tablename FROM pg_catalog.pg_tables WHERE schemaname='public';
[2024-02-05 09:34:22.323610] : Dataloom[postgres]: INSERT INTO "users" ("name", "username") VALUES (%s, %s) RETURNING *;
[2024-02-05 09:34:22.363648] : Dataloom[postgres]: DELETE FROM "users" WHERE "name" = %s;
[2024-02-05 09:34:22.399702] : Dataloom[postgres]: SELECT "createdAt", "id", "name", "updatedAt", "username" FROM "users" WHERE "name" = %s   ;
[2024-02-05 09:34:22.431691] : Dataloom[postgres]: INSERT INTO "users" ("name", "username") VALUES (%s, %s) RETURNING *;
[2024-02-05 09:34:22.468903] : Dataloom[postgres]: DELETE FROM "users" WHERE "name" = %s AND "id" = %s;
[2024-02-05 09:34:22.497981] : Dataloom[postgres]: SELECT "createdAt", "id", "name", "updatedAt", "username" FROM "users" WHERE "name" = %s   ;
[2024-02-05 09:34:22.524986] : Dataloom[postgres]: DELETE FROM "users" WHERE "name" = %s AND "id" = %s;
[2024-02-05 09:34:22.552932] : Dataloom[postgres]: SELECT "createdAt", "id", "name", "updatedAt", "username" FROM "users" WHERE "name" = %s   ;
[2024-02-05 09:34:22.732525] : Dataloom[postgres]: DROP TABLE IF EXISTS "posts" CASCADE;
[2024-02-05 09:34:22.784537] : Dataloom[postgres]: CREATE TABLE IF NOT EXISTS "posts" ("completed" BOOLEAN DEFAULT False, "id" BIGSERIAL PRIMARY KEY UNIQUE NOT NULL, "title" VARCHAR(255) NOT NULL, "createdAt" TIMESTAMP DEFAULT CURRENT_TIMESTAMP, "updatedAt" TIMESTAMP DEFAULT CURRENT_TIMESTAMP, "userId" BIGSERIAL NOT NULL REFERENCES "users"("id") ON DELETE CASCADE ON UPDATE CASCADE);
[2024-02-05 09:34:22.859005] : Dataloom[postgres]: DROP TABLE IF EXISTS "users" CASCADE;
[2024-02-05 09:34:22.913433] : Dataloom[postgres]: CREATE TABLE IF NOT EXISTS "users" ("id" BIGSERIAL PRIMARY KEY UNIQUE NOT NULL, "name" TEXT NOT NULL DEFAULT 'Bob', "username" VARCHAR(255) UNIQUE, "createdAt" TIMESTAMP DEFAULT CURRENT_TIMESTAMP, "updatedAt" TIMESTAMP DEFAULT CURRENT_TIMESTAMP);
[2024-02-05 09:34:22.972019] : Dataloom[postgres]: SELECT tablename FROM pg_catalog.pg_tables WHERE schemaname='public';
[2024-02-05 09:34:23.026597] : Dataloom[postgres]: INSERT INTO "users" ("username") VALUES (%s) RETURNING "id";
[2024-02-05 09:34:23.066579] : Dataloom[postgres]: INSERT INTO "posts" ("title", "userId") VALUES (%s, %s) RETURNING "id";
[2024-02-05 09:34:23.277179] : Dataloom[postgres]: DROP TABLE IF EXISTS "posts" CASCADE;
[2024-02-05 09:34:23.328231] : Dataloom[postgres]: CREATE TABLE IF NOT EXISTS "posts" ("completed" BOOLEAN DEFAULT False, "id" BIGSERIAL PRIMARY KEY UNIQUE NOT NULL, "title" VARCHAR(255) NOT NULL, "createdAt" TIMESTAMP DEFAULT CURRENT_TIMESTAMP, "updatedAt" TIMESTAMP DEFAULT CURRENT_TIMESTAMP, "userId" BIGSERIAL NOT NULL REFERENCES "users"("id") ON DELETE CASCADE ON UPDATE CASCADE);
[2024-02-05 09:34:23.393743] : Dataloom[postgres]: DROP TABLE IF EXISTS "users" CASCADE;
[2024-02-05 09:34:23.446737] : Dataloom[postgres]: CREATE TABLE IF NOT EXISTS "users" ("id" BIGSERIAL PRIMARY KEY UNIQUE NOT NULL, "name" TEXT NOT NULL DEFAULT 'Bob', "username" VARCHAR(255) UNIQUE, "createdAt" TIMESTAMP DEFAULT CURRENT_TIMESTAMP, "updatedAt" TIMESTAMP DEFAULT CURRENT_TIMESTAMP);
[2024-02-05 09:34:23.499787] : Dataloom[postgres]: SELECT tablename FROM pg_catalog.pg_tables WHERE schemaname='public';
[2024-02-05 09:34:23.547406] : Dataloom[postgres]: INSERT INTO "users" ("username") VALUES (%s) RETURNING "id";
[2024-02-05 09:34:23.584209] : Dataloom[postgres]: INSERT INTO "posts" ("title", "userId") VALUES (%s, %s) RETURNING *;
[2024-02-05 09:34:23.799492] : Dataloom[postgres]: DROP TABLE IF EXISTS "posts" CASCADE;
[2024-02-05 09:34:23.859442] : Dataloom[postgres]: CREATE TABLE IF NOT EXISTS "posts" ("completed" BOOLEAN DEFAULT False, "id" BIGSERIAL PRIMARY KEY UNIQUE NOT NULL, "title" VARCHAR(255) NOT NULL, "createdAt" TIMESTAMP DEFAULT CURRENT_TIMESTAMP, "updatedAt" TIMESTAMP DEFAULT CURRENT_TIMESTAMP, "userId" BIGSERIAL NOT NULL REFERENCES "users"("id") ON DELETE CASCADE ON UPDATE CASCADE);
[2024-02-05 09:34:23.927290] : Dataloom[postgres]: DROP TABLE IF EXISTS "users" CASCADE;
[2024-02-05 09:34:23.982078] : Dataloom[postgres]: CREATE TABLE IF NOT EXISTS "users" ("id" BIGSERIAL PRIMARY KEY UNIQUE NOT NULL, "name" TEXT NOT NULL DEFAULT 'Bob', "username" VARCHAR(255) UNIQUE);
[2024-02-05 09:34:24.035308] : Dataloom[postgres]: SELECT tablename FROM pg_catalog.pg_tables WHERE schemaname='public';
[2024-02-05 09:34:24.086631] : Dataloom[postgres]: INSERT INTO "users" ("username") VALUES (%s) RETURNING "id";
[2024-02-05 09:34:24.119714] : Dataloom[postgres]: INSERT INTO "posts" ("title", "userId") VALUES (%s, %s) RETURNING *;
[2024-02-05 09:34:24.152751] : Dataloom[postgres]: SELECT "id", "name", "username" FROM "users" WHERE "id" = %s;
[2024-02-05 09:34:24.178899] : Dataloom[postgres]: SELECT "id", "name", "username" FROM "users" WHERE "id" = %s;
[2024-02-05 09:34:24.205753] : Dataloom[postgres]: SELECT "id", "completed" FROM "posts" WHERE "id" = %s;
[2024-02-05 09:34:24.400099] : Dataloom[postgres]: DROP TABLE IF EXISTS "posts" CASCADE;
[2024-02-05 09:34:24.454107] : Dataloom[postgres]: CREATE TABLE IF NOT EXISTS "posts" ("completed" BOOLEAN DEFAULT False, "id" BIGSERIAL PRIMARY KEY UNIQUE NOT NULL, "title" VARCHAR(255) NOT NULL, "createdAt" TIMESTAMP DEFAULT CURRENT_TIMESTAMP, "updatedAt" TIMESTAMP DEFAULT CURRENT_TIMESTAMP, "userId" BIGSERIAL NOT NULL REFERENCES "users"("id") ON DELETE CASCADE ON UPDATE CASCADE);
[2024-02-05 09:34:24.548329] : Dataloom[postgres]: DROP TABLE IF EXISTS "users" CASCADE;
[2024-02-05 09:34:24.610679] : Dataloom[postgres]: CREATE TABLE IF NOT EXISTS "users" ("id" BIGSERIAL PRIMARY KEY UNIQUE NOT NULL, "name" TEXT NOT NULL DEFAULT 'Bob', "username" VARCHAR(255) UNIQUE);
[2024-02-05 09:34:24.649323] : Dataloom[postgres]: SELECT tablename FROM pg_catalog.pg_tables WHERE schemaname='public';
[2024-02-05 09:34:24.680323] : Dataloom[postgres]: INSERT INTO "users" ("username") VALUES (%s) RETURNING "id";
[2024-02-05 09:34:24.701327] : Dataloom[postgres]: INSERT INTO "posts" ("title", "userId") VALUES (%s, %s) RETURNING *;
[2024-02-05 09:34:24.726333] : Dataloom[postgres]: SELECT "id", "name", "username" FROM "users"   ;
[2024-02-05 09:34:24.746618] : Dataloom[postgres]: SELECT "completed", "createdAt", "id", "title", "updatedAt", "userId" FROM "posts"   ;
[2024-02-05 09:34:24.771618] : Dataloom[postgres]: SELECT "id", "completed" FROM "posts"  LIMIT 3 OFFSET 3;
[2024-02-05 09:34:24.892383] : Dataloom[postgres]: DROP TABLE IF EXISTS "posts" CASCADE;
[2024-02-05 09:34:24.937244] : Dataloom[postgres]: CREATE TABLE IF NOT EXISTS "posts" ("completed" BOOLEAN DEFAULT False, "id" BIGSERIAL PRIMARY KEY UNIQUE NOT NULL, "title" VARCHAR(255) NOT NULL, "createdAt" TIMESTAMP DEFAULT CURRENT_TIMESTAMP, "updatedAt" TIMESTAMP DEFAULT CURRENT_TIMESTAMP, "userId" BIGSERIAL NOT NULL REFERENCES "users"("id") ON DELETE CASCADE ON UPDATE CASCADE);
[2024-02-05 09:34:24.994972] : Dataloom[postgres]: DROP TABLE IF EXISTS "users" CASCADE;
[2024-02-05 09:34:25.039419] : Dataloom[postgres]: CREATE TABLE IF NOT EXISTS "users" ("id" BIGSERIAL PRIMARY KEY UNIQUE NOT NULL, "name" TEXT NOT NULL DEFAULT 'Bob', "username" VARCHAR(255) UNIQUE);
[2024-02-05 09:34:25.086205] : Dataloom[postgres]: SELECT tablename FROM pg_catalog.pg_tables WHERE schemaname='public';
[2024-02-05 09:34:25.130680] : Dataloom[postgres]: INSERT INTO "users" ("username") VALUES (%s) RETURNING "id";
[2024-02-05 09:34:25.164233] : Dataloom[postgres]: INSERT INTO "posts" ("title", "userId") VALUES (%s, %s) RETURNING *;
[2024-02-05 09:34:25.195693] : Dataloom[postgres]: SELECT "id", "name", "username" FROM "users" WHERE "id" = %s   ;
[2024-02-05 09:34:25.221690] : Dataloom[postgres]: SELECT "id", "name", "username" FROM "users" WHERE "id" = %s   ;
[2024-02-05 09:34:25.247630] : Dataloom[postgres]: SELECT "id", "name", "username" FROM "users" WHERE "id" = %s AND "name" = %s   ;
[2024-02-05 09:34:25.275691] : Dataloom[postgres]: SELECT "id", "name", "username" FROM "users" WHERE "id" = %s AND "username" = %s   ;
[2024-02-05 09:34:25.303755] : Dataloom[postgres]: SELECT "id", "name", "username" FROM "users" WHERE "name" = %s AND "username" = %s   ;
[2024-02-05 09:34:25.332852] : Dataloom[postgres]: SELECT "id", "completed" FROM "posts"   ;
[2024-02-05 09:34:25.515468] : Dataloom[postgres]: DROP TABLE IF EXISTS "posts" CASCADE;
[2024-02-05 09:34:25.558591] : Dataloom[postgres]: CREATE TABLE IF NOT EXISTS "posts" ("completed" BOOLEAN DEFAULT False, "id" BIGSERIAL PRIMARY KEY UNIQUE NOT NULL, "title" VARCHAR(255) NOT NULL, "createdAt" TIMESTAMP DEFAULT CURRENT_TIMESTAMP, "updatedAt" TIMESTAMP DEFAULT CURRENT_TIMESTAMP, "userId" BIGSERIAL NOT NULL REFERENCES "users"("id") ON DELETE CASCADE ON UPDATE CASCADE);
[2024-02-05 09:34:25.610351] : Dataloom[postgres]: DROP TABLE IF EXISTS "users" CASCADE;
[2024-02-05 09:34:25.650012] : Dataloom[postgres]: CREATE TABLE IF NOT EXISTS "users" ("id" BIGSERIAL PRIMARY KEY UNIQUE NOT NULL, "name" TEXT NOT NULL DEFAULT 'Bob', "username" VARCHAR(255) UNIQUE);
[2024-02-05 09:34:25.694423] : Dataloom[postgres]: SELECT tablename FROM pg_catalog.pg_tables WHERE schemaname='public';
[2024-02-05 09:34:25.735492] : Dataloom[postgres]: INSERT INTO "users" ("username") VALUES (%s) RETURNING "id";
[2024-02-05 09:34:25.765701] : Dataloom[postgres]: INSERT INTO "posts" ("title", "userId") VALUES (%s, %s) RETURNING *;
[2024-02-05 09:34:25.797984] : Dataloom[postgres]: SELECT "completed", "createdAt", "id", "title", "updatedAt", "userId" FROM "posts" WHERE "id" = %s AND "userId" = %s   ;
[2024-02-05 09:34:25.826994] : Dataloom[postgres]: SELECT "id", "name", "username" FROM "users"   ;
[2024-02-05 09:34:25.852051] : Dataloom[postgres]: SELECT "id", "name", "username" FROM "users" WHERE "id" = %s   ;
[2024-02-05 09:34:25.878070] : Dataloom[postgres]: SELECT "id", "name", "username" FROM "users" WHERE "id" = %s   ;
[2024-02-05 09:34:25.902091] : Dataloom[postgres]: SELECT "id", "name", "username" FROM "users" WHERE "id" = %s AND "name" = %s   ;
[2024-02-05 09:34:25.927028] : Dataloom[postgres]: SELECT "id", "name", "username" FROM "users" WHERE "id" = %s AND "username" = %s   ;
[2024-02-05 09:34:25.951806] : Dataloom[postgres]: SELECT "id", "name", "username" FROM "users" WHERE "name" = %s AND "username" = %s   ;
[2024-02-05 09:34:25.975758] : Dataloom[postgres]: SELECT "id", "completed" FROM "posts" WHERE "userId" = %s  LIMIT 3 OFFSET 3;
[2024-02-05 09:34:26.001767] : Dataloom[postgres]: SELECT "completed", "createdAt", "id", "title", "updatedAt", "userId" FROM "posts"   ;
[2024-02-05 09:34:26.171761] : Dataloom[postgres]: DROP TABLE IF EXISTS "posts" CASCADE;
[2024-02-05 09:34:26.215927] : Dataloom[postgres]: CREATE TABLE IF NOT EXISTS "posts" ("completed" BOOLEAN DEFAULT False, "id" BIGSERIAL PRIMARY KEY UNIQUE NOT NULL, "title" VARCHAR(255) NOT NULL, "createdAt" TIMESTAMP DEFAULT CURRENT_TIMESTAMP, "updatedAt" TIMESTAMP DEFAULT CURRENT_TIMESTAMP, "userId" BIGSERIAL NOT NULL REFERENCES "users"("id") ON DELETE CASCADE ON UPDATE CASCADE);
[2024-02-05 09:34:26.266568] : Dataloom[postgres]: DROP TABLE IF EXISTS "users" CASCADE;
[2024-02-05 09:34:26.308734] : Dataloom[postgres]: CREATE TABLE IF NOT EXISTS "users" ("id" BIGSERIAL PRIMARY KEY UNIQUE NOT NULL, "name" TEXT NOT NULL DEFAULT 'Bob', "username" VARCHAR(255) UNIQUE, "createdAt" TIMESTAMP DEFAULT CURRENT_TIMESTAMP, "updatedAt" TIMESTAMP DEFAULT CURRENT_TIMESTAMP);
[2024-02-05 09:34:26.355559] : Dataloom[postgres]: SELECT tablename FROM pg_catalog.pg_tables WHERE schemaname='public';
[2024-02-05 09:34:26.396167] : Dataloom[postgres]: INSERT INTO "users" ("username") VALUES (%s) RETURNING "id";
[2024-02-05 09:34:26.427613] : Dataloom[postgres]: INSERT INTO "posts" ("title", "userId") VALUES (%s, %s) RETURNING *;
[2024-02-05 09:34:26.511452] : Dataloom[postgres]: UPDATE "users" SET "updatedAt" = %s WHERE "id" = %s;
[2024-02-05 09:34:26.541495] : Dataloom[postgres]: UPDATE "users" SET "updatedAt" = %s WHERE "id" = %s;
[2024-02-05 09:34:26.576557] : Dataloom[postgres]: SELECT "createdAt", "id", "name", "updatedAt", "username" FROM "users" WHERE "id" = %s;
[2024-02-05 09:34:26.609449] : Dataloom[postgres]: UPDATE "users" SET "id" = %s, "updatedAt" = %s WHERE "id" = %s;
[2024-02-05 09:34:26.801355] : Dataloom[postgres]: DROP TABLE IF EXISTS "posts" CASCADE;
[2024-02-05 09:34:26.850461] : Dataloom[postgres]: CREATE TABLE IF NOT EXISTS "posts" ("completed" BOOLEAN DEFAULT False, "id" BIGSERIAL PRIMARY KEY UNIQUE NOT NULL, "title" VARCHAR(255) NOT NULL, "createdAt" TIMESTAMP DEFAULT CURRENT_TIMESTAMP, "userId" BIGSERIAL NOT NULL REFERENCES "users"("id") ON DELETE CASCADE ON UPDATE CASCADE);
[2024-02-05 09:34:26.911445] : Dataloom[postgres]: DROP TABLE IF EXISTS "users" CASCADE;
[2024-02-05 09:34:26.957626] : Dataloom[postgres]: CREATE TABLE IF NOT EXISTS "users" ("id" BIGSERIAL PRIMARY KEY UNIQUE NOT NULL, "name" TEXT NOT NULL DEFAULT 'Bob', "username" VARCHAR(255) UNIQUE, "createdAt" TIMESTAMP DEFAULT CURRENT_TIMESTAMP, "updatedAt" TIMESTAMP DEFAULT CURRENT_TIMESTAMP);
[2024-02-05 09:34:27.002657] : Dataloom[postgres]: SELECT tablename FROM pg_catalog.pg_tables WHERE schemaname='public';
[2024-02-05 09:34:27.045156] : Dataloom[postgres]: INSERT INTO "users" ("username") VALUES (%s) RETURNING "id";
[2024-02-05 09:34:27.076396] : Dataloom[postgres]: INSERT INTO "posts" ("title", "userId") VALUES (%s, %s) RETURNING *;
[2024-02-05 09:34:27.163914] : Dataloom[postgres]: 
        UPDATE "users" SET "name" = %s, "updatedAt" = %s WHERE "id" = (
            SELECT "id" FROM  "users" WHERE "username" = %s LIMIT 1
        );
        
[2024-02-05 09:34:27.196503] : Dataloom[postgres]: 
        UPDATE "users" SET "name" = %s, "updatedAt" = %s WHERE "id" = (
            SELECT "id" FROM  "users" WHERE "username" = %s LIMIT 1
        );
        
[2024-02-05 09:34:27.226764] : Dataloom[postgres]: SELECT "createdAt", "id", "name", "updatedAt", "username" FROM "users" WHERE "id" = %s;
[2024-02-05 09:34:27.256791] : Dataloom[postgres]: 
        UPDATE "users" SET "id" = %s, "updatedAt" = %s WHERE "id" = (
            SELECT "id" FROM  "users" WHERE "username" = %s LIMIT 1
        );
        
[2024-02-05 09:34:27.416915] : Dataloom[postgres]: DROP TABLE IF EXISTS "posts" CASCADE;
[2024-02-05 09:34:27.451177] : Dataloom[postgres]: CREATE TABLE IF NOT EXISTS "posts" ("completed" BOOLEAN DEFAULT False, "id" BIGSERIAL PRIMARY KEY UNIQUE NOT NULL, "title" VARCHAR(255) NOT NULL, "createdAt" TIMESTAMP DEFAULT CURRENT_TIMESTAMP, "userId" BIGSERIAL NOT NULL REFERENCES "users"("id") ON DELETE CASCADE ON UPDATE CASCADE);
[2024-02-05 09:34:27.494131] : Dataloom[postgres]: DROP TABLE IF EXISTS "users" CASCADE;
[2024-02-05 09:34:27.528462] : Dataloom[postgres]: CREATE TABLE IF NOT EXISTS "users" ("id" BIGSERIAL PRIMARY KEY UNIQUE NOT NULL, "name" TEXT NOT NULL DEFAULT 'Bob', "username" VARCHAR(255) UNIQUE, "createdAt" TIMESTAMP DEFAULT CURRENT_TIMESTAMP, "updatedAt" TIMESTAMP DEFAULT CURRENT_TIMESTAMP);
[2024-02-05 09:34:27.564099] : Dataloom[postgres]: SELECT tablename FROM pg_catalog.pg_tables WHERE schemaname='public';
[2024-02-05 09:34:27.598761] : Dataloom[postgres]: INSERT INTO "users" ("username") VALUES (%s) RETURNING "id";
[2024-02-05 09:34:27.628210] : Dataloom[postgres]: INSERT INTO "posts" ("title", "userId") VALUES (%s, %s) RETURNING *;
[2024-02-05 09:34:27.654502] : Dataloom[postgres]: UPDATE "posts" SET "title" = %s WHERE "userId" = %s;
[2024-02-05 09:34:27.677224] : Dataloom[postgres]: UPDATE "posts" SET "title" = %s WHERE "userId" = %s;
[2024-02-05 09:34:27.703218] : Dataloom[postgres]: UPDATE "posts" SET "userId" = %s WHERE "userId" = %s;
[2024-02-05 09:34:27.771273] : Dataloom[sqlite]: DROP TABLE IF EXISTS users;
[2024-02-05 09:34:27.856252] : Dataloom[sqlite]: DROP TABLE IF EXISTS users;
[2024-02-05 09:34:27.926181] : Dataloom[sqlite]: DROP TABLE IF EXISTS users;
[2024-02-05 09:34:27.979690] : Dataloom[sqlite]: CREATE TABLE IF NOT EXISTS `users` (`id` INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL, `name` VARCHAR, `username` TEXT NOT NULL);
[2024-02-05 09:34:28.032689] : Dataloom[sqlite]: DROP TABLE IF EXISTS posts;
[2024-02-05 09:34:28.071689] : Dataloom[sqlite]: CREATE TABLE IF NOT EXISTS `posts` (`id` INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL, `title` TEXT NOT NULL);
[2024-02-05 09:34:28.109740] : Dataloom[sqlite]: SELECT name FROM sqlite_master WHERE type='table';
[2024-02-05 09:34:28.152194] : Dataloom[sqlite]: DROP TABLE IF EXISTS users;
[2024-02-05 09:34:28.199077] : Dataloom[sqlite]: CREATE TABLE IF NOT EXISTS `users` (`id` INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL, `name` VARCHAR UNIQUE, `username` TEXT NOT NULL DEFAULT 'Hello there!!');
[2024-02-05 09:34:28.242022] : Dataloom[sqlite]: DROP TABLE IF EXISTS posts;
[2024-02-05 09:34:28.282080] : Dataloom[sqlite]: CREATE TABLE IF NOT EXISTS `posts` (`completed` BOOLEAN DEFAULT False, `id` INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL, `title` VARCHAR NOT NULL);
[2024-02-05 09:34:28.320082] : Dataloom[sqlite]: SELECT name FROM sqlite_master WHERE type='table';
[2024-02-05 09:34:28.366546] : Dataloom[sqlite]: DROP TABLE IF EXISTS posts;
[2024-02-05 09:34:28.426556] : Dataloom[sqlite]: CREATE TABLE IF NOT EXISTS `posts` (`completed` BOOLEAN DEFAULT False, `id` INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL, `title` VARCHAR NOT NULL, `createdAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP, `updatedAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP, `userId` INTEGER NOT NULL REFERENCES `users`(`id`) ON DELETE CASCADE ON UPDATE CASCADE);
[2024-02-05 09:34:28.477540] : Dataloom[sqlite]: DROP TABLE IF EXISTS users;
[2024-02-05 09:34:28.522500] : Dataloom[sqlite]: CREATE TABLE IF NOT EXISTS `users` (`id` INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL, `name` TEXT NOT NULL DEFAULT 'Bob', `username` VARCHAR UNIQUE, `createdAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP, `updatedAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP);
[2024-02-05 09:34:28.569488] : Dataloom[sqlite]: SELECT name FROM sqlite_master WHERE type='table';
[2024-02-05 09:34:28.611570] : Dataloom[sqlite]: INSERT INTO `users` (`name`, `username`) VALUES (?, ?);
[2024-02-05 09:34:28.662532] : Dataloom[sqlite]: DELETE FROM `users` WHERE `id` = ?;
[2024-02-05 09:34:28.714494] : Dataloom[sqlite]: DELETE FROM `users` WHERE `id` = ?;
[2024-02-05 09:34:28.768496] : Dataloom[sqlite]: DROP TABLE IF EXISTS posts;
[2024-02-05 09:34:28.830630] : Dataloom[sqlite]: CREATE TABLE IF NOT EXISTS `posts` (`completed` BOOLEAN DEFAULT False, `id` INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL, `title` VARCHAR NOT NULL, `createdAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP, `updatedAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP, `userId` INTEGER NOT NULL REFERENCES `users`(`id`) ON DELETE CASCADE ON UPDATE CASCADE);
[2024-02-05 09:34:28.883146] : Dataloom[sqlite]: DROP TABLE IF EXISTS users;
[2024-02-05 09:34:28.938141] : Dataloom[sqlite]: CREATE TABLE IF NOT EXISTS `users` (`id` INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL, `name` TEXT NOT NULL DEFAULT 'Bob', `username` VARCHAR UNIQUE, `createdAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP, `updatedAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP);
[2024-02-05 09:34:28.980049] : Dataloom[sqlite]: SELECT name FROM sqlite_master WHERE type='table';
[2024-02-05 09:34:29.017277] : Dataloom[sqlite]: INSERT INTO `users` (`name`, `username`) VALUES (?, ?);
[2024-02-05 09:34:29.071068] : Dataloom[sqlite]: 
    DELETE FROM `users` WHERE `id` = (
        SELECT `id` FROM  `users` WHERE `name` = ? LIMIT 1
    );
    
[2024-02-05 09:34:29.112307] : Dataloom[sqlite]: SELECT `createdAt`, `id`, `name`, `updatedAt`, `username` FROM `users` WHERE `name` = ?   ;
[2024-02-05 09:34:29.156310] : Dataloom[sqlite]: 
    DELETE FROM `users` WHERE `id` = (
        SELECT `id` FROM  `users` WHERE `name` = ? AND `id` = ? LIMIT 1
    );
    
[2024-02-05 09:34:29.202313] : Dataloom[sqlite]: SELECT `createdAt`, `id`, `name`, `updatedAt`, `username` FROM `users` WHERE `name` = ?   ;
[2024-02-05 09:34:29.245328] : Dataloom[sqlite]: 
    DELETE FROM `users` WHERE `id` = (
        SELECT `id` FROM  `users` WHERE `name` = ? AND `id` = ? LIMIT 1
    );
    
[2024-02-05 09:34:29.298323] : Dataloom[sqlite]: SELECT `createdAt`, `id`, `name`, `updatedAt`, `username` FROM `users` WHERE `name` = ?   ;
[2024-02-05 09:34:29.348307] : Dataloom[sqlite]: DROP TABLE IF EXISTS posts;
[2024-02-05 09:34:29.403597] : Dataloom[sqlite]: CREATE TABLE IF NOT EXISTS `posts` (`completed` BOOLEAN DEFAULT False, `id` INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL, `title` VARCHAR NOT NULL, `createdAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP, `updatedAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP, `userId` INTEGER NOT NULL REFERENCES `users`(`id`) ON DELETE CASCADE ON UPDATE CASCADE);
[2024-02-05 09:34:29.452145] : Dataloom[sqlite]: DROP TABLE IF EXISTS users;
[2024-02-05 09:34:29.494905] : Dataloom[sqlite]: CREATE TABLE IF NOT EXISTS `users` (`id` INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL, `name` TEXT NOT NULL DEFAULT 'Bob', `username` VARCHAR UNIQUE, `createdAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP, `updatedAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP);
[2024-02-05 09:34:29.534891] : Dataloom[sqlite]: SELECT name FROM sqlite_master WHERE type='table';
[2024-02-05 09:34:29.567900] : Dataloom[sqlite]: INSERT INTO `users` (`name`, `username`) VALUES (?, ?);
[2024-02-05 09:34:29.613650] : Dataloom[sqlite]: DELETE FROM `users` WHERE `name` = ?;
[2024-02-05 09:34:29.653664] : Dataloom[sqlite]: SELECT `createdAt`, `id`, `name`, `updatedAt`, `username` FROM `users` WHERE `name` = ?   ;
[2024-02-05 09:34:29.686703] : Dataloom[sqlite]: INSERT INTO `users` (`name`, `username`) VALUES (?, ?);
[2024-02-05 09:34:29.736687] : Dataloom[sqlite]: DELETE FROM `users` WHERE `name` = ? AND `id` = ?;
[2024-02-05 09:34:29.774687] : Dataloom[sqlite]: SELECT `createdAt`, `id`, `name`, `updatedAt`, `username` FROM `users` WHERE `name` = ?   ;
[2024-02-05 09:34:29.812760] : Dataloom[sqlite]: DELETE FROM `users` WHERE `name` = ? AND `id` = ?;
[2024-02-05 09:34:29.879676] : Dataloom[sqlite]: SELECT `createdAt`, `id`, `name`, `updatedAt`, `username` FROM `users` WHERE `name` = ?   ;
[2024-02-05 09:34:29.934669] : Dataloom[sqlite]: DROP TABLE IF EXISTS posts;
[2024-02-05 09:34:29.976672] : Dataloom[sqlite]: CREATE TABLE IF NOT EXISTS `posts` (`completed` BOOLEAN DEFAULT False, `id` INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL, `title` VARCHAR NOT NULL, `createdAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP, `updatedAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP, `userId` INTEGER NOT NULL REFERENCES `users`(`id`) ON DELETE CASCADE ON UPDATE CASCADE);
[2024-02-05 09:34:30.013671] : Dataloom[sqlite]: DROP TABLE IF EXISTS users;
[2024-02-05 09:34:30.046670] : Dataloom[sqlite]: CREATE TABLE IF NOT EXISTS `users` (`id` INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL, `name` TEXT NOT NULL DEFAULT 'Bob', `username` VARCHAR UNIQUE, `createdAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP, `updatedAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP);
[2024-02-05 09:34:30.076928] : Dataloom[sqlite]: SELECT name FROM sqlite_master WHERE type='table';
[2024-02-05 09:34:30.098926] : Dataloom[sqlite]: INSERT INTO `users` (`username`) VALUES (?);
[2024-02-05 09:34:30.122930] : Dataloom[sqlite]: INSERT INTO `posts` (`title`, `userId`) VALUES (?, ?);
[2024-02-05 09:34:30.152932] : Dataloom[sqlite]: DROP TABLE IF EXISTS posts;
[2024-02-05 09:34:30.181928] : Dataloom[sqlite]: CREATE TABLE IF NOT EXISTS `posts` (`completed` BOOLEAN DEFAULT False, `id` INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL, `title` VARCHAR NOT NULL, `createdAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP, `updatedAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP, `userId` INTEGER NOT NULL REFERENCES `users`(`id`) ON DELETE CASCADE ON UPDATE CASCADE);
[2024-02-05 09:34:30.214526] : Dataloom[sqlite]: DROP TABLE IF EXISTS users;
[2024-02-05 09:34:30.255634] : Dataloom[sqlite]: CREATE TABLE IF NOT EXISTS `users` (`id` INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL, `name` TEXT NOT NULL DEFAULT 'Bob', `username` VARCHAR UNIQUE, `createdAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP, `updatedAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP);
[2024-02-05 09:34:30.294264] : Dataloom[sqlite]: SELECT name FROM sqlite_master WHERE type='table';
[2024-02-05 09:34:30.324263] : Dataloom[sqlite]: INSERT INTO `users` (`username`) VALUES (?);
[2024-02-05 09:34:30.362260] : Dataloom[sqlite]: INSERT INTO `posts` (`title`, `userId`) VALUES (?, ?);
[2024-02-05 09:34:30.419159] : Dataloom[sqlite]: DROP TABLE IF EXISTS posts;
[2024-02-05 09:34:30.476165] : Dataloom[sqlite]: CREATE TABLE IF NOT EXISTS `posts` (`completed` BOOLEAN DEFAULT False, `id` INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL, `title` VARCHAR NOT NULL, `createdAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP, `updatedAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP, `userId` INTEGER NOT NULL REFERENCES `users`(`id`) ON DELETE CASCADE ON UPDATE CASCADE);
[2024-02-05 09:34:30.522372] : Dataloom[sqlite]: DROP TABLE IF EXISTS users;
[2024-02-05 09:34:30.575159] : Dataloom[sqlite]: CREATE TABLE IF NOT EXISTS `users` (`id` INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL, `name` TEXT NOT NULL DEFAULT 'Bob', `username` VARCHAR UNIQUE);
[2024-02-05 09:34:30.631159] : Dataloom[sqlite]: SELECT name FROM sqlite_master WHERE type='table';
[2024-02-05 09:34:30.680158] : Dataloom[sqlite]: INSERT INTO `users` (`username`) VALUES (?);
[2024-02-05 09:34:30.735154] : Dataloom[sqlite]: INSERT INTO `posts` (`title`, `userId`) VALUES (?, ?);
[2024-02-05 09:34:30.786156] : Dataloom[sqlite]: SELECT `id`, `name`, `username` FROM `users` WHERE `id` = ?;
[2024-02-05 09:34:30.827642] : Dataloom[sqlite]: SELECT `id`, `name`, `username` FROM `users` WHERE `id` = ?;
[2024-02-05 09:34:30.867341] : Dataloom[sqlite]: SELECT `id`, `completed` FROM `posts` WHERE `id` = ?;
[2024-02-05 09:34:30.931154] : Dataloom[sqlite]: DROP TABLE IF EXISTS posts;
[2024-02-05 09:34:30.978157] : Dataloom[sqlite]: CREATE TABLE IF NOT EXISTS `posts` (`completed` BOOLEAN DEFAULT False, `id` INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL, `title` VARCHAR NOT NULL, `createdAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP, `updatedAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP, `userId` INTEGER NOT NULL REFERENCES `users`(`id`) ON DELETE CASCADE ON UPDATE CASCADE);
[2024-02-05 09:34:31.021158] : Dataloom[sqlite]: DROP TABLE IF EXISTS users;
[2024-02-05 09:34:31.060208] : Dataloom[sqlite]: CREATE TABLE IF NOT EXISTS `users` (`id` INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL, `name` TEXT NOT NULL DEFAULT 'Bob', `username` VARCHAR UNIQUE);
[2024-02-05 09:34:31.099108] : Dataloom[sqlite]: SELECT name FROM sqlite_master WHERE type='table';
[2024-02-05 09:34:31.134116] : Dataloom[sqlite]: INSERT INTO `users` (`username`) VALUES (?);
[2024-02-05 09:34:31.194096] : Dataloom[sqlite]: INSERT INTO `posts` (`title`, `userId`) VALUES (?, ?);
[2024-02-05 09:34:31.247098] : Dataloom[sqlite]: SELECT `id`, `name`, `username` FROM `users`   ;
[2024-02-05 09:34:31.284089] : Dataloom[sqlite]: SELECT `completed`, `createdAt`, `id`, `title`, `updatedAt`, `userId` FROM `posts`   ;
[2024-02-05 09:34:31.313649] : Dataloom[sqlite]: SELECT `id`, `completed` FROM `posts`  LIMIT 3 OFFSET 3;
[2024-02-05 09:34:31.350801] : Dataloom[sqlite]: DROP TABLE IF EXISTS posts;
[2024-02-05 09:34:31.396648] : Dataloom[sqlite]: CREATE TABLE IF NOT EXISTS `posts` (`completed` BOOLEAN DEFAULT False, `id` INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL, `title` VARCHAR NOT NULL, `createdAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP, `updatedAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP, `userId` INTEGER NOT NULL REFERENCES `users`(`id`) ON DELETE CASCADE ON UPDATE CASCADE);
[2024-02-05 09:34:31.433645] : Dataloom[sqlite]: DROP TABLE IF EXISTS users;
[2024-02-05 09:34:31.472660] : Dataloom[sqlite]: CREATE TABLE IF NOT EXISTS `users` (`id` INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL, `name` TEXT NOT NULL DEFAULT 'Bob', `username` VARCHAR UNIQUE);
[2024-02-05 09:34:31.521654] : Dataloom[sqlite]: SELECT name FROM sqlite_master WHERE type='table';
[2024-02-05 09:34:31.557660] : Dataloom[sqlite]: INSERT INTO `users` (`username`) VALUES (?);
[2024-02-05 09:34:31.599715] : Dataloom[sqlite]: INSERT INTO `posts` (`title`, `userId`) VALUES (?, ?);
[2024-02-05 09:34:31.637651] : Dataloom[sqlite]: SELECT `id`, `name`, `username` FROM `users` WHERE `id` = ?   ;
[2024-02-05 09:34:31.665056] : Dataloom[sqlite]: SELECT `id`, `name`, `username` FROM `users` WHERE `id` = ?   ;
[2024-02-05 09:34:31.692091] : Dataloom[sqlite]: SELECT `id`, `name`, `username` FROM `users` WHERE `id` = ? AND `name` = ?   ;
[2024-02-05 09:34:31.719116] : Dataloom[sqlite]: SELECT `id`, `name`, `username` FROM `users` WHERE `id` = ? AND `username` = ?   ;
[2024-02-05 09:34:31.747097] : Dataloom[sqlite]: SELECT `id`, `name`, `username` FROM `users` WHERE `name` = ? AND `username` = ?   ;
[2024-02-05 09:34:31.783153] : Dataloom[sqlite]: SELECT `id`, `completed` FROM `posts`   ;
[2024-02-05 09:34:31.836627] : Dataloom[sqlite]: DROP TABLE IF EXISTS posts;
[2024-02-05 09:34:31.908633] : Dataloom[sqlite]: CREATE TABLE IF NOT EXISTS `posts` (`completed` BOOLEAN DEFAULT False, `id` INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL, `title` VARCHAR NOT NULL, `createdAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP, `updatedAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP, `userId` INTEGER NOT NULL REFERENCES `users`(`id`) ON DELETE CASCADE ON UPDATE CASCADE);
[2024-02-05 09:34:31.973647] : Dataloom[sqlite]: DROP TABLE IF EXISTS users;
[2024-02-05 09:34:32.036637] : Dataloom[sqlite]: CREATE TABLE IF NOT EXISTS `users` (`id` INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL, `name` TEXT NOT NULL DEFAULT 'Bob', `username` VARCHAR UNIQUE);
[2024-02-05 09:34:32.098631] : Dataloom[sqlite]: SELECT name FROM sqlite_master WHERE type='table';
[2024-02-05 09:34:32.146238] : Dataloom[sqlite]: INSERT INTO `users` (`username`) VALUES (?);
[2024-02-05 09:34:32.208237] : Dataloom[sqlite]: INSERT INTO `posts` (`title`, `userId`) VALUES (?, ?);
[2024-02-05 09:34:32.259232] : Dataloom[sqlite]: SELECT `completed`, `createdAt`, `id`, `title`, `updatedAt`, `userId` FROM `posts` WHERE `id` = ? AND `userId` = ?   ;
[2024-02-05 09:34:32.295228] : Dataloom[sqlite]: SELECT `id`, `name`, `username` FROM `users`   ;
[2024-02-05 09:34:32.334417] : Dataloom[sqlite]: SELECT `id`, `name`, `username` FROM `users` WHERE `id` = ?   ;
[2024-02-05 09:34:32.371369] : Dataloom[sqlite]: SELECT `id`, `name`, `username` FROM `users` WHERE `id` = ?   ;
[2024-02-05 09:34:32.408413] : Dataloom[sqlite]: SELECT `id`, `name`, `username` FROM `users` WHERE `id` = ? AND `name` = ?   ;
[2024-02-05 09:34:32.446358] : Dataloom[sqlite]: SELECT `id`, `name`, `username` FROM `users` WHERE `id` = ? AND `username` = ?   ;
[2024-02-05 09:34:32.484371] : Dataloom[sqlite]: SELECT `id`, `name`, `username` FROM `users` WHERE `name` = ? AND `username` = ?   ;
[2024-02-05 09:34:32.527279] : Dataloom[sqlite]: SELECT `id`, `completed` FROM `posts` WHERE `userId` = ?  LIMIT 3 OFFSET 3;
[2024-02-05 09:34:32.569211] : Dataloom[sqlite]: SELECT `completed`, `createdAt`, `id`, `title`, `updatedAt`, `userId` FROM `posts`   ;
[2024-02-05 09:34:32.614135] : Dataloom[sqlite]: DROP TABLE IF EXISTS posts;
[2024-02-05 09:34:32.660182] : Dataloom[sqlite]: CREATE TABLE IF NOT EXISTS `posts` (`completed` BOOLEAN DEFAULT False, `id` INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL, `title` VARCHAR NOT NULL, `createdAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP, `updatedAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP, `userId` INTEGER NOT NULL REFERENCES `users`(`id`) ON DELETE CASCADE ON UPDATE CASCADE);
[2024-02-05 09:34:32.694684] : Dataloom[sqlite]: DROP TABLE IF EXISTS users;
[2024-02-05 09:34:32.731132] : Dataloom[sqlite]: CREATE TABLE IF NOT EXISTS `users` (`id` INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL, `name` TEXT NOT NULL DEFAULT 'Bob', `username` VARCHAR UNIQUE, `createdAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP, `updatedAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP);
[2024-02-05 09:34:32.766140] : Dataloom[sqlite]: SELECT name FROM sqlite_master WHERE type='table';
[2024-02-05 09:34:32.798177] : Dataloom[sqlite]: INSERT INTO `users` (`username`) VALUES (?);
[2024-02-05 09:34:32.831180] : Dataloom[sqlite]: INSERT INTO `posts` (`title`, `userId`) VALUES (?, ?);
[2024-02-05 09:34:32.923140] : Dataloom[sqlite]: UPDATE `users` SET `updatedAt` = ? WHERE `id` = ?;
[2024-02-05 09:34:32.980090] : Dataloom[sqlite]: UPDATE `users` SET `updatedAt` = ? WHERE `id` = ?;
[2024-02-05 09:34:33.022144] : Dataloom[sqlite]: SELECT `createdAt`, `id`, `name`, `updatedAt`, `username` FROM `users` WHERE `id` = ?;
[2024-02-05 09:34:33.071090] : Dataloom[sqlite]: DROP TABLE IF EXISTS posts;
[2024-02-05 09:34:33.124087] : Dataloom[sqlite]: CREATE TABLE IF NOT EXISTS `posts` (`completed` BOOLEAN DEFAULT False, `id` INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL, `title` VARCHAR NOT NULL, `createdAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP, `userId` INTEGER NOT NULL REFERENCES `users`(`id`) ON DELETE CASCADE ON UPDATE CASCADE);
[2024-02-05 09:34:33.173086] : Dataloom[sqlite]: DROP TABLE IF EXISTS users;
[2024-02-05 09:34:33.223092] : Dataloom[sqlite]: CREATE TABLE IF NOT EXISTS `users` (`id` INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL, `name` TEXT NOT NULL DEFAULT 'Bob', `username` VARCHAR UNIQUE, `createdAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP, `updatedAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP);
[2024-02-05 09:34:33.281143] : Dataloom[sqlite]: SELECT name FROM sqlite_master WHERE type='table';
[2024-02-05 09:34:33.330887] : Dataloom[sqlite]: INSERT INTO `users` (`username`) VALUES (?);
[2024-02-05 09:34:33.377884] : Dataloom[sqlite]: INSERT INTO `posts` (`title`, `userId`) VALUES (?, ?);
[2024-02-05 09:34:33.462867] : Dataloom[sqlite]: 
        UPDATE `posts` SET `title` = ? WHERE `id` = (
            SELECT `id` FROM  `posts` WHERE `userId` = ? LIMIT 1
        );
        
[2024-02-05 09:34:33.491953] : Dataloom[sqlite]: 
        UPDATE `posts` SET `title` = ? WHERE `id` = (
            SELECT `id` FROM  `posts` WHERE `userId` = ? LIMIT 1
        );
        
[2024-02-05 09:34:33.513856] : Dataloom[sqlite]: SELECT `completed`, `createdAt`, `id`, `title`, `userId` FROM `posts` WHERE `id` = ?;
[2024-02-05 09:34:33.542042] : Dataloom[sqlite]: DROP TABLE IF EXISTS posts;
[2024-02-05 09:34:33.575784] : Dataloom[sqlite]: CREATE TABLE IF NOT EXISTS `posts` (`completed` BOOLEAN DEFAULT False, `id` INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL, `title` VARCHAR NOT NULL, `createdAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP, `userId` INTEGER NOT NULL REFERENCES `users`(`id`) ON DELETE CASCADE ON UPDATE CASCADE);
[2024-02-05 09:34:33.601087] : Dataloom[sqlite]: DROP TABLE IF EXISTS users;
[2024-02-05 09:34:33.628091] : Dataloom[sqlite]: CREATE TABLE IF NOT EXISTS `users` (`id` INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL, `name` TEXT NOT NULL DEFAULT 'Bob', `username` VARCHAR UNIQUE, `createdAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP, `updatedAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP);
[2024-02-05 09:34:33.654092] : Dataloom[sqlite]: SELECT name FROM sqlite_master WHERE type='table';
[2024-02-05 09:34:33.674082] : Dataloom[sqlite]: INSERT INTO `users` (`username`) VALUES (?);
[2024-02-05 09:34:33.700039] : Dataloom[sqlite]: INSERT INTO `posts` (`title`, `userId`) VALUES (?, ?);
[2024-02-05 09:34:33.799244] : Dataloom[sqlite]: UPDATE `posts` SET `title` = ? WHERE `userId` = ?;
[2024-02-05 09:34:33.857638] : Dataloom[sqlite]: UPDATE `posts` SET `title` = ? WHERE `userId` = ?;
[2024-02-05 09:34:33.892223] : Dataloom[sqlite]: SELECT `completed`, `createdAt`, `id`, `title`, `userId` FROM `posts` WHERE `id` = ?;
[2024-02-05 09:35:44.873739] : Dataloom[postgres]: DROP TABLE IF EXISTS "posts" CASCADE;
[2024-02-05 09:35:44.914035] : Dataloom[postgres]: CREATE TABLE IF NOT EXISTS "posts" ("completed" BOOLEAN DEFAULT False, "id" BIGSERIAL PRIMARY KEY UNIQUE NOT NULL, "title" VARCHAR(255) NOT NULL, "createdAt" TIMESTAMP DEFAULT CURRENT_TIMESTAMP, "updatedAt" TIMESTAMP DEFAULT CURRENT_TIMESTAMP, "userId" BIGSERIAL NOT NULL REFERENCES "users"("id") ON DELETE CASCADE ON UPDATE CASCADE);
[2024-02-05 09:35:44.964028] : Dataloom[postgres]: DROP TABLE IF EXISTS "users" CASCADE;
[2024-02-05 09:35:45.007019] : Dataloom[postgres]: CREATE TABLE IF NOT EXISTS "users" ("id" BIGSERIAL PRIMARY KEY UNIQUE NOT NULL, "name" TEXT NOT NULL DEFAULT 'Bob', "username" VARCHAR(255) UNIQUE);
[2024-02-05 09:35:45.064024] : Dataloom[postgres]: SELECT tablename FROM pg_catalog.pg_tables WHERE schemaname='public';
[2024-02-05 09:35:45.113122] : Dataloom[postgres]: INSERT INTO "users" ("username") VALUES (%s) RETURNING "id";
[2024-02-05 09:35:45.147173] : Dataloom[postgres]: INSERT INTO "posts" ("title", "userId") VALUES (%s, %s) RETURNING *;
[2024-02-05 09:35:45.179261] : Dataloom[postgres]: 
        SELECT 
            parent.id AS "posts_id", parent.completed AS "posts_completed", parent.title AS "posts_title",
            child_user.id AS "users_id", child_user.username AS "users_username"
        FROM 
            posts parent
        JOIN users child_user ON parent."userId" = child_user.id 
        WHERE 
            parent."id" = %s;
    
[2024-02-05 09:48:54.037595] : Dataloom[postgres]: DROP TABLE IF EXISTS "posts" CASCADE;
[2024-02-05 09:48:54.068796] : Dataloom[postgres]: CREATE TABLE IF NOT EXISTS "posts" ("completed" BOOLEAN DEFAULT False, "id" BIGSERIAL PRIMARY KEY UNIQUE NOT NULL, "title" VARCHAR(255) NOT NULL, "createdAt" TIMESTAMP DEFAULT CURRENT_TIMESTAMP, "updatedAt" TIMESTAMP DEFAULT CURRENT_TIMESTAMP, "userId" BIGSERIAL NOT NULL REFERENCES "users"("id") ON DELETE CASCADE ON UPDATE CASCADE);
[2024-02-05 09:48:54.109418] : Dataloom[postgres]: DROP TABLE IF EXISTS "users" CASCADE;
[2024-02-05 09:48:54.140418] : Dataloom[postgres]: CREATE TABLE IF NOT EXISTS "users" ("id" BIGSERIAL PRIMARY KEY UNIQUE NOT NULL, "name" TEXT NOT NULL DEFAULT 'Bob', "username" VARCHAR(255) UNIQUE);
[2024-02-05 09:48:54.171445] : Dataloom[postgres]: SELECT tablename FROM pg_catalog.pg_tables WHERE schemaname='public';
[2024-02-05 09:48:54.204420] : Dataloom[postgres]: INSERT INTO "users" ("username") VALUES (%s) RETURNING "id";
[2024-02-05 09:48:54.227418] : Dataloom[postgres]: INSERT INTO "posts" ("title", "userId") VALUES (%s, %s) RETURNING *;
[2024-02-05 09:48:54.252417] : Dataloom[postgres]: 
        SELECT 
            parent.id AS "posts_id", parent.completed AS "posts_completed", parent.title AS "posts_title",
            child_user.id AS "users_id", child_user.username AS "users_username"
        FROM 
            posts parent
        JOIN users child_user ON parent."userId" = child_user.id 
        WHERE 
            parent."id" = %s;
    
[2024-02-05 09:50:55.846851] : Dataloom[postgres]: DROP TABLE IF EXISTS "posts" CASCADE;
[2024-02-05 09:50:55.877890] : Dataloom[postgres]: CREATE TABLE IF NOT EXISTS "posts" ("completed" BOOLEAN DEFAULT False, "id" BIGSERIAL PRIMARY KEY UNIQUE NOT NULL, "title" VARCHAR(255) NOT NULL, "createdAt" TIMESTAMP DEFAULT CURRENT_TIMESTAMP, "updatedAt" TIMESTAMP DEFAULT CURRENT_TIMESTAMP, "userId" BIGSERIAL NOT NULL REFERENCES "users"("id") ON DELETE CASCADE ON UPDATE CASCADE);
[2024-02-05 09:50:55.919921] : Dataloom[postgres]: DROP TABLE IF EXISTS "users" CASCADE;
[2024-02-05 09:50:55.953427] : Dataloom[postgres]: CREATE TABLE IF NOT EXISTS "users" ("id" BIGSERIAL PRIMARY KEY UNIQUE NOT NULL, "name" TEXT NOT NULL DEFAULT 'Bob', "username" VARCHAR(255) UNIQUE);
[2024-02-05 09:50:55.987461] : Dataloom[postgres]: SELECT tablename FROM pg_catalog.pg_tables WHERE schemaname='public';
[2024-02-05 09:50:56.022421] : Dataloom[postgres]: INSERT INTO "users" ("username") VALUES (%s) RETURNING "id";
[2024-02-05 09:50:56.051581] : Dataloom[postgres]: INSERT INTO "posts" ("title", "userId") VALUES (%s, %s) RETURNING *;
[2024-02-05 09:50:56.081560] : Dataloom[postgres]: 
        SELECT 
            parent.id AS "posts_id", parent.completed AS "posts_completed", parent.title AS "posts_title",
            child_user.id AS "users_id", child_user.username AS "users_username"
        FROM 
            posts parent
        JOIN users child_user ON parent."userId" = child_user.id 
        WHERE 
            parent."id" = %s;
    
[2024-02-05 09:51:56.649775] : Dataloom[postgres]: DROP TABLE IF EXISTS "posts" CASCADE;
[2024-02-05 09:51:56.702730] : Dataloom[postgres]: CREATE TABLE IF NOT EXISTS "posts" ("completed" BOOLEAN DEFAULT False, "id" BIGSERIAL PRIMARY KEY UNIQUE NOT NULL, "title" VARCHAR(255) NOT NULL, "createdAt" TIMESTAMP DEFAULT CURRENT_TIMESTAMP, "updatedAt" TIMESTAMP DEFAULT CURRENT_TIMESTAMP, "userId" BIGSERIAL NOT NULL REFERENCES "users"("id") ON DELETE CASCADE ON UPDATE CASCADE);
[2024-02-05 09:51:56.762318] : Dataloom[postgres]: DROP TABLE IF EXISTS "users" CASCADE;
[2024-02-05 09:51:56.813309] : Dataloom[postgres]: CREATE TABLE IF NOT EXISTS "users" ("id" BIGSERIAL PRIMARY KEY UNIQUE NOT NULL, "name" TEXT NOT NULL DEFAULT 'Bob', "username" VARCHAR(255) UNIQUE);
[2024-02-05 09:51:56.875643] : Dataloom[postgres]: SELECT tablename FROM pg_catalog.pg_tables WHERE schemaname='public';
[2024-02-05 09:51:56.925629] : Dataloom[postgres]: INSERT INTO "users" ("username") VALUES (%s) RETURNING "id";
[2024-02-05 09:51:56.965317] : Dataloom[postgres]: INSERT INTO "posts" ("title", "userId") VALUES (%s, %s) RETURNING *;
[2024-02-05 09:51:57.012407] : Dataloom[postgres]: 
        SELECT 
            parent.id AS "posts_id", parent.completed AS "posts_completed", parent.title AS "posts_title",
            child_user.id AS "users_id", child_user.username AS "users_username"
        FROM 
            posts parent
        JOIN users child_user ON parent."userId" = child_user.id 
        WHERE 
            parent."id" = %s;
    
[2024-02-05 09:53:45.029963] : Dataloom[postgres]: DROP TABLE IF EXISTS "posts" CASCADE;
[2024-02-05 09:53:45.093294] : Dataloom[postgres]: CREATE TABLE IF NOT EXISTS "posts" ("completed" BOOLEAN DEFAULT False, "id" BIGSERIAL PRIMARY KEY UNIQUE NOT NULL, "title" VARCHAR(255) NOT NULL, "createdAt" TIMESTAMP DEFAULT CURRENT_TIMESTAMP, "updatedAt" TIMESTAMP DEFAULT CURRENT_TIMESTAMP, "userId" BIGSERIAL NOT NULL REFERENCES "users"("id") ON DELETE CASCADE ON UPDATE CASCADE);
[2024-02-05 09:53:45.169873] : Dataloom[postgres]: DROP TABLE IF EXISTS "users" CASCADE;
[2024-02-05 09:53:45.228384] : Dataloom[postgres]: CREATE TABLE IF NOT EXISTS "users" ("id" BIGSERIAL PRIMARY KEY UNIQUE NOT NULL, "name" TEXT NOT NULL DEFAULT 'Bob', "username" VARCHAR(255) UNIQUE);
[2024-02-05 09:53:45.290748] : Dataloom[postgres]: SELECT tablename FROM pg_catalog.pg_tables WHERE schemaname='public';
[2024-02-05 09:53:45.363094] : Dataloom[postgres]: INSERT INTO "users" ("username") VALUES (%s) RETURNING "id";
[2024-02-05 09:53:45.410566] : Dataloom[postgres]: INSERT INTO "posts" ("title", "userId") VALUES (%s, %s) RETURNING *;
[2024-02-05 09:53:45.457281] : Dataloom[postgres]: 
        SELECT 
            parent.id AS "posts_id", parent.completed AS "posts_completed", parent.title AS "posts_title",
            child_user.id AS "users_id", child_user.username AS "users_username"
        FROM 
            posts parent
        JOIN users child_user ON parent."userId" = child_user.id 
        WHERE 
            parent."id" = %s;
    
[2024-02-05 09:54:25.514580] : Dataloom[postgres]: DROP TABLE IF EXISTS "posts" CASCADE;
[2024-02-05 09:54:25.562255] : Dataloom[postgres]: CREATE TABLE IF NOT EXISTS "posts" ("completed" BOOLEAN DEFAULT False, "id" BIGSERIAL PRIMARY KEY UNIQUE NOT NULL, "title" VARCHAR(255) NOT NULL, "createdAt" TIMESTAMP DEFAULT CURRENT_TIMESTAMP, "updatedAt" TIMESTAMP DEFAULT CURRENT_TIMESTAMP, "userId" BIGSERIAL NOT NULL REFERENCES "users"("id") ON DELETE CASCADE ON UPDATE CASCADE);
[2024-02-05 09:54:25.612579] : Dataloom[postgres]: DROP TABLE IF EXISTS "users" CASCADE;
[2024-02-05 09:54:25.652302] : Dataloom[postgres]: CREATE TABLE IF NOT EXISTS "users" ("id" BIGSERIAL PRIMARY KEY UNIQUE NOT NULL, "name" TEXT NOT NULL DEFAULT 'Bob', "username" VARCHAR(255) UNIQUE);
[2024-02-05 09:54:25.693302] : Dataloom[postgres]: SELECT tablename FROM pg_catalog.pg_tables WHERE schemaname='public';
[2024-02-05 09:54:25.731301] : Dataloom[postgres]: INSERT INTO "users" ("username") VALUES (%s) RETURNING "id";
[2024-02-05 09:54:25.763788] : Dataloom[postgres]: INSERT INTO "posts" ("title", "userId") VALUES (%s, %s) RETURNING *;
[2024-02-05 09:54:25.799988] : Dataloom[postgres]: 
        SELECT 
            parent.id AS "posts_id", parent.completed AS "posts_completed", parent.title AS "posts_title",
            child_user.id AS "users_id", child_user.username AS "users_username"
        FROM 
            posts parent
        JOIN users child_user ON parent."userId" = child_user.id 
        WHERE 
            parent."id" = %s;
    
[2024-02-05 09:54:55.474575] : Dataloom[postgres]: DROP TABLE IF EXISTS "posts" CASCADE;
[2024-02-05 09:54:55.539459] : Dataloom[postgres]: CREATE TABLE IF NOT EXISTS "posts" ("completed" BOOLEAN DEFAULT False, "id" BIGSERIAL PRIMARY KEY UNIQUE NOT NULL, "title" VARCHAR(255) NOT NULL, "createdAt" TIMESTAMP DEFAULT CURRENT_TIMESTAMP, "updatedAt" TIMESTAMP DEFAULT CURRENT_TIMESTAMP, "userId" BIGSERIAL NOT NULL REFERENCES "users"("id") ON DELETE CASCADE ON UPDATE CASCADE);
[2024-02-05 09:54:55.613029] : Dataloom[postgres]: DROP TABLE IF EXISTS "users" CASCADE;
[2024-02-05 09:54:55.691284] : Dataloom[postgres]: CREATE TABLE IF NOT EXISTS "users" ("id" BIGSERIAL PRIMARY KEY UNIQUE NOT NULL, "name" TEXT NOT NULL DEFAULT 'Bob', "username" VARCHAR(255) UNIQUE);
[2024-02-05 09:54:55.756282] : Dataloom[postgres]: SELECT tablename FROM pg_catalog.pg_tables WHERE schemaname='public';
[2024-02-05 09:54:55.808286] : Dataloom[postgres]: INSERT INTO "users" ("username") VALUES (%s) RETURNING "id";
[2024-02-05 09:54:55.873490] : Dataloom[postgres]: INSERT INTO "posts" ("title", "userId") VALUES (%s, %s) RETURNING *;
[2024-02-05 09:54:55.908286] : Dataloom[postgres]: 
        SELECT 
            parent.id AS "posts_id", parent.completed AS "posts_completed", parent.title AS "posts_title",
            child_user.id AS "users_id", child_user.username AS "users_username"
        FROM 
            posts parent
        JOIN users child_user ON parent."userId" = child_user.id 
        WHERE 
            parent."id" = %s;
    
[2024-02-05 09:55:55.039401] : Dataloom[postgres]: DROP TABLE IF EXISTS "posts" CASCADE;
[2024-02-05 09:55:55.116412] : Dataloom[postgres]: CREATE TABLE IF NOT EXISTS "posts" ("completed" BOOLEAN DEFAULT False, "id" BIGSERIAL PRIMARY KEY UNIQUE NOT NULL, "title" VARCHAR(255) NOT NULL, "createdAt" TIMESTAMP DEFAULT CURRENT_TIMESTAMP, "updatedAt" TIMESTAMP DEFAULT CURRENT_TIMESTAMP, "userId" BIGSERIAL NOT NULL REFERENCES "users"("id") ON DELETE CASCADE ON UPDATE CASCADE);
[2024-02-05 09:55:55.189408] : Dataloom[postgres]: DROP TABLE IF EXISTS "users" CASCADE;
[2024-02-05 09:55:55.273405] : Dataloom[postgres]: CREATE TABLE IF NOT EXISTS "users" ("id" BIGSERIAL PRIMARY KEY UNIQUE NOT NULL, "name" TEXT NOT NULL DEFAULT 'Bob', "username" VARCHAR(255) UNIQUE);
[2024-02-05 09:55:55.316409] : Dataloom[postgres]: SELECT tablename FROM pg_catalog.pg_tables WHERE schemaname='public';
[2024-02-05 09:55:55.357944] : Dataloom[postgres]: INSERT INTO "users" ("username") VALUES (%s) RETURNING "id";
[2024-02-05 09:55:55.391943] : Dataloom[postgres]: INSERT INTO "posts" ("title", "userId") VALUES (%s, %s) RETURNING *;
[2024-02-05 09:55:55.417946] : Dataloom[postgres]: 
        SELECT 
            parent.id AS "posts_id", parent.completed AS "posts_completed", parent.title AS "posts_title",
            child_user.id AS "users_id", child_user.username AS "users_username"
        FROM 
            posts parent
        JOIN users child_user ON parent."userId" = child_user.id 
        WHERE 
            parent."id" = %s;
    
[2024-02-05 09:56:26.227253] : Dataloom[postgres]: DROP TABLE IF EXISTS "posts" CASCADE;
[2024-02-05 09:56:26.278981] : Dataloom[postgres]: CREATE TABLE IF NOT EXISTS "posts" ("completed" BOOLEAN DEFAULT False, "id" BIGSERIAL PRIMARY KEY UNIQUE NOT NULL, "title" VARCHAR(255) NOT NULL, "createdAt" TIMESTAMP DEFAULT CURRENT_TIMESTAMP, "updatedAt" TIMESTAMP DEFAULT CURRENT_TIMESTAMP, "userId" BIGSERIAL NOT NULL REFERENCES "users"("id") ON DELETE CASCADE ON UPDATE CASCADE);
[2024-02-05 09:56:26.340569] : Dataloom[postgres]: DROP TABLE IF EXISTS "users" CASCADE;
[2024-02-05 09:56:26.392534] : Dataloom[postgres]: CREATE TABLE IF NOT EXISTS "users" ("id" BIGSERIAL PRIMARY KEY UNIQUE NOT NULL, "name" TEXT NOT NULL DEFAULT 'Bob', "username" VARCHAR(255) UNIQUE);
[2024-02-05 09:56:26.450527] : Dataloom[postgres]: SELECT tablename FROM pg_catalog.pg_tables WHERE schemaname='public';
[2024-02-05 09:56:26.538528] : Dataloom[postgres]: INSERT INTO "users" ("username") VALUES (%s) RETURNING "id";
[2024-02-05 09:56:26.595529] : Dataloom[postgres]: INSERT INTO "posts" ("title", "userId") VALUES (%s, %s) RETURNING *;
[2024-02-05 09:56:26.631528] : Dataloom[postgres]: 
        SELECT 
            parent.id AS "posts_id", parent.completed AS "posts_completed", parent.title AS "posts_title",
            child_user.id AS "users_id", child_user.username AS "users_username"
        FROM 
            posts parent
        JOIN users child_user ON parent."userId" = child_user.id 
        WHERE 
            parent."id" = %s;
    
[2024-02-05 09:56:39.938544] : Dataloom[postgres]: DROP TABLE IF EXISTS "posts" CASCADE;
[2024-02-05 09:56:39.978542] : Dataloom[postgres]: CREATE TABLE IF NOT EXISTS "posts" ("completed" BOOLEAN DEFAULT False, "id" BIGSERIAL PRIMARY KEY UNIQUE NOT NULL, "title" VARCHAR(255) NOT NULL, "createdAt" TIMESTAMP DEFAULT CURRENT_TIMESTAMP, "updatedAt" TIMESTAMP DEFAULT CURRENT_TIMESTAMP, "userId" BIGSERIAL NOT NULL REFERENCES "users"("id") ON DELETE CASCADE ON UPDATE CASCADE);
[2024-02-05 09:56:40.027548] : Dataloom[postgres]: DROP TABLE IF EXISTS "users" CASCADE;
[2024-02-05 09:56:40.068197] : Dataloom[postgres]: CREATE TABLE IF NOT EXISTS "users" ("id" BIGSERIAL PRIMARY KEY UNIQUE NOT NULL, "name" TEXT NOT NULL DEFAULT 'Bob', "username" VARCHAR(255) UNIQUE);
[2024-02-05 09:56:40.110208] : Dataloom[postgres]: SELECT tablename FROM pg_catalog.pg_tables WHERE schemaname='public';
[2024-02-05 09:56:40.149005] : Dataloom[postgres]: INSERT INTO "users" ("username") VALUES (%s) RETURNING "id";
[2024-02-05 09:56:40.180004] : Dataloom[postgres]: INSERT INTO "posts" ("title", "userId") VALUES (%s, %s) RETURNING *;
[2024-02-05 09:56:40.215006] : Dataloom[postgres]: 
        SELECT 
            parent.id AS "posts_id", parent.completed AS "posts_completed", parent.title AS "posts_title",
            child_user.id AS "users_id", child_user.username AS "users_username"
        FROM 
            posts parent
        JOIN users child_user ON parent."userId" = child_user.id 
        WHERE 
            parent."id" = %s;
    
[2024-02-05 09:57:17.744208] : Dataloom[postgres]: DROP TABLE IF EXISTS "posts" CASCADE;
[2024-02-05 09:57:17.783268] : Dataloom[postgres]: CREATE TABLE IF NOT EXISTS "posts" ("completed" BOOLEAN DEFAULT False, "id" BIGSERIAL PRIMARY KEY UNIQUE NOT NULL, "title" VARCHAR(255) NOT NULL, "createdAt" TIMESTAMP DEFAULT CURRENT_TIMESTAMP, "updatedAt" TIMESTAMP DEFAULT CURRENT_TIMESTAMP, "userId" BIGSERIAL NOT NULL REFERENCES "users"("id") ON DELETE CASCADE ON UPDATE CASCADE);
[2024-02-05 09:57:17.826050] : Dataloom[postgres]: DROP TABLE IF EXISTS "users" CASCADE;
[2024-02-05 09:57:17.864000] : Dataloom[postgres]: CREATE TABLE IF NOT EXISTS "users" ("id" BIGSERIAL PRIMARY KEY UNIQUE NOT NULL, "name" TEXT NOT NULL DEFAULT 'Bob', "username" VARCHAR(255) UNIQUE);
[2024-02-05 09:57:17.904035] : Dataloom[postgres]: SELECT tablename FROM pg_catalog.pg_tables WHERE schemaname='public';
[2024-02-05 09:57:17.945052] : Dataloom[postgres]: INSERT INTO "users" ("username") VALUES (%s) RETURNING "id";
[2024-02-05 09:57:17.977012] : Dataloom[postgres]: INSERT INTO "posts" ("title", "userId") VALUES (%s, %s) RETURNING *;
[2024-02-05 09:57:18.009055] : Dataloom[postgres]: 
        SELECT 
            parent.id AS "posts_id", parent.completed AS "posts_completed", parent.title AS "posts_title",
            child_user.id AS "users_id", child_user.username AS "users_username"
        FROM 
            posts parent
        JOIN users child_user ON parent."userId" = child_user.id 
        WHERE 
            parent."id" = %s;
    
[2024-02-05 09:57:32.971944] : Dataloom[postgres]: DROP TABLE IF EXISTS "posts" CASCADE;
[2024-02-05 09:57:33.011612] : Dataloom[postgres]: CREATE TABLE IF NOT EXISTS "posts" ("completed" BOOLEAN DEFAULT False, "id" BIGSERIAL PRIMARY KEY UNIQUE NOT NULL, "title" VARCHAR(255) NOT NULL, "createdAt" TIMESTAMP DEFAULT CURRENT_TIMESTAMP, "updatedAt" TIMESTAMP DEFAULT CURRENT_TIMESTAMP, "userId" BIGSERIAL NOT NULL REFERENCES "users"("id") ON DELETE CASCADE ON UPDATE CASCADE);
[2024-02-05 09:57:33.061338] : Dataloom[postgres]: DROP TABLE IF EXISTS "users" CASCADE;
[2024-02-05 09:57:33.099767] : Dataloom[postgres]: CREATE TABLE IF NOT EXISTS "users" ("id" BIGSERIAL PRIMARY KEY UNIQUE NOT NULL, "name" TEXT NOT NULL DEFAULT 'Bob', "username" VARCHAR(255) UNIQUE);
[2024-02-05 09:57:33.139046] : Dataloom[postgres]: SELECT tablename FROM pg_catalog.pg_tables WHERE schemaname='public';
[2024-02-05 09:57:33.176954] : Dataloom[postgres]: INSERT INTO "users" ("username") VALUES (%s) RETURNING "id";
[2024-02-05 09:57:33.206794] : Dataloom[postgres]: INSERT INTO "posts" ("title", "userId") VALUES (%s, %s) RETURNING *;
[2024-02-05 09:57:33.241831] : Dataloom[postgres]: 
        SELECT 
            parent.id AS "posts_id", parent.completed AS "posts_completed", parent.title AS "posts_title",
            child_user.id AS "users_id", child_user.username AS "users_username"
        FROM 
            posts parent
        JOIN users child_user ON parent."userId" = child_user.id 
        WHERE 
            parent."id" = %s;
    
[2024-02-05 09:57:41.456761] : Dataloom[postgres]: DROP TABLE IF EXISTS "posts" CASCADE;
[2024-02-05 09:57:41.500724] : Dataloom[postgres]: CREATE TABLE IF NOT EXISTS "posts" ("completed" BOOLEAN DEFAULT False, "id" BIGSERIAL PRIMARY KEY UNIQUE NOT NULL, "title" VARCHAR(255) NOT NULL, "createdAt" TIMESTAMP DEFAULT CURRENT_TIMESTAMP, "updatedAt" TIMESTAMP DEFAULT CURRENT_TIMESTAMP, "userId" BIGSERIAL NOT NULL REFERENCES "users"("id") ON DELETE CASCADE ON UPDATE CASCADE);
[2024-02-05 09:57:41.547755] : Dataloom[postgres]: DROP TABLE IF EXISTS "users" CASCADE;
[2024-02-05 09:57:41.585534] : Dataloom[postgres]: CREATE TABLE IF NOT EXISTS "users" ("id" BIGSERIAL PRIMARY KEY UNIQUE NOT NULL, "name" TEXT NOT NULL DEFAULT 'Bob', "username" VARCHAR(255) UNIQUE);
[2024-02-05 09:57:41.624575] : Dataloom[postgres]: SELECT tablename FROM pg_catalog.pg_tables WHERE schemaname='public';
[2024-02-05 09:57:41.663571] : Dataloom[postgres]: INSERT INTO "users" ("username") VALUES (%s) RETURNING "id";
[2024-02-05 09:57:41.703610] : Dataloom[postgres]: INSERT INTO "posts" ("title", "userId") VALUES (%s, %s) RETURNING *;
[2024-02-05 09:57:41.740131] : Dataloom[postgres]: 
        SELECT 
            parent.id AS "posts_id", parent.completed AS "posts_completed", parent.title AS "posts_title",
            child_user.id AS "users_id", child_user.username AS "users_username"
        FROM 
            posts parent
        JOIN users child_user ON parent."userId" = child_user.id 
        WHERE 
            parent."id" = %s;
    
[2024-02-05 09:58:04.677728] : Dataloom[postgres]: DROP TABLE IF EXISTS "posts" CASCADE;
[2024-02-05 09:58:04.713807] : Dataloom[postgres]: CREATE TABLE IF NOT EXISTS "posts" ("completed" BOOLEAN DEFAULT False, "id" BIGSERIAL PRIMARY KEY UNIQUE NOT NULL, "title" VARCHAR(255) NOT NULL, "createdAt" TIMESTAMP DEFAULT CURRENT_TIMESTAMP, "updatedAt" TIMESTAMP DEFAULT CURRENT_TIMESTAMP, "userId" BIGSERIAL NOT NULL REFERENCES "users"("id") ON DELETE CASCADE ON UPDATE CASCADE);
[2024-02-05 09:58:04.756666] : Dataloom[postgres]: DROP TABLE IF EXISTS "users" CASCADE;
[2024-02-05 09:58:04.791679] : Dataloom[postgres]: CREATE TABLE IF NOT EXISTS "users" ("id" BIGSERIAL PRIMARY KEY UNIQUE NOT NULL, "name" TEXT NOT NULL DEFAULT 'Bob', "username" VARCHAR(255) UNIQUE);
[2024-02-05 09:58:04.825865] : Dataloom[postgres]: SELECT tablename FROM pg_catalog.pg_tables WHERE schemaname='public';
[2024-02-05 09:58:04.860668] : Dataloom[postgres]: INSERT INTO "users" ("username") VALUES (%s) RETURNING "id";
[2024-02-05 09:58:04.886665] : Dataloom[postgres]: INSERT INTO "posts" ("title", "userId") VALUES (%s, %s) RETURNING *;
[2024-02-05 09:58:04.913366] : Dataloom[postgres]: 
        SELECT 
            parent.id AS "posts_id", parent.completed AS "posts_completed", parent.title AS "posts_title",
            child_user.id AS "users_id", child_user.username AS "users_username"
        FROM 
            posts parent
        JOIN users child_user ON parent."userId" = child_user.id 
        WHERE 
            parent."id" = %s;
    
[2024-02-05 10:00:58.645911] : Dataloom[postgres]: DROP TABLE IF EXISTS "posts" CASCADE;
[2024-02-05 10:00:58.682655] : Dataloom[postgres]: CREATE TABLE IF NOT EXISTS "posts" ("completed" BOOLEAN DEFAULT False, "id" BIGSERIAL PRIMARY KEY UNIQUE NOT NULL, "title" VARCHAR(255) NOT NULL, "createdAt" TIMESTAMP DEFAULT CURRENT_TIMESTAMP, "updatedAt" TIMESTAMP DEFAULT CURRENT_TIMESTAMP, "userId" BIGSERIAL NOT NULL REFERENCES "users"("id") ON DELETE CASCADE ON UPDATE CASCADE);
[2024-02-05 10:00:58.720190] : Dataloom[postgres]: DROP TABLE IF EXISTS "users" CASCADE;
[2024-02-05 10:00:58.769195] : Dataloom[postgres]: CREATE TABLE IF NOT EXISTS "users" ("id" BIGSERIAL PRIMARY KEY UNIQUE NOT NULL, "name" TEXT NOT NULL DEFAULT 'Bob', "username" VARCHAR(255) UNIQUE);
[2024-02-05 10:00:58.835181] : Dataloom[postgres]: SELECT tablename FROM pg_catalog.pg_tables WHERE schemaname='public';
[2024-02-05 10:00:58.896131] : Dataloom[postgres]: INSERT INTO "users" ("username") VALUES (%s) RETURNING "id";
[2024-02-05 10:00:58.949223] : Dataloom[postgres]: INSERT INTO "posts" ("title", "userId") VALUES (%s, %s) RETURNING *;
[2024-02-05 10:00:58.999121] : Dataloom[postgres]: 
        SELECT 
            parent.id AS "posts_id", parent.completed AS "posts_completed", parent.title AS "posts_title",
            child_user.id AS "users_id", child_user.username AS "users_username"
        FROM 
            posts parent
        JOIN users child_user ON parent."userId" = child_user.id 
        WHERE 
            parent."id" = %s;
    
[2024-02-05 10:01:55.721670] : Dataloom[postgres]: DROP TABLE IF EXISTS "posts" CASCADE;
[2024-02-05 10:01:55.762704] : Dataloom[postgres]: CREATE TABLE IF NOT EXISTS "posts" ("completed" BOOLEAN DEFAULT False, "id" BIGSERIAL PRIMARY KEY UNIQUE NOT NULL, "title" VARCHAR(255) NOT NULL, "createdAt" TIMESTAMP DEFAULT CURRENT_TIMESTAMP, "updatedAt" TIMESTAMP DEFAULT CURRENT_TIMESTAMP, "userId" BIGSERIAL NOT NULL REFERENCES "users"("id") ON DELETE CASCADE ON UPDATE CASCADE);
[2024-02-05 10:01:55.813666] : Dataloom[postgres]: DROP TABLE IF EXISTS "users" CASCADE;
[2024-02-05 10:01:55.849667] : Dataloom[postgres]: CREATE TABLE IF NOT EXISTS "users" ("id" BIGSERIAL PRIMARY KEY UNIQUE NOT NULL, "name" TEXT NOT NULL DEFAULT 'Bob', "username" VARCHAR(255) UNIQUE);
[2024-02-05 10:01:55.890667] : Dataloom[postgres]: SELECT tablename FROM pg_catalog.pg_tables WHERE schemaname='public';
[2024-02-05 10:01:55.933705] : Dataloom[postgres]: INSERT INTO "users" ("username") VALUES (%s) RETURNING "id";
[2024-02-05 10:01:55.965708] : Dataloom[postgres]: INSERT INTO "posts" ("title", "userId") VALUES (%s, %s) RETURNING *;
[2024-02-05 10:01:55.996704] : Dataloom[postgres]: 
        SELECT 
            parent.id AS "posts_id", parent.completed AS "posts_completed", parent.title AS "posts_title",
            child_user.id AS "users_id", child_user.username AS "users_username"
        FROM 
            posts parent
        JOIN users child_user ON parent."userId" = child_user.id 
        WHERE 
            parent."id" = %s;
    
[2024-02-05 10:08:51.476789] : Dataloom[postgres]: DROP TABLE IF EXISTS "posts" CASCADE;
[2024-02-05 10:08:51.511823] : Dataloom[postgres]: CREATE TABLE IF NOT EXISTS "posts" ("completed" BOOLEAN DEFAULT False, "id" BIGSERIAL PRIMARY KEY UNIQUE NOT NULL, "title" VARCHAR(255) NOT NULL, "createdAt" TIMESTAMP DEFAULT CURRENT_TIMESTAMP, "updatedAt" TIMESTAMP DEFAULT CURRENT_TIMESTAMP, "userId" BIGSERIAL NOT NULL REFERENCES "users"("id") ON DELETE CASCADE ON UPDATE CASCADE);
[2024-02-05 10:08:51.549841] : Dataloom[postgres]: DROP TABLE IF EXISTS "users" CASCADE;
[2024-02-05 10:08:51.593795] : Dataloom[postgres]: CREATE TABLE IF NOT EXISTS "users" ("id" BIGSERIAL PRIMARY KEY UNIQUE NOT NULL, "name" TEXT NOT NULL DEFAULT 'Bob', "username" VARCHAR(255) UNIQUE);
[2024-02-05 10:08:51.630790] : Dataloom[postgres]: SELECT tablename FROM pg_catalog.pg_tables WHERE schemaname='public';
[2024-02-05 10:08:51.667790] : Dataloom[postgres]: INSERT INTO "users" ("username") VALUES (%s) RETURNING "id";
[2024-02-05 10:08:51.695239] : Dataloom[postgres]: INSERT INTO "posts" ("title", "userId") VALUES (%s, %s) RETURNING *;
[2024-02-05 10:08:51.727793] : Dataloom[postgres]: 
        SELECT 
            parent.id AS "posts_id", parent.completed AS "posts_completed", parent.title AS "posts_title",
            child_user.id AS "users_id", child_user.username AS "users_username"
        FROM 
            posts parent
        JOIN users child_user ON parent."userId" = child_user.id 
        WHERE 
            parent."id" = %s;
    
[2024-02-05 10:11:55.468415] : Dataloom[postgres]: DROP TABLE IF EXISTS "posts" CASCADE;
[2024-02-05 10:11:55.510383] : Dataloom[postgres]: CREATE TABLE IF NOT EXISTS "posts" ("completed" BOOLEAN DEFAULT False, "id" BIGSERIAL PRIMARY KEY UNIQUE NOT NULL, "title" VARCHAR(255) NOT NULL, "createdAt" TIMESTAMP DEFAULT CURRENT_TIMESTAMP, "updatedAt" TIMESTAMP DEFAULT CURRENT_TIMESTAMP, "userId" BIGSERIAL NOT NULL REFERENCES "users"("id") ON DELETE CASCADE ON UPDATE CASCADE);
[2024-02-05 10:11:55.561380] : Dataloom[postgres]: DROP TABLE IF EXISTS "users" CASCADE;
[2024-02-05 10:11:55.603963] : Dataloom[postgres]: CREATE TABLE IF NOT EXISTS "users" ("id" BIGSERIAL PRIMARY KEY UNIQUE NOT NULL, "name" TEXT NOT NULL DEFAULT 'Bob', "username" VARCHAR(255) UNIQUE);
[2024-02-05 10:11:55.650965] : Dataloom[postgres]: SELECT tablename FROM pg_catalog.pg_tables WHERE schemaname='public';
[2024-02-05 10:11:55.695464] : Dataloom[postgres]: INSERT INTO "users" ("username") VALUES (%s) RETURNING "id";
[2024-02-05 10:11:55.733059] : Dataloom[postgres]: INSERT INTO "posts" ("title", "userId") VALUES (%s, %s) RETURNING *;
[2024-02-05 10:11:55.768459] : Dataloom[postgres]: 
        SELECT 
            parent.id AS "posts_id", parent.completed AS "posts_completed", parent.title AS "posts_title",
            child_user.id AS "users_id", child_user.username AS "users_username"
        FROM 
            posts parent
        JOIN users child_user ON parent."userId" = child_user.id 
        WHERE 
            parent."id" = %s;
    
[2024-02-05 10:12:53.962629] : Dataloom[postgres]: DROP TABLE IF EXISTS "posts" CASCADE;
[2024-02-05 10:12:53.993590] : Dataloom[postgres]: CREATE TABLE IF NOT EXISTS "posts" ("completed" BOOLEAN DEFAULT False, "id" BIGSERIAL PRIMARY KEY UNIQUE NOT NULL, "title" VARCHAR(255) NOT NULL, "createdAt" TIMESTAMP DEFAULT CURRENT_TIMESTAMP, "updatedAt" TIMESTAMP DEFAULT CURRENT_TIMESTAMP, "userId" BIGSERIAL NOT NULL REFERENCES "users"("id") ON DELETE CASCADE ON UPDATE CASCADE);
[2024-02-05 10:12:54.033634] : Dataloom[postgres]: DROP TABLE IF EXISTS "users" CASCADE;
[2024-02-05 10:12:54.067687] : Dataloom[postgres]: CREATE TABLE IF NOT EXISTS "users" ("id" BIGSERIAL PRIMARY KEY UNIQUE NOT NULL, "name" TEXT NOT NULL DEFAULT 'Bob', "username" VARCHAR(255) UNIQUE);
[2024-02-05 10:12:54.100702] : Dataloom[postgres]: SELECT tablename FROM pg_catalog.pg_tables WHERE schemaname='public';
[2024-02-05 10:12:54.131655] : Dataloom[postgres]: INSERT INTO "users" ("username") VALUES (%s) RETURNING "id";
[2024-02-05 10:12:54.154239] : Dataloom[postgres]: INSERT INTO "posts" ("title", "userId") VALUES (%s, %s) RETURNING *;
[2024-02-05 10:13:13.760440] : Dataloom[postgres]: DROP TABLE IF EXISTS "posts" CASCADE;
[2024-02-05 10:13:13.816402] : Dataloom[postgres]: CREATE TABLE IF NOT EXISTS "posts" ("completed" BOOLEAN DEFAULT False, "id" BIGSERIAL PRIMARY KEY UNIQUE NOT NULL, "title" VARCHAR(255) NOT NULL, "createdAt" TIMESTAMP DEFAULT CURRENT_TIMESTAMP, "updatedAt" TIMESTAMP DEFAULT CURRENT_TIMESTAMP, "userId" BIGSERIAL NOT NULL REFERENCES "users"("id") ON DELETE CASCADE ON UPDATE CASCADE);
[2024-02-05 10:13:13.898411] : Dataloom[postgres]: DROP TABLE IF EXISTS "users" CASCADE;
[2024-02-05 10:13:13.961647] : Dataloom[postgres]: CREATE TABLE IF NOT EXISTS "users" ("id" BIGSERIAL PRIMARY KEY UNIQUE NOT NULL, "name" TEXT NOT NULL DEFAULT 'Bob', "username" VARCHAR(255) UNIQUE);
[2024-02-05 10:13:14.027056] : Dataloom[postgres]: SELECT tablename FROM pg_catalog.pg_tables WHERE schemaname='public';
[2024-02-05 10:13:14.095054] : Dataloom[postgres]: INSERT INTO "users" ("username") VALUES (%s) RETURNING "id";
[2024-02-05 10:13:14.148495] : Dataloom[postgres]: INSERT INTO "posts" ("title", "userId") VALUES (%s, %s) RETURNING *;
[2024-02-05 10:13:14.198508] : Dataloom[postgres]: 
        SELECT 
            parent.id AS "posts_id", parent.completed AS "posts_completed", parent.title AS "posts_title",
            child_user.id AS "users_id", child_user.username AS "users_username", child_user.name AS "users_name"
        FROM 
            posts parent
        JOIN users child_user ON parent."userId" = child_user.id 
        WHERE 
            parent."id" = %s;
    
[2024-02-05 10:13:54.772619] : Dataloom[postgres]: DROP TABLE IF EXISTS "posts" CASCADE;
[2024-02-05 10:13:54.814002] : Dataloom[postgres]: CREATE TABLE IF NOT EXISTS "posts" ("completed" BOOLEAN DEFAULT False, "id" BIGSERIAL PRIMARY KEY UNIQUE NOT NULL, "title" VARCHAR(255) NOT NULL, "createdAt" TIMESTAMP DEFAULT CURRENT_TIMESTAMP, "updatedAt" TIMESTAMP DEFAULT CURRENT_TIMESTAMP, "userId" BIGSERIAL NOT NULL REFERENCES "users"("id") ON DELETE CASCADE ON UPDATE CASCADE);
[2024-02-05 10:13:54.863691] : Dataloom[postgres]: DROP TABLE IF EXISTS "users" CASCADE;
[2024-02-05 10:13:54.902673] : Dataloom[postgres]: CREATE TABLE IF NOT EXISTS "users" ("id" BIGSERIAL PRIMARY KEY UNIQUE NOT NULL, "name" TEXT NOT NULL DEFAULT 'Bob', "username" VARCHAR(255) UNIQUE);
[2024-02-05 10:13:54.941761] : Dataloom[postgres]: SELECT tablename FROM pg_catalog.pg_tables WHERE schemaname='public';
[2024-02-05 10:13:54.979716] : Dataloom[postgres]: INSERT INTO "users" ("username") VALUES (%s) RETURNING "id";
[2024-02-05 10:13:55.011683] : Dataloom[postgres]: INSERT INTO "posts" ("title", "userId") VALUES (%s, %s) RETURNING *;
[2024-02-05 10:13:55.044243] : Dataloom[postgres]: 
        SELECT 
            parent.id AS "posts_id", parent.completed AS "posts_completed", parent.title AS "posts_title",
            child_user.id AS "users_id", child_user.username AS "users_username", child_user.name AS "users_name"
        FROM 
            posts parent
        JOIN users child_user ON parent."userId" = child_user.id 
        WHERE 
            parent."id" = %s;
    
[2024-02-05 10:14:14.739965] : Dataloom[postgres]: DROP TABLE IF EXISTS "posts" CASCADE;
[2024-02-05 10:14:14.776145] : Dataloom[postgres]: CREATE TABLE IF NOT EXISTS "posts" ("completed" BOOLEAN DEFAULT False, "id" BIGSERIAL PRIMARY KEY UNIQUE NOT NULL, "title" VARCHAR(255) NOT NULL, "createdAt" TIMESTAMP DEFAULT CURRENT_TIMESTAMP, "updatedAt" TIMESTAMP DEFAULT CURRENT_TIMESTAMP, "userId" BIGSERIAL NOT NULL REFERENCES "users"("id") ON DELETE CASCADE ON UPDATE CASCADE);
[2024-02-05 10:14:14.810144] : Dataloom[postgres]: DROP TABLE IF EXISTS "users" CASCADE;
[2024-02-05 10:14:14.839713] : Dataloom[postgres]: CREATE TABLE IF NOT EXISTS "users" ("id" BIGSERIAL PRIMARY KEY UNIQUE NOT NULL, "name" TEXT NOT NULL DEFAULT 'Bob', "username" VARCHAR(255) UNIQUE);
[2024-02-05 10:14:14.868757] : Dataloom[postgres]: SELECT tablename FROM pg_catalog.pg_tables WHERE schemaname='public';
[2024-02-05 10:14:14.899724] : Dataloom[postgres]: INSERT INTO "users" ("username") VALUES (%s) RETURNING "id";
[2024-02-05 10:14:14.927717] : Dataloom[postgres]: INSERT INTO "posts" ("title", "userId") VALUES (%s, %s) RETURNING *;
[2024-02-05 10:14:14.956970] : Dataloom[postgres]: 
        SELECT 
            parent.id AS "posts_id", parent.completed AS "posts_completed", parent.title AS "posts_title", parent.createdAt AS "posts_createdAt",
            child_user.id AS "users_id", child_user.username AS "users_username", child_user.name AS "users_name"
        FROM 
            posts parent
        JOIN users child_user ON parent."userId" = child_user.id 
        WHERE 
            parent."id" = %s;
    
[2024-02-05 10:19:01.404424] : Dataloom[postgres]: DROP TABLE IF EXISTS "posts" CASCADE;
[2024-02-05 10:19:01.444389] : Dataloom[postgres]: CREATE TABLE IF NOT EXISTS "posts" ("completed" BOOLEAN DEFAULT False, "id" BIGSERIAL PRIMARY KEY UNIQUE NOT NULL, "title" VARCHAR(255) NOT NULL, "createdAt" TIMESTAMP DEFAULT CURRENT_TIMESTAMP, "updatedAt" TIMESTAMP DEFAULT CURRENT_TIMESTAMP, "userId" BIGSERIAL NOT NULL REFERENCES "users"("id") ON DELETE CASCADE ON UPDATE CASCADE);
[2024-02-05 10:19:01.494353] : Dataloom[postgres]: DROP TABLE IF EXISTS "users" CASCADE;
[2024-02-05 10:19:01.531547] : Dataloom[postgres]: CREATE TABLE IF NOT EXISTS "users" ("id" BIGSERIAL PRIMARY KEY UNIQUE NOT NULL, "name" TEXT NOT NULL DEFAULT 'Bob', "username" VARCHAR(255) UNIQUE);
[2024-02-05 10:19:01.571005] : Dataloom[postgres]: SELECT tablename FROM pg_catalog.pg_tables WHERE schemaname='public';
[2024-02-05 10:19:01.609799] : Dataloom[postgres]: INSERT INTO "users" ("username") VALUES (%s) RETURNING "id";
[2024-02-05 10:19:01.642797] : Dataloom[postgres]: INSERT INTO "posts" ("title", "userId") VALUES (%s, %s) RETURNING *;
[2024-02-05 10:19:01.678082] : Dataloom[postgres]: 
        SELECT 
            parent."id" AS "posts_id", parent."completed" AS "posts_completed", parent."title" AS "posts_title", parent."createdAt" AS "posts_createdAt",
            child_user."id" AS "users_id", child_user."username" AS "users_username", child_user."name" AS "users_name"
        FROM 
            posts parent
        JOIN users child_user ON parent."userId" = child_user.id 
        WHERE 
            parent."id" = %s;
    
[2024-02-05 10:22:31.666786] : Dataloom[postgres]: DROP TABLE IF EXISTS "posts" CASCADE;
[2024-02-05 10:22:31.710820] : Dataloom[postgres]: CREATE TABLE IF NOT EXISTS "posts" ("completed" BOOLEAN DEFAULT False, "id" BIGSERIAL PRIMARY KEY UNIQUE NOT NULL, "title" VARCHAR(255) NOT NULL, "categoryId" BIGSERIAL NOT NULL REFERENCES "users"("id") ON DELETE CASCADE ON UPDATE CASCADE, "createdAt" TIMESTAMP DEFAULT CURRENT_TIMESTAMP, "updatedAt" TIMESTAMP DEFAULT CURRENT_TIMESTAMP, "userId" BIGSERIAL NOT NULL REFERENCES "users"("id") ON DELETE CASCADE ON UPDATE CASCADE);
[2024-02-05 10:22:31.766747] : Dataloom[postgres]: DROP TABLE IF EXISTS "users" CASCADE;
[2024-02-05 10:22:31.813752] : Dataloom[postgres]: CREATE TABLE IF NOT EXISTS "users" ("id" BIGSERIAL PRIMARY KEY UNIQUE NOT NULL, "name" TEXT NOT NULL DEFAULT 'Bob', "username" VARCHAR(255) UNIQUE);
[2024-02-05 10:22:31.869374] : Dataloom[postgres]: SELECT tablename FROM pg_catalog.pg_tables WHERE schemaname='public';
[2024-02-05 10:22:31.913102] : Dataloom[postgres]: INSERT INTO "users" ("username") VALUES (%s) RETURNING "id";
[2024-02-05 10:22:31.944747] : Dataloom[postgres]: INSERT INTO "categories" ("name") VALUES (%s) RETURNING None;
[2024-02-05 10:23:02.170854] : Dataloom[postgres]: DROP TABLE IF EXISTS "posts" CASCADE;
[2024-02-05 10:23:02.211824] : Dataloom[postgres]: CREATE TABLE IF NOT EXISTS "posts" ("completed" BOOLEAN DEFAULT False, "id" BIGSERIAL PRIMARY KEY UNIQUE NOT NULL, "title" VARCHAR(255) NOT NULL, "categoryId" BIGSERIAL NOT NULL REFERENCES "users"("id") ON DELETE CASCADE ON UPDATE CASCADE, "createdAt" TIMESTAMP DEFAULT CURRENT_TIMESTAMP, "updatedAt" TIMESTAMP DEFAULT CURRENT_TIMESTAMP, "userId" BIGSERIAL NOT NULL REFERENCES "users"("id") ON DELETE CASCADE ON UPDATE CASCADE);
[2024-02-05 10:23:02.257814] : Dataloom[postgres]: DROP TABLE IF EXISTS "users" CASCADE;
[2024-02-05 10:23:02.296135] : Dataloom[postgres]: CREATE TABLE IF NOT EXISTS "users" ("id" BIGSERIAL PRIMARY KEY UNIQUE NOT NULL, "name" TEXT NOT NULL DEFAULT 'Bob', "username" VARCHAR(255) UNIQUE);
[2024-02-05 10:23:02.335442] : Dataloom[postgres]: DROP TABLE IF EXISTS "categories" CASCADE;
[2024-02-05 10:23:22.667850] : Dataloom[postgres]: DROP TABLE IF EXISTS "posts" CASCADE;
[2024-02-05 10:23:22.705807] : Dataloom[postgres]: CREATE TABLE IF NOT EXISTS "posts" ("completed" BOOLEAN DEFAULT False, "id" BIGSERIAL PRIMARY KEY UNIQUE NOT NULL, "title" VARCHAR(255) NOT NULL, "categoryId" BIGSERIAL NOT NULL REFERENCES "users"("id") ON DELETE CASCADE ON UPDATE CASCADE, "createdAt" TIMESTAMP DEFAULT CURRENT_TIMESTAMP, "updatedAt" TIMESTAMP DEFAULT CURRENT_TIMESTAMP, "userId" BIGSERIAL NOT NULL REFERENCES "users"("id") ON DELETE CASCADE ON UPDATE CASCADE);
[2024-02-05 10:23:22.758656] : Dataloom[postgres]: DROP TABLE IF EXISTS "users" CASCADE;
[2024-02-05 10:23:22.796616] : Dataloom[postgres]: CREATE TABLE IF NOT EXISTS "users" ("id" BIGSERIAL PRIMARY KEY UNIQUE NOT NULL, "name" TEXT NOT NULL DEFAULT 'Bob', "username" VARCHAR(255) UNIQUE);
[2024-02-05 10:23:22.836615] : Dataloom[postgres]: DROP TABLE IF EXISTS "categories" CASCADE;
[2024-02-05 10:23:22.860656] : Dataloom[postgres]: CREATE TABLE IF NOT EXISTS "categories" ("id" BIGSERIAL PRIMARY KEY UNIQUE NOT NULL, "name" VARCHAR(255) NOT NULL);
[2024-02-05 10:23:22.892654] : Dataloom[postgres]: SELECT tablename FROM pg_catalog.pg_tables WHERE schemaname='public';
[2024-02-05 10:23:22.932599] : Dataloom[postgres]: INSERT INTO "users" ("username") VALUES (%s) RETURNING "id";
[2024-02-05 10:23:22.961627] : Dataloom[postgres]: INSERT INTO "categories" ("name") VALUES (%s) RETURNING "id";
[2024-02-05 10:23:22.990672] : Dataloom[postgres]: INSERT INTO "posts" ("categoryId", "title", "userId") VALUES (%s, %s, %s) RETURNING *;
[2024-02-05 10:23:23.024834] : Dataloom[postgres]: 
        SELECT 
            parent."id" AS "posts_id", parent."completed" AS "posts_completed", parent."title" AS "posts_title", parent."createdAt" AS "posts_createdAt",
            child_user."id" AS "users_id", child_user."username" AS "users_username", child_user."name" AS "users_name"
        FROM 
            posts parent
        JOIN users child_user ON parent."userId" = child_user.id 
        WHERE 
            parent."id" = %s;
    
[2024-02-05 10:23:31.088458] : Dataloom[mysql]: DROP TABLE IF EXISTS `users`;
[2024-02-05 10:23:31.207628] : Dataloom[mysql]: DROP TABLE IF EXISTS `users`;
[2024-02-05 10:23:31.323523] : Dataloom[mysql]: DROP TABLE IF EXISTS `users`;
[2024-02-05 10:23:31.375502] : Dataloom[mysql]: CREATE TABLE IF NOT EXISTS `users` (`id` INT PRIMARY KEY AUTO_INCREMENT UNIQUE NOT NULL, `name` VARCHAR(255), `username` TEXT NOT NULL);
[2024-02-05 10:23:31.474497] : Dataloom[mysql]: DROP TABLE IF EXISTS `posts`;
[2024-02-05 10:23:31.529622] : Dataloom[mysql]: CREATE TABLE IF NOT EXISTS `posts` (`id` INT PRIMARY KEY AUTO_INCREMENT UNIQUE NOT NULL, `title` TEXT NOT NULL);
[2024-02-05 10:23:31.587986] : Dataloom[mysql]: SHOW TABLES;
[2024-02-05 10:23:31.626517] : Dataloom[mysql]: DROP TABLE IF EXISTS `users`;
[2024-02-05 10:23:31.709385] : Dataloom[mysql]: CREATE TABLE IF NOT EXISTS `users` (`id` INT PRIMARY KEY AUTO_INCREMENT UNIQUE NOT NULL, `name` VARCHAR(255) UNIQUE, `username` VARCHAR(255) NOT NULL DEFAULT 'Hello there!!');
[2024-02-05 10:23:31.844295] : Dataloom[mysql]: DROP TABLE IF EXISTS `posts`;
[2024-02-05 10:23:31.942091] : Dataloom[mysql]: CREATE TABLE IF NOT EXISTS `posts` (`completed` BOOLEAN DEFAULT False, `id` INT PRIMARY KEY AUTO_INCREMENT UNIQUE NOT NULL, `title` VARCHAR(255) NOT NULL);
[2024-02-05 10:23:32.227429] : Dataloom[mysql]: SHOW TABLES;
[2024-02-05 10:23:32.294426] : Dataloom[mysql]: DROP TABLE IF EXISTS `posts`;
[2024-02-05 10:23:32.539420] : Dataloom[mysql]: CREATE TABLE IF NOT EXISTS `posts` (`completed` BOOLEAN DEFAULT False, `id` INT PRIMARY KEY AUTO_INCREMENT UNIQUE NOT NULL, `title` VARCHAR(255) NOT NULL, `createdAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP, `updatedAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP, `userId` INT NOT NULL REFERENCES `users`(`id`) ON DELETE CASCADE ON UPDATE CASCADE);
[2024-02-05 10:23:32.659461] : Dataloom[mysql]: DROP TABLE IF EXISTS `users`;
[2024-02-05 10:23:32.735768] : Dataloom[mysql]: CREATE TABLE IF NOT EXISTS `users` (`id` INT PRIMARY KEY AUTO_INCREMENT UNIQUE NOT NULL, `name` VARCHAR(255) NOT NULL DEFAULT 'Bob', `username` VARCHAR(255) UNIQUE, `createdAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP, `updatedAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP);
[2024-02-05 10:23:32.814419] : Dataloom[mysql]: SHOW TABLES;
[2024-02-05 10:23:32.839365] : Dataloom[mysql]: INSERT INTO `users` (`name`, `username`) VALUES (%s, %s);
[2024-02-05 10:23:32.866414] : Dataloom[mysql]: DELETE FROM `users` WHERE `id` = %s;
[2024-02-05 10:23:32.891370] : Dataloom[mysql]: DELETE FROM `users` WHERE `id` = %s;
[2024-02-05 10:23:32.934370] : Dataloom[mysql]: DROP TABLE IF EXISTS `posts`;
[2024-02-05 10:23:33.007367] : Dataloom[mysql]: CREATE TABLE IF NOT EXISTS `posts` (`completed` BOOLEAN DEFAULT False, `id` INT PRIMARY KEY AUTO_INCREMENT UNIQUE NOT NULL, `title` VARCHAR(255) NOT NULL, `createdAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP, `updatedAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP, `userId` INT NOT NULL REFERENCES `users`(`id`) ON DELETE CASCADE ON UPDATE CASCADE);
[2024-02-05 10:23:33.079369] : Dataloom[mysql]: DROP TABLE IF EXISTS `users`;
[2024-02-05 10:23:33.139416] : Dataloom[mysql]: CREATE TABLE IF NOT EXISTS `users` (`id` INT PRIMARY KEY AUTO_INCREMENT UNIQUE NOT NULL, `name` VARCHAR(255) NOT NULL DEFAULT 'Bob', `username` VARCHAR(255) UNIQUE, `createdAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP, `updatedAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP);
[2024-02-05 10:23:33.225833] : Dataloom[mysql]: SHOW TABLES;
[2024-02-05 10:23:33.244874] : Dataloom[mysql]: INSERT INTO `users` (`name`, `username`) VALUES (%s, %s);
[2024-02-05 10:23:33.265837] : Dataloom[mysql]: 
    DELETE FROM `users` WHERE `id` IN (
       SELECT `id` FROM  (
                SELECT `id` FROM `users` WHERE `name` = %s LIMIT 1
        ) AS subquery
    );
    
[2024-02-05 10:23:33.284621] : Dataloom[mysql]: SELECT `createdAt`, `id`, `name`, `updatedAt`, `username` FROM `users` WHERE `name` = %s   ;
[2024-02-05 10:23:33.304666] : Dataloom[mysql]: 
    DELETE FROM `users` WHERE `id` IN (
       SELECT `id` FROM  (
                SELECT `id` FROM `users` WHERE `name` = %s AND `id` = %s LIMIT 1
        ) AS subquery
    );
    
[2024-02-05 10:23:33.324186] : Dataloom[mysql]: SELECT `createdAt`, `id`, `name`, `updatedAt`, `username` FROM `users` WHERE `name` = %s   ;
[2024-02-05 10:23:33.341552] : Dataloom[mysql]: 
    DELETE FROM `users` WHERE `id` IN (
       SELECT `id` FROM  (
                SELECT `id` FROM `users` WHERE `name` = %s AND `id` = %s LIMIT 1
        ) AS subquery
    );
    
[2024-02-05 10:23:33.361208] : Dataloom[mysql]: SELECT `createdAt`, `id`, `name`, `updatedAt`, `username` FROM `users` WHERE `name` = %s   ;
[2024-02-05 10:23:33.392177] : Dataloom[mysql]: DROP TABLE IF EXISTS `posts`;
[2024-02-05 10:23:33.461045] : Dataloom[mysql]: CREATE TABLE IF NOT EXISTS `posts` (`completed` BOOLEAN DEFAULT False, `id` INT PRIMARY KEY AUTO_INCREMENT UNIQUE NOT NULL, `title` VARCHAR(255) NOT NULL, `createdAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP, `updatedAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP, `userId` INT NOT NULL REFERENCES `users`(`id`) ON DELETE CASCADE ON UPDATE CASCADE);
[2024-02-05 10:23:33.543022] : Dataloom[mysql]: DROP TABLE IF EXISTS `users`;
[2024-02-05 10:23:33.619984] : Dataloom[mysql]: CREATE TABLE IF NOT EXISTS `users` (`id` INT PRIMARY KEY AUTO_INCREMENT UNIQUE NOT NULL, `name` VARCHAR(255) NOT NULL DEFAULT 'Bob', `username` VARCHAR(255) UNIQUE, `createdAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP, `updatedAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP);
[2024-02-05 10:23:33.703131] : Dataloom[mysql]: SHOW TABLES;
[2024-02-05 10:23:33.728154] : Dataloom[mysql]: INSERT INTO `users` (`name`, `username`) VALUES (%s, %s);
[2024-02-05 10:23:33.756160] : Dataloom[mysql]: DELETE FROM `users` WHERE `name` = %s;
[2024-02-05 10:23:33.784164] : Dataloom[mysql]: SELECT `createdAt`, `id`, `name`, `updatedAt`, `username` FROM `users` WHERE `name` = %s   ;
[2024-02-05 10:23:33.803395] : Dataloom[mysql]: INSERT INTO `users` (`name`, `username`) VALUES (%s, %s);
[2024-02-05 10:23:33.822151] : Dataloom[mysql]: DELETE FROM `users` WHERE `name` = %s AND `id` = %s;
[2024-02-05 10:23:33.839274] : Dataloom[mysql]: SELECT `createdAt`, `id`, `name`, `updatedAt`, `username` FROM `users` WHERE `name` = %s   ;
[2024-02-05 10:23:33.856264] : Dataloom[mysql]: DELETE FROM `users` WHERE `name` = %s AND `id` = %s;
[2024-02-05 10:23:33.875156] : Dataloom[mysql]: SELECT `createdAt`, `id`, `name`, `updatedAt`, `username` FROM `users` WHERE `name` = %s   ;
[2024-02-05 10:23:33.913203] : Dataloom[mysql]: DROP TABLE IF EXISTS `posts`;
[2024-02-05 10:23:33.988929] : Dataloom[mysql]: CREATE TABLE IF NOT EXISTS `posts` (`completed` BOOLEAN DEFAULT False, `id` INT PRIMARY KEY AUTO_INCREMENT UNIQUE NOT NULL, `title` VARCHAR(255) NOT NULL, `createdAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP, `updatedAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP, `userId` INT NOT NULL REFERENCES `users`(`id`) ON DELETE CASCADE ON UPDATE CASCADE);
[2024-02-05 10:23:34.088922] : Dataloom[mysql]: DROP TABLE IF EXISTS `users`;
[2024-02-05 10:23:34.169819] : Dataloom[mysql]: CREATE TABLE IF NOT EXISTS `users` (`id` INT PRIMARY KEY AUTO_INCREMENT UNIQUE NOT NULL, `name` VARCHAR(255) NOT NULL DEFAULT 'Bob', `username` VARCHAR(255) UNIQUE, `createdAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP, `updatedAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP);
[2024-02-05 10:23:34.237520] : Dataloom[mysql]: SHOW TABLES;
[2024-02-05 10:23:34.263560] : Dataloom[mysql]: INSERT INTO `users` (`username`) VALUES (%s);
[2024-02-05 10:23:34.288512] : Dataloom[mysql]: INSERT INTO `posts` (`title`, `userId`) VALUES (%s, %s);
[2024-02-05 10:23:34.352385] : Dataloom[mysql]: DROP TABLE IF EXISTS `posts`;
[2024-02-05 10:23:34.472032] : Dataloom[mysql]: CREATE TABLE IF NOT EXISTS `posts` (`completed` BOOLEAN DEFAULT False, `id` INT PRIMARY KEY AUTO_INCREMENT UNIQUE NOT NULL, `title` VARCHAR(255) NOT NULL, `createdAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP, `updatedAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP, `userId` INT NOT NULL REFERENCES `users`(`id`) ON DELETE CASCADE ON UPDATE CASCADE);
[2024-02-05 10:23:34.571031] : Dataloom[mysql]: DROP TABLE IF EXISTS `users`;
[2024-02-05 10:23:34.656109] : Dataloom[mysql]: CREATE TABLE IF NOT EXISTS `users` (`id` INT PRIMARY KEY AUTO_INCREMENT UNIQUE NOT NULL, `name` VARCHAR(255) NOT NULL DEFAULT 'Bob', `username` VARCHAR(255) UNIQUE, `createdAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP, `updatedAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP);
[2024-02-05 10:23:34.793020] : Dataloom[mysql]: SHOW TABLES;
[2024-02-05 10:23:34.831103] : Dataloom[mysql]: INSERT INTO `users` (`username`) VALUES (%s);
[2024-02-05 10:23:34.871022] : Dataloom[mysql]: INSERT INTO `posts` (`title`, `userId`) VALUES (%s, %s);
[2024-02-05 10:23:34.936846] : Dataloom[mysql]: DROP TABLE IF EXISTS `posts`;
[2024-02-05 10:23:35.015783] : Dataloom[mysql]: CREATE TABLE IF NOT EXISTS `posts` (`completed` BOOLEAN DEFAULT False, `id` INT PRIMARY KEY AUTO_INCREMENT UNIQUE NOT NULL, `title` VARCHAR(255) NOT NULL, `createdAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP, `updatedAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP, `userId` INT NOT NULL REFERENCES `users`(`id`) ON DELETE CASCADE ON UPDATE CASCADE);
[2024-02-05 10:23:35.116050] : Dataloom[mysql]: DROP TABLE IF EXISTS `users`;
[2024-02-05 10:23:35.206523] : Dataloom[mysql]: CREATE TABLE IF NOT EXISTS `users` (`id` INT PRIMARY KEY AUTO_INCREMENT UNIQUE NOT NULL, `name` VARCHAR(255) NOT NULL DEFAULT 'Bob', `username` VARCHAR(255) UNIQUE);
[2024-02-05 10:23:35.316679] : Dataloom[mysql]: SHOW TABLES;
[2024-02-05 10:23:35.351703] : Dataloom[mysql]: INSERT INTO `users` (`username`) VALUES (%s);
[2024-02-05 10:23:35.387734] : Dataloom[mysql]: INSERT INTO `posts` (`title`, `userId`) VALUES (%s, %s);
[2024-02-05 10:23:35.425735] : Dataloom[mysql]: SELECT `id`, `name`, `username` FROM `users` WHERE `id` = %s;
[2024-02-05 10:23:35.459269] : Dataloom[mysql]: SELECT `id`, `name`, `username` FROM `users` WHERE `id` = %s;
[2024-02-05 10:23:35.494270] : Dataloom[mysql]: SELECT `id`, `completed` FROM `posts` WHERE `id` = %s;
[2024-02-05 10:23:35.553267] : Dataloom[mysql]: DROP TABLE IF EXISTS `posts`;
[2024-02-05 10:23:35.658018] : Dataloom[mysql]: CREATE TABLE IF NOT EXISTS `posts` (`completed` BOOLEAN DEFAULT False, `id` INT PRIMARY KEY AUTO_INCREMENT UNIQUE NOT NULL, `title` VARCHAR(255) NOT NULL, `createdAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP, `updatedAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP, `userId` INT NOT NULL REFERENCES `users`(`id`) ON DELETE CASCADE ON UPDATE CASCADE);
[2024-02-05 10:23:35.782020] : Dataloom[mysql]: DROP TABLE IF EXISTS `users`;
[2024-02-05 10:23:35.882087] : Dataloom[mysql]: CREATE TABLE IF NOT EXISTS `users` (`id` INT PRIMARY KEY AUTO_INCREMENT UNIQUE NOT NULL, `name` VARCHAR(255) NOT NULL DEFAULT 'Bob', `username` VARCHAR(255) UNIQUE);
[2024-02-05 10:23:36.017154] : Dataloom[mysql]: SHOW TABLES;
[2024-02-05 10:23:36.053244] : Dataloom[mysql]: INSERT INTO `users` (`username`) VALUES (%s);
[2024-02-05 10:23:36.094254] : Dataloom[mysql]: INSERT INTO `posts` (`title`, `userId`) VALUES (%s, %s);
[2024-02-05 10:23:36.128495] : Dataloom[mysql]: SELECT `id`, `name`, `username` FROM `users`   ;
[2024-02-05 10:23:36.157512] : Dataloom[mysql]: SELECT `completed`, `createdAt`, `id`, `title`, `updatedAt`, `userId` FROM `posts`   ;
[2024-02-05 10:23:36.186461] : Dataloom[mysql]: SELECT `id`, `completed` FROM `posts`  LIMIT 3 OFFSET 3;
[2024-02-05 10:23:36.239636] : Dataloom[mysql]: DROP TABLE IF EXISTS `posts`;
[2024-02-05 10:23:36.334039] : Dataloom[mysql]: CREATE TABLE IF NOT EXISTS `posts` (`completed` BOOLEAN DEFAULT False, `id` INT PRIMARY KEY AUTO_INCREMENT UNIQUE NOT NULL, `title` VARCHAR(255) NOT NULL, `createdAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP, `updatedAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP, `userId` INT NOT NULL REFERENCES `users`(`id`) ON DELETE CASCADE ON UPDATE CASCADE);
[2024-02-05 10:23:36.479040] : Dataloom[mysql]: DROP TABLE IF EXISTS `users`;
[2024-02-05 10:23:36.591883] : Dataloom[mysql]: CREATE TABLE IF NOT EXISTS `users` (`id` INT PRIMARY KEY AUTO_INCREMENT UNIQUE NOT NULL, `name` VARCHAR(255) NOT NULL DEFAULT 'Bob', `username` VARCHAR(255) UNIQUE);
[2024-02-05 10:23:36.726872] : Dataloom[mysql]: SHOW TABLES;
[2024-02-05 10:23:36.755872] : Dataloom[mysql]: INSERT INTO `users` (`username`) VALUES (%s);
[2024-02-05 10:23:36.790000] : Dataloom[mysql]: INSERT INTO `posts` (`title`, `userId`) VALUES (%s, %s);
[2024-02-05 10:23:36.832871] : Dataloom[mysql]: SELECT `id`, `name`, `username` FROM `users` WHERE `id` = %s   ;
[2024-02-05 10:23:36.870709] : Dataloom[mysql]: SELECT `id`, `name`, `username` FROM `users` WHERE `id` = %s   ;
[2024-02-05 10:23:36.896711] : Dataloom[mysql]: SELECT `id`, `name`, `username` FROM `users` WHERE `id` = %s AND `name` = %s   ;
[2024-02-05 10:23:36.915004] : Dataloom[mysql]: SELECT `id`, `name`, `username` FROM `users` WHERE `id` = %s AND `username` = %s   ;
[2024-02-05 10:23:36.933708] : Dataloom[mysql]: SELECT `id`, `name`, `username` FROM `users` WHERE `name` = %s AND `username` = %s   ;
[2024-02-05 10:23:36.951712] : Dataloom[mysql]: SELECT `id`, `completed` FROM `posts`   ;
[2024-02-05 10:23:36.988712] : Dataloom[mysql]: DROP TABLE IF EXISTS `posts`;
[2024-02-05 10:23:37.092280] : Dataloom[mysql]: CREATE TABLE IF NOT EXISTS `posts` (`completed` BOOLEAN DEFAULT False, `id` INT PRIMARY KEY AUTO_INCREMENT UNIQUE NOT NULL, `title` VARCHAR(255) NOT NULL, `createdAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP, `updatedAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP, `userId` INT NOT NULL REFERENCES `users`(`id`) ON DELETE CASCADE ON UPDATE CASCADE);
[2024-02-05 10:23:37.213796] : Dataloom[mysql]: DROP TABLE IF EXISTS `users`;
[2024-02-05 10:23:37.330746] : Dataloom[mysql]: CREATE TABLE IF NOT EXISTS `users` (`id` INT PRIMARY KEY AUTO_INCREMENT UNIQUE NOT NULL, `name` VARCHAR(255) NOT NULL DEFAULT 'Bob', `username` VARCHAR(255) UNIQUE);
[2024-02-05 10:23:37.487436] : Dataloom[mysql]: SHOW TABLES;
[2024-02-05 10:23:37.510433] : Dataloom[mysql]: INSERT INTO `users` (`username`) VALUES (%s);
[2024-02-05 10:23:37.535585] : Dataloom[mysql]: INSERT INTO `posts` (`title`, `userId`) VALUES (%s, %s);
[2024-02-05 10:23:37.561807] : Dataloom[mysql]: SELECT `completed`, `createdAt`, `id`, `title`, `updatedAt`, `userId` FROM `posts` WHERE `id` = %s AND `userId` = %s   ;
[2024-02-05 10:23:37.584694] : Dataloom[mysql]: SELECT `id`, `name`, `username` FROM `users`   ;
[2024-02-05 10:23:37.607549] : Dataloom[mysql]: SELECT `id`, `name`, `username` FROM `users` WHERE `id` = %s   ;
[2024-02-05 10:23:37.630586] : Dataloom[mysql]: SELECT `id`, `name`, `username` FROM `users` WHERE `id` = %s   ;
[2024-02-05 10:23:37.652540] : Dataloom[mysql]: SELECT `id`, `name`, `username` FROM `users` WHERE `id` = %s AND `name` = %s   ;
[2024-02-05 10:23:37.674623] : Dataloom[mysql]: SELECT `id`, `name`, `username` FROM `users` WHERE `id` = %s AND `username` = %s   ;
[2024-02-05 10:23:37.697702] : Dataloom[mysql]: SELECT `id`, `name`, `username` FROM `users` WHERE `name` = %s AND `username` = %s   ;
[2024-02-05 10:23:37.720240] : Dataloom[mysql]: SELECT `id`, `completed` FROM `posts` WHERE `userId` = %s  LIMIT 3 OFFSET 3;
[2024-02-05 10:23:37.743064] : Dataloom[mysql]: SELECT `completed`, `createdAt`, `id`, `title`, `updatedAt`, `userId` FROM `posts`   ;
[2024-02-05 10:23:37.787064] : Dataloom[mysql]: DROP TABLE IF EXISTS `posts`;
[2024-02-05 10:23:37.874150] : Dataloom[mysql]: CREATE TABLE IF NOT EXISTS `posts` (`completed` BOOLEAN DEFAULT False, `id` INT PRIMARY KEY AUTO_INCREMENT UNIQUE NOT NULL, `title` VARCHAR(255) NOT NULL, `createdAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP, `updatedAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP, `userId` INT NOT NULL REFERENCES `users`(`id`) ON DELETE CASCADE ON UPDATE CASCADE);
[2024-02-05 10:23:37.952708] : Dataloom[mysql]: DROP TABLE IF EXISTS `users`;
[2024-02-05 10:23:38.050069] : Dataloom[mysql]: CREATE TABLE IF NOT EXISTS `users` (`id` INT PRIMARY KEY AUTO_INCREMENT UNIQUE NOT NULL, `name` VARCHAR(255) NOT NULL DEFAULT 'Bob', `username` VARCHAR(255) UNIQUE, `createdAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP, `updatedAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP);
[2024-02-05 10:23:38.132452] : Dataloom[mysql]: SHOW TABLES;
[2024-02-05 10:23:38.158449] : Dataloom[mysql]: INSERT INTO `users` (`username`) VALUES (%s);
[2024-02-05 10:23:38.184492] : Dataloom[mysql]: INSERT INTO `posts` (`title`, `userId`) VALUES (%s, %s);
[2024-02-05 10:23:38.281168] : Dataloom[mysql]: UPDATE `users` SET `updatedAt` = %s WHERE `id` = %s;
[2024-02-05 10:23:38.318157] : Dataloom[mysql]: UPDATE `users` SET `updatedAt` = %s WHERE `id` = %s;
[2024-02-05 10:23:38.353214] : Dataloom[mysql]: SELECT `createdAt`, `id`, `name`, `updatedAt`, `username` FROM `users` WHERE `id` = %s;
[2024-02-05 10:23:38.388409] : Dataloom[mysql]: UPDATE `users` SET `id` = %s, `updatedAt` = %s WHERE `id` = %s;
[2024-02-05 10:23:38.443930] : Dataloom[mysql]: DROP TABLE IF EXISTS `posts`;
[2024-02-05 10:23:38.545551] : Dataloom[mysql]: CREATE TABLE IF NOT EXISTS `posts` (`completed` BOOLEAN DEFAULT False, `id` INT PRIMARY KEY AUTO_INCREMENT UNIQUE NOT NULL, `title` VARCHAR(255) NOT NULL, `createdAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP, `userId` INT NOT NULL REFERENCES `users`(`id`) ON DELETE CASCADE ON UPDATE CASCADE);
[2024-02-05 10:23:38.659474] : Dataloom[mysql]: DROP TABLE IF EXISTS `users`;
[2024-02-05 10:23:38.783425] : Dataloom[mysql]: CREATE TABLE IF NOT EXISTS `users` (`id` INT PRIMARY KEY AUTO_INCREMENT UNIQUE NOT NULL, `name` VARCHAR(255) NOT NULL DEFAULT 'Bob', `username` VARCHAR(255) UNIQUE, `createdAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP, `updatedAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP);
[2024-02-05 10:23:38.906600] : Dataloom[mysql]: SHOW TABLES;
[2024-02-05 10:23:38.942504] : Dataloom[mysql]: INSERT INTO `users` (`username`) VALUES (%s);
[2024-02-05 10:23:38.985613] : Dataloom[mysql]: INSERT INTO `posts` (`title`, `userId`) VALUES (%s, %s);
[2024-02-05 10:23:39.080268] : Dataloom[mysql]: 
        UPDATE `posts` SET `title` = %s WHERE `id` IN (
            SELECT `id` FROM  (
                SELECT `id` FROM `posts` WHERE `userId` = %s LIMIT 1
            ) AS subquery
        );
        
[2024-02-05 10:23:39.121559] : Dataloom[mysql]: 
        UPDATE `posts` SET `title` = %s WHERE `id` IN (
            SELECT `id` FROM  (
                SELECT `id` FROM `posts` WHERE `userId` = %s LIMIT 1
            ) AS subquery
        );
        
[2024-02-05 10:23:39.158273] : Dataloom[mysql]: SELECT `completed`, `createdAt`, `id`, `title`, `userId` FROM `posts` WHERE `id` = %s;
[2024-02-05 10:23:39.194042] : Dataloom[mysql]: 
        UPDATE `posts` SET `userId` = %s WHERE `id` IN (
            SELECT `id` FROM  (
                SELECT `id` FROM `posts` WHERE `userId` = %s LIMIT 1
            ) AS subquery
        );
        
[2024-02-05 10:23:39.259981] : Dataloom[mysql]: DROP TABLE IF EXISTS `posts`;
[2024-02-05 10:23:39.351181] : Dataloom[mysql]: CREATE TABLE IF NOT EXISTS `posts` (`completed` BOOLEAN DEFAULT False, `id` INT PRIMARY KEY AUTO_INCREMENT UNIQUE NOT NULL, `title` VARCHAR(255) NOT NULL, `createdAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP, `userId` INT NOT NULL REFERENCES `users`(`id`) ON DELETE CASCADE ON UPDATE CASCADE);
[2024-02-05 10:23:39.478808] : Dataloom[mysql]: DROP TABLE IF EXISTS `users`;
[2024-02-05 10:23:39.596458] : Dataloom[mysql]: CREATE TABLE IF NOT EXISTS `users` (`id` INT PRIMARY KEY AUTO_INCREMENT UNIQUE NOT NULL, `name` VARCHAR(255) NOT NULL DEFAULT 'Bob', `username` VARCHAR(255) UNIQUE, `createdAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP, `updatedAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP);
[2024-02-05 10:23:39.762021] : Dataloom[mysql]: SHOW TABLES;
[2024-02-05 10:23:39.800013] : Dataloom[mysql]: INSERT INTO `users` (`username`) VALUES (%s);
[2024-02-05 10:23:39.828012] : Dataloom[mysql]: INSERT INTO `posts` (`title`, `userId`) VALUES (%s, %s);
[2024-02-05 10:23:39.913295] : Dataloom[mysql]: UPDATE `posts` SET `title` = %s WHERE `userId` = %s;
[2024-02-05 10:23:39.947252] : Dataloom[mysql]: UPDATE `posts` SET `title` = %s WHERE `userId` = %s;
[2024-02-05 10:23:39.979283] : Dataloom[mysql]: SELECT `completed`, `createdAt`, `id`, `title`, `userId` FROM `posts` WHERE `id` = %s;
[2024-02-05 10:23:40.014284] : Dataloom[mysql]: UPDATE `posts` SET `userId` = %s WHERE `userId` = %s;
[2024-02-05 10:23:40.817551] : Dataloom[postgres]: DROP TABLE IF EXISTS "users" CASCADE;
[2024-02-05 10:23:41.067290] : Dataloom[postgres]: DROP TABLE IF EXISTS "users" CASCADE;
[2024-02-05 10:23:41.385398] : Dataloom[postgres]: DROP TABLE IF EXISTS "users" CASCADE;
[2024-02-05 10:23:41.420672] : Dataloom[postgres]: CREATE TABLE IF NOT EXISTS "users" ("id" BIGSERIAL PRIMARY KEY UNIQUE NOT NULL, "name" VARCHAR(255), "username" TEXT NOT NULL);
[2024-02-05 10:23:41.506105] : Dataloom[postgres]: DROP TABLE IF EXISTS "posts" CASCADE;
[2024-02-05 10:23:41.567094] : Dataloom[postgres]: CREATE TABLE IF NOT EXISTS "posts" ("id" BIGSERIAL PRIMARY KEY UNIQUE NOT NULL, "title" TEXT NOT NULL DEFAULT 'Hello there!!');
[2024-02-05 10:23:41.644008] : Dataloom[postgres]: SELECT tablename FROM pg_catalog.pg_tables WHERE schemaname='public';
[2024-02-05 10:23:41.840849] : Dataloom[postgres]: DROP TABLE IF EXISTS "users" CASCADE;
[2024-02-05 10:23:41.882854] : Dataloom[postgres]: CREATE TABLE IF NOT EXISTS "users" ("id" BIGSERIAL PRIMARY KEY UNIQUE NOT NULL, "name" VARCHAR(255) UNIQUE, "username" TEXT NOT NULL DEFAULT 'Hello there!!');
[2024-02-05 10:23:41.972121] : Dataloom[postgres]: DROP TABLE IF EXISTS "posts" CASCADE;
[2024-02-05 10:23:42.053170] : Dataloom[postgres]: CREATE TABLE IF NOT EXISTS "posts" ("completed" BOOLEAN DEFAULT False, "id" BIGSERIAL PRIMARY KEY UNIQUE NOT NULL, "title" VARCHAR(255) NOT NULL);
[2024-02-05 10:23:42.097111] : Dataloom[postgres]: SELECT tablename FROM pg_catalog.pg_tables WHERE schemaname='public';
[2024-02-05 10:23:42.249111] : Dataloom[postgres]: DROP TABLE IF EXISTS "posts" CASCADE;
[2024-02-05 10:23:42.274200] : Dataloom[postgres]: CREATE TABLE IF NOT EXISTS "posts" ("completed" BOOLEAN DEFAULT False, "id" BIGSERIAL PRIMARY KEY UNIQUE NOT NULL, "title" VARCHAR(255) NOT NULL, "createdAt" TIMESTAMP DEFAULT CURRENT_TIMESTAMP, "updatedAt" TIMESTAMP DEFAULT CURRENT_TIMESTAMP, "userId" BIGSERIAL NOT NULL REFERENCES "users"("id") ON DELETE CASCADE ON UPDATE CASCADE);
[2024-02-05 10:23:42.307668] : Dataloom[postgres]: DROP TABLE IF EXISTS "users" CASCADE;
[2024-02-05 10:23:42.332666] : Dataloom[postgres]: CREATE TABLE IF NOT EXISTS "users" ("id" BIGSERIAL PRIMARY KEY UNIQUE NOT NULL, "name" TEXT NOT NULL DEFAULT 'Bob', "username" VARCHAR(255) UNIQUE, "createdAt" TIMESTAMP DEFAULT CURRENT_TIMESTAMP, "updatedAt" TIMESTAMP DEFAULT CURRENT_TIMESTAMP);
[2024-02-05 10:23:42.359665] : Dataloom[postgres]: SELECT tablename FROM pg_catalog.pg_tables WHERE schemaname='public';
[2024-02-05 10:23:42.397331] : Dataloom[postgres]: INSERT INTO "users" ("name", "username") VALUES (%s, %s) RETURNING "id";
[2024-02-05 10:23:42.436335] : Dataloom[postgres]: DELETE FROM "users" WHERE "id" = %s;
[2024-02-05 10:23:42.484331] : Dataloom[postgres]: DELETE FROM "users" WHERE "id" = %s;
[2024-02-05 10:23:42.735719] : Dataloom[postgres]: DROP TABLE IF EXISTS "posts" CASCADE;
[2024-02-05 10:23:42.802347] : Dataloom[postgres]: CREATE TABLE IF NOT EXISTS "posts" ("completed" BOOLEAN DEFAULT False, "id" BIGSERIAL PRIMARY KEY UNIQUE NOT NULL, "title" VARCHAR(255) NOT NULL, "createdAt" TIMESTAMP DEFAULT CURRENT_TIMESTAMP, "updatedAt" TIMESTAMP DEFAULT CURRENT_TIMESTAMP, "userId" BIGSERIAL NOT NULL REFERENCES "users"("id") ON DELETE CASCADE ON UPDATE CASCADE);
[2024-02-05 10:23:42.871166] : Dataloom[postgres]: DROP TABLE IF EXISTS "users" CASCADE;
[2024-02-05 10:23:42.927812] : Dataloom[postgres]: CREATE TABLE IF NOT EXISTS "users" ("id" BIGSERIAL PRIMARY KEY UNIQUE NOT NULL, "name" TEXT NOT NULL DEFAULT 'Bob', "username" VARCHAR(255) UNIQUE, "createdAt" TIMESTAMP DEFAULT CURRENT_TIMESTAMP, "updatedAt" TIMESTAMP DEFAULT CURRENT_TIMESTAMP);
[2024-02-05 10:23:42.989931] : Dataloom[postgres]: SELECT tablename FROM pg_catalog.pg_tables WHERE schemaname='public';
[2024-02-05 10:23:43.060810] : Dataloom[postgres]: INSERT INTO "users" ("name", "username") VALUES (%s, %s) RETURNING *;
[2024-02-05 10:23:43.108335] : Dataloom[postgres]: 
    DELETE FROM "users" WHERE "id" = (
        SELECT "id" FROM  "users" WHERE "name" = %s LIMIT 1
    );
    
[2024-02-05 10:23:43.144347] : Dataloom[postgres]: SELECT "createdAt", "id", "name", "updatedAt", "username" FROM "users" WHERE "name" = %s   ;
[2024-02-05 10:23:43.179483] : Dataloom[postgres]: 
    DELETE FROM "users" WHERE "id" = (
        SELECT "id" FROM  "users" WHERE "name" = %s AND "id" = %s LIMIT 1
    );
    
[2024-02-05 10:23:43.213441] : Dataloom[postgres]: SELECT "createdAt", "id", "name", "updatedAt", "username" FROM "users" WHERE "name" = %s   ;
[2024-02-05 10:23:43.250802] : Dataloom[postgres]: 
    DELETE FROM "users" WHERE "id" = (
        SELECT "id" FROM  "users" WHERE "name" = %s AND "id" = %s LIMIT 1
    );
    
[2024-02-05 10:23:43.284501] : Dataloom[postgres]: SELECT "createdAt", "id", "name", "updatedAt", "username" FROM "users" WHERE "name" = %s   ;
[2024-02-05 10:23:43.529153] : Dataloom[postgres]: DROP TABLE IF EXISTS "posts" CASCADE;
[2024-02-05 10:23:43.578161] : Dataloom[postgres]: CREATE TABLE IF NOT EXISTS "posts" ("completed" BOOLEAN DEFAULT False, "id" BIGSERIAL PRIMARY KEY UNIQUE NOT NULL, "title" VARCHAR(255) NOT NULL, "createdAt" TIMESTAMP DEFAULT CURRENT_TIMESTAMP, "updatedAt" TIMESTAMP DEFAULT CURRENT_TIMESTAMP, "userId" BIGSERIAL NOT NULL REFERENCES "users"("id") ON DELETE CASCADE ON UPDATE CASCADE);
[2024-02-05 10:23:43.646572] : Dataloom[postgres]: DROP TABLE IF EXISTS "users" CASCADE;
[2024-02-05 10:23:43.701586] : Dataloom[postgres]: CREATE TABLE IF NOT EXISTS "users" ("id" BIGSERIAL PRIMARY KEY UNIQUE NOT NULL, "name" TEXT NOT NULL DEFAULT 'Bob', "username" VARCHAR(255) UNIQUE, "createdAt" TIMESTAMP DEFAULT CURRENT_TIMESTAMP, "updatedAt" TIMESTAMP DEFAULT CURRENT_TIMESTAMP);
[2024-02-05 10:23:43.756109] : Dataloom[postgres]: SELECT tablename FROM pg_catalog.pg_tables WHERE schemaname='public';
[2024-02-05 10:23:43.810733] : Dataloom[postgres]: INSERT INTO "users" ("name", "username") VALUES (%s, %s) RETURNING *;
[2024-02-05 10:23:43.848723] : Dataloom[postgres]: DELETE FROM "users" WHERE "name" = %s;
[2024-02-05 10:23:43.879730] : Dataloom[postgres]: SELECT "createdAt", "id", "name", "updatedAt", "username" FROM "users" WHERE "name" = %s   ;
[2024-02-05 10:23:43.910770] : Dataloom[postgres]: INSERT INTO "users" ("name", "username") VALUES (%s, %s) RETURNING *;
[2024-02-05 10:23:43.944016] : Dataloom[postgres]: DELETE FROM "users" WHERE "name" = %s AND "id" = %s;
[2024-02-05 10:23:43.975086] : Dataloom[postgres]: SELECT "createdAt", "id", "name", "updatedAt", "username" FROM "users" WHERE "name" = %s   ;
[2024-02-05 10:23:44.007018] : Dataloom[postgres]: DELETE FROM "users" WHERE "name" = %s AND "id" = %s;
[2024-02-05 10:23:44.038542] : Dataloom[postgres]: SELECT "createdAt", "id", "name", "updatedAt", "username" FROM "users" WHERE "name" = %s   ;
[2024-02-05 10:23:44.227542] : Dataloom[postgres]: DROP TABLE IF EXISTS "posts" CASCADE;
[2024-02-05 10:23:44.271201] : Dataloom[postgres]: CREATE TABLE IF NOT EXISTS "posts" ("completed" BOOLEAN DEFAULT False, "id" BIGSERIAL PRIMARY KEY UNIQUE NOT NULL, "title" VARCHAR(255) NOT NULL, "createdAt" TIMESTAMP DEFAULT CURRENT_TIMESTAMP, "updatedAt" TIMESTAMP DEFAULT CURRENT_TIMESTAMP, "userId" BIGSERIAL NOT NULL REFERENCES "users"("id") ON DELETE CASCADE ON UPDATE CASCADE);
[2024-02-05 10:23:44.322914] : Dataloom[postgres]: DROP TABLE IF EXISTS "users" CASCADE;
[2024-02-05 10:23:44.369224] : Dataloom[postgres]: CREATE TABLE IF NOT EXISTS "users" ("id" BIGSERIAL PRIMARY KEY UNIQUE NOT NULL, "name" TEXT NOT NULL DEFAULT 'Bob', "username" VARCHAR(255) UNIQUE, "createdAt" TIMESTAMP DEFAULT CURRENT_TIMESTAMP, "updatedAt" TIMESTAMP DEFAULT CURRENT_TIMESTAMP);
[2024-02-05 10:23:44.414648] : Dataloom[postgres]: SELECT tablename FROM pg_catalog.pg_tables WHERE schemaname='public';
[2024-02-05 10:23:44.461735] : Dataloom[postgres]: INSERT INTO "users" ("username") VALUES (%s) RETURNING "id";
[2024-02-05 10:23:44.496772] : Dataloom[postgres]: INSERT INTO "posts" ("title", "userId") VALUES (%s, %s) RETURNING "id";
[2024-02-05 10:23:44.631691] : Dataloom[postgres]: DROP TABLE IF EXISTS "posts" CASCADE;
[2024-02-05 10:23:44.665730] : Dataloom[postgres]: CREATE TABLE IF NOT EXISTS "posts" ("completed" BOOLEAN DEFAULT False, "id" BIGSERIAL PRIMARY KEY UNIQUE NOT NULL, "title" VARCHAR(255) NOT NULL, "createdAt" TIMESTAMP DEFAULT CURRENT_TIMESTAMP, "updatedAt" TIMESTAMP DEFAULT CURRENT_TIMESTAMP, "userId" BIGSERIAL NOT NULL REFERENCES "users"("id") ON DELETE CASCADE ON UPDATE CASCADE);
[2024-02-05 10:23:44.720161] : Dataloom[postgres]: DROP TABLE IF EXISTS "users" CASCADE;
[2024-02-05 10:23:44.765194] : Dataloom[postgres]: CREATE TABLE IF NOT EXISTS "users" ("id" BIGSERIAL PRIMARY KEY UNIQUE NOT NULL, "name" TEXT NOT NULL DEFAULT 'Bob', "username" VARCHAR(255) UNIQUE, "createdAt" TIMESTAMP DEFAULT CURRENT_TIMESTAMP, "updatedAt" TIMESTAMP DEFAULT CURRENT_TIMESTAMP);
[2024-02-05 10:23:44.810145] : Dataloom[postgres]: SELECT tablename FROM pg_catalog.pg_tables WHERE schemaname='public';
[2024-02-05 10:23:44.886717] : Dataloom[postgres]: INSERT INTO "users" ("username") VALUES (%s) RETURNING "id";
[2024-02-05 10:23:44.975720] : Dataloom[postgres]: INSERT INTO "posts" ("title", "userId") VALUES (%s, %s) RETURNING *;
[2024-02-05 10:23:45.289266] : Dataloom[postgres]: DROP TABLE IF EXISTS "posts" CASCADE;
[2024-02-05 10:23:45.319500] : Dataloom[postgres]: CREATE TABLE IF NOT EXISTS "posts" ("completed" BOOLEAN DEFAULT False, "id" BIGSERIAL PRIMARY KEY UNIQUE NOT NULL, "title" VARCHAR(255) NOT NULL, "createdAt" TIMESTAMP DEFAULT CURRENT_TIMESTAMP, "updatedAt" TIMESTAMP DEFAULT CURRENT_TIMESTAMP, "userId" BIGSERIAL NOT NULL REFERENCES "users"("id") ON DELETE CASCADE ON UPDATE CASCADE);
[2024-02-05 10:23:45.356270] : Dataloom[postgres]: DROP TABLE IF EXISTS "users" CASCADE;
[2024-02-05 10:23:45.384811] : Dataloom[postgres]: CREATE TABLE IF NOT EXISTS "users" ("id" BIGSERIAL PRIMARY KEY UNIQUE NOT NULL, "name" TEXT NOT NULL DEFAULT 'Bob', "username" VARCHAR(255) UNIQUE);
[2024-02-05 10:23:45.426815] : Dataloom[postgres]: SELECT tablename FROM pg_catalog.pg_tables WHERE schemaname='public';
[2024-02-05 10:23:45.479586] : Dataloom[postgres]: INSERT INTO "users" ("username") VALUES (%s) RETURNING "id";
[2024-02-05 10:23:45.511586] : Dataloom[postgres]: INSERT INTO "posts" ("title", "userId") VALUES (%s, %s) RETURNING *;
[2024-02-05 10:23:45.541584] : Dataloom[postgres]: SELECT "id", "name", "username" FROM "users" WHERE "id" = %s;
[2024-02-05 10:23:45.562586] : Dataloom[postgres]: SELECT "id", "name", "username" FROM "users" WHERE "id" = %s;
[2024-02-05 10:23:45.582589] : Dataloom[postgres]: SELECT "id", "completed" FROM "posts" WHERE "id" = %s;
[2024-02-05 10:23:45.755585] : Dataloom[postgres]: DROP TABLE IF EXISTS "posts" CASCADE;
[2024-02-05 10:23:45.808588] : Dataloom[postgres]: CREATE TABLE IF NOT EXISTS "posts" ("completed" BOOLEAN DEFAULT False, "id" BIGSERIAL PRIMARY KEY UNIQUE NOT NULL, "title" VARCHAR(255) NOT NULL, "createdAt" TIMESTAMP DEFAULT CURRENT_TIMESTAMP, "updatedAt" TIMESTAMP DEFAULT CURRENT_TIMESTAMP, "userId" BIGSERIAL NOT NULL REFERENCES "users"("id") ON DELETE CASCADE ON UPDATE CASCADE);
[2024-02-05 10:23:45.866868] : Dataloom[postgres]: DROP TABLE IF EXISTS "users" CASCADE;
[2024-02-05 10:23:45.900583] : Dataloom[postgres]: CREATE TABLE IF NOT EXISTS "users" ("id" BIGSERIAL PRIMARY KEY UNIQUE NOT NULL, "name" TEXT NOT NULL DEFAULT 'Bob', "username" VARCHAR(255) UNIQUE);
[2024-02-05 10:23:45.938585] : Dataloom[postgres]: SELECT tablename FROM pg_catalog.pg_tables WHERE schemaname='public';
[2024-02-05 10:23:45.985712] : Dataloom[postgres]: INSERT INTO "users" ("username") VALUES (%s) RETURNING "id";
[2024-02-05 10:23:46.015326] : Dataloom[postgres]: INSERT INTO "posts" ("title", "userId") VALUES (%s, %s) RETURNING *;
[2024-02-05 10:23:46.041144] : Dataloom[postgres]: SELECT "id", "name", "username" FROM "users"   ;
[2024-02-05 10:23:46.062147] : Dataloom[postgres]: SELECT "completed", "createdAt", "id", "title", "updatedAt", "userId" FROM "posts"   ;
[2024-02-05 10:23:46.096689] : Dataloom[postgres]: SELECT "id", "completed" FROM "posts"  LIMIT 3 OFFSET 3;
[2024-02-05 10:23:46.217228] : Dataloom[postgres]: DROP TABLE IF EXISTS "posts" CASCADE;
[2024-02-05 10:23:46.250615] : Dataloom[postgres]: CREATE TABLE IF NOT EXISTS "posts" ("completed" BOOLEAN DEFAULT False, "id" BIGSERIAL PRIMARY KEY UNIQUE NOT NULL, "title" VARCHAR(255) NOT NULL, "createdAt" TIMESTAMP DEFAULT CURRENT_TIMESTAMP, "updatedAt" TIMESTAMP DEFAULT CURRENT_TIMESTAMP, "userId" BIGSERIAL NOT NULL REFERENCES "users"("id") ON DELETE CASCADE ON UPDATE CASCADE);
[2024-02-05 10:23:46.287926] : Dataloom[postgres]: DROP TABLE IF EXISTS "users" CASCADE;
[2024-02-05 10:23:46.315960] : Dataloom[postgres]: CREATE TABLE IF NOT EXISTS "users" ("id" BIGSERIAL PRIMARY KEY UNIQUE NOT NULL, "name" TEXT NOT NULL DEFAULT 'Bob', "username" VARCHAR(255) UNIQUE);
[2024-02-05 10:23:46.346924] : Dataloom[postgres]: SELECT tablename FROM pg_catalog.pg_tables WHERE schemaname='public';
[2024-02-05 10:23:46.379927] : Dataloom[postgres]: INSERT INTO "users" ("username") VALUES (%s) RETURNING "id";
[2024-02-05 10:23:46.418276] : Dataloom[postgres]: INSERT INTO "posts" ("title", "userId") VALUES (%s, %s) RETURNING *;
[2024-02-05 10:23:46.457227] : Dataloom[postgres]: SELECT "id", "name", "username" FROM "users" WHERE "id" = %s   ;
[2024-02-05 10:23:46.487352] : Dataloom[postgres]: SELECT "id", "name", "username" FROM "users" WHERE "id" = %s   ;
[2024-02-05 10:23:46.516366] : Dataloom[postgres]: SELECT "id", "name", "username" FROM "users" WHERE "id" = %s AND "name" = %s   ;
[2024-02-05 10:23:46.548366] : Dataloom[postgres]: SELECT "id", "name", "username" FROM "users" WHERE "id" = %s AND "username" = %s   ;
[2024-02-05 10:23:46.574366] : Dataloom[postgres]: SELECT "id", "name", "username" FROM "users" WHERE "name" = %s AND "username" = %s   ;
[2024-02-05 10:23:46.601050] : Dataloom[postgres]: SELECT "id", "completed" FROM "posts"   ;
[2024-02-05 10:23:46.789581] : Dataloom[postgres]: DROP TABLE IF EXISTS "posts" CASCADE;
[2024-02-05 10:23:46.832901] : Dataloom[postgres]: CREATE TABLE IF NOT EXISTS "posts" ("completed" BOOLEAN DEFAULT False, "id" BIGSERIAL PRIMARY KEY UNIQUE NOT NULL, "title" VARCHAR(255) NOT NULL, "createdAt" TIMESTAMP DEFAULT CURRENT_TIMESTAMP, "updatedAt" TIMESTAMP DEFAULT CURRENT_TIMESTAMP, "userId" BIGSERIAL NOT NULL REFERENCES "users"("id") ON DELETE CASCADE ON UPDATE CASCADE);
[2024-02-05 10:23:46.896182] : Dataloom[postgres]: DROP TABLE IF EXISTS "users" CASCADE;
[2024-02-05 10:23:46.940511] : Dataloom[postgres]: CREATE TABLE IF NOT EXISTS "users" ("id" BIGSERIAL PRIMARY KEY UNIQUE NOT NULL, "name" TEXT NOT NULL DEFAULT 'Bob', "username" VARCHAR(255) UNIQUE);
[2024-02-05 10:23:46.983181] : Dataloom[postgres]: SELECT tablename FROM pg_catalog.pg_tables WHERE schemaname='public';
[2024-02-05 10:23:47.031734] : Dataloom[postgres]: INSERT INTO "users" ("username") VALUES (%s) RETURNING "id";
[2024-02-05 10:23:47.062729] : Dataloom[postgres]: INSERT INTO "posts" ("title", "userId") VALUES (%s, %s) RETURNING *;
[2024-02-05 10:23:47.091729] : Dataloom[postgres]: SELECT "completed", "createdAt", "id", "title", "updatedAt", "userId" FROM "posts" WHERE "id" = %s AND "userId" = %s   ;
[2024-02-05 10:23:47.125272] : Dataloom[postgres]: SELECT "id", "name", "username" FROM "users"   ;
[2024-02-05 10:23:47.146289] : Dataloom[postgres]: SELECT "id", "name", "username" FROM "users" WHERE "id" = %s   ;
[2024-02-05 10:23:47.168320] : Dataloom[postgres]: SELECT "id", "name", "username" FROM "users" WHERE "id" = %s   ;
[2024-02-05 10:23:47.193274] : Dataloom[postgres]: SELECT "id", "name", "username" FROM "users" WHERE "id" = %s AND "name" = %s   ;
[2024-02-05 10:23:47.217101] : Dataloom[postgres]: SELECT "id", "name", "username" FROM "users" WHERE "id" = %s AND "username" = %s   ;
[2024-02-05 10:23:47.245096] : Dataloom[postgres]: SELECT "id", "name", "username" FROM "users" WHERE "name" = %s AND "username" = %s   ;
[2024-02-05 10:23:47.273117] : Dataloom[postgres]: SELECT "id", "completed" FROM "posts" WHERE "userId" = %s  LIMIT 3 OFFSET 3;
[2024-02-05 10:23:47.299862] : Dataloom[postgres]: SELECT "completed", "createdAt", "id", "title", "updatedAt", "userId" FROM "posts"   ;
[2024-02-05 10:23:47.569530] : Dataloom[postgres]: DROP TABLE IF EXISTS "posts" CASCADE;
[2024-02-05 10:23:47.628255] : Dataloom[postgres]: CREATE TABLE IF NOT EXISTS "posts" ("completed" BOOLEAN DEFAULT False, "id" BIGSERIAL PRIMARY KEY UNIQUE NOT NULL, "title" VARCHAR(255) NOT NULL, "createdAt" TIMESTAMP DEFAULT CURRENT_TIMESTAMP, "updatedAt" TIMESTAMP DEFAULT CURRENT_TIMESTAMP, "userId" BIGSERIAL NOT NULL REFERENCES "users"("id") ON DELETE CASCADE ON UPDATE CASCADE);
[2024-02-05 10:23:47.688253] : Dataloom[postgres]: DROP TABLE IF EXISTS "users" CASCADE;
[2024-02-05 10:23:47.731250] : Dataloom[postgres]: CREATE TABLE IF NOT EXISTS "users" ("id" BIGSERIAL PRIMARY KEY UNIQUE NOT NULL, "name" TEXT NOT NULL DEFAULT 'Bob', "username" VARCHAR(255) UNIQUE, "createdAt" TIMESTAMP DEFAULT CURRENT_TIMESTAMP, "updatedAt" TIMESTAMP DEFAULT CURRENT_TIMESTAMP);
[2024-02-05 10:23:47.776255] : Dataloom[postgres]: SELECT tablename FROM pg_catalog.pg_tables WHERE schemaname='public';
[2024-02-05 10:23:47.818970] : Dataloom[postgres]: INSERT INTO "users" ("username") VALUES (%s) RETURNING "id";
[2024-02-05 10:23:47.848985] : Dataloom[postgres]: INSERT INTO "posts" ("title", "userId") VALUES (%s, %s) RETURNING *;
[2024-02-05 10:23:47.924554] : Dataloom[postgres]: UPDATE "users" SET "updatedAt" = %s WHERE "id" = %s;
[2024-02-05 10:23:47.949554] : Dataloom[postgres]: UPDATE "users" SET "updatedAt" = %s WHERE "id" = %s;
[2024-02-05 10:23:47.977056] : Dataloom[postgres]: SELECT "createdAt", "id", "name", "updatedAt", "username" FROM "users" WHERE "id" = %s;
[2024-02-05 10:23:48.001555] : Dataloom[postgres]: UPDATE "users" SET "id" = %s, "updatedAt" = %s WHERE "id" = %s;
[2024-02-05 10:23:48.151092] : Dataloom[postgres]: DROP TABLE IF EXISTS "posts" CASCADE;
[2024-02-05 10:23:48.180089] : Dataloom[postgres]: CREATE TABLE IF NOT EXISTS "posts" ("completed" BOOLEAN DEFAULT False, "id" BIGSERIAL PRIMARY KEY UNIQUE NOT NULL, "title" VARCHAR(255) NOT NULL, "createdAt" TIMESTAMP DEFAULT CURRENT_TIMESTAMP, "userId" BIGSERIAL NOT NULL REFERENCES "users"("id") ON DELETE CASCADE ON UPDATE CASCADE);
[2024-02-05 10:23:48.213090] : Dataloom[postgres]: DROP TABLE IF EXISTS "users" CASCADE;
[2024-02-05 10:23:48.250243] : Dataloom[postgres]: CREATE TABLE IF NOT EXISTS "users" ("id" BIGSERIAL PRIMARY KEY UNIQUE NOT NULL, "name" TEXT NOT NULL DEFAULT 'Bob', "username" VARCHAR(255) UNIQUE, "createdAt" TIMESTAMP DEFAULT CURRENT_TIMESTAMP, "updatedAt" TIMESTAMP DEFAULT CURRENT_TIMESTAMP);
[2024-02-05 10:23:48.284271] : Dataloom[postgres]: SELECT tablename FROM pg_catalog.pg_tables WHERE schemaname='public';
[2024-02-05 10:23:48.315087] : Dataloom[postgres]: INSERT INTO "users" ("username") VALUES (%s) RETURNING "id";
[2024-02-05 10:23:48.339091] : Dataloom[postgres]: INSERT INTO "posts" ("title", "userId") VALUES (%s, %s) RETURNING *;
[2024-02-05 10:23:48.430876] : Dataloom[postgres]: 
        UPDATE "users" SET "name" = %s, "updatedAt" = %s WHERE "id" = (
            SELECT "id" FROM  "users" WHERE "username" = %s LIMIT 1
        );
        
[2024-02-05 10:23:48.469866] : Dataloom[postgres]: 
        UPDATE "users" SET "name" = %s, "updatedAt" = %s WHERE "id" = (
            SELECT "id" FROM  "users" WHERE "username" = %s LIMIT 1
        );
        
[2024-02-05 10:23:48.506921] : Dataloom[postgres]: SELECT "createdAt", "id", "name", "updatedAt", "username" FROM "users" WHERE "id" = %s;
[2024-02-05 10:23:48.545937] : Dataloom[postgres]: 
        UPDATE "users" SET "id" = %s, "updatedAt" = %s WHERE "id" = (
            SELECT "id" FROM  "users" WHERE "username" = %s LIMIT 1
        );
        
[2024-02-05 10:23:48.746902] : Dataloom[postgres]: DROP TABLE IF EXISTS "posts" CASCADE;
[2024-02-05 10:23:48.785906] : Dataloom[postgres]: CREATE TABLE IF NOT EXISTS "posts" ("completed" BOOLEAN DEFAULT False, "id" BIGSERIAL PRIMARY KEY UNIQUE NOT NULL, "title" VARCHAR(255) NOT NULL, "createdAt" TIMESTAMP DEFAULT CURRENT_TIMESTAMP, "userId" BIGSERIAL NOT NULL REFERENCES "users"("id") ON DELETE CASCADE ON UPDATE CASCADE);
[2024-02-05 10:23:48.848117] : Dataloom[postgres]: DROP TABLE IF EXISTS "users" CASCADE;
[2024-02-05 10:23:48.903391] : Dataloom[postgres]: CREATE TABLE IF NOT EXISTS "users" ("id" BIGSERIAL PRIMARY KEY UNIQUE NOT NULL, "name" TEXT NOT NULL DEFAULT 'Bob', "username" VARCHAR(255) UNIQUE, "createdAt" TIMESTAMP DEFAULT CURRENT_TIMESTAMP, "updatedAt" TIMESTAMP DEFAULT CURRENT_TIMESTAMP);
[2024-02-05 10:23:48.962130] : Dataloom[postgres]: SELECT tablename FROM pg_catalog.pg_tables WHERE schemaname='public';
[2024-02-05 10:23:49.015646] : Dataloom[postgres]: INSERT INTO "users" ("username") VALUES (%s) RETURNING "id";
[2024-02-05 10:23:49.039292] : Dataloom[postgres]: INSERT INTO "posts" ("title", "userId") VALUES (%s, %s) RETURNING *;
[2024-02-05 10:23:49.071221] : Dataloom[postgres]: UPDATE "posts" SET "title" = %s WHERE "userId" = %s;
[2024-02-05 10:23:49.091224] : Dataloom[postgres]: UPDATE "posts" SET "title" = %s WHERE "userId" = %s;
[2024-02-05 10:23:49.112890] : Dataloom[postgres]: UPDATE "posts" SET "userId" = %s WHERE "userId" = %s;
[2024-02-05 10:23:49.161729] : Dataloom[sqlite]: DROP TABLE IF EXISTS users;
[2024-02-05 10:23:49.200726] : Dataloom[sqlite]: DROP TABLE IF EXISTS users;
[2024-02-05 10:23:49.229731] : Dataloom[sqlite]: DROP TABLE IF EXISTS users;
[2024-02-05 10:23:49.255743] : Dataloom[sqlite]: CREATE TABLE IF NOT EXISTS `users` (`id` INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL, `name` VARCHAR, `username` TEXT NOT NULL);
[2024-02-05 10:23:49.283753] : Dataloom[sqlite]: DROP TABLE IF EXISTS posts;
[2024-02-05 10:23:49.312725] : Dataloom[sqlite]: CREATE TABLE IF NOT EXISTS `posts` (`id` INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL, `title` TEXT NOT NULL);
[2024-02-05 10:23:49.343728] : Dataloom[sqlite]: SELECT name FROM sqlite_master WHERE type='table';
[2024-02-05 10:23:49.375728] : Dataloom[sqlite]: DROP TABLE IF EXISTS users;
[2024-02-05 10:23:49.411074] : Dataloom[sqlite]: CREATE TABLE IF NOT EXISTS `users` (`id` INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL, `name` VARCHAR UNIQUE, `username` TEXT NOT NULL DEFAULT 'Hello there!!');
[2024-02-05 10:23:49.444332] : Dataloom[sqlite]: DROP TABLE IF EXISTS posts;
[2024-02-05 10:23:49.481331] : Dataloom[sqlite]: CREATE TABLE IF NOT EXISTS `posts` (`completed` BOOLEAN DEFAULT False, `id` INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL, `title` VARCHAR NOT NULL);
[2024-02-05 10:23:49.516334] : Dataloom[sqlite]: SELECT name FROM sqlite_master WHERE type='table';
[2024-02-05 10:23:49.558786] : Dataloom[sqlite]: DROP TABLE IF EXISTS posts;
[2024-02-05 10:23:49.590797] : Dataloom[sqlite]: CREATE TABLE IF NOT EXISTS `posts` (`completed` BOOLEAN DEFAULT False, `id` INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL, `title` VARCHAR NOT NULL, `createdAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP, `updatedAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP, `userId` INTEGER NOT NULL REFERENCES `users`(`id`) ON DELETE CASCADE ON UPDATE CASCADE);
[2024-02-05 10:23:49.625786] : Dataloom[sqlite]: DROP TABLE IF EXISTS users;
[2024-02-05 10:23:49.662345] : Dataloom[sqlite]: CREATE TABLE IF NOT EXISTS `users` (`id` INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL, `name` TEXT NOT NULL DEFAULT 'Bob', `username` VARCHAR UNIQUE, `createdAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP, `updatedAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP);
[2024-02-05 10:23:49.689986] : Dataloom[sqlite]: SELECT name FROM sqlite_master WHERE type='table';
[2024-02-05 10:23:49.712344] : Dataloom[sqlite]: INSERT INTO `users` (`name`, `username`) VALUES (?, ?);
[2024-02-05 10:23:49.741349] : Dataloom[sqlite]: DELETE FROM `users` WHERE `id` = ?;
[2024-02-05 10:23:49.774348] : Dataloom[sqlite]: DELETE FROM `users` WHERE `id` = ?;
[2024-02-05 10:23:49.804346] : Dataloom[sqlite]: DROP TABLE IF EXISTS posts;
[2024-02-05 10:23:49.828342] : Dataloom[sqlite]: CREATE TABLE IF NOT EXISTS `posts` (`completed` BOOLEAN DEFAULT False, `id` INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL, `title` VARCHAR NOT NULL, `createdAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP, `updatedAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP, `userId` INTEGER NOT NULL REFERENCES `users`(`id`) ON DELETE CASCADE ON UPDATE CASCADE);
[2024-02-05 10:23:49.852925] : Dataloom[sqlite]: DROP TABLE IF EXISTS users;
[2024-02-05 10:23:49.878926] : Dataloom[sqlite]: CREATE TABLE IF NOT EXISTS `users` (`id` INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL, `name` TEXT NOT NULL DEFAULT 'Bob', `username` VARCHAR UNIQUE, `createdAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP, `updatedAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP);
[2024-02-05 10:23:49.905063] : Dataloom[sqlite]: SELECT name FROM sqlite_master WHERE type='table';
[2024-02-05 10:23:49.927409] : Dataloom[sqlite]: INSERT INTO `users` (`name`, `username`) VALUES (?, ?);
[2024-02-05 10:23:49.955928] : Dataloom[sqlite]: 
    DELETE FROM `users` WHERE `id` = (
        SELECT `id` FROM  `users` WHERE `name` = ? LIMIT 1
    );
    
[2024-02-05 10:23:49.982926] : Dataloom[sqlite]: SELECT `createdAt`, `id`, `name`, `updatedAt`, `username` FROM `users` WHERE `name` = ?   ;
[2024-02-05 10:23:50.006927] : Dataloom[sqlite]: 
    DELETE FROM `users` WHERE `id` = (
        SELECT `id` FROM  `users` WHERE `name` = ? AND `id` = ? LIMIT 1
    );
    
[2024-02-05 10:23:50.037924] : Dataloom[sqlite]: SELECT `createdAt`, `id`, `name`, `updatedAt`, `username` FROM `users` WHERE `name` = ?   ;
[2024-02-05 10:23:50.075681] : Dataloom[sqlite]: 
    DELETE FROM `users` WHERE `id` = (
        SELECT `id` FROM  `users` WHERE `name` = ? AND `id` = ? LIMIT 1
    );
    
[2024-02-05 10:23:50.124687] : Dataloom[sqlite]: SELECT `createdAt`, `id`, `name`, `updatedAt`, `username` FROM `users` WHERE `name` = ?   ;
[2024-02-05 10:23:50.164031] : Dataloom[sqlite]: DROP TABLE IF EXISTS posts;
[2024-02-05 10:23:50.207687] : Dataloom[sqlite]: CREATE TABLE IF NOT EXISTS `posts` (`completed` BOOLEAN DEFAULT False, `id` INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL, `title` VARCHAR NOT NULL, `createdAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP, `updatedAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP, `userId` INTEGER NOT NULL REFERENCES `users`(`id`) ON DELETE CASCADE ON UPDATE CASCADE);
[2024-02-05 10:23:50.257685] : Dataloom[sqlite]: DROP TABLE IF EXISTS users;
[2024-02-05 10:23:50.304698] : Dataloom[sqlite]: CREATE TABLE IF NOT EXISTS `users` (`id` INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL, `name` TEXT NOT NULL DEFAULT 'Bob', `username` VARCHAR UNIQUE, `createdAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP, `updatedAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP);
[2024-02-05 10:23:50.338683] : Dataloom[sqlite]: SELECT name FROM sqlite_master WHERE type='table';
[2024-02-05 10:23:50.364277] : Dataloom[sqlite]: INSERT INTO `users` (`name`, `username`) VALUES (?, ?);
[2024-02-05 10:23:50.395247] : Dataloom[sqlite]: DELETE FROM `users` WHERE `name` = ?;
[2024-02-05 10:23:50.424245] : Dataloom[sqlite]: SELECT `createdAt`, `id`, `name`, `updatedAt`, `username` FROM `users` WHERE `name` = ?   ;
[2024-02-05 10:23:50.448790] : Dataloom[sqlite]: INSERT INTO `users` (`name`, `username`) VALUES (?, ?);
[2024-02-05 10:23:50.475797] : Dataloom[sqlite]: DELETE FROM `users` WHERE `name` = ? AND `id` = ?;
[2024-02-05 10:23:50.502852] : Dataloom[sqlite]: SELECT `createdAt`, `id`, `name`, `updatedAt`, `username` FROM `users` WHERE `name` = ?   ;
[2024-02-05 10:23:50.523791] : Dataloom[sqlite]: DELETE FROM `users` WHERE `name` = ? AND `id` = ?;
[2024-02-05 10:23:50.552232] : Dataloom[sqlite]: SELECT `createdAt`, `id`, `name`, `updatedAt`, `username` FROM `users` WHERE `name` = ?   ;
[2024-02-05 10:23:50.581792] : Dataloom[sqlite]: DROP TABLE IF EXISTS posts;
[2024-02-05 10:23:50.617164] : Dataloom[sqlite]: CREATE TABLE IF NOT EXISTS `posts` (`completed` BOOLEAN DEFAULT False, `id` INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL, `title` VARCHAR NOT NULL, `createdAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP, `updatedAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP, `userId` INTEGER NOT NULL REFERENCES `users`(`id`) ON DELETE CASCADE ON UPDATE CASCADE);
[2024-02-05 10:23:50.647239] : Dataloom[sqlite]: DROP TABLE IF EXISTS users;
[2024-02-05 10:23:50.677236] : Dataloom[sqlite]: CREATE TABLE IF NOT EXISTS `users` (`id` INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL, `name` TEXT NOT NULL DEFAULT 'Bob', `username` VARCHAR UNIQUE, `createdAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP, `updatedAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP);
[2024-02-05 10:23:50.707241] : Dataloom[sqlite]: SELECT name FROM sqlite_master WHERE type='table';
[2024-02-05 10:23:50.733235] : Dataloom[sqlite]: INSERT INTO `users` (`username`) VALUES (?);
[2024-02-05 10:23:50.766239] : Dataloom[sqlite]: INSERT INTO `posts` (`title`, `userId`) VALUES (?, ?);
[2024-02-05 10:23:50.814240] : Dataloom[sqlite]: DROP TABLE IF EXISTS posts;
[2024-02-05 10:23:50.909241] : Dataloom[sqlite]: CREATE TABLE IF NOT EXISTS `posts` (`completed` BOOLEAN DEFAULT False, `id` INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL, `title` VARCHAR NOT NULL, `createdAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP, `updatedAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP, `userId` INTEGER NOT NULL REFERENCES `users`(`id`) ON DELETE CASCADE ON UPDATE CASCADE);
[2024-02-05 10:23:50.993470] : Dataloom[sqlite]: DROP TABLE IF EXISTS users;
[2024-02-05 10:23:51.037808] : Dataloom[sqlite]: CREATE TABLE IF NOT EXISTS `users` (`id` INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL, `name` TEXT NOT NULL DEFAULT 'Bob', `username` VARCHAR UNIQUE, `createdAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP, `updatedAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP);
[2024-02-05 10:23:51.065910] : Dataloom[sqlite]: SELECT name FROM sqlite_master WHERE type='table';
[2024-02-05 10:23:51.090059] : Dataloom[sqlite]: INSERT INTO `users` (`username`) VALUES (?);
[2024-02-05 10:23:51.116059] : Dataloom[sqlite]: INSERT INTO `posts` (`title`, `userId`) VALUES (?, ?);
[2024-02-05 10:23:51.144058] : Dataloom[sqlite]: DROP TABLE IF EXISTS posts;
[2024-02-05 10:23:51.169063] : Dataloom[sqlite]: CREATE TABLE IF NOT EXISTS `posts` (`completed` BOOLEAN DEFAULT False, `id` INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL, `title` VARCHAR NOT NULL, `createdAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP, `updatedAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP, `userId` INTEGER NOT NULL REFERENCES `users`(`id`) ON DELETE CASCADE ON UPDATE CASCADE);
[2024-02-05 10:23:51.194061] : Dataloom[sqlite]: DROP TABLE IF EXISTS users;
[2024-02-05 10:23:51.224061] : Dataloom[sqlite]: CREATE TABLE IF NOT EXISTS `users` (`id` INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL, `name` TEXT NOT NULL DEFAULT 'Bob', `username` VARCHAR UNIQUE);
[2024-02-05 10:23:51.253060] : Dataloom[sqlite]: SELECT name FROM sqlite_master WHERE type='table';
[2024-02-05 10:23:51.273062] : Dataloom[sqlite]: INSERT INTO `users` (`username`) VALUES (?);
[2024-02-05 10:23:51.304062] : Dataloom[sqlite]: INSERT INTO `posts` (`title`, `userId`) VALUES (?, ?);
[2024-02-05 10:23:51.327061] : Dataloom[sqlite]: SELECT `id`, `name`, `username` FROM `users` WHERE `id` = ?;
[2024-02-05 10:23:51.355412] : Dataloom[sqlite]: SELECT `id`, `name`, `username` FROM `users` WHERE `id` = ?;
[2024-02-05 10:23:51.380505] : Dataloom[sqlite]: SELECT `id`, `completed` FROM `posts` WHERE `id` = ?;
[2024-02-05 10:23:51.408510] : Dataloom[sqlite]: DROP TABLE IF EXISTS posts;
[2024-02-05 10:23:51.437507] : Dataloom[sqlite]: CREATE TABLE IF NOT EXISTS `posts` (`completed` BOOLEAN DEFAULT False, `id` INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL, `title` VARCHAR NOT NULL, `createdAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP, `updatedAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP, `userId` INTEGER NOT NULL REFERENCES `users`(`id`) ON DELETE CASCADE ON UPDATE CASCADE);
[2024-02-05 10:23:51.463509] : Dataloom[sqlite]: DROP TABLE IF EXISTS users;
[2024-02-05 10:23:51.494134] : Dataloom[sqlite]: CREATE TABLE IF NOT EXISTS `users` (`id` INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL, `name` TEXT NOT NULL DEFAULT 'Bob', `username` VARCHAR UNIQUE);
[2024-02-05 10:23:51.524174] : Dataloom[sqlite]: SELECT name FROM sqlite_master WHERE type='table';
[2024-02-05 10:23:51.548136] : Dataloom[sqlite]: INSERT INTO `users` (`username`) VALUES (?);
[2024-02-05 10:23:51.577634] : Dataloom[sqlite]: INSERT INTO `posts` (`title`, `userId`) VALUES (?, ?);
[2024-02-05 10:23:51.610640] : Dataloom[sqlite]: SELECT `id`, `name`, `username` FROM `users`   ;
[2024-02-05 10:23:51.629635] : Dataloom[sqlite]: SELECT `completed`, `createdAt`, `id`, `title`, `updatedAt`, `userId` FROM `posts`   ;
[2024-02-05 10:23:51.649635] : Dataloom[sqlite]: SELECT `id`, `completed` FROM `posts`  LIMIT 3 OFFSET 3;
[2024-02-05 10:23:51.675742] : Dataloom[sqlite]: DROP TABLE IF EXISTS posts;
[2024-02-05 10:23:51.701741] : Dataloom[sqlite]: CREATE TABLE IF NOT EXISTS `posts` (`completed` BOOLEAN DEFAULT False, `id` INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL, `title` VARCHAR NOT NULL, `createdAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP, `updatedAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP, `userId` INTEGER NOT NULL REFERENCES `users`(`id`) ON DELETE CASCADE ON UPDATE CASCADE);
[2024-02-05 10:23:51.724738] : Dataloom[sqlite]: DROP TABLE IF EXISTS users;
[2024-02-05 10:23:51.751741] : Dataloom[sqlite]: CREATE TABLE IF NOT EXISTS `users` (`id` INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL, `name` TEXT NOT NULL DEFAULT 'Bob', `username` VARCHAR UNIQUE);
[2024-02-05 10:23:51.785747] : Dataloom[sqlite]: SELECT name FROM sqlite_master WHERE type='table';
[2024-02-05 10:23:51.811739] : Dataloom[sqlite]: INSERT INTO `users` (`username`) VALUES (?);
[2024-02-05 10:23:51.835736] : Dataloom[sqlite]: INSERT INTO `posts` (`title`, `userId`) VALUES (?, ?);
[2024-02-05 10:23:51.858739] : Dataloom[sqlite]: SELECT `id`, `name`, `username` FROM `users` WHERE `id` = ?   ;
[2024-02-05 10:23:51.876439] : Dataloom[sqlite]: SELECT `id`, `name`, `username` FROM `users` WHERE `id` = ?   ;
[2024-02-05 10:23:51.894444] : Dataloom[sqlite]: SELECT `id`, `name`, `username` FROM `users` WHERE `id` = ? AND `name` = ?   ;
[2024-02-05 10:23:51.912442] : Dataloom[sqlite]: SELECT `id`, `name`, `username` FROM `users` WHERE `id` = ? AND `username` = ?   ;
[2024-02-05 10:23:51.932443] : Dataloom[sqlite]: SELECT `id`, `name`, `username` FROM `users` WHERE `name` = ? AND `username` = ?   ;
[2024-02-05 10:23:51.963485] : Dataloom[sqlite]: SELECT `id`, `completed` FROM `posts`   ;
[2024-02-05 10:23:52.025162] : Dataloom[sqlite]: DROP TABLE IF EXISTS posts;
[2024-02-05 10:23:52.070161] : Dataloom[sqlite]: CREATE TABLE IF NOT EXISTS `posts` (`completed` BOOLEAN DEFAULT False, `id` INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL, `title` VARCHAR NOT NULL, `createdAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP, `updatedAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP, `userId` INTEGER NOT NULL REFERENCES `users`(`id`) ON DELETE CASCADE ON UPDATE CASCADE);
[2024-02-05 10:23:52.107557] : Dataloom[sqlite]: DROP TABLE IF EXISTS users;
[2024-02-05 10:23:52.137916] : Dataloom[sqlite]: CREATE TABLE IF NOT EXISTS `users` (`id` INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL, `name` TEXT NOT NULL DEFAULT 'Bob', `username` VARCHAR UNIQUE);
[2024-02-05 10:23:52.167557] : Dataloom[sqlite]: SELECT name FROM sqlite_master WHERE type='table';
[2024-02-05 10:23:52.191121] : Dataloom[sqlite]: INSERT INTO `users` (`username`) VALUES (?);
[2024-02-05 10:23:52.220123] : Dataloom[sqlite]: INSERT INTO `posts` (`title`, `userId`) VALUES (?, ?);
[2024-02-05 10:23:52.255122] : Dataloom[sqlite]: SELECT `completed`, `createdAt`, `id`, `title`, `updatedAt`, `userId` FROM `posts` WHERE `id` = ? AND `userId` = ?   ;
[2024-02-05 10:23:52.279126] : Dataloom[sqlite]: SELECT `id`, `name`, `username` FROM `users`   ;
[2024-02-05 10:23:52.308256] : Dataloom[sqlite]: SELECT `id`, `name`, `username` FROM `users` WHERE `id` = ?   ;
[2024-02-05 10:23:52.337124] : Dataloom[sqlite]: SELECT `id`, `name`, `username` FROM `users` WHERE `id` = ?   ;
[2024-02-05 10:23:52.368182] : Dataloom[sqlite]: SELECT `id`, `name`, `username` FROM `users` WHERE `id` = ? AND `name` = ?   ;
[2024-02-05 10:23:52.393707] : Dataloom[sqlite]: SELECT `id`, `name`, `username` FROM `users` WHERE `id` = ? AND `username` = ?   ;
[2024-02-05 10:23:52.415713] : Dataloom[sqlite]: SELECT `id`, `name`, `username` FROM `users` WHERE `name` = ? AND `username` = ?   ;
[2024-02-05 10:23:52.443710] : Dataloom[sqlite]: SELECT `id`, `completed` FROM `posts` WHERE `userId` = ?  LIMIT 3 OFFSET 3;
[2024-02-05 10:23:52.472709] : Dataloom[sqlite]: SELECT `completed`, `createdAt`, `id`, `title`, `updatedAt`, `userId` FROM `posts`   ;
[2024-02-05 10:23:52.509708] : Dataloom[sqlite]: DROP TABLE IF EXISTS posts;
[2024-02-05 10:23:52.544706] : Dataloom[sqlite]: CREATE TABLE IF NOT EXISTS `posts` (`completed` BOOLEAN DEFAULT False, `id` INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL, `title` VARCHAR NOT NULL, `createdAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP, `updatedAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP, `userId` INTEGER NOT NULL REFERENCES `users`(`id`) ON DELETE CASCADE ON UPDATE CASCADE);
[2024-02-05 10:23:52.575709] : Dataloom[sqlite]: DROP TABLE IF EXISTS users;
[2024-02-05 10:23:52.611709] : Dataloom[sqlite]: CREATE TABLE IF NOT EXISTS `users` (`id` INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL, `name` TEXT NOT NULL DEFAULT 'Bob', `username` VARCHAR UNIQUE, `createdAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP, `updatedAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP);
[2024-02-05 10:23:52.652712] : Dataloom[sqlite]: SELECT name FROM sqlite_master WHERE type='table';
[2024-02-05 10:23:52.693292] : Dataloom[sqlite]: INSERT INTO `users` (`username`) VALUES (?);
[2024-02-05 10:23:52.727280] : Dataloom[sqlite]: INSERT INTO `posts` (`title`, `userId`) VALUES (?, ?);
[2024-02-05 10:23:52.892857] : Dataloom[sqlite]: UPDATE `users` SET `updatedAt` = ? WHERE `id` = ?;
[2024-02-05 10:23:52.942914] : Dataloom[sqlite]: UPDATE `users` SET `updatedAt` = ? WHERE `id` = ?;
[2024-02-05 10:23:52.972851] : Dataloom[sqlite]: SELECT `createdAt`, `id`, `name`, `updatedAt`, `username` FROM `users` WHERE `id` = ?;
[2024-02-05 10:23:53.009412] : Dataloom[sqlite]: DROP TABLE IF EXISTS posts;
[2024-02-05 10:23:53.037414] : Dataloom[sqlite]: CREATE TABLE IF NOT EXISTS `posts` (`completed` BOOLEAN DEFAULT False, `id` INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL, `title` VARCHAR NOT NULL, `createdAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP, `userId` INTEGER NOT NULL REFERENCES `users`(`id`) ON DELETE CASCADE ON UPDATE CASCADE);
[2024-02-05 10:23:53.059413] : Dataloom[sqlite]: DROP TABLE IF EXISTS users;
[2024-02-05 10:23:53.080411] : Dataloom[sqlite]: CREATE TABLE IF NOT EXISTS `users` (`id` INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL, `name` TEXT NOT NULL DEFAULT 'Bob', `username` VARCHAR UNIQUE, `createdAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP, `updatedAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP);
[2024-02-05 10:23:53.101944] : Dataloom[sqlite]: SELECT name FROM sqlite_master WHERE type='table';
[2024-02-05 10:23:53.119944] : Dataloom[sqlite]: INSERT INTO `users` (`username`) VALUES (?);
[2024-02-05 10:23:53.148958] : Dataloom[sqlite]: INSERT INTO `posts` (`title`, `userId`) VALUES (?, ?);
[2024-02-05 10:23:53.238510] : Dataloom[sqlite]: 
        UPDATE `posts` SET `title` = ? WHERE `id` = (
            SELECT `id` FROM  `posts` WHERE `userId` = ? LIMIT 1
        );
        
[2024-02-05 10:23:53.289506] : Dataloom[sqlite]: 
        UPDATE `posts` SET `title` = ? WHERE `id` = (
            SELECT `id` FROM  `posts` WHERE `userId` = ? LIMIT 1
        );
        
[2024-02-05 10:23:53.333599] : Dataloom[sqlite]: SELECT `completed`, `createdAt`, `id`, `title`, `userId` FROM `posts` WHERE `id` = ?;
[2024-02-05 10:23:53.442567] : Dataloom[sqlite]: DROP TABLE IF EXISTS posts;
[2024-02-05 10:23:53.573252] : Dataloom[sqlite]: CREATE TABLE IF NOT EXISTS `posts` (`completed` BOOLEAN DEFAULT False, `id` INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL, `title` VARCHAR NOT NULL, `createdAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP, `userId` INTEGER NOT NULL REFERENCES `users`(`id`) ON DELETE CASCADE ON UPDATE CASCADE);
[2024-02-05 10:23:53.635525] : Dataloom[sqlite]: DROP TABLE IF EXISTS users;
[2024-02-05 10:23:53.684392] : Dataloom[sqlite]: CREATE TABLE IF NOT EXISTS `users` (`id` INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL, `name` TEXT NOT NULL DEFAULT 'Bob', `username` VARCHAR UNIQUE, `createdAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP, `updatedAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP);
[2024-02-05 10:23:53.726244] : Dataloom[sqlite]: SELECT name FROM sqlite_master WHERE type='table';
[2024-02-05 10:23:53.758243] : Dataloom[sqlite]: INSERT INTO `users` (`username`) VALUES (?);
[2024-02-05 10:23:53.796373] : Dataloom[sqlite]: INSERT INTO `posts` (`title`, `userId`) VALUES (?, ?);
[2024-02-05 10:23:53.878457] : Dataloom[sqlite]: UPDATE `posts` SET `title` = ? WHERE `userId` = ?;
[2024-02-05 10:23:53.905305] : Dataloom[sqlite]: UPDATE `posts` SET `title` = ? WHERE `userId` = ?;
[2024-02-05 10:23:53.934304] : Dataloom[sqlite]: SELECT `completed`, `createdAt`, `id`, `title`, `userId` FROM `posts` WHERE `id` = ?;
[2024-02-05 10:24:13.214380] : Dataloom[postgres]: DROP TABLE IF EXISTS "posts" CASCADE;
[2024-02-05 10:24:13.254468] : Dataloom[postgres]: CREATE TABLE IF NOT EXISTS "posts" ("completed" BOOLEAN DEFAULT False, "id" BIGSERIAL PRIMARY KEY UNIQUE NOT NULL, "title" VARCHAR(255) NOT NULL, "categoryId" BIGSERIAL NOT NULL REFERENCES "users"("id") ON DELETE CASCADE ON UPDATE CASCADE, "createdAt" TIMESTAMP DEFAULT CURRENT_TIMESTAMP, "updatedAt" TIMESTAMP DEFAULT CURRENT_TIMESTAMP, "userId" BIGSERIAL NOT NULL REFERENCES "users"("id") ON DELETE CASCADE ON UPDATE CASCADE);
[2024-02-05 10:24:13.305805] : Dataloom[postgres]: DROP TABLE IF EXISTS "users" CASCADE;
[2024-02-05 10:24:13.347017] : Dataloom[postgres]: CREATE TABLE IF NOT EXISTS "users" ("id" BIGSERIAL PRIMARY KEY UNIQUE NOT NULL, "name" TEXT NOT NULL DEFAULT 'Bob', "username" VARCHAR(255) UNIQUE);
[2024-02-05 10:24:13.387544] : Dataloom[postgres]: DROP TABLE IF EXISTS "categories" CASCADE;
[2024-02-05 10:24:13.420782] : Dataloom[postgres]: CREATE TABLE IF NOT EXISTS "categories" ("id" BIGSERIAL PRIMARY KEY UNIQUE NOT NULL, "name" VARCHAR(255) NOT NULL);
[2024-02-05 10:24:13.451744] : Dataloom[postgres]: SELECT tablename FROM pg_catalog.pg_tables WHERE schemaname='public';
[2024-02-05 10:24:13.493690] : Dataloom[postgres]: INSERT INTO "users" ("username") VALUES (%s) RETURNING "id";
[2024-02-05 10:24:13.522238] : Dataloom[postgres]: INSERT INTO "categories" ("name") VALUES (%s) RETURNING "id";
[2024-02-05 10:24:13.547368] : Dataloom[postgres]: INSERT INTO "posts" ("categoryId", "title", "userId") VALUES (%s, %s, %s) RETURNING *;
[2024-02-05 10:24:25.615120] : Dataloom[postgres]: DROP TABLE IF EXISTS "posts" CASCADE;
[2024-02-05 10:24:25.655717] : Dataloom[postgres]: CREATE TABLE IF NOT EXISTS "posts" ("completed" BOOLEAN DEFAULT False, "id" BIGSERIAL PRIMARY KEY UNIQUE NOT NULL, "title" VARCHAR(255) NOT NULL, "categoryId" BIGSERIAL NOT NULL REFERENCES "users"("id") ON DELETE CASCADE ON UPDATE CASCADE, "createdAt" TIMESTAMP DEFAULT CURRENT_TIMESTAMP, "updatedAt" TIMESTAMP DEFAULT CURRENT_TIMESTAMP, "userId" BIGSERIAL NOT NULL REFERENCES "users"("id") ON DELETE CASCADE ON UPDATE CASCADE);
[2024-02-05 10:24:25.707690] : Dataloom[postgres]: DROP TABLE IF EXISTS "users" CASCADE;
[2024-02-05 10:24:25.747716] : Dataloom[postgres]: CREATE TABLE IF NOT EXISTS "users" ("id" BIGSERIAL PRIMARY KEY UNIQUE NOT NULL, "name" TEXT NOT NULL DEFAULT 'Bob', "username" VARCHAR(255) UNIQUE);
[2024-02-05 10:24:25.790325] : Dataloom[postgres]: DROP TABLE IF EXISTS "categories" CASCADE;
[2024-02-05 10:24:25.832328] : Dataloom[postgres]: CREATE TABLE IF NOT EXISTS "categories" ("id" BIGSERIAL PRIMARY KEY UNIQUE NOT NULL, "name" VARCHAR(255) NOT NULL);
[2024-02-05 10:24:25.868326] : Dataloom[postgres]: SELECT tablename FROM pg_catalog.pg_tables WHERE schemaname='public';
[2024-02-05 10:24:25.908684] : Dataloom[postgres]: INSERT INTO "users" ("username") VALUES (%s) RETURNING "id";
[2024-02-05 10:24:25.939303] : Dataloom[postgres]: INSERT INTO "categories" ("name") VALUES (%s) RETURNING "id";
[2024-02-05 10:24:25.970636] : Dataloom[postgres]: INSERT INTO "posts" ("categoryId", "title", "userId") VALUES (%s, %s, %s) RETURNING *;
[2024-02-05 10:26:03.442483] : Dataloom[postgres]: DROP TABLE IF EXISTS "posts" CASCADE;
[2024-02-05 10:26:03.480485] : Dataloom[postgres]: CREATE TABLE IF NOT EXISTS "posts" ("completed" BOOLEAN DEFAULT False, "id" BIGSERIAL PRIMARY KEY UNIQUE NOT NULL, "title" VARCHAR(255) NOT NULL, "categoryId" BIGSERIAL NOT NULL REFERENCES "users"("id") ON DELETE CASCADE ON UPDATE CASCADE, "createdAt" TIMESTAMP DEFAULT CURRENT_TIMESTAMP, "updatedAt" TIMESTAMP DEFAULT CURRENT_TIMESTAMP, "userId" BIGSERIAL NOT NULL REFERENCES "users"("id") ON DELETE CASCADE ON UPDATE CASCADE);
[2024-02-05 10:26:03.534442] : Dataloom[postgres]: DROP TABLE IF EXISTS "users" CASCADE;
[2024-02-05 10:26:03.575441] : Dataloom[postgres]: CREATE TABLE IF NOT EXISTS "users" ("id" BIGSERIAL PRIMARY KEY UNIQUE NOT NULL, "name" TEXT NOT NULL DEFAULT 'Bob', "username" VARCHAR(255) UNIQUE);
[2024-02-05 10:26:03.615444] : Dataloom[postgres]: DROP TABLE IF EXISTS "categories" CASCADE;
[2024-02-05 10:26:03.651012] : Dataloom[postgres]: CREATE TABLE IF NOT EXISTS "categories" ("id" BIGSERIAL PRIMARY KEY UNIQUE NOT NULL, "name" VARCHAR(255) NOT NULL);
[2024-02-05 10:26:03.689441] : Dataloom[postgres]: SELECT tablename FROM pg_catalog.pg_tables WHERE schemaname='public';
[2024-02-05 10:26:03.730936] : Dataloom[postgres]: INSERT INTO "users" ("username") VALUES (%s) RETURNING "id";
[2024-02-05 10:26:03.769004] : Dataloom[postgres]: INSERT INTO "categories" ("name") VALUES (%s) RETURNING "id";
[2024-02-05 10:26:03.804937] : Dataloom[postgres]: INSERT INTO "posts" ("categoryId", "title", "userId") VALUES (%s, %s, %s) RETURNING *;
[2024-02-05 10:28:38.668590] : Dataloom[postgres]: DROP TABLE IF EXISTS "posts" CASCADE;
[2024-02-05 10:28:38.697555] : Dataloom[postgres]: CREATE TABLE IF NOT EXISTS "posts" ("completed" BOOLEAN DEFAULT False, "id" BIGSERIAL PRIMARY KEY UNIQUE NOT NULL, "title" VARCHAR(255) NOT NULL, "categoryId" BIGSERIAL NOT NULL REFERENCES "users"("id") ON DELETE CASCADE ON UPDATE CASCADE, "createdAt" TIMESTAMP DEFAULT CURRENT_TIMESTAMP, "updatedAt" TIMESTAMP DEFAULT CURRENT_TIMESTAMP, "userId" BIGSERIAL NOT NULL REFERENCES "users"("id") ON DELETE CASCADE ON UPDATE CASCADE);
[2024-02-05 10:28:38.730596] : Dataloom[postgres]: DROP TABLE IF EXISTS "users" CASCADE;
[2024-02-05 10:28:38.762600] : Dataloom[postgres]: CREATE TABLE IF NOT EXISTS "users" ("id" BIGSERIAL PRIMARY KEY UNIQUE NOT NULL, "name" TEXT NOT NULL DEFAULT 'Bob', "username" VARCHAR(255) UNIQUE);
[2024-02-05 10:28:38.794512] : Dataloom[postgres]: DROP TABLE IF EXISTS "categories" CASCADE;
[2024-02-05 10:28:38.818465] : Dataloom[postgres]: CREATE TABLE IF NOT EXISTS "categories" ("id" BIGSERIAL PRIMARY KEY UNIQUE NOT NULL, "name" VARCHAR(255) NOT NULL);
[2024-02-05 10:28:38.843468] : Dataloom[postgres]: SELECT tablename FROM pg_catalog.pg_tables WHERE schemaname='public';
[2024-02-05 10:28:38.875466] : Dataloom[postgres]: INSERT INTO "users" ("username") VALUES (%s) RETURNING "id";
[2024-02-05 10:28:38.897108] : Dataloom[postgres]: INSERT INTO "categories" ("name") VALUES (%s) RETURNING "id";
[2024-02-05 10:28:38.922239] : Dataloom[postgres]: INSERT INTO "posts" ("categoryId", "title", "userId") VALUES (%s, %s, %s) RETURNING *;
[2024-02-05 10:30:34.281667] : Dataloom[postgres]: DROP TABLE IF EXISTS "posts" CASCADE;
[2024-02-05 10:30:34.325665] : Dataloom[postgres]: CREATE TABLE IF NOT EXISTS "posts" ("completed" BOOLEAN DEFAULT False, "id" BIGSERIAL PRIMARY KEY UNIQUE NOT NULL, "title" VARCHAR(255) NOT NULL, "categoryId" BIGSERIAL NOT NULL REFERENCES "categories"("id") ON DELETE CASCADE ON UPDATE CASCADE, "createdAt" TIMESTAMP DEFAULT CURRENT_TIMESTAMP, "updatedAt" TIMESTAMP DEFAULT CURRENT_TIMESTAMP, "userId" BIGSERIAL NOT NULL REFERENCES "users"("id") ON DELETE CASCADE ON UPDATE CASCADE);
[2024-02-05 10:30:34.377748] : Dataloom[postgres]: DROP TABLE IF EXISTS "users" CASCADE;
[2024-02-05 10:30:34.418707] : Dataloom[postgres]: CREATE TABLE IF NOT EXISTS "users" ("id" BIGSERIAL PRIMARY KEY UNIQUE NOT NULL, "name" TEXT NOT NULL DEFAULT 'Bob', "username" VARCHAR(255) UNIQUE);
[2024-02-05 10:30:34.457711] : Dataloom[postgres]: DROP TABLE IF EXISTS "categories" CASCADE;
[2024-02-05 10:30:34.492711] : Dataloom[postgres]: CREATE TABLE IF NOT EXISTS "categories" ("id" BIGSERIAL PRIMARY KEY UNIQUE NOT NULL, "name" VARCHAR(255) NOT NULL);
[2024-02-05 10:30:34.525708] : Dataloom[postgres]: SELECT tablename FROM pg_catalog.pg_tables WHERE schemaname='public';
[2024-02-05 10:30:34.566091] : Dataloom[postgres]: INSERT INTO "users" ("username") VALUES (%s) RETURNING "id";
[2024-02-05 10:30:34.595112] : Dataloom[postgres]: INSERT INTO "categories" ("name") VALUES (%s) RETURNING "id";
[2024-02-05 10:30:34.624121] : Dataloom[postgres]: INSERT INTO "posts" ("categoryId", "title", "userId") VALUES (%s, %s, %s) RETURNING *;
[2024-02-05 10:30:34.660153] : Dataloom[postgres]: 
        SELECT 
            parent."id" AS "posts_id", parent."completed" AS "posts_completed", parent."title" AS "posts_title", parent."createdAt" AS "posts_createdAt",
            child_user."id" AS "users_id", child_user."username" AS "users_username", child_user."name" AS "users_name"child_category."id" AS "categories_id", child_category."name" AS "categories_name"
        FROM 
            posts parent
        JOIN users child_user ON parent."userId" = child_user.id JOIN categories child_category ON parent."categoryId" = child_category.id 
        WHERE 
            parent."id" = %s;
    
[2024-02-05 10:38:31.654514] : Dataloom[postgres]: DROP TABLE IF EXISTS "posts" CASCADE;
[2024-02-05 10:38:31.729209] : Dataloom[postgres]: CREATE TABLE IF NOT EXISTS "posts" ("completed" BOOLEAN DEFAULT False, "id" BIGSERIAL PRIMARY KEY UNIQUE NOT NULL, "title" VARCHAR(255) NOT NULL, "categoryId" BIGSERIAL NOT NULL REFERENCES "categories"("id") ON DELETE CASCADE ON UPDATE CASCADE, "createdAt" TIMESTAMP DEFAULT CURRENT_TIMESTAMP, "updatedAt" TIMESTAMP DEFAULT CURRENT_TIMESTAMP, "userId" BIGSERIAL NOT NULL REFERENCES "users"("id") ON DELETE CASCADE ON UPDATE CASCADE);
[2024-02-05 10:38:31.807219] : Dataloom[postgres]: DROP TABLE IF EXISTS "users" CASCADE;
[2024-02-05 10:38:31.871343] : Dataloom[postgres]: CREATE TABLE IF NOT EXISTS "users" ("id" BIGSERIAL PRIMARY KEY UNIQUE NOT NULL, "name" TEXT NOT NULL DEFAULT 'Bob', "username" VARCHAR(255) UNIQUE);
[2024-02-05 10:38:31.938342] : Dataloom[postgres]: DROP TABLE IF EXISTS "categories" CASCADE;
[2024-02-05 10:38:31.998411] : Dataloom[postgres]: CREATE TABLE IF NOT EXISTS "categories" ("id" BIGSERIAL PRIMARY KEY UNIQUE NOT NULL, "name" VARCHAR(255) NOT NULL);
[2024-02-05 10:38:32.082821] : Dataloom[postgres]: SELECT tablename FROM pg_catalog.pg_tables WHERE schemaname='public';
[2024-02-05 10:38:32.147029] : Dataloom[postgres]: INSERT INTO "users" ("username") VALUES (%s) RETURNING "id";
[2024-02-05 10:38:32.177731] : Dataloom[postgres]: INSERT INTO "categories" ("name") VALUES (%s) RETURNING "id";
[2024-02-05 10:38:32.198731] : Dataloom[postgres]: INSERT INTO "posts" ("categoryId", "title", "userId") VALUES (%s, %s, %s) RETURNING *;
[2024-02-05 10:38:32.254736] : Dataloom[postgres]: 
        SELECT 
            parent."id" AS "posts_id", parent."completed" AS "posts_completed", parent."title" AS "posts_title", parent."createdAt" AS "posts_createdAt",
            child_user."id" AS "users_id", child_user."username" AS "users_username", child_user."name" AS "users_name"child_category."id" AS "categories_id", child_category."name" AS "categories_name"
        FROM 
            posts parent
        JOIN users child_user ON parent."userId" = child_user.id JOIN categories child_category ON parent."categoryId" = child_category.id 
        WHERE 
            parent."id" = %s;
    
[2024-02-05 10:39:46.911693] : Dataloom[postgres]: DROP TABLE IF EXISTS "posts" CASCADE;
[2024-02-05 10:39:46.955662] : Dataloom[postgres]: CREATE TABLE IF NOT EXISTS "posts" ("completed" BOOLEAN DEFAULT False, "id" BIGSERIAL PRIMARY KEY UNIQUE NOT NULL, "title" VARCHAR(255) NOT NULL, "categoryId" BIGSERIAL NOT NULL REFERENCES "categories"("id") ON DELETE CASCADE ON UPDATE CASCADE, "createdAt" TIMESTAMP DEFAULT CURRENT_TIMESTAMP, "updatedAt" TIMESTAMP DEFAULT CURRENT_TIMESTAMP, "userId" BIGSERIAL NOT NULL REFERENCES "users"("id") ON DELETE CASCADE ON UPDATE CASCADE);
[2024-02-05 10:39:47.007273] : Dataloom[postgres]: DROP TABLE IF EXISTS "users" CASCADE;
[2024-02-05 10:39:47.049338] : Dataloom[postgres]: CREATE TABLE IF NOT EXISTS "users" ("id" BIGSERIAL PRIMARY KEY UNIQUE NOT NULL, "name" TEXT NOT NULL DEFAULT 'Bob', "username" VARCHAR(255) UNIQUE);
[2024-02-05 10:39:47.089235] : Dataloom[postgres]: DROP TABLE IF EXISTS "categories" CASCADE;
[2024-02-05 10:39:47.123566] : Dataloom[postgres]: CREATE TABLE IF NOT EXISTS "categories" ("id" BIGSERIAL PRIMARY KEY UNIQUE NOT NULL, "name" VARCHAR(255) NOT NULL);
[2024-02-05 10:39:47.155675] : Dataloom[postgres]: SELECT tablename FROM pg_catalog.pg_tables WHERE schemaname='public';
[2024-02-05 10:39:47.197035] : Dataloom[postgres]: INSERT INTO "users" ("username") VALUES (%s) RETURNING "id";
[2024-02-05 10:39:47.231028] : Dataloom[postgres]: INSERT INTO "categories" ("name") VALUES (%s) RETURNING "id";
[2024-02-05 10:39:47.261032] : Dataloom[postgres]: INSERT INTO "posts" ("categoryId", "title", "userId") VALUES (%s, %s, %s) RETURNING *;
[2024-02-05 10:39:47.301026] : Dataloom[postgres]: 
        SELECT 
            parent."id" AS "posts_id", parent."completed" AS "posts_completed", parent."title" AS "posts_title", parent."createdAt" AS "posts_createdAt",
            , child_user."id" AS "users_id", child_user."username" AS "users_username", child_user."name" AS "users_name"child_category."id" AS "categories_id", child_category."name" AS "categories_name"
        FROM 
            posts parent
        JOIN users child_user ON parent."userId" = child_user.id JOIN categories child_category ON parent."categoryId" = child_category.id 
        WHERE 
            parent."id" = %s;
    
[2024-02-05 10:40:20.240897] : Dataloom[postgres]: DROP TABLE IF EXISTS "posts" CASCADE;
[2024-02-05 10:40:20.284226] : Dataloom[postgres]: CREATE TABLE IF NOT EXISTS "posts" ("completed" BOOLEAN DEFAULT False, "id" BIGSERIAL PRIMARY KEY UNIQUE NOT NULL, "title" VARCHAR(255) NOT NULL, "categoryId" BIGSERIAL NOT NULL REFERENCES "categories"("id") ON DELETE CASCADE ON UPDATE CASCADE, "createdAt" TIMESTAMP DEFAULT CURRENT_TIMESTAMP, "updatedAt" TIMESTAMP DEFAULT CURRENT_TIMESTAMP, "userId" BIGSERIAL NOT NULL REFERENCES "users"("id") ON DELETE CASCADE ON UPDATE CASCADE);
[2024-02-05 10:40:20.344081] : Dataloom[postgres]: DROP TABLE IF EXISTS "users" CASCADE;
[2024-02-05 10:40:20.380122] : Dataloom[postgres]: CREATE TABLE IF NOT EXISTS "users" ("id" BIGSERIAL PRIMARY KEY UNIQUE NOT NULL, "name" TEXT NOT NULL DEFAULT 'Bob', "username" VARCHAR(255) UNIQUE);
[2024-02-05 10:40:20.415075] : Dataloom[postgres]: DROP TABLE IF EXISTS "categories" CASCADE;
[2024-02-05 10:40:20.441070] : Dataloom[postgres]: CREATE TABLE IF NOT EXISTS "categories" ("id" BIGSERIAL PRIMARY KEY UNIQUE NOT NULL, "name" VARCHAR(255) NOT NULL);
[2024-02-05 10:40:20.466069] : Dataloom[postgres]: SELECT tablename FROM pg_catalog.pg_tables WHERE schemaname='public';
[2024-02-05 10:40:20.496884] : Dataloom[postgres]: INSERT INTO "users" ("username") VALUES (%s) RETURNING "id";
[2024-02-05 10:40:20.521910] : Dataloom[postgres]: INSERT INTO "categories" ("name") VALUES (%s) RETURNING "id";
[2024-02-05 10:40:20.545908] : Dataloom[postgres]: INSERT INTO "posts" ("categoryId", "title", "userId") VALUES (%s, %s, %s) RETURNING *;
[2024-02-05 10:40:20.584943] : Dataloom[postgres]: 
        SELECT 
            parent."id" AS "posts_id", parent."completed" AS "posts_completed", parent."title" AS "posts_title", parent."createdAt" AS "posts_createdAt"
            , child_user."id" AS "users_id", child_user."username" AS "users_username", child_user."name" AS "users_name"child_category."id" AS "categories_id", child_category."name" AS "categories_name"
        FROM 
            posts parent
        JOIN users child_user ON parent."userId" = child_user.id JOIN categories child_category ON parent."categoryId" = child_category.id 
        WHERE 
            parent."id" = %s;
    
[2024-02-05 10:40:47.599788] : Dataloom[postgres]: DROP TABLE IF EXISTS "posts" CASCADE;
[2024-02-05 10:40:47.651283] : Dataloom[postgres]: CREATE TABLE IF NOT EXISTS "posts" ("completed" BOOLEAN DEFAULT False, "id" BIGSERIAL PRIMARY KEY UNIQUE NOT NULL, "title" VARCHAR(255) NOT NULL, "categoryId" BIGSERIAL NOT NULL REFERENCES "categories"("id") ON DELETE CASCADE ON UPDATE CASCADE, "createdAt" TIMESTAMP DEFAULT CURRENT_TIMESTAMP, "updatedAt" TIMESTAMP DEFAULT CURRENT_TIMESTAMP, "userId" BIGSERIAL NOT NULL REFERENCES "users"("id") ON DELETE CASCADE ON UPDATE CASCADE);
[2024-02-05 10:40:47.709134] : Dataloom[postgres]: DROP TABLE IF EXISTS "users" CASCADE;
[2024-02-05 10:40:47.756943] : Dataloom[postgres]: CREATE TABLE IF NOT EXISTS "users" ("id" BIGSERIAL PRIMARY KEY UNIQUE NOT NULL, "name" TEXT NOT NULL DEFAULT 'Bob', "username" VARCHAR(255) UNIQUE);
[2024-02-05 10:40:47.797793] : Dataloom[postgres]: DROP TABLE IF EXISTS "categories" CASCADE;
[2024-02-05 10:40:47.833833] : Dataloom[postgres]: CREATE TABLE IF NOT EXISTS "categories" ("id" BIGSERIAL PRIMARY KEY UNIQUE NOT NULL, "name" VARCHAR(255) NOT NULL);
[2024-02-05 10:40:47.864385] : Dataloom[postgres]: SELECT tablename FROM pg_catalog.pg_tables WHERE schemaname='public';
[2024-02-05 10:40:47.898630] : Dataloom[postgres]: INSERT INTO "users" ("username") VALUES (%s) RETURNING "id";
[2024-02-05 10:40:47.928738] : Dataloom[postgres]: INSERT INTO "categories" ("name") VALUES (%s) RETURNING "id";
[2024-02-05 10:40:47.952303] : Dataloom[postgres]: INSERT INTO "posts" ("categoryId", "title", "userId") VALUES (%s, %s, %s) RETURNING *;
[2024-02-05 10:40:47.982306] : Dataloom[postgres]: 
        SELECT 
            parent."id" AS "posts_id", parent."completed" AS "posts_completed", parent."title" AS "posts_title", parent."createdAt" AS "posts_createdAt"
            , child_user."id" AS "users_id", child_user."username" AS "users_username", child_user."name" AS "users_name"child_category."id" AS "categories_id", child_category."name" AS "categories_name"
        FROM 
            posts parent
        , JOIN users child_user ON parent."userId" = child_user.id JOIN categories child_category ON parent."categoryId" = child_category.id 
        WHERE 
            parent."id" = %s;
    
[2024-02-05 10:44:55.936391] : Dataloom[postgres]: DROP TABLE IF EXISTS "posts" CASCADE;
[2024-02-05 10:44:55.981287] : Dataloom[postgres]: CREATE TABLE IF NOT EXISTS "posts" ("completed" BOOLEAN DEFAULT False, "id" BIGSERIAL PRIMARY KEY UNIQUE NOT NULL, "title" VARCHAR(255) NOT NULL, "categoryId" BIGSERIAL NOT NULL REFERENCES "categories"("id") ON DELETE CASCADE ON UPDATE CASCADE, "createdAt" TIMESTAMP DEFAULT CURRENT_TIMESTAMP, "updatedAt" TIMESTAMP DEFAULT CURRENT_TIMESTAMP, "userId" BIGSERIAL NOT NULL REFERENCES "users"("id") ON DELETE CASCADE ON UPDATE CASCADE);
[2024-02-05 10:44:56.035289] : Dataloom[postgres]: DROP TABLE IF EXISTS "users" CASCADE;
[2024-02-05 10:44:56.073966] : Dataloom[postgres]: CREATE TABLE IF NOT EXISTS "users" ("id" BIGSERIAL PRIMARY KEY UNIQUE NOT NULL, "name" TEXT NOT NULL DEFAULT 'Bob', "username" VARCHAR(255) UNIQUE);
[2024-02-05 10:44:56.115287] : Dataloom[postgres]: DROP TABLE IF EXISTS "categories" CASCADE;
[2024-02-05 10:44:56.166957] : Dataloom[postgres]: CREATE TABLE IF NOT EXISTS "categories" ("id" BIGSERIAL PRIMARY KEY UNIQUE NOT NULL, "name" VARCHAR(255) NOT NULL);
[2024-02-05 10:44:56.212944] : Dataloom[postgres]: SELECT tablename FROM pg_catalog.pg_tables WHERE schemaname='public';
[2024-02-05 10:44:56.264311] : Dataloom[postgres]: INSERT INTO "users" ("username") VALUES (%s) RETURNING "id";
[2024-02-05 10:44:56.298980] : Dataloom[postgres]: INSERT INTO "categories" ("name") VALUES (%s) RETURNING "id";
[2024-02-05 10:44:56.332944] : Dataloom[postgres]: INSERT INTO "posts" ("categoryId", "title", "userId") VALUES (%s, %s, %s) RETURNING *;
[2024-02-05 10:44:56.369945] : Dataloom[postgres]: 
        SELECT 
            parent."id" AS "posts_id", parent."completed" AS "posts_completed", parent."title" AS "posts_title", parent."createdAt" AS "posts_createdAt"
            [['child_user."id" AS "users_id"', 'child_user."username" AS "users_username"', 'child_user."name" AS "users_name"'], ['child_category."id" AS "categories_id"', 'child_category."name" AS "categories_name"']]
        FROM 
            posts parent
        , JOIN users child_user ON parent."userId" = child_user.id JOIN categories child_category ON parent."categoryId" = child_category.id 
        WHERE 
            parent."id" = %s;
    
[2024-02-05 10:45:42.440195] : Dataloom[postgres]: DROP TABLE IF EXISTS "posts" CASCADE;
[2024-02-05 10:45:42.483155] : Dataloom[postgres]: CREATE TABLE IF NOT EXISTS "posts" ("completed" BOOLEAN DEFAULT False, "id" BIGSERIAL PRIMARY KEY UNIQUE NOT NULL, "title" VARCHAR(255) NOT NULL, "categoryId" BIGSERIAL NOT NULL REFERENCES "categories"("id") ON DELETE CASCADE ON UPDATE CASCADE, "createdAt" TIMESTAMP DEFAULT CURRENT_TIMESTAMP, "updatedAt" TIMESTAMP DEFAULT CURRENT_TIMESTAMP, "userId" BIGSERIAL NOT NULL REFERENCES "users"("id") ON DELETE CASCADE ON UPDATE CASCADE);
[2024-02-05 10:45:42.538200] : Dataloom[postgres]: DROP TABLE IF EXISTS "users" CASCADE;
[2024-02-05 10:45:42.577211] : Dataloom[postgres]: CREATE TABLE IF NOT EXISTS "users" ("id" BIGSERIAL PRIMARY KEY UNIQUE NOT NULL, "name" TEXT NOT NULL DEFAULT 'Bob', "username" VARCHAR(255) UNIQUE);
[2024-02-05 10:45:42.617188] : Dataloom[postgres]: DROP TABLE IF EXISTS "categories" CASCADE;
[2024-02-05 10:45:42.655148] : Dataloom[postgres]: CREATE TABLE IF NOT EXISTS "categories" ("id" BIGSERIAL PRIMARY KEY UNIQUE NOT NULL, "name" VARCHAR(255) NOT NULL);
[2024-02-05 10:45:42.693153] : Dataloom[postgres]: SELECT tablename FROM pg_catalog.pg_tables WHERE schemaname='public';
[2024-02-05 10:45:42.733147] : Dataloom[postgres]: INSERT INTO "users" ("username") VALUES (%s) RETURNING "id";
[2024-02-05 10:45:42.767190] : Dataloom[postgres]: INSERT INTO "categories" ("name") VALUES (%s) RETURNING "id";
[2024-02-05 10:45:42.797147] : Dataloom[postgres]: INSERT INTO "posts" ("categoryId", "title", "userId") VALUES (%s, %s, %s) RETURNING *;
[2024-02-05 10:45:42.832146] : Dataloom[postgres]: 
        SELECT 
            parent."id" AS "posts_id", parent."completed" AS "posts_completed", parent."title" AS "posts_title", parent."createdAt" AS "posts_createdAt"
            ['child_user."id" AS "users_id", child_user."username" AS "users_username", child_user."name" AS "users_name"', 'child_category."id" AS "categories_id", child_category."name" AS "categories_name"']
        FROM 
            posts parent
        , JOIN users child_user ON parent."userId" = child_user.id JOIN categories child_category ON parent."categoryId" = child_category.id 
        WHERE 
            parent."id" = %s;
    
[2024-02-05 10:46:14.955490] : Dataloom[postgres]: DROP TABLE IF EXISTS "posts" CASCADE;
[2024-02-05 10:46:14.999534] : Dataloom[postgres]: CREATE TABLE IF NOT EXISTS "posts" ("completed" BOOLEAN DEFAULT False, "id" BIGSERIAL PRIMARY KEY UNIQUE NOT NULL, "title" VARCHAR(255) NOT NULL, "categoryId" BIGSERIAL NOT NULL REFERENCES "categories"("id") ON DELETE CASCADE ON UPDATE CASCADE, "createdAt" TIMESTAMP DEFAULT CURRENT_TIMESTAMP, "updatedAt" TIMESTAMP DEFAULT CURRENT_TIMESTAMP, "userId" BIGSERIAL NOT NULL REFERENCES "users"("id") ON DELETE CASCADE ON UPDATE CASCADE);
[2024-02-05 10:46:15.051500] : Dataloom[postgres]: DROP TABLE IF EXISTS "users" CASCADE;
[2024-02-05 10:46:15.092490] : Dataloom[postgres]: CREATE TABLE IF NOT EXISTS "users" ("id" BIGSERIAL PRIMARY KEY UNIQUE NOT NULL, "name" TEXT NOT NULL DEFAULT 'Bob', "username" VARCHAR(255) UNIQUE);
[2024-02-05 10:46:15.133535] : Dataloom[postgres]: DROP TABLE IF EXISTS "categories" CASCADE;
[2024-02-05 10:46:15.169650] : Dataloom[postgres]: CREATE TABLE IF NOT EXISTS "categories" ("id" BIGSERIAL PRIMARY KEY UNIQUE NOT NULL, "name" VARCHAR(255) NOT NULL);
[2024-02-05 10:46:15.201642] : Dataloom[postgres]: SELECT tablename FROM pg_catalog.pg_tables WHERE schemaname='public';
[2024-02-05 10:46:15.245643] : Dataloom[postgres]: INSERT INTO "users" ("username") VALUES (%s) RETURNING "id";
[2024-02-05 10:46:15.274644] : Dataloom[postgres]: INSERT INTO "categories" ("name") VALUES (%s) RETURNING "id";
[2024-02-05 10:46:15.303689] : Dataloom[postgres]: INSERT INTO "posts" ("categoryId", "title", "userId") VALUES (%s, %s, %s) RETURNING *;
[2024-02-05 10:46:15.341186] : Dataloom[postgres]: 
        SELECT 
            parent."id" AS "posts_id", parent."completed" AS "posts_completed", parent."title" AS "posts_title", parent."createdAt" AS "posts_createdAt"
            child_user."id" AS "users_id", child_user."username" AS "users_username", child_user."name" AS "users_name", child_category."id" AS "categories_id", child_category."name" AS "categories_name"
        FROM 
            posts parent
        , JOIN users child_user ON parent."userId" = child_user.id JOIN categories child_category ON parent."categoryId" = child_category.id 
        WHERE 
            parent."id" = %s;
    
[2024-02-05 10:48:37.845973] : Dataloom[postgres]: DROP TABLE IF EXISTS "posts" CASCADE;
[2024-02-05 10:48:37.890021] : Dataloom[postgres]: CREATE TABLE IF NOT EXISTS "posts" ("completed" BOOLEAN DEFAULT False, "id" BIGSERIAL PRIMARY KEY UNIQUE NOT NULL, "title" VARCHAR(255) NOT NULL, "categoryId" BIGSERIAL NOT NULL REFERENCES "categories"("id") ON DELETE CASCADE ON UPDATE CASCADE, "createdAt" TIMESTAMP DEFAULT CURRENT_TIMESTAMP, "updatedAt" TIMESTAMP DEFAULT CURRENT_TIMESTAMP, "userId" BIGSERIAL NOT NULL REFERENCES "users"("id") ON DELETE CASCADE ON UPDATE CASCADE);
[2024-02-05 10:48:37.941091] : Dataloom[postgres]: DROP TABLE IF EXISTS "users" CASCADE;
[2024-02-05 10:48:37.985090] : Dataloom[postgres]: CREATE TABLE IF NOT EXISTS "users" ("id" BIGSERIAL PRIMARY KEY UNIQUE NOT NULL, "name" TEXT NOT NULL DEFAULT 'Bob', "username" VARCHAR(255) UNIQUE);
[2024-02-05 10:48:38.026471] : Dataloom[postgres]: DROP TABLE IF EXISTS "categories" CASCADE;
[2024-02-05 10:48:38.062435] : Dataloom[postgres]: CREATE TABLE IF NOT EXISTS "categories" ("id" BIGSERIAL PRIMARY KEY UNIQUE NOT NULL, "name" VARCHAR(255) NOT NULL);
[2024-02-05 10:48:38.095473] : Dataloom[postgres]: SELECT tablename FROM pg_catalog.pg_tables WHERE schemaname='public';
[2024-02-05 10:48:38.138470] : Dataloom[postgres]: INSERT INTO "users" ("username") VALUES (%s) RETURNING "id";
[2024-02-05 10:48:38.167659] : Dataloom[postgres]: INSERT INTO "categories" ("name") VALUES (%s) RETURNING "id";
[2024-02-05 10:48:38.195433] : Dataloom[postgres]: INSERT INTO "posts" ("categoryId", "title", "userId") VALUES (%s, %s, %s) RETURNING *;
[2024-02-05 10:48:38.233334] : Dataloom[postgres]: 
        SELECT 
            parent."id" AS "posts_id", parent."completed" AS "posts_completed", parent."title" AS "posts_title", parent."createdAt" AS "posts_createdAt"
            child_user."id" AS "users_id", child_user."username" AS "users_username", child_user."name" AS "users_name", child_category."id" AS "categories_id", child_category."name" AS "categories_name"
        FROM 
            posts parent
        JOIN users child_user ON parent."userId" = child_user.id , JOIN categories child_category ON parent."categoryId" = child_category.id 
        WHERE 
            parent."id" = %s;
    
[2024-02-05 10:52:39.719356] : Dataloom[postgres]: DROP TABLE IF EXISTS "posts" CASCADE;
[2024-02-05 10:52:39.767632] : Dataloom[postgres]: CREATE TABLE IF NOT EXISTS "posts" ("completed" BOOLEAN DEFAULT False, "id" BIGSERIAL PRIMARY KEY UNIQUE NOT NULL, "title" VARCHAR(255) NOT NULL, "categoryId" BIGSERIAL NOT NULL REFERENCES "categories"("id") ON DELETE CASCADE ON UPDATE CASCADE, "createdAt" TIMESTAMP DEFAULT CURRENT_TIMESTAMP, "updatedAt" TIMESTAMP DEFAULT CURRENT_TIMESTAMP, "userId" BIGSERIAL NOT NULL REFERENCES "users"("id") ON DELETE CASCADE ON UPDATE CASCADE);
[2024-02-05 10:52:39.819632] : Dataloom[postgres]: DROP TABLE IF EXISTS "users" CASCADE;
[2024-02-05 10:52:39.860671] : Dataloom[postgres]: CREATE TABLE IF NOT EXISTS "users" ("id" BIGSERIAL PRIMARY KEY UNIQUE NOT NULL, "name" TEXT NOT NULL DEFAULT 'Bob', "username" VARCHAR(255) UNIQUE);
[2024-02-05 10:52:39.900680] : Dataloom[postgres]: DROP TABLE IF EXISTS "categories" CASCADE;
[2024-02-05 10:52:39.938572] : Dataloom[postgres]: CREATE TABLE IF NOT EXISTS "categories" ("id" BIGSERIAL PRIMARY KEY UNIQUE NOT NULL, "name" VARCHAR(255) NOT NULL);
[2024-02-05 10:52:39.974562] : Dataloom[postgres]: SELECT tablename FROM pg_catalog.pg_tables WHERE schemaname='public';
[2024-02-05 10:52:40.013210] : Dataloom[postgres]: INSERT INTO "users" ("username") VALUES (%s) RETURNING "id";
[2024-02-05 10:52:40.048205] : Dataloom[postgres]: INSERT INTO "categories" ("name") VALUES (%s) RETURNING "id";
[2024-02-05 10:52:40.098203] : Dataloom[postgres]: INSERT INTO "posts" ("categoryId", "title", "userId") VALUES (%s, %s, %s) RETURNING *;
[2024-02-05 10:52:40.162218] : Dataloom[postgres]: 
        SELECT 
            parent."id" AS "posts_id", parent."completed" AS "posts_completed", parent."title" AS "posts_title", parent."createdAt" AS "posts_createdAt"
            child_user."id" AS "users_id", child_user."username" AS "users_username", child_user."name" AS "users_name", child_category."id" AS "categories_id", child_category."name" AS "categories_name"
        FROM 
            posts parent
        JOIN users child_user ON parent."userId" = child_user.id JOIN categories child_category ON parent."categoryId" = child_category.id 
        WHERE 
            parent."id" = %s;
    
[2024-02-05 10:55:40.468648] : Dataloom[postgres]: DROP TABLE IF EXISTS "posts" CASCADE;
[2024-02-05 10:55:40.518553] : Dataloom[postgres]: CREATE TABLE IF NOT EXISTS "posts" ("completed" BOOLEAN DEFAULT False, "id" BIGSERIAL PRIMARY KEY UNIQUE NOT NULL, "title" VARCHAR(255) NOT NULL, "categoryId" BIGSERIAL NOT NULL REFERENCES "categories"("id") ON DELETE CASCADE ON UPDATE CASCADE, "createdAt" TIMESTAMP DEFAULT CURRENT_TIMESTAMP, "updatedAt" TIMESTAMP DEFAULT CURRENT_TIMESTAMP, "userId" BIGSERIAL NOT NULL REFERENCES "users"("id") ON DELETE CASCADE ON UPDATE CASCADE);
[2024-02-05 10:55:40.569445] : Dataloom[postgres]: DROP TABLE IF EXISTS "users" CASCADE;
[2024-02-05 10:55:40.611536] : Dataloom[postgres]: CREATE TABLE IF NOT EXISTS "users" ("id" BIGSERIAL PRIMARY KEY UNIQUE NOT NULL, "name" TEXT NOT NULL DEFAULT 'Bob', "username" VARCHAR(255) UNIQUE);
[2024-02-05 10:55:40.653444] : Dataloom[postgres]: DROP TABLE IF EXISTS "categories" CASCADE;
[2024-02-05 10:55:40.691981] : Dataloom[postgres]: CREATE TABLE IF NOT EXISTS "categories" ("id" BIGSERIAL PRIMARY KEY UNIQUE NOT NULL, "name" VARCHAR(255) NOT NULL);
[2024-02-05 10:55:40.726012] : Dataloom[postgres]: SELECT tablename FROM pg_catalog.pg_tables WHERE schemaname='public';
[2024-02-05 10:55:40.765964] : Dataloom[postgres]: INSERT INTO "users" ("username") VALUES (%s) RETURNING "id";
[2024-02-05 10:55:40.796557] : Dataloom[postgres]: INSERT INTO "categories" ("name") VALUES (%s) RETURNING "id";
[2024-02-05 10:55:40.829563] : Dataloom[postgres]: INSERT INTO "posts" ("categoryId", "title", "userId") VALUES (%s, %s, %s) RETURNING *;
[2024-02-05 10:55:40.865560] : Dataloom[postgres]: 
        SELECT 
            parent."id" AS "posts_id", parent."completed" AS "posts_completed", parent."title" AS "posts_title", parent."createdAt" AS "posts_createdAt",
            child_user."id" AS "users_id", child_user."username" AS "users_username", child_user."name" AS "users_name", child_category."id" AS "categories_id", child_category."name" AS "categories_name"
        FROM 
            posts parent
        JOIN users child_user ON parent."userId" = child_user.id JOIN categories child_category ON parent."categoryId" = child_category.id 
        WHERE 
            parent."id" = %s;
    
[2024-02-05 10:57:25.709269] : Dataloom[postgres]: DROP TABLE IF EXISTS "posts" CASCADE;
[2024-02-05 10:57:25.753441] : Dataloom[postgres]: CREATE TABLE IF NOT EXISTS "posts" ("completed" BOOLEAN DEFAULT False, "id" BIGSERIAL PRIMARY KEY UNIQUE NOT NULL, "title" VARCHAR(255) NOT NULL, "categoryId" BIGSERIAL NOT NULL REFERENCES "categories"("id") ON DELETE CASCADE ON UPDATE CASCADE, "createdAt" TIMESTAMP DEFAULT CURRENT_TIMESTAMP, "updatedAt" TIMESTAMP DEFAULT CURRENT_TIMESTAMP, "userId" BIGSERIAL NOT NULL REFERENCES "users"("id") ON DELETE CASCADE ON UPDATE CASCADE);
[2024-02-05 10:57:25.804407] : Dataloom[postgres]: DROP TABLE IF EXISTS "users" CASCADE;
[2024-02-05 10:57:25.842897] : Dataloom[postgres]: CREATE TABLE IF NOT EXISTS "users" ("id" BIGSERIAL PRIMARY KEY UNIQUE NOT NULL, "name" TEXT NOT NULL DEFAULT 'Bob', "username" VARCHAR(255) UNIQUE);
[2024-02-05 10:57:25.884840] : Dataloom[postgres]: DROP TABLE IF EXISTS "categories" CASCADE;
[2024-02-05 10:57:25.920879] : Dataloom[postgres]: CREATE TABLE IF NOT EXISTS "categories" ("id" BIGSERIAL PRIMARY KEY UNIQUE NOT NULL, "name" VARCHAR(255) NOT NULL);
[2024-02-05 10:57:25.956268] : Dataloom[postgres]: SELECT tablename FROM pg_catalog.pg_tables WHERE schemaname='public';
[2024-02-05 10:57:26.001269] : Dataloom[postgres]: INSERT INTO "users" ("username") VALUES (%s) RETURNING "id";
[2024-02-05 10:57:26.033773] : Dataloom[postgres]: INSERT INTO "categories" ("name") VALUES (%s) RETURNING "id";
[2024-02-05 10:57:26.062779] : Dataloom[postgres]: INSERT INTO "posts" ("categoryId", "title", "userId") VALUES (%s, %s, %s) RETURNING *;
[2024-02-05 10:57:26.105792] : Dataloom[postgres]: 
        SELECT 
            parent."id" AS "posts_id", parent."completed" AS "posts_completed", parent."title" AS "posts_title", parent."createdAt" AS "posts_createdAt",
            child_user."id" AS "users_id", child_user."username" AS "users_username", child_user."name" AS "users_name"
        FROM 
            posts parent
        JOIN users child_user ON parent."userId" = child_user.id 
        WHERE 
            parent."id" = %s;
    
[2024-02-05 11:07:49.754214] : Dataloom[postgres]: DROP TABLE IF EXISTS "posts" CASCADE;
[2024-02-05 11:07:49.804247] : Dataloom[postgres]: CREATE TABLE IF NOT EXISTS "posts" ("completed" BOOLEAN DEFAULT False, "id" BIGSERIAL PRIMARY KEY UNIQUE NOT NULL, "title" VARCHAR(255) NOT NULL, "categoryId" BIGSERIAL NOT NULL REFERENCES "categories"("id") ON DELETE CASCADE ON UPDATE CASCADE, "createdAt" TIMESTAMP DEFAULT CURRENT_TIMESTAMP, "updatedAt" TIMESTAMP DEFAULT CURRENT_TIMESTAMP, "userId" BIGSERIAL NOT NULL REFERENCES "users"("id") ON DELETE CASCADE ON UPDATE CASCADE);
[2024-02-05 11:07:49.862521] : Dataloom[postgres]: DROP TABLE IF EXISTS "users" CASCADE;
[2024-02-05 11:07:49.902509] : Dataloom[postgres]: CREATE TABLE IF NOT EXISTS "users" ("id" BIGSERIAL PRIMARY KEY UNIQUE NOT NULL, "name" TEXT NOT NULL DEFAULT 'Bob', "username" VARCHAR(255) UNIQUE);
[2024-02-05 11:07:49.951669] : Dataloom[postgres]: DROP TABLE IF EXISTS "categories" CASCADE;
[2024-02-05 11:07:49.990669] : Dataloom[postgres]: CREATE TABLE IF NOT EXISTS "categories" ("id" BIGSERIAL PRIMARY KEY UNIQUE NOT NULL, "name" VARCHAR(255) NOT NULL);
[2024-02-05 11:07:50.026096] : Dataloom[postgres]: SELECT tablename FROM pg_catalog.pg_tables WHERE schemaname='public';
[2024-02-05 11:07:50.070095] : Dataloom[postgres]: INSERT INTO "users" ("username") VALUES (%s) RETURNING "id";
[2024-02-05 11:07:50.102189] : Dataloom[postgres]: INSERT INTO "categories" ("name") VALUES (%s) RETURNING "id";
[2024-02-05 11:07:50.135149] : Dataloom[postgres]: INSERT INTO "posts" ("categoryId", "title", "userId") VALUES (%s, %s, %s) RETURNING *;
[2024-02-05 11:07:50.172096] : Dataloom[postgres]: 
        SELECT 
            parent."id" AS "posts_id", parent."completed" AS "posts_completed", parent."title" AS "posts_title", parent."createdAt" AS "posts_createdAt",
            child_user."id" AS "users_id", child_user."username" AS "users_username", child_user."name" AS "users_name"
        FROM 
            posts parent
        JOIN users child_user ON parent."userId" = child_user.id 
        WHERE 
            parent."id" = %s;
    
[2024-02-05 11:22:12.733685] : Dataloom[mysql]: DROP TABLE IF EXISTS `users`;
[2024-02-05 11:22:12.894672] : Dataloom[mysql]: DROP TABLE IF EXISTS `users`;
[2024-02-05 11:22:13.018733] : Dataloom[mysql]: DROP TABLE IF EXISTS `users`;
[2024-02-05 11:22:13.040670] : Dataloom[mysql]: CREATE TABLE IF NOT EXISTS `users` (`id` INT PRIMARY KEY AUTO_INCREMENT UNIQUE NOT NULL, `name` VARCHAR(255), `username` TEXT NOT NULL);
[2024-02-05 11:22:13.128733] : Dataloom[mysql]: DROP TABLE IF EXISTS `posts`;
[2024-02-05 11:22:13.210720] : Dataloom[mysql]: CREATE TABLE IF NOT EXISTS `posts` (`id` INT PRIMARY KEY AUTO_INCREMENT UNIQUE NOT NULL, `title` TEXT NOT NULL);
[2024-02-05 11:22:13.300971] : Dataloom[mysql]: SHOW TABLES;
[2024-02-05 11:22:13.372948] : Dataloom[mysql]: DROP TABLE IF EXISTS `users`;
[2024-02-05 11:22:13.488767] : Dataloom[mysql]: CREATE TABLE IF NOT EXISTS `users` (`id` INT PRIMARY KEY AUTO_INCREMENT UNIQUE NOT NULL, `name` VARCHAR(255) UNIQUE, `username` VARCHAR(255) NOT NULL DEFAULT 'Hello there!!');
[2024-02-05 11:22:13.615431] : Dataloom[mysql]: DROP TABLE IF EXISTS `posts`;
[2024-02-05 11:22:13.693464] : Dataloom[mysql]: CREATE TABLE IF NOT EXISTS `posts` (`completed` BOOLEAN DEFAULT False, `id` INT PRIMARY KEY AUTO_INCREMENT UNIQUE NOT NULL, `title` VARCHAR(255) NOT NULL);
[2024-02-05 11:22:13.749508] : Dataloom[mysql]: SHOW TABLES;
[2024-02-05 11:22:13.788464] : Dataloom[mysql]: DROP TABLE IF EXISTS `posts`;
[2024-02-05 11:22:13.840034] : Dataloom[mysql]: CREATE TABLE IF NOT EXISTS `posts` (`completed` BOOLEAN DEFAULT False, `id` INT PRIMARY KEY AUTO_INCREMENT UNIQUE NOT NULL, `title` VARCHAR(255) NOT NULL, `createdAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP, `updatedAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP, `userId` INT NOT NULL REFERENCES `users`(`id`) ON DELETE CASCADE ON UPDATE CASCADE);
[2024-02-05 11:22:13.918449] : Dataloom[mysql]: DROP TABLE IF EXISTS `users`;
[2024-02-05 11:22:13.976337] : Dataloom[mysql]: CREATE TABLE IF NOT EXISTS `users` (`id` INT PRIMARY KEY AUTO_INCREMENT UNIQUE NOT NULL, `name` VARCHAR(255) NOT NULL DEFAULT 'Bob', `username` VARCHAR(255) UNIQUE, `createdAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP, `updatedAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP);
[2024-02-05 11:22:14.057795] : Dataloom[mysql]: SHOW TABLES;
[2024-02-05 11:22:14.087992] : Dataloom[mysql]: INSERT INTO `users` (`name`, `username`) VALUES (%s, %s);
[2024-02-05 11:22:14.120581] : Dataloom[mysql]: DELETE FROM `users` WHERE `id` = %s;
[2024-02-05 11:22:14.149875] : Dataloom[mysql]: DELETE FROM `users` WHERE `id` = %s;
[2024-02-05 11:22:14.221881] : Dataloom[mysql]: DROP TABLE IF EXISTS `posts`;
[2024-02-05 11:22:14.352136] : Dataloom[mysql]: CREATE TABLE IF NOT EXISTS `posts` (`completed` BOOLEAN DEFAULT False, `id` INT PRIMARY KEY AUTO_INCREMENT UNIQUE NOT NULL, `title` VARCHAR(255) NOT NULL, `createdAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP, `updatedAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP, `userId` INT NOT NULL REFERENCES `users`(`id`) ON DELETE CASCADE ON UPDATE CASCADE);
[2024-02-05 11:22:14.479181] : Dataloom[mysql]: DROP TABLE IF EXISTS `users`;
[2024-02-05 11:22:14.542877] : Dataloom[mysql]: CREATE TABLE IF NOT EXISTS `users` (`id` INT PRIMARY KEY AUTO_INCREMENT UNIQUE NOT NULL, `name` VARCHAR(255) NOT NULL DEFAULT 'Bob', `username` VARCHAR(255) UNIQUE, `createdAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP, `updatedAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP);
[2024-02-05 11:22:14.643413] : Dataloom[mysql]: SHOW TABLES;
[2024-02-05 11:22:14.678456] : Dataloom[mysql]: INSERT INTO `users` (`name`, `username`) VALUES (%s, %s);
[2024-02-05 11:22:14.715517] : Dataloom[mysql]: 
    DELETE FROM `users` WHERE `id` IN (
       SELECT `id` FROM  (
                SELECT `id` FROM `users` WHERE `name` = %s LIMIT 1
        ) AS subquery
    );
    
[2024-02-05 11:22:14.750100] : Dataloom[mysql]: SELECT `createdAt`, `id`, `name`, `updatedAt`, `username` FROM `users` WHERE `name` = %s   ;
[2024-02-05 11:22:14.781113] : Dataloom[mysql]: 
    DELETE FROM `users` WHERE `id` IN (
       SELECT `id` FROM  (
                SELECT `id` FROM `users` WHERE `name` = %s AND `id` = %s LIMIT 1
        ) AS subquery
    );
    
[2024-02-05 11:22:14.810096] : Dataloom[mysql]: SELECT `createdAt`, `id`, `name`, `updatedAt`, `username` FROM `users` WHERE `name` = %s   ;
[2024-02-05 11:22:14.834246] : Dataloom[mysql]: 
    DELETE FROM `users` WHERE `id` IN (
       SELECT `id` FROM  (
                SELECT `id` FROM `users` WHERE `name` = %s AND `id` = %s LIMIT 1
        ) AS subquery
    );
    
[2024-02-05 11:22:14.858245] : Dataloom[mysql]: SELECT `createdAt`, `id`, `name`, `updatedAt`, `username` FROM `users` WHERE `name` = %s   ;
[2024-02-05 11:22:14.901243] : Dataloom[mysql]: DROP TABLE IF EXISTS `posts`;
[2024-02-05 11:22:14.989665] : Dataloom[mysql]: CREATE TABLE IF NOT EXISTS `posts` (`completed` BOOLEAN DEFAULT False, `id` INT PRIMARY KEY AUTO_INCREMENT UNIQUE NOT NULL, `title` VARCHAR(255) NOT NULL, `createdAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP, `updatedAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP, `userId` INT NOT NULL REFERENCES `users`(`id`) ON DELETE CASCADE ON UPDATE CASCADE);
[2024-02-05 11:22:15.083585] : Dataloom[mysql]: DROP TABLE IF EXISTS `users`;
[2024-02-05 11:22:15.183396] : Dataloom[mysql]: CREATE TABLE IF NOT EXISTS `users` (`id` INT PRIMARY KEY AUTO_INCREMENT UNIQUE NOT NULL, `name` VARCHAR(255) NOT NULL DEFAULT 'Bob', `username` VARCHAR(255) UNIQUE, `createdAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP, `updatedAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP);
[2024-02-05 11:22:15.291949] : Dataloom[mysql]: SHOW TABLES;
[2024-02-05 11:22:15.325926] : Dataloom[mysql]: INSERT INTO `users` (`name`, `username`) VALUES (%s, %s);
[2024-02-05 11:22:15.360950] : Dataloom[mysql]: DELETE FROM `users` WHERE `name` = %s;
[2024-02-05 11:22:15.391935] : Dataloom[mysql]: SELECT `createdAt`, `id`, `name`, `updatedAt`, `username` FROM `users` WHERE `name` = %s   ;
[2024-02-05 11:22:15.418934] : Dataloom[mysql]: INSERT INTO `users` (`name`, `username`) VALUES (%s, %s);
[2024-02-05 11:22:15.440934] : Dataloom[mysql]: DELETE FROM `users` WHERE `name` = %s AND `id` = %s;
[2024-02-05 11:22:15.457935] : Dataloom[mysql]: SELECT `createdAt`, `id`, `name`, `updatedAt`, `username` FROM `users` WHERE `name` = %s   ;
[2024-02-05 11:22:15.476827] : Dataloom[mysql]: DELETE FROM `users` WHERE `name` = %s AND `id` = %s;
[2024-02-05 11:22:15.499850] : Dataloom[mysql]: SELECT `createdAt`, `id`, `name`, `updatedAt`, `username` FROM `users` WHERE `name` = %s   ;
[2024-02-05 11:22:15.546851] : Dataloom[mysql]: DROP TABLE IF EXISTS `posts`;
[2024-02-05 11:22:15.620992] : Dataloom[mysql]: CREATE TABLE IF NOT EXISTS `posts` (`completed` BOOLEAN DEFAULT False, `id` INT PRIMARY KEY AUTO_INCREMENT UNIQUE NOT NULL, `title` VARCHAR(255) NOT NULL, `createdAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP, `updatedAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP, `userId` INT NOT NULL REFERENCES `users`(`id`) ON DELETE CASCADE ON UPDATE CASCADE);
[2024-02-05 11:22:15.711871] : Dataloom[mysql]: DROP TABLE IF EXISTS `users`;
[2024-02-05 11:22:15.810914] : Dataloom[mysql]: CREATE TABLE IF NOT EXISTS `users` (`id` INT PRIMARY KEY AUTO_INCREMENT UNIQUE NOT NULL, `name` VARCHAR(255) NOT NULL DEFAULT 'Bob', `username` VARCHAR(255) UNIQUE, `createdAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP, `updatedAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP);
[2024-02-05 11:22:15.969344] : Dataloom[mysql]: SHOW TABLES;
[2024-02-05 11:22:15.997231] : Dataloom[mysql]: INSERT INTO `users` (`username`) VALUES (%s);
[2024-02-05 11:22:16.027349] : Dataloom[mysql]: INSERT INTO `posts` (`title`, `userId`) VALUES (%s, %s);
[2024-02-05 11:22:16.090290] : Dataloom[mysql]: DROP TABLE IF EXISTS `posts`;
[2024-02-05 11:22:16.189721] : Dataloom[mysql]: CREATE TABLE IF NOT EXISTS `posts` (`completed` BOOLEAN DEFAULT False, `id` INT PRIMARY KEY AUTO_INCREMENT UNIQUE NOT NULL, `title` VARCHAR(255) NOT NULL, `createdAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP, `updatedAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP, `userId` INT NOT NULL REFERENCES `users`(`id`) ON DELETE CASCADE ON UPDATE CASCADE);
[2024-02-05 11:22:16.270045] : Dataloom[mysql]: DROP TABLE IF EXISTS `users`;
[2024-02-05 11:22:16.367019] : Dataloom[mysql]: CREATE TABLE IF NOT EXISTS `users` (`id` INT PRIMARY KEY AUTO_INCREMENT UNIQUE NOT NULL, `name` VARCHAR(255) NOT NULL DEFAULT 'Bob', `username` VARCHAR(255) UNIQUE, `createdAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP, `updatedAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP);
[2024-02-05 11:22:16.466342] : Dataloom[mysql]: SHOW TABLES;
[2024-02-05 11:22:16.496996] : Dataloom[mysql]: INSERT INTO `users` (`username`) VALUES (%s);
[2024-02-05 11:22:16.531995] : Dataloom[mysql]: INSERT INTO `posts` (`title`, `userId`) VALUES (%s, %s);
[2024-02-05 11:22:16.593805] : Dataloom[mysql]: DROP TABLE IF EXISTS `posts`;
[2024-02-05 11:22:16.663596] : Dataloom[mysql]: CREATE TABLE IF NOT EXISTS `posts` (`completed` BOOLEAN DEFAULT False, `id` INT PRIMARY KEY AUTO_INCREMENT UNIQUE NOT NULL, `title` VARCHAR(255) NOT NULL, `createdAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP, `updatedAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP, `userId` INT NOT NULL REFERENCES `users`(`id`) ON DELETE CASCADE ON UPDATE CASCADE);
[2024-02-05 11:22:16.760566] : Dataloom[mysql]: DROP TABLE IF EXISTS `users`;
[2024-02-05 11:22:16.850210] : Dataloom[mysql]: CREATE TABLE IF NOT EXISTS `users` (`id` INT PRIMARY KEY AUTO_INCREMENT UNIQUE NOT NULL, `name` VARCHAR(255) NOT NULL DEFAULT 'Bob', `username` VARCHAR(255) UNIQUE);
[2024-02-05 11:22:16.954735] : Dataloom[mysql]: SHOW TABLES;
[2024-02-05 11:22:16.984678] : Dataloom[mysql]: INSERT INTO `users` (`username`) VALUES (%s);
[2024-02-05 11:22:17.017582] : Dataloom[mysql]: INSERT INTO `posts` (`title`, `userId`) VALUES (%s, %s);
[2024-02-05 11:22:17.050664] : Dataloom[mysql]: SELECT `id`, `name`, `username` FROM `users` WHERE `id` = %s;
[2024-02-05 11:22:17.077657] : Dataloom[mysql]: SELECT `id`, `name`, `username` FROM `users` WHERE `id` = %s;
[2024-02-05 11:22:17.105611] : Dataloom[mysql]: SELECT `id`, `completed` FROM `posts` WHERE `id` = %s;
[2024-02-05 11:22:17.157701] : Dataloom[mysql]: DROP TABLE IF EXISTS `posts`;
[2024-02-05 11:22:17.238169] : Dataloom[mysql]: CREATE TABLE IF NOT EXISTS `posts` (`completed` BOOLEAN DEFAULT False, `id` INT PRIMARY KEY AUTO_INCREMENT UNIQUE NOT NULL, `title` VARCHAR(255) NOT NULL, `createdAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP, `updatedAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP, `userId` INT NOT NULL REFERENCES `users`(`id`) ON DELETE CASCADE ON UPDATE CASCADE);
[2024-02-05 11:22:17.334719] : Dataloom[mysql]: DROP TABLE IF EXISTS `users`;
[2024-02-05 11:22:17.416931] : Dataloom[mysql]: CREATE TABLE IF NOT EXISTS `users` (`id` INT PRIMARY KEY AUTO_INCREMENT UNIQUE NOT NULL, `name` VARCHAR(255) NOT NULL DEFAULT 'Bob', `username` VARCHAR(255) UNIQUE);
[2024-02-05 11:22:17.494265] : Dataloom[mysql]: SHOW TABLES;
[2024-02-05 11:22:17.521567] : Dataloom[mysql]: INSERT INTO `users` (`username`) VALUES (%s);
[2024-02-05 11:22:17.550499] : Dataloom[mysql]: INSERT INTO `posts` (`title`, `userId`) VALUES (%s, %s);
[2024-02-05 11:22:17.580577] : Dataloom[mysql]: SELECT `id`, `name`, `username` FROM `users`   ;
[2024-02-05 11:22:17.610518] : Dataloom[mysql]: SELECT `completed`, `createdAt`, `id`, `title`, `updatedAt`, `userId` FROM `posts`   ;
[2024-02-05 11:22:17.641522] : Dataloom[mysql]: SELECT `id`, `completed` FROM `posts`  LIMIT 3 OFFSET 3;
[2024-02-05 11:22:17.707520] : Dataloom[mysql]: DROP TABLE IF EXISTS `posts`;
[2024-02-05 11:22:17.769986] : Dataloom[mysql]: CREATE TABLE IF NOT EXISTS `posts` (`completed` BOOLEAN DEFAULT False, `id` INT PRIMARY KEY AUTO_INCREMENT UNIQUE NOT NULL, `title` VARCHAR(255) NOT NULL, `createdAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP, `updatedAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP, `userId` INT NOT NULL REFERENCES `users`(`id`) ON DELETE CASCADE ON UPDATE CASCADE);
[2024-02-05 11:22:17.856503] : Dataloom[mysql]: DROP TABLE IF EXISTS `users`;
[2024-02-05 11:22:17.906503] : Dataloom[mysql]: CREATE TABLE IF NOT EXISTS `users` (`id` INT PRIMARY KEY AUTO_INCREMENT UNIQUE NOT NULL, `name` VARCHAR(255) NOT NULL DEFAULT 'Bob', `username` VARCHAR(255) UNIQUE);
[2024-02-05 11:22:17.996507] : Dataloom[mysql]: SHOW TABLES;
[2024-02-05 11:22:18.029576] : Dataloom[mysql]: INSERT INTO `users` (`username`) VALUES (%s);
[2024-02-05 11:22:18.064505] : Dataloom[mysql]: INSERT INTO `posts` (`title`, `userId`) VALUES (%s, %s);
[2024-02-05 11:22:18.096507] : Dataloom[mysql]: SELECT `id`, `name`, `username` FROM `users` WHERE `id` = %s   ;
[2024-02-05 11:22:18.123559] : Dataloom[mysql]: SELECT `id`, `name`, `username` FROM `users` WHERE `id` = %s   ;
[2024-02-05 11:22:18.151507] : Dataloom[mysql]: SELECT `id`, `name`, `username` FROM `users` WHERE `id` = %s AND `name` = %s   ;
[2024-02-05 11:22:18.176530] : Dataloom[mysql]: SELECT `id`, `name`, `username` FROM `users` WHERE `id` = %s AND `username` = %s   ;
[2024-02-05 11:22:18.200590] : Dataloom[mysql]: SELECT `id`, `name`, `username` FROM `users` WHERE `name` = %s AND `username` = %s   ;
[2024-02-05 11:22:18.226577] : Dataloom[mysql]: SELECT `id`, `completed` FROM `posts`   ;
[2024-02-05 11:22:18.274567] : Dataloom[mysql]: DROP TABLE IF EXISTS `posts`;
[2024-02-05 11:22:18.360540] : Dataloom[mysql]: CREATE TABLE IF NOT EXISTS `posts` (`completed` BOOLEAN DEFAULT False, `id` INT PRIMARY KEY AUTO_INCREMENT UNIQUE NOT NULL, `title` VARCHAR(255) NOT NULL, `createdAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP, `updatedAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP, `userId` INT NOT NULL REFERENCES `users`(`id`) ON DELETE CASCADE ON UPDATE CASCADE);
[2024-02-05 11:22:18.444385] : Dataloom[mysql]: DROP TABLE IF EXISTS `users`;
[2024-02-05 11:22:18.536319] : Dataloom[mysql]: CREATE TABLE IF NOT EXISTS `users` (`id` INT PRIMARY KEY AUTO_INCREMENT UNIQUE NOT NULL, `name` VARCHAR(255) NOT NULL DEFAULT 'Bob', `username` VARCHAR(255) UNIQUE);
[2024-02-05 11:22:18.611858] : Dataloom[mysql]: SHOW TABLES;
[2024-02-05 11:22:18.634941] : Dataloom[mysql]: INSERT INTO `users` (`username`) VALUES (%s);
[2024-02-05 11:22:18.660873] : Dataloom[mysql]: INSERT INTO `posts` (`title`, `userId`) VALUES (%s, %s);
[2024-02-05 11:22:18.687473] : Dataloom[mysql]: SELECT `completed`, `createdAt`, `id`, `title`, `updatedAt`, `userId` FROM `posts` WHERE `id` = %s AND `userId` = %s   ;
[2024-02-05 11:22:18.708556] : Dataloom[mysql]: SELECT `id`, `name`, `username` FROM `users`   ;
[2024-02-05 11:22:18.731496] : Dataloom[mysql]: SELECT `id`, `name`, `username` FROM `users` WHERE `id` = %s   ;
[2024-02-05 11:22:18.753498] : Dataloom[mysql]: SELECT `id`, `name`, `username` FROM `users` WHERE `id` = %s   ;
[2024-02-05 11:22:18.776496] : Dataloom[mysql]: SELECT `id`, `name`, `username` FROM `users` WHERE `id` = %s AND `name` = %s   ;
[2024-02-05 11:22:18.798495] : Dataloom[mysql]: SELECT `id`, `name`, `username` FROM `users` WHERE `id` = %s AND `username` = %s   ;
[2024-02-05 11:22:18.819539] : Dataloom[mysql]: SELECT `id`, `name`, `username` FROM `users` WHERE `name` = %s AND `username` = %s   ;
[2024-02-05 11:22:18.846508] : Dataloom[mysql]: SELECT `id`, `completed` FROM `posts` WHERE `userId` = %s  LIMIT 3 OFFSET 3;
[2024-02-05 11:22:18.874500] : Dataloom[mysql]: SELECT `completed`, `createdAt`, `id`, `title`, `updatedAt`, `userId` FROM `posts`   ;
[2024-02-05 11:22:18.932506] : Dataloom[mysql]: DROP TABLE IF EXISTS `posts`;
[2024-02-05 11:22:19.025411] : Dataloom[mysql]: CREATE TABLE IF NOT EXISTS `posts` (`completed` BOOLEAN DEFAULT False, `id` INT PRIMARY KEY AUTO_INCREMENT UNIQUE NOT NULL, `title` VARCHAR(255) NOT NULL, `createdAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP, `updatedAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP, `userId` INT NOT NULL REFERENCES `users`(`id`) ON DELETE CASCADE ON UPDATE CASCADE);
[2024-02-05 11:22:19.098307] : Dataloom[mysql]: DROP TABLE IF EXISTS `users`;
[2024-02-05 11:22:19.178976] : Dataloom[mysql]: CREATE TABLE IF NOT EXISTS `users` (`id` INT PRIMARY KEY AUTO_INCREMENT UNIQUE NOT NULL, `name` VARCHAR(255) NOT NULL DEFAULT 'Bob', `username` VARCHAR(255) UNIQUE, `createdAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP, `updatedAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP);
[2024-02-05 11:22:19.271058] : Dataloom[mysql]: SHOW TABLES;
[2024-02-05 11:22:19.299051] : Dataloom[mysql]: INSERT INTO `users` (`username`) VALUES (%s);
[2024-02-05 11:22:19.329006] : Dataloom[mysql]: INSERT INTO `posts` (`title`, `userId`) VALUES (%s, %s);
[2024-02-05 11:22:19.415061] : Dataloom[mysql]: UPDATE `users` SET `updatedAt` = %s WHERE `id` = %s;
[2024-02-05 11:22:19.441010] : Dataloom[mysql]: UPDATE `users` SET `updatedAt` = %s WHERE `id` = %s;
[2024-02-05 11:22:19.466278] : Dataloom[mysql]: SELECT `createdAt`, `id`, `name`, `updatedAt`, `username` FROM `users` WHERE `id` = %s;
[2024-02-05 11:22:19.490470] : Dataloom[mysql]: UPDATE `users` SET `id` = %s, `updatedAt` = %s WHERE `id` = %s;
[2024-02-05 11:22:19.537103] : Dataloom[mysql]: DROP TABLE IF EXISTS `posts`;
[2024-02-05 11:22:19.596891] : Dataloom[mysql]: CREATE TABLE IF NOT EXISTS `posts` (`completed` BOOLEAN DEFAULT False, `id` INT PRIMARY KEY AUTO_INCREMENT UNIQUE NOT NULL, `title` VARCHAR(255) NOT NULL, `createdAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP, `userId` INT NOT NULL REFERENCES `users`(`id`) ON DELETE CASCADE ON UPDATE CASCADE);
[2024-02-05 11:22:19.685763] : Dataloom[mysql]: DROP TABLE IF EXISTS `users`;
[2024-02-05 11:22:19.773760] : Dataloom[mysql]: CREATE TABLE IF NOT EXISTS `users` (`id` INT PRIMARY KEY AUTO_INCREMENT UNIQUE NOT NULL, `name` VARCHAR(255) NOT NULL DEFAULT 'Bob', `username` VARCHAR(255) UNIQUE, `createdAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP, `updatedAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP);
[2024-02-05 11:22:19.861130] : Dataloom[mysql]: SHOW TABLES;
[2024-02-05 11:22:19.886534] : Dataloom[mysql]: INSERT INTO `users` (`username`) VALUES (%s);
[2024-02-05 11:22:19.914590] : Dataloom[mysql]: INSERT INTO `posts` (`title`, `userId`) VALUES (%s, %s);
[2024-02-05 11:22:19.998693] : Dataloom[mysql]: 
        UPDATE `posts` SET `title` = %s WHERE `id` IN (
            SELECT `id` FROM  (
                SELECT `id` FROM `posts` WHERE `userId` = %s LIMIT 1
            ) AS subquery
        );
        
[2024-02-05 11:22:20.031698] : Dataloom[mysql]: 
        UPDATE `posts` SET `title` = %s WHERE `id` IN (
            SELECT `id` FROM  (
                SELECT `id` FROM `posts` WHERE `userId` = %s LIMIT 1
            ) AS subquery
        );
        
[2024-02-05 11:22:20.058717] : Dataloom[mysql]: SELECT `completed`, `createdAt`, `id`, `title`, `userId` FROM `posts` WHERE `id` = %s;
[2024-02-05 11:22:20.085327] : Dataloom[mysql]: 
        UPDATE `posts` SET `userId` = %s WHERE `id` IN (
            SELECT `id` FROM  (
                SELECT `id` FROM `posts` WHERE `userId` = %s LIMIT 1
            ) AS subquery
        );
        
[2024-02-05 11:22:20.139404] : Dataloom[mysql]: DROP TABLE IF EXISTS `posts`;
[2024-02-05 11:22:20.249193] : Dataloom[mysql]: CREATE TABLE IF NOT EXISTS `posts` (`completed` BOOLEAN DEFAULT False, `id` INT PRIMARY KEY AUTO_INCREMENT UNIQUE NOT NULL, `title` VARCHAR(255) NOT NULL, `createdAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP, `userId` INT NOT NULL REFERENCES `users`(`id`) ON DELETE CASCADE ON UPDATE CASCADE);
[2024-02-05 11:22:20.337272] : Dataloom[mysql]: DROP TABLE IF EXISTS `users`;
[2024-02-05 11:22:20.416367] : Dataloom[mysql]: CREATE TABLE IF NOT EXISTS `users` (`id` INT PRIMARY KEY AUTO_INCREMENT UNIQUE NOT NULL, `name` VARCHAR(255) NOT NULL DEFAULT 'Bob', `username` VARCHAR(255) UNIQUE, `createdAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP, `updatedAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP);
[2024-02-05 11:22:20.511049] : Dataloom[mysql]: SHOW TABLES;
[2024-02-05 11:22:20.537048] : Dataloom[mysql]: INSERT INTO `users` (`username`) VALUES (%s);
[2024-02-05 11:22:20.564996] : Dataloom[mysql]: INSERT INTO `posts` (`title`, `userId`) VALUES (%s, %s);
[2024-02-05 11:22:20.657395] : Dataloom[mysql]: UPDATE `posts` SET `title` = %s WHERE `userId` = %s;
[2024-02-05 11:22:20.695081] : Dataloom[mysql]: UPDATE `posts` SET `title` = %s WHERE `userId` = %s;
[2024-02-05 11:22:20.729082] : Dataloom[mysql]: SELECT `completed`, `createdAt`, `id`, `title`, `userId` FROM `posts` WHERE `id` = %s;
[2024-02-05 11:22:20.761095] : Dataloom[mysql]: UPDATE `posts` SET `userId` = %s WHERE `userId` = %s;
[2024-02-05 11:22:21.625339] : Dataloom[postgres]: DROP TABLE IF EXISTS "users" CASCADE;
[2024-02-05 11:22:21.785029] : Dataloom[postgres]: DROP TABLE IF EXISTS "users" CASCADE;
[2024-02-05 11:22:22.048551] : Dataloom[postgres]: DROP TABLE IF EXISTS "users" CASCADE;
[2024-02-05 11:22:22.070548] : Dataloom[postgres]: CREATE TABLE IF NOT EXISTS "users" ("id" BIGSERIAL PRIMARY KEY UNIQUE NOT NULL, "name" VARCHAR(255), "username" TEXT NOT NULL);
[2024-02-05 11:22:22.123551] : Dataloom[postgres]: DROP TABLE IF EXISTS "posts" CASCADE;
[2024-02-05 11:22:22.173562] : Dataloom[postgres]: CREATE TABLE IF NOT EXISTS "posts" ("id" BIGSERIAL PRIMARY KEY UNIQUE NOT NULL, "title" TEXT NOT NULL DEFAULT 'Hello there!!');
[2024-02-05 11:22:22.226639] : Dataloom[postgres]: SELECT tablename FROM pg_catalog.pg_tables WHERE schemaname='public';
[2024-02-05 11:22:22.464454] : Dataloom[postgres]: DROP TABLE IF EXISTS "users" CASCADE;
[2024-02-05 11:22:22.510491] : Dataloom[postgres]: CREATE TABLE IF NOT EXISTS "users" ("id" BIGSERIAL PRIMARY KEY UNIQUE NOT NULL, "name" VARCHAR(255) UNIQUE, "username" TEXT NOT NULL DEFAULT 'Hello there!!');
[2024-02-05 11:22:22.572490] : Dataloom[postgres]: DROP TABLE IF EXISTS "posts" CASCADE;
[2024-02-05 11:22:22.613493] : Dataloom[postgres]: CREATE TABLE IF NOT EXISTS "posts" ("completed" BOOLEAN DEFAULT False, "id" BIGSERIAL PRIMARY KEY UNIQUE NOT NULL, "title" VARCHAR(255) NOT NULL);
[2024-02-05 11:22:22.655584] : Dataloom[postgres]: SELECT tablename FROM pg_catalog.pg_tables WHERE schemaname='public';
[2024-02-05 11:22:22.875222] : Dataloom[postgres]: DROP TABLE IF EXISTS "posts" CASCADE;
[2024-02-05 11:22:22.922237] : Dataloom[postgres]: CREATE TABLE IF NOT EXISTS "posts" ("completed" BOOLEAN DEFAULT False, "id" BIGSERIAL PRIMARY KEY UNIQUE NOT NULL, "title" VARCHAR(255) NOT NULL, "createdAt" TIMESTAMP DEFAULT CURRENT_TIMESTAMP, "updatedAt" TIMESTAMP DEFAULT CURRENT_TIMESTAMP, "userId" BIGSERIAL NOT NULL REFERENCES "users"("id") ON DELETE CASCADE ON UPDATE CASCADE);
[2024-02-05 11:22:23.001227] : Dataloom[postgres]: DROP TABLE IF EXISTS "users" CASCADE;
[2024-02-05 11:22:23.064203] : Dataloom[postgres]: CREATE TABLE IF NOT EXISTS "users" ("id" BIGSERIAL PRIMARY KEY UNIQUE NOT NULL, "name" TEXT NOT NULL DEFAULT 'Bob', "username" VARCHAR(255) UNIQUE, "createdAt" TIMESTAMP DEFAULT CURRENT_TIMESTAMP, "updatedAt" TIMESTAMP DEFAULT CURRENT_TIMESTAMP);
[2024-02-05 11:22:23.125200] : Dataloom[postgres]: SELECT tablename FROM pg_catalog.pg_tables WHERE schemaname='public';
[2024-02-05 11:22:23.163196] : Dataloom[postgres]: INSERT INTO "users" ("name", "username") VALUES (%s, %s) RETURNING "id";
[2024-02-05 11:22:23.192201] : Dataloom[postgres]: DELETE FROM "users" WHERE "id" = %s;
[2024-02-05 11:22:23.216015] : Dataloom[postgres]: DELETE FROM "users" WHERE "id" = %s;
[2024-02-05 11:22:23.339612] : Dataloom[postgres]: DROP TABLE IF EXISTS "posts" CASCADE;
[2024-02-05 11:22:23.380547] : Dataloom[postgres]: CREATE TABLE IF NOT EXISTS "posts" ("completed" BOOLEAN DEFAULT False, "id" BIGSERIAL PRIMARY KEY UNIQUE NOT NULL, "title" VARCHAR(255) NOT NULL, "createdAt" TIMESTAMP DEFAULT CURRENT_TIMESTAMP, "updatedAt" TIMESTAMP DEFAULT CURRENT_TIMESTAMP, "userId" BIGSERIAL NOT NULL REFERENCES "users"("id") ON DELETE CASCADE ON UPDATE CASCADE);
[2024-02-05 11:22:23.431499] : Dataloom[postgres]: DROP TABLE IF EXISTS "users" CASCADE;
[2024-02-05 11:22:23.473943] : Dataloom[postgres]: CREATE TABLE IF NOT EXISTS "users" ("id" BIGSERIAL PRIMARY KEY UNIQUE NOT NULL, "name" TEXT NOT NULL DEFAULT 'Bob', "username" VARCHAR(255) UNIQUE, "createdAt" TIMESTAMP DEFAULT CURRENT_TIMESTAMP, "updatedAt" TIMESTAMP DEFAULT CURRENT_TIMESTAMP);
[2024-02-05 11:22:23.518945] : Dataloom[postgres]: SELECT tablename FROM pg_catalog.pg_tables WHERE schemaname='public';
[2024-02-05 11:22:23.563945] : Dataloom[postgres]: INSERT INTO "users" ("name", "username") VALUES (%s, %s) RETURNING *;
[2024-02-05 11:22:23.599009] : Dataloom[postgres]: 
    DELETE FROM "users" WHERE "id" = (
        SELECT "id" FROM  "users" WHERE "name" = %s LIMIT 1
    );
    
[2024-02-05 11:22:23.629958] : Dataloom[postgres]: SELECT "createdAt", "id", "name", "updatedAt", "username" FROM "users" WHERE "name" = %s   ;
[2024-02-05 11:22:23.664949] : Dataloom[postgres]: 
    DELETE FROM "users" WHERE "id" = (
        SELECT "id" FROM  "users" WHERE "name" = %s AND "id" = %s LIMIT 1
    );
    
[2024-02-05 11:22:23.697946] : Dataloom[postgres]: SELECT "createdAt", "id", "name", "updatedAt", "username" FROM "users" WHERE "name" = %s   ;
[2024-02-05 11:22:23.727944] : Dataloom[postgres]: 
    DELETE FROM "users" WHERE "id" = (
        SELECT "id" FROM  "users" WHERE "name" = %s AND "id" = %s LIMIT 1
    );
    
[2024-02-05 11:22:23.756945] : Dataloom[postgres]: SELECT "createdAt", "id", "name", "updatedAt", "username" FROM "users" WHERE "name" = %s   ;
[2024-02-05 11:22:23.932862] : Dataloom[postgres]: DROP TABLE IF EXISTS "posts" CASCADE;
[2024-02-05 11:22:23.972877] : Dataloom[postgres]: CREATE TABLE IF NOT EXISTS "posts" ("completed" BOOLEAN DEFAULT False, "id" BIGSERIAL PRIMARY KEY UNIQUE NOT NULL, "title" VARCHAR(255) NOT NULL, "createdAt" TIMESTAMP DEFAULT CURRENT_TIMESTAMP, "updatedAt" TIMESTAMP DEFAULT CURRENT_TIMESTAMP, "userId" BIGSERIAL NOT NULL REFERENCES "users"("id") ON DELETE CASCADE ON UPDATE CASCADE);
[2024-02-05 11:22:24.023861] : Dataloom[postgres]: DROP TABLE IF EXISTS "users" CASCADE;
[2024-02-05 11:22:24.063864] : Dataloom[postgres]: CREATE TABLE IF NOT EXISTS "users" ("id" BIGSERIAL PRIMARY KEY UNIQUE NOT NULL, "name" TEXT NOT NULL DEFAULT 'Bob', "username" VARCHAR(255) UNIQUE, "createdAt" TIMESTAMP DEFAULT CURRENT_TIMESTAMP, "updatedAt" TIMESTAMP DEFAULT CURRENT_TIMESTAMP);
[2024-02-05 11:22:24.106920] : Dataloom[postgres]: SELECT tablename FROM pg_catalog.pg_tables WHERE schemaname='public';
[2024-02-05 11:22:24.146759] : Dataloom[postgres]: INSERT INTO "users" ("name", "username") VALUES (%s, %s) RETURNING *;
[2024-02-05 11:22:24.180728] : Dataloom[postgres]: DELETE FROM "users" WHERE "name" = %s;
[2024-02-05 11:22:24.206765] : Dataloom[postgres]: SELECT "createdAt", "id", "name", "updatedAt", "username" FROM "users" WHERE "name" = %s   ;
[2024-02-05 11:22:24.233357] : Dataloom[postgres]: INSERT INTO "users" ("name", "username") VALUES (%s, %s) RETURNING *;
[2024-02-05 11:22:24.261331] : Dataloom[postgres]: DELETE FROM "users" WHERE "name" = %s AND "id" = %s;
[2024-02-05 11:22:24.287361] : Dataloom[postgres]: SELECT "createdAt", "id", "name", "updatedAt", "username" FROM "users" WHERE "name" = %s   ;
[2024-02-05 11:22:24.314356] : Dataloom[postgres]: DELETE FROM "users" WHERE "name" = %s AND "id" = %s;
[2024-02-05 11:22:24.341408] : Dataloom[postgres]: SELECT "createdAt", "id", "name", "updatedAt", "username" FROM "users" WHERE "name" = %s   ;
[2024-02-05 11:22:24.505349] : Dataloom[postgres]: DROP TABLE IF EXISTS "posts" CASCADE;
[2024-02-05 11:22:24.541433] : Dataloom[postgres]: CREATE TABLE IF NOT EXISTS "posts" ("completed" BOOLEAN DEFAULT False, "id" BIGSERIAL PRIMARY KEY UNIQUE NOT NULL, "title" VARCHAR(255) NOT NULL, "createdAt" TIMESTAMP DEFAULT CURRENT_TIMESTAMP, "updatedAt" TIMESTAMP DEFAULT CURRENT_TIMESTAMP, "userId" BIGSERIAL NOT NULL REFERENCES "users"("id") ON DELETE CASCADE ON UPDATE CASCADE);
[2024-02-05 11:22:24.583444] : Dataloom[postgres]: DROP TABLE IF EXISTS "users" CASCADE;
[2024-02-05 11:22:24.619429] : Dataloom[postgres]: CREATE TABLE IF NOT EXISTS "users" ("id" BIGSERIAL PRIMARY KEY UNIQUE NOT NULL, "name" TEXT NOT NULL DEFAULT 'Bob', "username" VARCHAR(255) UNIQUE, "createdAt" TIMESTAMP DEFAULT CURRENT_TIMESTAMP, "updatedAt" TIMESTAMP DEFAULT CURRENT_TIMESTAMP);
[2024-02-05 11:22:24.660377] : Dataloom[postgres]: SELECT tablename FROM pg_catalog.pg_tables WHERE schemaname='public';
[2024-02-05 11:22:24.685411] : Dataloom[postgres]: INSERT INTO "users" ("username") VALUES (%s) RETURNING "id";
[2024-02-05 11:22:24.704931] : Dataloom[postgres]: INSERT INTO "posts" ("title", "userId") VALUES (%s, %s) RETURNING "id";
[2024-02-05 11:22:24.819003] : Dataloom[postgres]: DROP TABLE IF EXISTS "posts" CASCADE;
[2024-02-05 11:22:24.850004] : Dataloom[postgres]: CREATE TABLE IF NOT EXISTS "posts" ("completed" BOOLEAN DEFAULT False, "id" BIGSERIAL PRIMARY KEY UNIQUE NOT NULL, "title" VARCHAR(255) NOT NULL, "createdAt" TIMESTAMP DEFAULT CURRENT_TIMESTAMP, "updatedAt" TIMESTAMP DEFAULT CURRENT_TIMESTAMP, "userId" BIGSERIAL NOT NULL REFERENCES "users"("id") ON DELETE CASCADE ON UPDATE CASCADE);
[2024-02-05 11:22:24.891051] : Dataloom[postgres]: DROP TABLE IF EXISTS "users" CASCADE;
[2024-02-05 11:22:24.925050] : Dataloom[postgres]: CREATE TABLE IF NOT EXISTS "users" ("id" BIGSERIAL PRIMARY KEY UNIQUE NOT NULL, "name" TEXT NOT NULL DEFAULT 'Bob', "username" VARCHAR(255) UNIQUE, "createdAt" TIMESTAMP DEFAULT CURRENT_TIMESTAMP, "updatedAt" TIMESTAMP DEFAULT CURRENT_TIMESTAMP);
[2024-02-05 11:22:24.965011] : Dataloom[postgres]: SELECT tablename FROM pg_catalog.pg_tables WHERE schemaname='public';
[2024-02-05 11:22:25.001004] : Dataloom[postgres]: INSERT INTO "users" ("username") VALUES (%s) RETURNING "id";
[2024-02-05 11:22:25.027431] : Dataloom[postgres]: INSERT INTO "posts" ("title", "userId") VALUES (%s, %s) RETURNING *;
[2024-02-05 11:22:25.152066] : Dataloom[postgres]: DROP TABLE IF EXISTS "posts" CASCADE;
[2024-02-05 11:22:25.185043] : Dataloom[postgres]: CREATE TABLE IF NOT EXISTS "posts" ("completed" BOOLEAN DEFAULT False, "id" BIGSERIAL PRIMARY KEY UNIQUE NOT NULL, "title" VARCHAR(255) NOT NULL, "createdAt" TIMESTAMP DEFAULT CURRENT_TIMESTAMP, "updatedAt" TIMESTAMP DEFAULT CURRENT_TIMESTAMP, "userId" BIGSERIAL NOT NULL REFERENCES "users"("id") ON DELETE CASCADE ON UPDATE CASCADE);
[2024-02-05 11:22:25.219145] : Dataloom[postgres]: DROP TABLE IF EXISTS "users" CASCADE;
[2024-02-05 11:22:25.252428] : Dataloom[postgres]: CREATE TABLE IF NOT EXISTS "users" ("id" BIGSERIAL PRIMARY KEY UNIQUE NOT NULL, "name" TEXT NOT NULL DEFAULT 'Bob', "username" VARCHAR(255) UNIQUE);
[2024-02-05 11:22:25.294440] : Dataloom[postgres]: SELECT tablename FROM pg_catalog.pg_tables WHERE schemaname='public';
[2024-02-05 11:22:25.335472] : Dataloom[postgres]: INSERT INTO "users" ("username") VALUES (%s) RETURNING "id";
[2024-02-05 11:22:25.368533] : Dataloom[postgres]: INSERT INTO "posts" ("title", "userId") VALUES (%s, %s) RETURNING *;
[2024-02-05 11:22:25.399542] : Dataloom[postgres]: SELECT "id", "name", "username" FROM "users" WHERE "id" = %s;
[2024-02-05 11:22:25.426534] : Dataloom[postgres]: SELECT "id", "name", "username" FROM "users" WHERE "id" = %s;
[2024-02-05 11:22:25.451534] : Dataloom[postgres]: SELECT "id", "completed" FROM "posts" WHERE "id" = %s;
[2024-02-05 11:22:25.613763] : Dataloom[postgres]: DROP TABLE IF EXISTS "posts" CASCADE;
[2024-02-05 11:22:25.659268] : Dataloom[postgres]: CREATE TABLE IF NOT EXISTS "posts" ("completed" BOOLEAN DEFAULT False, "id" BIGSERIAL PRIMARY KEY UNIQUE NOT NULL, "title" VARCHAR(255) NOT NULL, "createdAt" TIMESTAMP DEFAULT CURRENT_TIMESTAMP, "updatedAt" TIMESTAMP DEFAULT CURRENT_TIMESTAMP, "userId" BIGSERIAL NOT NULL REFERENCES "users"("id") ON DELETE CASCADE ON UPDATE CASCADE);
[2024-02-05 11:22:25.699291] : Dataloom[postgres]: DROP TABLE IF EXISTS "users" CASCADE;
[2024-02-05 11:22:25.721253] : Dataloom[postgres]: CREATE TABLE IF NOT EXISTS "users" ("id" BIGSERIAL PRIMARY KEY UNIQUE NOT NULL, "name" TEXT NOT NULL DEFAULT 'Bob', "username" VARCHAR(255) UNIQUE);
[2024-02-05 11:22:25.743633] : Dataloom[postgres]: SELECT tablename FROM pg_catalog.pg_tables WHERE schemaname='public';
[2024-02-05 11:22:25.764672] : Dataloom[postgres]: INSERT INTO "users" ("username") VALUES (%s) RETURNING "id";
[2024-02-05 11:22:25.783078] : Dataloom[postgres]: INSERT INTO "posts" ("title", "userId") VALUES (%s, %s) RETURNING *;
[2024-02-05 11:22:25.801847] : Dataloom[postgres]: SELECT "id", "name", "username" FROM "users"   ;
[2024-02-05 11:22:25.819900] : Dataloom[postgres]: SELECT "completed", "createdAt", "id", "title", "updatedAt", "userId" FROM "posts"   ;
[2024-02-05 11:22:25.840905] : Dataloom[postgres]: SELECT "id", "completed" FROM "posts"  LIMIT 3 OFFSET 3;
[2024-02-05 11:22:25.982463] : Dataloom[postgres]: DROP TABLE IF EXISTS "posts" CASCADE;
[2024-02-05 11:22:26.021300] : Dataloom[postgres]: CREATE TABLE IF NOT EXISTS "posts" ("completed" BOOLEAN DEFAULT False, "id" BIGSERIAL PRIMARY KEY UNIQUE NOT NULL, "title" VARCHAR(255) NOT NULL, "createdAt" TIMESTAMP DEFAULT CURRENT_TIMESTAMP, "updatedAt" TIMESTAMP DEFAULT CURRENT_TIMESTAMP, "userId" BIGSERIAL NOT NULL REFERENCES "users"("id") ON DELETE CASCADE ON UPDATE CASCADE);
[2024-02-05 11:22:26.075448] : Dataloom[postgres]: DROP TABLE IF EXISTS "users" CASCADE;
[2024-02-05 11:22:26.119830] : Dataloom[postgres]: CREATE TABLE IF NOT EXISTS "users" ("id" BIGSERIAL PRIMARY KEY UNIQUE NOT NULL, "name" TEXT NOT NULL DEFAULT 'Bob', "username" VARCHAR(255) UNIQUE);
[2024-02-05 11:22:26.165277] : Dataloom[postgres]: SELECT tablename FROM pg_catalog.pg_tables WHERE schemaname='public';
[2024-02-05 11:22:26.215280] : Dataloom[postgres]: INSERT INTO "users" ("username") VALUES (%s) RETURNING "id";
[2024-02-05 11:22:26.249279] : Dataloom[postgres]: INSERT INTO "posts" ("title", "userId") VALUES (%s, %s) RETURNING *;
[2024-02-05 11:22:26.276285] : Dataloom[postgres]: SELECT "id", "name", "username" FROM "users" WHERE "id" = %s   ;
[2024-02-05 11:22:26.295275] : Dataloom[postgres]: SELECT "id", "name", "username" FROM "users" WHERE "id" = %s   ;
[2024-02-05 11:22:26.312273] : Dataloom[postgres]: SELECT "id", "name", "username" FROM "users" WHERE "id" = %s AND "name" = %s   ;
[2024-02-05 11:22:26.331280] : Dataloom[postgres]: SELECT "id", "name", "username" FROM "users" WHERE "id" = %s AND "username" = %s   ;
[2024-02-05 11:22:26.353414] : Dataloom[postgres]: SELECT "id", "name", "username" FROM "users" WHERE "name" = %s AND "username" = %s   ;
[2024-02-05 11:22:26.374476] : Dataloom[postgres]: SELECT "id", "completed" FROM "posts"   ;
[2024-02-05 11:22:26.511705] : Dataloom[postgres]: DROP TABLE IF EXISTS "posts" CASCADE;
[2024-02-05 11:22:26.548211] : Dataloom[postgres]: CREATE TABLE IF NOT EXISTS "posts" ("completed" BOOLEAN DEFAULT False, "id" BIGSERIAL PRIMARY KEY UNIQUE NOT NULL, "title" VARCHAR(255) NOT NULL, "createdAt" TIMESTAMP DEFAULT CURRENT_TIMESTAMP, "updatedAt" TIMESTAMP DEFAULT CURRENT_TIMESTAMP, "userId" BIGSERIAL NOT NULL REFERENCES "users"("id") ON DELETE CASCADE ON UPDATE CASCADE);
[2024-02-05 11:22:26.591563] : Dataloom[postgres]: DROP TABLE IF EXISTS "users" CASCADE;
[2024-02-05 11:22:26.626613] : Dataloom[postgres]: CREATE TABLE IF NOT EXISTS "users" ("id" BIGSERIAL PRIMARY KEY UNIQUE NOT NULL, "name" TEXT NOT NULL DEFAULT 'Bob', "username" VARCHAR(255) UNIQUE);
[2024-02-05 11:22:26.661908] : Dataloom[postgres]: SELECT tablename FROM pg_catalog.pg_tables WHERE schemaname='public';
[2024-02-05 11:22:26.699032] : Dataloom[postgres]: INSERT INTO "users" ("username") VALUES (%s) RETURNING "id";
[2024-02-05 11:22:26.727456] : Dataloom[postgres]: INSERT INTO "posts" ("title", "userId") VALUES (%s, %s) RETURNING *;
[2024-02-05 11:22:26.754702] : Dataloom[postgres]: SELECT "completed", "createdAt", "id", "title", "updatedAt", "userId" FROM "posts" WHERE "id" = %s AND "userId" = %s   ;
[2024-02-05 11:22:26.776795] : Dataloom[postgres]: SELECT "id", "name", "username" FROM "users"   ;
[2024-02-05 11:22:26.799725] : Dataloom[postgres]: SELECT "id", "name", "username" FROM "users" WHERE "id" = %s   ;
[2024-02-05 11:22:26.821727] : Dataloom[postgres]: SELECT "id", "name", "username" FROM "users" WHERE "id" = %s   ;
[2024-02-05 11:22:26.844779] : Dataloom[postgres]: SELECT "id", "name", "username" FROM "users" WHERE "id" = %s AND "name" = %s   ;
[2024-02-05 11:22:26.866779] : Dataloom[postgres]: SELECT "id", "name", "username" FROM "users" WHERE "id" = %s AND "username" = %s   ;
[2024-02-05 11:22:26.888837] : Dataloom[postgres]: SELECT "id", "name", "username" FROM "users" WHERE "name" = %s AND "username" = %s   ;
[2024-02-05 11:22:26.910928] : Dataloom[postgres]: SELECT "id", "completed" FROM "posts" WHERE "userId" = %s  LIMIT 3 OFFSET 3;
[2024-02-05 11:22:26.933927] : Dataloom[postgres]: SELECT "completed", "createdAt", "id", "title", "updatedAt", "userId" FROM "posts"   ;
[2024-02-05 11:22:27.079339] : Dataloom[postgres]: DROP TABLE IF EXISTS "posts" CASCADE;
[2024-02-05 11:22:27.116005] : Dataloom[postgres]: CREATE TABLE IF NOT EXISTS "posts" ("completed" BOOLEAN DEFAULT False, "id" BIGSERIAL PRIMARY KEY UNIQUE NOT NULL, "title" VARCHAR(255) NOT NULL, "createdAt" TIMESTAMP DEFAULT CURRENT_TIMESTAMP, "updatedAt" TIMESTAMP DEFAULT CURRENT_TIMESTAMP, "userId" BIGSERIAL NOT NULL REFERENCES "users"("id") ON DELETE CASCADE ON UPDATE CASCADE);
[2024-02-05 11:22:27.158619] : Dataloom[postgres]: DROP TABLE IF EXISTS "users" CASCADE;
[2024-02-05 11:22:27.196625] : Dataloom[postgres]: CREATE TABLE IF NOT EXISTS "users" ("id" BIGSERIAL PRIMARY KEY UNIQUE NOT NULL, "name" TEXT NOT NULL DEFAULT 'Bob', "username" VARCHAR(255) UNIQUE, "createdAt" TIMESTAMP DEFAULT CURRENT_TIMESTAMP, "updatedAt" TIMESTAMP DEFAULT CURRENT_TIMESTAMP);
[2024-02-05 11:22:27.239551] : Dataloom[postgres]: SELECT tablename FROM pg_catalog.pg_tables WHERE schemaname='public';
[2024-02-05 11:22:27.276294] : Dataloom[postgres]: INSERT INTO "users" ("username") VALUES (%s) RETURNING "id";
[2024-02-05 11:22:27.302298] : Dataloom[postgres]: INSERT INTO "posts" ("title", "userId") VALUES (%s, %s) RETURNING *;
[2024-02-05 11:22:27.383749] : Dataloom[postgres]: UPDATE "users" SET "updatedAt" = %s WHERE "id" = %s;
[2024-02-05 11:22:27.411690] : Dataloom[postgres]: UPDATE "users" SET "updatedAt" = %s WHERE "id" = %s;
[2024-02-05 11:22:27.441379] : Dataloom[postgres]: SELECT "createdAt", "id", "name", "updatedAt", "username" FROM "users" WHERE "id" = %s;
[2024-02-05 11:22:27.467589] : Dataloom[postgres]: UPDATE "users" SET "id" = %s, "updatedAt" = %s WHERE "id" = %s;
[2024-02-05 11:22:27.644317] : Dataloom[postgres]: DROP TABLE IF EXISTS "posts" CASCADE;
[2024-02-05 11:22:27.700318] : Dataloom[postgres]: CREATE TABLE IF NOT EXISTS "posts" ("completed" BOOLEAN DEFAULT False, "id" BIGSERIAL PRIMARY KEY UNIQUE NOT NULL, "title" VARCHAR(255) NOT NULL, "createdAt" TIMESTAMP DEFAULT CURRENT_TIMESTAMP, "userId" BIGSERIAL NOT NULL REFERENCES "users"("id") ON DELETE CASCADE ON UPDATE CASCADE);
[2024-02-05 11:22:27.780977] : Dataloom[postgres]: DROP TABLE IF EXISTS "users" CASCADE;
[2024-02-05 11:22:27.842756] : Dataloom[postgres]: CREATE TABLE IF NOT EXISTS "users" ("id" BIGSERIAL PRIMARY KEY UNIQUE NOT NULL, "name" TEXT NOT NULL DEFAULT 'Bob', "username" VARCHAR(255) UNIQUE, "createdAt" TIMESTAMP DEFAULT CURRENT_TIMESTAMP, "updatedAt" TIMESTAMP DEFAULT CURRENT_TIMESTAMP);
[2024-02-05 11:22:27.905748] : Dataloom[postgres]: SELECT tablename FROM pg_catalog.pg_tables WHERE schemaname='public';
[2024-02-05 11:22:27.961746] : Dataloom[postgres]: INSERT INTO "users" ("username") VALUES (%s) RETURNING "id";
[2024-02-05 11:22:27.999794] : Dataloom[postgres]: INSERT INTO "posts" ("title", "userId") VALUES (%s, %s) RETURNING *;
[2024-02-05 11:22:28.086799] : Dataloom[postgres]: 
        UPDATE "users" SET "name" = %s, "updatedAt" = %s WHERE "id" = (
            SELECT "id" FROM  "users" WHERE "username" = %s LIMIT 1
        );
        
[2024-02-05 11:22:28.112743] : Dataloom[postgres]: 
        UPDATE "users" SET "name" = %s, "updatedAt" = %s WHERE "id" = (
            SELECT "id" FROM  "users" WHERE "username" = %s LIMIT 1
        );
        
[2024-02-05 11:22:28.135743] : Dataloom[postgres]: SELECT "createdAt", "id", "name", "updatedAt", "username" FROM "users" WHERE "id" = %s;
[2024-02-05 11:22:28.157755] : Dataloom[postgres]: 
        UPDATE "users" SET "id" = %s, "updatedAt" = %s WHERE "id" = (
            SELECT "id" FROM  "users" WHERE "username" = %s LIMIT 1
        );
        
[2024-02-05 11:22:28.398750] : Dataloom[postgres]: DROP TABLE IF EXISTS "posts" CASCADE;
[2024-02-05 11:22:28.436745] : Dataloom[postgres]: CREATE TABLE IF NOT EXISTS "posts" ("completed" BOOLEAN DEFAULT False, "id" BIGSERIAL PRIMARY KEY UNIQUE NOT NULL, "title" VARCHAR(255) NOT NULL, "createdAt" TIMESTAMP DEFAULT CURRENT_TIMESTAMP, "userId" BIGSERIAL NOT NULL REFERENCES "users"("id") ON DELETE CASCADE ON UPDATE CASCADE);
[2024-02-05 11:22:28.479198] : Dataloom[postgres]: DROP TABLE IF EXISTS "users" CASCADE;
[2024-02-05 11:22:28.520199] : Dataloom[postgres]: CREATE TABLE IF NOT EXISTS "users" ("id" BIGSERIAL PRIMARY KEY UNIQUE NOT NULL, "name" TEXT NOT NULL DEFAULT 'Bob', "username" VARCHAR(255) UNIQUE, "createdAt" TIMESTAMP DEFAULT CURRENT_TIMESTAMP, "updatedAt" TIMESTAMP DEFAULT CURRENT_TIMESTAMP);
[2024-02-05 11:22:28.558199] : Dataloom[postgres]: SELECT tablename FROM pg_catalog.pg_tables WHERE schemaname='public';
[2024-02-05 11:22:28.590199] : Dataloom[postgres]: INSERT INTO "users" ("username") VALUES (%s) RETURNING "id";
[2024-02-05 11:22:28.618201] : Dataloom[postgres]: INSERT INTO "posts" ("title", "userId") VALUES (%s, %s) RETURNING *;
[2024-02-05 11:22:28.646208] : Dataloom[postgres]: UPDATE "posts" SET "title" = %s WHERE "userId" = %s;
[2024-02-05 11:22:28.670638] : Dataloom[postgres]: UPDATE "posts" SET "title" = %s WHERE "userId" = %s;
[2024-02-05 11:22:28.693682] : Dataloom[postgres]: UPDATE "posts" SET "userId" = %s WHERE "userId" = %s;
[2024-02-05 11:22:28.736641] : Dataloom[sqlite]: DROP TABLE IF EXISTS users;
[2024-02-05 11:22:28.774631] : Dataloom[sqlite]: DROP TABLE IF EXISTS users;
[2024-02-05 11:22:28.812644] : Dataloom[sqlite]: DROP TABLE IF EXISTS users;
[2024-02-05 11:22:28.848646] : Dataloom[sqlite]: CREATE TABLE IF NOT EXISTS `users` (`id` INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL, `name` VARCHAR, `username` TEXT NOT NULL);
[2024-02-05 11:22:28.882465] : Dataloom[sqlite]: DROP TABLE IF EXISTS posts;
[2024-02-05 11:22:28.918421] : Dataloom[sqlite]: CREATE TABLE IF NOT EXISTS `posts` (`id` INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL, `title` TEXT NOT NULL);
[2024-02-05 11:22:28.966424] : Dataloom[sqlite]: SELECT name FROM sqlite_master WHERE type='table';
[2024-02-05 11:22:29.011417] : Dataloom[sqlite]: DROP TABLE IF EXISTS users;
[2024-02-05 11:22:29.048421] : Dataloom[sqlite]: CREATE TABLE IF NOT EXISTS `users` (`id` INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL, `name` VARCHAR UNIQUE, `username` TEXT NOT NULL DEFAULT 'Hello there!!');
[2024-02-05 11:22:29.078462] : Dataloom[sqlite]: DROP TABLE IF EXISTS posts;
[2024-02-05 11:22:29.113423] : Dataloom[sqlite]: CREATE TABLE IF NOT EXISTS `posts` (`completed` BOOLEAN DEFAULT False, `id` INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL, `title` VARCHAR NOT NULL);
[2024-02-05 11:22:29.146463] : Dataloom[sqlite]: SELECT name FROM sqlite_master WHERE type='table';
[2024-02-05 11:22:29.180952] : Dataloom[sqlite]: DROP TABLE IF EXISTS posts;
[2024-02-05 11:22:29.214989] : Dataloom[sqlite]: CREATE TABLE IF NOT EXISTS `posts` (`completed` BOOLEAN DEFAULT False, `id` INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL, `title` VARCHAR NOT NULL, `createdAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP, `updatedAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP, `userId` INTEGER NOT NULL REFERENCES `users`(`id`) ON DELETE CASCADE ON UPDATE CASCADE);
[2024-02-05 11:22:29.249955] : Dataloom[sqlite]: DROP TABLE IF EXISTS users;
[2024-02-05 11:22:29.315949] : Dataloom[sqlite]: CREATE TABLE IF NOT EXISTS `users` (`id` INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL, `name` TEXT NOT NULL DEFAULT 'Bob', `username` VARCHAR UNIQUE, `createdAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP, `updatedAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP);
[2024-02-05 11:22:29.346945] : Dataloom[sqlite]: SELECT name FROM sqlite_master WHERE type='table';
[2024-02-05 11:22:29.371943] : Dataloom[sqlite]: INSERT INTO `users` (`name`, `username`) VALUES (?, ?);
[2024-02-05 11:22:29.403951] : Dataloom[sqlite]: DELETE FROM `users` WHERE `id` = ?;
[2024-02-05 11:22:29.434953] : Dataloom[sqlite]: DELETE FROM `users` WHERE `id` = ?;
[2024-02-05 11:22:29.469192] : Dataloom[sqlite]: DROP TABLE IF EXISTS posts;
[2024-02-05 11:22:29.512946] : Dataloom[sqlite]: CREATE TABLE IF NOT EXISTS `posts` (`completed` BOOLEAN DEFAULT False, `id` INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL, `title` VARCHAR NOT NULL, `createdAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP, `updatedAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP, `userId` INTEGER NOT NULL REFERENCES `users`(`id`) ON DELETE CASCADE ON UPDATE CASCADE);
[2024-02-05 11:22:29.549945] : Dataloom[sqlite]: DROP TABLE IF EXISTS users;
[2024-02-05 11:22:29.588088] : Dataloom[sqlite]: CREATE TABLE IF NOT EXISTS `users` (`id` INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL, `name` TEXT NOT NULL DEFAULT 'Bob', `username` VARCHAR UNIQUE, `createdAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP, `updatedAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP);
[2024-02-05 11:22:29.619091] : Dataloom[sqlite]: SELECT name FROM sqlite_master WHERE type='table';
[2024-02-05 11:22:29.648093] : Dataloom[sqlite]: INSERT INTO `users` (`name`, `username`) VALUES (?, ?);
[2024-02-05 11:22:29.682687] : Dataloom[sqlite]: 
    DELETE FROM `users` WHERE `id` = (
        SELECT `id` FROM  `users` WHERE `name` = ? LIMIT 1
    );
    
[2024-02-05 11:22:29.713699] : Dataloom[sqlite]: SELECT `createdAt`, `id`, `name`, `updatedAt`, `username` FROM `users` WHERE `name` = ?   ;
[2024-02-05 11:22:29.738689] : Dataloom[sqlite]: 
    DELETE FROM `users` WHERE `id` = (
        SELECT `id` FROM  `users` WHERE `name` = ? AND `id` = ? LIMIT 1
    );
    
[2024-02-05 11:22:29.767734] : Dataloom[sqlite]: SELECT `createdAt`, `id`, `name`, `updatedAt`, `username` FROM `users` WHERE `name` = ?   ;
[2024-02-05 11:22:29.789734] : Dataloom[sqlite]: 
    DELETE FROM `users` WHERE `id` = (
        SELECT `id` FROM  `users` WHERE `name` = ? AND `id` = ? LIMIT 1
    );
    
[2024-02-05 11:22:29.816689] : Dataloom[sqlite]: SELECT `createdAt`, `id`, `name`, `updatedAt`, `username` FROM `users` WHERE `name` = ?   ;
[2024-02-05 11:22:29.849687] : Dataloom[sqlite]: DROP TABLE IF EXISTS posts;
[2024-02-05 11:22:29.885689] : Dataloom[sqlite]: CREATE TABLE IF NOT EXISTS `posts` (`completed` BOOLEAN DEFAULT False, `id` INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL, `title` VARCHAR NOT NULL, `createdAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP, `updatedAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP, `userId` INTEGER NOT NULL REFERENCES `users`(`id`) ON DELETE CASCADE ON UPDATE CASCADE);
[2024-02-05 11:22:29.914689] : Dataloom[sqlite]: DROP TABLE IF EXISTS users;
[2024-02-05 11:22:29.944688] : Dataloom[sqlite]: CREATE TABLE IF NOT EXISTS `users` (`id` INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL, `name` TEXT NOT NULL DEFAULT 'Bob', `username` VARCHAR UNIQUE, `createdAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP, `updatedAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP);
[2024-02-05 11:22:29.978737] : Dataloom[sqlite]: SELECT name FROM sqlite_master WHERE type='table';
[2024-02-05 11:22:30.003701] : Dataloom[sqlite]: INSERT INTO `users` (`name`, `username`) VALUES (?, ?);
[2024-02-05 11:22:30.034690] : Dataloom[sqlite]: DELETE FROM `users` WHERE `name` = ?;
[2024-02-05 11:22:30.070297] : Dataloom[sqlite]: SELECT `createdAt`, `id`, `name`, `updatedAt`, `username` FROM `users` WHERE `name` = ?   ;
[2024-02-05 11:22:30.098298] : Dataloom[sqlite]: INSERT INTO `users` (`name`, `username`) VALUES (?, ?);
[2024-02-05 11:22:30.130293] : Dataloom[sqlite]: DELETE FROM `users` WHERE `name` = ? AND `id` = ?;
[2024-02-05 11:22:30.155453] : Dataloom[sqlite]: SELECT `createdAt`, `id`, `name`, `updatedAt`, `username` FROM `users` WHERE `name` = ?   ;
[2024-02-05 11:22:30.184294] : Dataloom[sqlite]: DELETE FROM `users` WHERE `name` = ? AND `id` = ?;
[2024-02-05 11:22:30.214342] : Dataloom[sqlite]: SELECT `createdAt`, `id`, `name`, `updatedAt`, `username` FROM `users` WHERE `name` = ?   ;
[2024-02-05 11:22:30.256306] : Dataloom[sqlite]: DROP TABLE IF EXISTS posts;
[2024-02-05 11:22:30.294297] : Dataloom[sqlite]: CREATE TABLE IF NOT EXISTS `posts` (`completed` BOOLEAN DEFAULT False, `id` INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL, `title` VARCHAR NOT NULL, `createdAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP, `updatedAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP, `userId` INTEGER NOT NULL REFERENCES `users`(`id`) ON DELETE CASCADE ON UPDATE CASCADE);
[2024-02-05 11:22:30.329296] : Dataloom[sqlite]: DROP TABLE IF EXISTS users;
[2024-02-05 11:22:30.357295] : Dataloom[sqlite]: CREATE TABLE IF NOT EXISTS `users` (`id` INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL, `name` TEXT NOT NULL DEFAULT 'Bob', `username` VARCHAR UNIQUE, `createdAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP, `updatedAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP);
[2024-02-05 11:22:30.384344] : Dataloom[sqlite]: SELECT name FROM sqlite_master WHERE type='table';
[2024-02-05 11:22:30.410387] : Dataloom[sqlite]: INSERT INTO `users` (`username`) VALUES (?);
[2024-02-05 11:22:30.447387] : Dataloom[sqlite]: INSERT INTO `posts` (`title`, `userId`) VALUES (?, ?);
[2024-02-05 11:22:30.491818] : Dataloom[sqlite]: DROP TABLE IF EXISTS posts;
[2024-02-05 11:22:30.529823] : Dataloom[sqlite]: CREATE TABLE IF NOT EXISTS `posts` (`completed` BOOLEAN DEFAULT False, `id` INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL, `title` VARCHAR NOT NULL, `createdAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP, `updatedAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP, `userId` INTEGER NOT NULL REFERENCES `users`(`id`) ON DELETE CASCADE ON UPDATE CASCADE);
[2024-02-05 11:22:30.570441] : Dataloom[sqlite]: DROP TABLE IF EXISTS users;
[2024-02-05 11:22:30.610446] : Dataloom[sqlite]: CREATE TABLE IF NOT EXISTS `users` (`id` INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL, `name` TEXT NOT NULL DEFAULT 'Bob', `username` VARCHAR UNIQUE, `createdAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP, `updatedAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP);
[2024-02-05 11:22:30.647447] : Dataloom[sqlite]: SELECT name FROM sqlite_master WHERE type='table';
[2024-02-05 11:22:30.676501] : Dataloom[sqlite]: INSERT INTO `users` (`username`) VALUES (?);
[2024-02-05 11:22:30.707499] : Dataloom[sqlite]: INSERT INTO `posts` (`title`, `userId`) VALUES (?, ?);
[2024-02-05 11:22:30.751958] : Dataloom[sqlite]: DROP TABLE IF EXISTS posts;
[2024-02-05 11:22:30.798507] : Dataloom[sqlite]: CREATE TABLE IF NOT EXISTS `posts` (`completed` BOOLEAN DEFAULT False, `id` INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL, `title` VARCHAR NOT NULL, `createdAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP, `updatedAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP, `userId` INTEGER NOT NULL REFERENCES `users`(`id`) ON DELETE CASCADE ON UPDATE CASCADE);
[2024-02-05 11:22:30.835504] : Dataloom[sqlite]: DROP TABLE IF EXISTS users;
[2024-02-05 11:22:30.876504] : Dataloom[sqlite]: CREATE TABLE IF NOT EXISTS `users` (`id` INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL, `name` TEXT NOT NULL DEFAULT 'Bob', `username` VARCHAR UNIQUE);
[2024-02-05 11:22:30.915522] : Dataloom[sqlite]: SELECT name FROM sqlite_master WHERE type='table';
[2024-02-05 11:22:30.956510] : Dataloom[sqlite]: INSERT INTO `users` (`username`) VALUES (?);
[2024-02-05 11:22:31.012078] : Dataloom[sqlite]: INSERT INTO `posts` (`title`, `userId`) VALUES (?, ?);
[2024-02-05 11:22:31.059130] : Dataloom[sqlite]: SELECT `id`, `name`, `username` FROM `users` WHERE `id` = ?;
[2024-02-05 11:22:31.099092] : Dataloom[sqlite]: SELECT `id`, `name`, `username` FROM `users` WHERE `id` = ?;
[2024-02-05 11:22:31.126081] : Dataloom[sqlite]: SELECT `id`, `completed` FROM `posts` WHERE `id` = ?;
[2024-02-05 11:22:31.173078] : Dataloom[sqlite]: DROP TABLE IF EXISTS posts;
[2024-02-05 11:22:31.202885] : Dataloom[sqlite]: CREATE TABLE IF NOT EXISTS `posts` (`completed` BOOLEAN DEFAULT False, `id` INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL, `title` VARCHAR NOT NULL, `createdAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP, `updatedAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP, `userId` INTEGER NOT NULL REFERENCES `users`(`id`) ON DELETE CASCADE ON UPDATE CASCADE);
[2024-02-05 11:22:31.228886] : Dataloom[sqlite]: DROP TABLE IF EXISTS users;
[2024-02-05 11:22:31.258883] : Dataloom[sqlite]: CREATE TABLE IF NOT EXISTS `users` (`id` INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL, `name` TEXT NOT NULL DEFAULT 'Bob', `username` VARCHAR UNIQUE);
[2024-02-05 11:22:31.290884] : Dataloom[sqlite]: SELECT name FROM sqlite_master WHERE type='table';
[2024-02-05 11:22:31.321884] : Dataloom[sqlite]: INSERT INTO `users` (`username`) VALUES (?);
[2024-02-05 11:22:31.354884] : Dataloom[sqlite]: INSERT INTO `posts` (`title`, `userId`) VALUES (?, ?);
[2024-02-05 11:22:31.391458] : Dataloom[sqlite]: SELECT `id`, `name`, `username` FROM `users`   ;
[2024-02-05 11:22:31.412452] : Dataloom[sqlite]: SELECT `completed`, `createdAt`, `id`, `title`, `updatedAt`, `userId` FROM `posts`   ;
[2024-02-05 11:22:31.442454] : Dataloom[sqlite]: SELECT `id`, `completed` FROM `posts`  LIMIT 3 OFFSET 3;
[2024-02-05 11:22:31.484455] : Dataloom[sqlite]: DROP TABLE IF EXISTS posts;
[2024-02-05 11:22:31.527458] : Dataloom[sqlite]: CREATE TABLE IF NOT EXISTS `posts` (`completed` BOOLEAN DEFAULT False, `id` INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL, `title` VARCHAR NOT NULL, `createdAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP, `updatedAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP, `userId` INTEGER NOT NULL REFERENCES `users`(`id`) ON DELETE CASCADE ON UPDATE CASCADE);
[2024-02-05 11:22:31.564458] : Dataloom[sqlite]: DROP TABLE IF EXISTS users;
[2024-02-05 11:22:31.593680] : Dataloom[sqlite]: CREATE TABLE IF NOT EXISTS `users` (`id` INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL, `name` TEXT NOT NULL DEFAULT 'Bob', `username` VARCHAR UNIQUE);
[2024-02-05 11:22:31.623454] : Dataloom[sqlite]: SELECT name FROM sqlite_master WHERE type='table';
[2024-02-05 11:22:31.656455] : Dataloom[sqlite]: INSERT INTO `users` (`username`) VALUES (?);
[2024-02-05 11:22:31.689558] : Dataloom[sqlite]: INSERT INTO `posts` (`title`, `userId`) VALUES (?, ?);
[2024-02-05 11:22:31.717562] : Dataloom[sqlite]: SELECT `id`, `name`, `username` FROM `users` WHERE `id` = ?   ;
[2024-02-05 11:22:31.742562] : Dataloom[sqlite]: SELECT `id`, `name`, `username` FROM `users` WHERE `id` = ?   ;
[2024-02-05 11:22:31.774561] : Dataloom[sqlite]: SELECT `id`, `name`, `username` FROM `users` WHERE `id` = ? AND `name` = ?   ;
[2024-02-05 11:22:31.804214] : Dataloom[sqlite]: SELECT `id`, `name`, `username` FROM `users` WHERE `id` = ? AND `username` = ?   ;
[2024-02-05 11:22:31.836012] : Dataloom[sqlite]: SELECT `id`, `name`, `username` FROM `users` WHERE `name` = ? AND `username` = ?   ;
[2024-02-05 11:22:31.867085] : Dataloom[sqlite]: SELECT `id`, `completed` FROM `posts`   ;
[2024-02-05 11:22:31.921009] : Dataloom[sqlite]: DROP TABLE IF EXISTS posts;
[2024-02-05 11:22:31.970004] : Dataloom[sqlite]: CREATE TABLE IF NOT EXISTS `posts` (`completed` BOOLEAN DEFAULT False, `id` INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL, `title` VARCHAR NOT NULL, `createdAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP, `updatedAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP, `userId` INTEGER NOT NULL REFERENCES `users`(`id`) ON DELETE CASCADE ON UPDATE CASCADE);
[2024-02-05 11:22:32.001003] : Dataloom[sqlite]: DROP TABLE IF EXISTS users;
[2024-02-05 11:22:32.027180] : Dataloom[sqlite]: CREATE TABLE IF NOT EXISTS `users` (`id` INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL, `name` TEXT NOT NULL DEFAULT 'Bob', `username` VARCHAR UNIQUE);
[2024-02-05 11:22:32.054005] : Dataloom[sqlite]: SELECT name FROM sqlite_master WHERE type='table';
[2024-02-05 11:22:32.080002] : Dataloom[sqlite]: INSERT INTO `users` (`username`) VALUES (?);
[2024-02-05 11:22:32.112001] : Dataloom[sqlite]: INSERT INTO `posts` (`title`, `userId`) VALUES (?, ?);
[2024-02-05 11:22:32.137999] : Dataloom[sqlite]: SELECT `completed`, `createdAt`, `id`, `title`, `updatedAt`, `userId` FROM `posts` WHERE `id` = ? AND `userId` = ?   ;
[2024-02-05 11:22:32.161001] : Dataloom[sqlite]: SELECT `id`, `name`, `username` FROM `users`   ;
[2024-02-05 11:22:32.185364] : Dataloom[sqlite]: SELECT `id`, `name`, `username` FROM `users` WHERE `id` = ?   ;
[2024-02-05 11:22:32.216364] : Dataloom[sqlite]: SELECT `id`, `name`, `username` FROM `users` WHERE `id` = ?   ;
[2024-02-05 11:22:32.245461] : Dataloom[sqlite]: SELECT `id`, `name`, `username` FROM `users` WHERE `id` = ? AND `name` = ?   ;
[2024-02-05 11:22:32.271359] : Dataloom[sqlite]: SELECT `id`, `name`, `username` FROM `users` WHERE `id` = ? AND `username` = ?   ;
[2024-02-05 11:22:32.300364] : Dataloom[sqlite]: SELECT `id`, `name`, `username` FROM `users` WHERE `name` = ? AND `username` = ?   ;
[2024-02-05 11:22:32.331417] : Dataloom[sqlite]: SELECT `id`, `completed` FROM `posts` WHERE `userId` = ?  LIMIT 3 OFFSET 3;
[2024-02-05 11:22:32.362419] : Dataloom[sqlite]: SELECT `completed`, `createdAt`, `id`, `title`, `updatedAt`, `userId` FROM `posts`   ;
[2024-02-05 11:22:32.395406] : Dataloom[sqlite]: DROP TABLE IF EXISTS posts;
[2024-02-05 11:22:32.441385] : Dataloom[sqlite]: CREATE TABLE IF NOT EXISTS `posts` (`completed` BOOLEAN DEFAULT False, `id` INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL, `title` VARCHAR NOT NULL, `createdAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP, `updatedAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP, `userId` INTEGER NOT NULL REFERENCES `users`(`id`) ON DELETE CASCADE ON UPDATE CASCADE);
[2024-02-05 11:22:32.474407] : Dataloom[sqlite]: DROP TABLE IF EXISTS users;
[2024-02-05 11:22:32.504016] : Dataloom[sqlite]: CREATE TABLE IF NOT EXISTS `users` (`id` INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL, `name` TEXT NOT NULL DEFAULT 'Bob', `username` VARCHAR UNIQUE, `createdAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP, `updatedAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP);
[2024-02-05 11:22:32.538058] : Dataloom[sqlite]: SELECT name FROM sqlite_master WHERE type='table';
[2024-02-05 11:22:32.568007] : Dataloom[sqlite]: INSERT INTO `users` (`username`) VALUES (?);
[2024-02-05 11:22:32.603007] : Dataloom[sqlite]: INSERT INTO `posts` (`title`, `userId`) VALUES (?, ?);
[2024-02-05 11:22:32.683051] : Dataloom[sqlite]: UPDATE `users` SET `updatedAt` = ? WHERE `id` = ?;
[2024-02-05 11:22:32.712788] : Dataloom[sqlite]: UPDATE `users` SET `updatedAt` = ? WHERE `id` = ?;
[2024-02-05 11:22:32.733832] : Dataloom[sqlite]: SELECT `createdAt`, `id`, `name`, `updatedAt`, `username` FROM `users` WHERE `id` = ?;
[2024-02-05 11:22:32.769821] : Dataloom[sqlite]: DROP TABLE IF EXISTS posts;
[2024-02-05 11:22:32.809338] : Dataloom[sqlite]: CREATE TABLE IF NOT EXISTS `posts` (`completed` BOOLEAN DEFAULT False, `id` INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL, `title` VARCHAR NOT NULL, `createdAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP, `userId` INTEGER NOT NULL REFERENCES `users`(`id`) ON DELETE CASCADE ON UPDATE CASCADE);
[2024-02-05 11:22:32.845334] : Dataloom[sqlite]: DROP TABLE IF EXISTS users;
[2024-02-05 11:22:32.886389] : Dataloom[sqlite]: CREATE TABLE IF NOT EXISTS `users` (`id` INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL, `name` TEXT NOT NULL DEFAULT 'Bob', `username` VARCHAR UNIQUE, `createdAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP, `updatedAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP);
[2024-02-05 11:22:32.919340] : Dataloom[sqlite]: SELECT name FROM sqlite_master WHERE type='table';
[2024-02-05 11:22:32.953336] : Dataloom[sqlite]: INSERT INTO `users` (`username`) VALUES (?);
[2024-02-05 11:22:32.992344] : Dataloom[sqlite]: INSERT INTO `posts` (`title`, `userId`) VALUES (?, ?);
[2024-02-05 11:22:33.070380] : Dataloom[sqlite]: 
        UPDATE `posts` SET `title` = ? WHERE `id` = (
            SELECT `id` FROM  `posts` WHERE `userId` = ? LIMIT 1
        );
        
[2024-02-05 11:22:33.099380] : Dataloom[sqlite]: 
        UPDATE `posts` SET `title` = ? WHERE `id` = (
            SELECT `id` FROM  `posts` WHERE `userId` = ? LIMIT 1
        );
        
[2024-02-05 11:22:33.121334] : Dataloom[sqlite]: SELECT `completed`, `createdAt`, `id`, `title`, `userId` FROM `posts` WHERE `id` = ?;
[2024-02-05 11:22:33.148457] : Dataloom[sqlite]: DROP TABLE IF EXISTS posts;
[2024-02-05 11:22:33.187947] : Dataloom[sqlite]: CREATE TABLE IF NOT EXISTS `posts` (`completed` BOOLEAN DEFAULT False, `id` INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL, `title` VARCHAR NOT NULL, `createdAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP, `userId` INTEGER NOT NULL REFERENCES `users`(`id`) ON DELETE CASCADE ON UPDATE CASCADE);
[2024-02-05 11:22:33.225337] : Dataloom[sqlite]: DROP TABLE IF EXISTS users;
[2024-02-05 11:22:33.257337] : Dataloom[sqlite]: CREATE TABLE IF NOT EXISTS `users` (`id` INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL, `name` TEXT NOT NULL DEFAULT 'Bob', `username` VARCHAR UNIQUE, `createdAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP, `updatedAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP);
[2024-02-05 11:22:33.287336] : Dataloom[sqlite]: SELECT name FROM sqlite_master WHERE type='table';
[2024-02-05 11:22:33.317924] : Dataloom[sqlite]: INSERT INTO `users` (`username`) VALUES (?);
[2024-02-05 11:22:33.345931] : Dataloom[sqlite]: INSERT INTO `posts` (`title`, `userId`) VALUES (?, ?);
[2024-02-05 11:22:33.431540] : Dataloom[sqlite]: UPDATE `posts` SET `title` = ? WHERE `userId` = ?;
[2024-02-05 11:22:33.467540] : Dataloom[sqlite]: UPDATE `posts` SET `title` = ? WHERE `userId` = ?;
[2024-02-05 11:22:33.497540] : Dataloom[sqlite]: SELECT `completed`, `createdAt`, `id`, `title`, `userId` FROM `posts` WHERE `id` = ?;
