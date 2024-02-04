[2024-02-04 11:48:44.605899] : Dataloom[mysql]: DROP TABLE IF EXISTS `users`;
[2024-02-04 11:48:44.740876] : Dataloom[mysql]: DROP TABLE IF EXISTS `users`;
[2024-02-04 11:48:44.854880] : Dataloom[mysql]: DROP TABLE IF EXISTS `users`;
[2024-02-04 11:48:44.897869] : Dataloom[mysql]: CREATE TABLE IF NOT EXISTS `users` (`id` INT PRIMARY KEY AUTO_INCREMENT UNIQUE NOT NULL, `name` VARCHAR(255), `username` TEXT NOT NULL);
[2024-02-04 11:48:44.990864] : Dataloom[mysql]: DROP TABLE IF EXISTS `posts`;
[2024-02-04 11:48:45.057871] : Dataloom[mysql]: CREATE TABLE IF NOT EXISTS `posts` (`id` INT PRIMARY KEY AUTO_INCREMENT UNIQUE NOT NULL, `title` TEXT NOT NULL);
[2024-02-04 11:48:45.149614] : Dataloom[mysql]: SHOW TABLES;
[2024-02-04 11:48:45.203955] : Dataloom[mysql]: DROP TABLE IF EXISTS `users`;
[2024-02-04 11:48:45.287936] : Dataloom[mysql]: CREATE TABLE IF NOT EXISTS `users` (`id` INT PRIMARY KEY AUTO_INCREMENT UNIQUE NOT NULL, `name` VARCHAR(255) UNIQUE, `username` VARCHAR(255) NOT NULL DEFAULT 'Hello there!!');
[2024-02-04 11:48:45.410723] : Dataloom[mysql]: DROP TABLE IF EXISTS `posts`;
[2024-02-04 11:48:45.490725] : Dataloom[mysql]: CREATE TABLE IF NOT EXISTS `posts` (`completed` BOOLEAN DEFAULT False, `id` INT PRIMARY KEY AUTO_INCREMENT UNIQUE NOT NULL, `title` VARCHAR(255) NOT NULL);
[2024-02-04 11:48:45.593720] : Dataloom[mysql]: SHOW TABLES;
[2024-02-04 11:48:45.657722] : Dataloom[mysql]: DROP TABLE IF EXISTS `posts`;
[2024-02-04 11:48:45.764241] : Dataloom[mysql]: CREATE TABLE IF NOT EXISTS `posts` (`completed` BOOLEAN DEFAULT False, `id` INT PRIMARY KEY AUTO_INCREMENT UNIQUE NOT NULL, `title` VARCHAR(255) NOT NULL, `createdAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP, `updatedAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP, `userId` INT NOT NULL REFERENCES `users`(`id`) ON DELETE CASCADE ON UPDATE CASCADE);
[2024-02-04 11:48:45.852194] : Dataloom[mysql]: DROP TABLE IF EXISTS `users`;
[2024-02-04 11:48:45.906754] : Dataloom[mysql]: CREATE TABLE IF NOT EXISTS `users` (`id` INT PRIMARY KEY AUTO_INCREMENT UNIQUE NOT NULL, `name` VARCHAR(255) NOT NULL DEFAULT 'Bob', `username` VARCHAR(255) UNIQUE, `createdAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP, `updatedAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP);
[2024-02-04 11:48:46.024130] : Dataloom[mysql]: SHOW TABLES;
[2024-02-04 11:48:46.058134] : Dataloom[mysql]: INSERT INTO `users` (`username`) VALUES (%s);
[2024-02-04 11:48:46.104123] : Dataloom[mysql]: INSERT INTO `posts` (`title`, `userId`) VALUES (%s, %s);
[2024-02-04 11:48:46.207538] : Dataloom[mysql]: DROP TABLE IF EXISTS `posts`;
[2024-02-04 11:48:46.272040] : Dataloom[mysql]: CREATE TABLE IF NOT EXISTS `posts` (`completed` BOOLEAN DEFAULT False, `id` INT PRIMARY KEY AUTO_INCREMENT UNIQUE NOT NULL, `title` VARCHAR(255) NOT NULL, `createdAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP, `updatedAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP, `userId` INT NOT NULL REFERENCES `users`(`id`) ON DELETE CASCADE ON UPDATE CASCADE);
[2024-02-04 11:48:46.340037] : Dataloom[mysql]: DROP TABLE IF EXISTS `users`;
[2024-02-04 11:48:46.410662] : Dataloom[mysql]: CREATE TABLE IF NOT EXISTS `users` (`id` INT PRIMARY KEY AUTO_INCREMENT UNIQUE NOT NULL, `name` VARCHAR(255) NOT NULL DEFAULT 'Bob', `username` VARCHAR(255) UNIQUE, `createdAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP, `updatedAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP);
[2024-02-04 11:48:46.514292] : Dataloom[mysql]: SHOW TABLES;
[2024-02-04 11:48:46.556294] : Dataloom[mysql]: INSERT INTO `users` (`username`) VALUES (%s);
[2024-02-04 11:48:46.604302] : Dataloom[mysql]: INSERT INTO `posts` (`title`, `userId`) VALUES (%s, %s);
[2024-02-04 11:48:46.704877] : Dataloom[mysql]: DROP TABLE IF EXISTS `posts`;
[2024-02-04 11:48:46.816164] : Dataloom[mysql]: CREATE TABLE IF NOT EXISTS `posts` (`completed` BOOLEAN DEFAULT False, `id` INT PRIMARY KEY AUTO_INCREMENT UNIQUE NOT NULL, `title` VARCHAR(255) NOT NULL, `createdAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP, `updatedAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP, `userId` INT NOT NULL REFERENCES `users`(`id`) ON DELETE CASCADE ON UPDATE CASCADE);
[2024-02-04 11:48:46.936274] : Dataloom[mysql]: DROP TABLE IF EXISTS `users`;
[2024-02-04 11:48:47.034383] : Dataloom[mysql]: CREATE TABLE IF NOT EXISTS `users` (`id` INT PRIMARY KEY AUTO_INCREMENT UNIQUE NOT NULL, `name` VARCHAR(255) NOT NULL DEFAULT 'Bob', `username` VARCHAR(255) UNIQUE);
[2024-02-04 11:48:47.160806] : Dataloom[mysql]: SHOW TABLES;
[2024-02-04 11:48:47.192448] : Dataloom[mysql]: INSERT INTO `users` (`username`) VALUES (%s);
[2024-02-04 11:48:47.228450] : Dataloom[mysql]: INSERT INTO `posts` (`title`, `userId`) VALUES (%s, %s);
[2024-02-04 11:48:47.265449] : Dataloom[mysql]: SELECT `completed`, `createdAt`, `id`, `title`, `updatedAt`, `userId` FROM `posts` WHERE `id` = %s AND `userId` = %s;
[2024-02-04 11:48:47.293208] : Dataloom[mysql]: SELECT `id`, `name`, `username` FROM `users`;
[2024-02-04 11:48:47.322215] : Dataloom[mysql]: SELECT `id`, `name`, `username` FROM `users` WHERE `id` = %s;
[2024-02-04 11:48:47.354209] : Dataloom[mysql]: SELECT `id`, `name`, `username` FROM `users` WHERE `id` = %s;
[2024-02-04 11:48:47.381931] : Dataloom[mysql]: SELECT `id`, `name`, `username` FROM `users` WHERE `id` = %s;
[2024-02-04 11:48:47.409049] : Dataloom[mysql]: SELECT `id`, `name`, `username` FROM `users` WHERE `id` = %s;
[2024-02-04 11:48:47.440084] : Dataloom[mysql]: SELECT `id`, `name`, `username` FROM `users` WHERE `id` = %s AND `name` = %s;
[2024-02-04 11:48:47.469081] : Dataloom[mysql]: SELECT `id`, `name`, `username` FROM `users` WHERE `id` = %s AND `username` = %s;
[2024-02-04 11:48:47.495711] : Dataloom[mysql]: SELECT `id`, `name`, `username` FROM `users` WHERE `name` = %s AND `username` = %s;
[2024-02-04 11:48:47.522703] : Dataloom[mysql]: SELECT `id`, `name`, `username` FROM `users` WHERE `id` = %s;
[2024-02-04 11:48:47.549681] : Dataloom[mysql]: SELECT `id`, `name`, `username` FROM `users` WHERE `id` = %s;
[2024-02-04 11:48:47.576681] : Dataloom[mysql]: SELECT `id`, `name`, `username` FROM `users` WHERE `id` = %s AND `name` = %s;
[2024-02-04 11:48:47.603346] : Dataloom[mysql]: SELECT `id`, `name`, `username` FROM `users` WHERE `id` = %s AND `username` = %s;
[2024-02-04 11:48:47.630346] : Dataloom[mysql]: SELECT `id`, `name`, `username` FROM `users` WHERE `name` = %s AND `username` = %s;
[2024-02-04 11:48:47.657297] : Dataloom[mysql]: SELECT `completed`, `createdAt`, `id`, `title`, `updatedAt`, `userId` FROM `posts`;
[2024-02-04 11:48:47.727689] : Dataloom[mysql]: DROP TABLE IF EXISTS `posts`;
[2024-02-04 11:48:47.835270] : Dataloom[mysql]: CREATE TABLE IF NOT EXISTS `posts` (`completed` BOOLEAN DEFAULT False, `id` INT PRIMARY KEY AUTO_INCREMENT UNIQUE NOT NULL, `title` VARCHAR(255) NOT NULL, `createdAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP, `updatedAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP, `userId` INT NOT NULL REFERENCES `users`(`id`) ON DELETE CASCADE ON UPDATE CASCADE);
[2024-02-04 11:48:47.937669] : Dataloom[mysql]: DROP TABLE IF EXISTS `users`;
[2024-02-04 11:48:48.028555] : Dataloom[mysql]: CREATE TABLE IF NOT EXISTS `users` (`id` INT PRIMARY KEY AUTO_INCREMENT UNIQUE NOT NULL, `name` VARCHAR(255) NOT NULL DEFAULT 'Bob', `username` VARCHAR(255) UNIQUE, `createdAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP, `updatedAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP);
[2024-02-04 11:48:48.144296] : Dataloom[mysql]: SHOW TABLES;
[2024-02-04 11:48:48.180305] : Dataloom[mysql]: INSERT INTO `users` (`username`) VALUES (%s);
[2024-02-04 11:48:48.218298] : Dataloom[mysql]: INSERT INTO `posts` (`title`, `userId`) VALUES (%s, %s);
[2024-02-04 11:48:48.306298] : Dataloom[mysql]: UPDATE `users` SET `updatedAt` = %s WHERE `id` = %s;
[2024-02-04 11:48:48.347298] : Dataloom[mysql]: UPDATE `users` SET `updatedAt` = %s WHERE `id` = %s;
[2024-02-04 11:48:48.381368] : Dataloom[mysql]: SELECT `createdAt`, `id`, `name`, `updatedAt`, `username` FROM `users` WHERE `id` = %s;
[2024-02-04 11:48:48.408865] : Dataloom[mysql]: UPDATE `users` SET `id` = %s, `updatedAt` = %s WHERE `id` = %s;
[2024-02-04 11:48:48.453862] : Dataloom[mysql]: DROP TABLE IF EXISTS `posts`;
[2024-02-04 11:48:48.541113] : Dataloom[mysql]: CREATE TABLE IF NOT EXISTS `posts` (`completed` BOOLEAN DEFAULT False, `id` INT PRIMARY KEY AUTO_INCREMENT UNIQUE NOT NULL, `title` VARCHAR(255) NOT NULL, `createdAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP, `userId` INT NOT NULL REFERENCES `users`(`id`) ON DELETE CASCADE ON UPDATE CASCADE);
[2024-02-04 11:48:48.634252] : Dataloom[mysql]: DROP TABLE IF EXISTS `users`;
[2024-02-04 11:48:48.715825] : Dataloom[mysql]: CREATE TABLE IF NOT EXISTS `users` (`id` INT PRIMARY KEY AUTO_INCREMENT UNIQUE NOT NULL, `name` VARCHAR(255) NOT NULL DEFAULT 'Bob', `username` VARCHAR(255) UNIQUE, `createdAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP, `updatedAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP);
[2024-02-04 11:48:48.826047] : Dataloom[mysql]: SHOW TABLES;
[2024-02-04 11:48:48.857986] : Dataloom[mysql]: INSERT INTO `users` (`username`) VALUES (%s);
[2024-02-04 11:48:48.896910] : Dataloom[mysql]: INSERT INTO `posts` (`title`, `userId`) VALUES (%s, %s);
[2024-02-04 11:48:48.985753] : Dataloom[mysql]: 
        UPDATE `posts` SET `title` = %s WHERE `id` IN (
            SELECT `id` FROM  (
                SELECT `id` FROM `posts` WHERE `userId` = %s LIMIT 1
            ) AS subquery
        );
        
[2024-02-04 11:48:49.020818] : Dataloom[mysql]: 
        UPDATE `posts` SET `title` = %s WHERE `id` IN (
            SELECT `id` FROM  (
                SELECT `id` FROM `posts` WHERE `userId` = %s LIMIT 1
            ) AS subquery
        );
        
[2024-02-04 11:48:49.048826] : Dataloom[mysql]: SELECT `completed`, `createdAt`, `id`, `title`, `userId` FROM `posts` WHERE `id` = %s;
[2024-02-04 11:48:49.075825] : Dataloom[mysql]: 
        UPDATE `posts` SET `userId` = %s WHERE `id` IN (
            SELECT `id` FROM  (
                SELECT `id` FROM `posts` WHERE `userId` = %s LIMIT 1
            ) AS subquery
        );
        
[2024-02-04 11:48:49.135575] : Dataloom[mysql]: DROP TABLE IF EXISTS `posts`;
[2024-02-04 11:48:49.241260] : Dataloom[mysql]: CREATE TABLE IF NOT EXISTS `posts` (`completed` BOOLEAN DEFAULT False, `id` INT PRIMARY KEY AUTO_INCREMENT UNIQUE NOT NULL, `title` VARCHAR(255) NOT NULL, `createdAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP, `userId` INT NOT NULL REFERENCES `users`(`id`) ON DELETE CASCADE ON UPDATE CASCADE);
[2024-02-04 11:48:49.351510] : Dataloom[mysql]: DROP TABLE IF EXISTS `users`;
[2024-02-04 11:48:49.438731] : Dataloom[mysql]: CREATE TABLE IF NOT EXISTS `users` (`id` INT PRIMARY KEY AUTO_INCREMENT UNIQUE NOT NULL, `name` VARCHAR(255) NOT NULL DEFAULT 'Bob', `username` VARCHAR(255) UNIQUE, `createdAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP, `updatedAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP);
[2024-02-04 11:48:49.555130] : Dataloom[mysql]: SHOW TABLES;
[2024-02-04 11:48:49.587119] : Dataloom[mysql]: INSERT INTO `users` (`username`) VALUES (%s);
[2024-02-04 11:48:49.620279] : Dataloom[mysql]: INSERT INTO `posts` (`title`, `userId`) VALUES (%s, %s);
[2024-02-04 11:48:49.714040] : Dataloom[mysql]: UPDATE `posts` SET `title` = %s WHERE `userId` = %s;
[2024-02-04 11:48:49.754026] : Dataloom[mysql]: UPDATE `posts` SET `title` = %s WHERE `userId` = %s;
[2024-02-04 11:48:49.793023] : Dataloom[mysql]: SELECT `completed`, `createdAt`, `id`, `title`, `userId` FROM `posts` WHERE `id` = %s;
[2024-02-04 11:48:49.824059] : Dataloom[mysql]: UPDATE `posts` SET `userId` = %s WHERE `userId` = %s;
[2024-02-04 11:48:50.870002] : Dataloom[postgres]: DROP TABLE IF EXISTS "users" CASCADE;
[2024-02-04 11:48:51.056997] : Dataloom[postgres]: DROP TABLE IF EXISTS "users" CASCADE;
[2024-02-04 11:48:51.258035] : Dataloom[postgres]: DROP TABLE IF EXISTS "users" CASCADE;
[2024-02-04 11:48:51.278768] : Dataloom[postgres]: CREATE TABLE IF NOT EXISTS "users" ("id" BIGSERIAL PRIMARY KEY UNIQUE NOT NULL, "name" VARCHAR(255), "username" TEXT NOT NULL);
[2024-02-04 11:48:51.343648] : Dataloom[postgres]: DROP TABLE IF EXISTS "posts" CASCADE;
[2024-02-04 11:48:51.396699] : Dataloom[postgres]: CREATE TABLE IF NOT EXISTS "posts" ("id" BIGSERIAL PRIMARY KEY UNIQUE NOT NULL, "title" TEXT NOT NULL DEFAULT 'Hello there!!');
[2024-02-04 11:48:51.444886] : Dataloom[postgres]: SELECT tablename FROM pg_catalog.pg_tables WHERE schemaname='public';
[2024-02-04 11:48:51.691407] : Dataloom[postgres]: DROP TABLE IF EXISTS "users" CASCADE;
[2024-02-04 11:48:51.746306] : Dataloom[postgres]: CREATE TABLE IF NOT EXISTS "users" ("id" BIGSERIAL PRIMARY KEY UNIQUE NOT NULL, "name" VARCHAR(255) UNIQUE, "username" TEXT NOT NULL DEFAULT 'Hello there!!');
[2024-02-04 11:48:51.816315] : Dataloom[postgres]: DROP TABLE IF EXISTS "posts" CASCADE;
[2024-02-04 11:48:51.857688] : Dataloom[postgres]: CREATE TABLE IF NOT EXISTS "posts" ("completed" BOOLEAN DEFAULT False, "id" BIGSERIAL PRIMARY KEY UNIQUE NOT NULL, "title" VARCHAR(255) NOT NULL);
[2024-02-04 11:48:51.901722] : Dataloom[postgres]: SELECT tablename FROM pg_catalog.pg_tables WHERE schemaname='public';
[2024-02-04 11:48:52.222311] : Dataloom[postgres]: DROP TABLE IF EXISTS "posts" CASCADE;
[2024-02-04 11:48:52.264311] : Dataloom[postgres]: CREATE TABLE IF NOT EXISTS "posts" ("completed" BOOLEAN DEFAULT False, "id" BIGSERIAL PRIMARY KEY UNIQUE NOT NULL, "title" VARCHAR(255) NOT NULL, "createdAt" TIMESTAMP DEFAULT CURRENT_TIMESTAMP, "updatedAt" TIMESTAMP DEFAULT CURRENT_TIMESTAMP, "userId" BIGSERIAL NOT NULL REFERENCES "users"("id") ON DELETE CASCADE ON UPDATE CASCADE);
[2024-02-04 11:48:52.322922] : Dataloom[postgres]: DROP TABLE IF EXISTS "users" CASCADE;
[2024-02-04 11:48:52.366951] : Dataloom[postgres]: CREATE TABLE IF NOT EXISTS "users" ("id" BIGSERIAL PRIMARY KEY UNIQUE NOT NULL, "name" TEXT NOT NULL DEFAULT 'Bob', "username" VARCHAR(255) UNIQUE, "createdAt" TIMESTAMP DEFAULT CURRENT_TIMESTAMP, "updatedAt" TIMESTAMP DEFAULT CURRENT_TIMESTAMP);
[2024-02-04 11:48:52.419921] : Dataloom[postgres]: SELECT tablename FROM pg_catalog.pg_tables WHERE schemaname='public';
[2024-02-04 11:48:52.468921] : Dataloom[postgres]: INSERT INTO "users" ("username") VALUES (%s) RETURNING "id";
[2024-02-04 11:48:52.501978] : Dataloom[postgres]: INSERT INTO "posts" ("title", "userId") VALUES (%s, %s) RETURNING "id";
[2024-02-04 11:48:52.822859] : Dataloom[postgres]: DROP TABLE IF EXISTS "posts" CASCADE;
[2024-02-04 11:48:52.889768] : Dataloom[postgres]: CREATE TABLE IF NOT EXISTS "posts" ("completed" BOOLEAN DEFAULT False, "id" BIGSERIAL PRIMARY KEY UNIQUE NOT NULL, "title" VARCHAR(255) NOT NULL, "createdAt" TIMESTAMP DEFAULT CURRENT_TIMESTAMP, "updatedAt" TIMESTAMP DEFAULT CURRENT_TIMESTAMP, "userId" BIGSERIAL NOT NULL REFERENCES "users"("id") ON DELETE CASCADE ON UPDATE CASCADE);
[2024-02-04 11:48:52.985679] : Dataloom[postgres]: DROP TABLE IF EXISTS "users" CASCADE;
[2024-02-04 11:48:53.050500] : Dataloom[postgres]: CREATE TABLE IF NOT EXISTS "users" ("id" BIGSERIAL PRIMARY KEY UNIQUE NOT NULL, "name" TEXT NOT NULL DEFAULT 'Bob', "username" VARCHAR(255) UNIQUE, "createdAt" TIMESTAMP DEFAULT CURRENT_TIMESTAMP, "updatedAt" TIMESTAMP DEFAULT CURRENT_TIMESTAMP);
[2024-02-04 11:48:53.106497] : Dataloom[postgres]: SELECT tablename FROM pg_catalog.pg_tables WHERE schemaname='public';
[2024-02-04 11:48:53.165507] : Dataloom[postgres]: INSERT INTO "users" ("username") VALUES (%s) RETURNING "id";
[2024-02-04 11:48:53.203505] : Dataloom[postgres]: INSERT INTO "posts" ("title", "userId") VALUES (%s, %s) RETURNING *;
[2024-02-04 11:48:53.436504] : Dataloom[postgres]: DROP TABLE IF EXISTS "posts" CASCADE;
[2024-02-04 11:48:53.493521] : Dataloom[postgres]: CREATE TABLE IF NOT EXISTS "posts" ("completed" BOOLEAN DEFAULT False, "id" BIGSERIAL PRIMARY KEY UNIQUE NOT NULL, "title" VARCHAR(255) NOT NULL, "createdAt" TIMESTAMP DEFAULT CURRENT_TIMESTAMP, "updatedAt" TIMESTAMP DEFAULT CURRENT_TIMESTAMP, "userId" BIGSERIAL NOT NULL REFERENCES "users"("id") ON DELETE CASCADE ON UPDATE CASCADE);
[2024-02-04 11:48:53.564354] : Dataloom[postgres]: DROP TABLE IF EXISTS "users" CASCADE;
[2024-02-04 11:48:53.617272] : Dataloom[postgres]: CREATE TABLE IF NOT EXISTS "users" ("id" BIGSERIAL PRIMARY KEY UNIQUE NOT NULL, "name" TEXT NOT NULL DEFAULT 'Bob', "username" VARCHAR(255) UNIQUE);
[2024-02-04 11:48:53.670876] : Dataloom[postgres]: SELECT tablename FROM pg_catalog.pg_tables WHERE schemaname='public';
[2024-02-04 11:48:53.725820] : Dataloom[postgres]: INSERT INTO "users" ("username") VALUES (%s) RETURNING "id";
[2024-02-04 11:48:53.769168] : Dataloom[postgres]: INSERT INTO "posts" ("title", "userId") VALUES (%s, %s) RETURNING *;
[2024-02-04 11:48:53.809823] : Dataloom[postgres]: SELECT "completed", "createdAt", "id", "title", "updatedAt", "userId" FROM "posts" WHERE "id" = %s AND "userId" = %s;
[2024-02-04 11:48:53.842578] : Dataloom[postgres]: SELECT "id", "name", "username" FROM "users";
[2024-02-04 11:48:53.878529] : Dataloom[postgres]: SELECT "id", "name", "username" FROM "users" WHERE "id" = %s;
[2024-02-04 11:48:53.918522] : Dataloom[postgres]: SELECT "id", "name", "username" FROM "users" WHERE "id" = %s;
[2024-02-04 11:48:53.950530] : Dataloom[postgres]: SELECT "id", "name", "username" FROM "users" WHERE "id" = %s;
[2024-02-04 11:48:53.985529] : Dataloom[postgres]: SELECT "id", "name", "username" FROM "users" WHERE "id" = %s;
[2024-02-04 11:48:54.019520] : Dataloom[postgres]: SELECT "id", "name", "username" FROM "users" WHERE "id" = %s AND "name" = %s;
[2024-02-04 11:48:54.050732] : Dataloom[postgres]: SELECT "id", "name", "username" FROM "users" WHERE "id" = %s AND "username" = %s;
[2024-02-04 11:48:54.086203] : Dataloom[postgres]: SELECT "id", "name", "username" FROM "users" WHERE "name" = %s AND "username" = %s;
[2024-02-04 11:48:54.118318] : Dataloom[postgres]: SELECT "id", "name", "username" FROM "users" WHERE "id" = %s;
[2024-02-04 11:48:54.149394] : Dataloom[postgres]: SELECT "id", "name", "username" FROM "users" WHERE "id" = %s;
[2024-02-04 11:48:54.181428] : Dataloom[postgres]: SELECT "id", "name", "username" FROM "users" WHERE "id" = %s AND "name" = %s;
[2024-02-04 11:48:54.214428] : Dataloom[postgres]: SELECT "id", "name", "username" FROM "users" WHERE "id" = %s AND "username" = %s;
[2024-02-04 11:48:54.247992] : Dataloom[postgres]: SELECT "id", "name", "username" FROM "users" WHERE "name" = %s AND "username" = %s;
[2024-02-04 11:48:54.282060] : Dataloom[postgres]: SELECT "completed", "createdAt", "id", "title", "updatedAt", "userId" FROM "posts";
[2024-02-04 11:48:54.516256] : Dataloom[postgres]: DROP TABLE IF EXISTS "posts" CASCADE;
[2024-02-04 11:48:54.572575] : Dataloom[postgres]: CREATE TABLE IF NOT EXISTS "posts" ("completed" BOOLEAN DEFAULT False, "id" BIGSERIAL PRIMARY KEY UNIQUE NOT NULL, "title" VARCHAR(255) NOT NULL, "createdAt" TIMESTAMP DEFAULT CURRENT_TIMESTAMP, "updatedAt" TIMESTAMP DEFAULT CURRENT_TIMESTAMP, "userId" BIGSERIAL NOT NULL REFERENCES "users"("id") ON DELETE CASCADE ON UPDATE CASCADE);
[2024-02-04 11:48:54.633159] : Dataloom[postgres]: DROP TABLE IF EXISTS "users" CASCADE;
[2024-02-04 11:48:54.681030] : Dataloom[postgres]: CREATE TABLE IF NOT EXISTS "users" ("id" BIGSERIAL PRIMARY KEY UNIQUE NOT NULL, "name" TEXT NOT NULL DEFAULT 'Bob', "username" VARCHAR(255) UNIQUE, "createdAt" TIMESTAMP DEFAULT CURRENT_TIMESTAMP, "updatedAt" TIMESTAMP DEFAULT CURRENT_TIMESTAMP);
[2024-02-04 11:48:54.725766] : Dataloom[postgres]: SELECT tablename FROM pg_catalog.pg_tables WHERE schemaname='public';
[2024-02-04 11:48:54.775765] : Dataloom[postgres]: INSERT INTO "users" ("username") VALUES (%s) RETURNING "id";
[2024-02-04 11:48:54.807760] : Dataloom[postgres]: INSERT INTO "posts" ("title", "userId") VALUES (%s, %s) RETURNING *;
[2024-02-04 11:48:54.894293] : Dataloom[postgres]: UPDATE "users" SET "updatedAt" = %s WHERE "id" = %s;
[2024-02-04 11:48:54.928751] : Dataloom[postgres]: UPDATE "users" SET "updatedAt" = %s WHERE "id" = %s;
[2024-02-04 11:48:54.962293] : Dataloom[postgres]: SELECT "createdAt", "id", "name", "updatedAt", "username" FROM "users" WHERE "id" = %s;
[2024-02-04 11:48:55.008299] : Dataloom[postgres]: UPDATE "users" SET "id" = %s, "updatedAt" = %s WHERE "id" = %s;
[2024-02-04 11:48:55.182816] : Dataloom[postgres]: DROP TABLE IF EXISTS "posts" CASCADE;
[2024-02-04 11:48:55.219888] : Dataloom[postgres]: CREATE TABLE IF NOT EXISTS "posts" ("completed" BOOLEAN DEFAULT False, "id" BIGSERIAL PRIMARY KEY UNIQUE NOT NULL, "title" VARCHAR(255) NOT NULL, "createdAt" TIMESTAMP DEFAULT CURRENT_TIMESTAMP, "userId" BIGSERIAL NOT NULL REFERENCES "users"("id") ON DELETE CASCADE ON UPDATE CASCADE);
[2024-02-04 11:48:55.285816] : Dataloom[postgres]: DROP TABLE IF EXISTS "users" CASCADE;
[2024-02-04 11:48:55.342827] : Dataloom[postgres]: CREATE TABLE IF NOT EXISTS "users" ("id" BIGSERIAL PRIMARY KEY UNIQUE NOT NULL, "name" TEXT NOT NULL DEFAULT 'Bob', "username" VARCHAR(255) UNIQUE, "createdAt" TIMESTAMP DEFAULT CURRENT_TIMESTAMP, "updatedAt" TIMESTAMP DEFAULT CURRENT_TIMESTAMP);
[2024-02-04 11:48:55.397905] : Dataloom[postgres]: SELECT tablename FROM pg_catalog.pg_tables WHERE schemaname='public';
[2024-02-04 11:48:55.456913] : Dataloom[postgres]: INSERT INTO "users" ("username") VALUES (%s) RETURNING "id";
[2024-02-04 11:48:55.500920] : Dataloom[postgres]: INSERT INTO "posts" ("title", "userId") VALUES (%s, %s) RETURNING *;
[2024-02-04 11:48:55.590456] : Dataloom[postgres]: 
        UPDATE "users" SET "name" = %s, "updatedAt" = %s WHERE "id" = (
            SELECT "id" FROM  "users" WHERE "username" = %s LIMIT 1
        );
        
[2024-02-04 11:48:55.624542] : Dataloom[postgres]: 
        UPDATE "users" SET "name" = %s, "updatedAt" = %s WHERE "id" = (
            SELECT "id" FROM  "users" WHERE "username" = %s LIMIT 1
        );
        
[2024-02-04 11:48:55.656864] : Dataloom[postgres]: SELECT "createdAt", "id", "name", "updatedAt", "username" FROM "users" WHERE "id" = %s;
[2024-02-04 11:48:55.689085] : Dataloom[postgres]: 
        UPDATE "users" SET "id" = %s, "updatedAt" = %s WHERE "id" = (
            SELECT "id" FROM  "users" WHERE "username" = %s LIMIT 1
        );
        
[2024-02-04 11:48:55.915679] : Dataloom[postgres]: DROP TABLE IF EXISTS "posts" CASCADE;
[2024-02-04 11:48:55.974945] : Dataloom[postgres]: CREATE TABLE IF NOT EXISTS "posts" ("completed" BOOLEAN DEFAULT False, "id" BIGSERIAL PRIMARY KEY UNIQUE NOT NULL, "title" VARCHAR(255) NOT NULL, "createdAt" TIMESTAMP DEFAULT CURRENT_TIMESTAMP, "userId" BIGSERIAL NOT NULL REFERENCES "users"("id") ON DELETE CASCADE ON UPDATE CASCADE);
[2024-02-04 11:48:56.039691] : Dataloom[postgres]: DROP TABLE IF EXISTS "users" CASCADE;
[2024-02-04 11:48:56.090756] : Dataloom[postgres]: CREATE TABLE IF NOT EXISTS "users" ("id" BIGSERIAL PRIMARY KEY UNIQUE NOT NULL, "name" TEXT NOT NULL DEFAULT 'Bob', "username" VARCHAR(255) UNIQUE, "createdAt" TIMESTAMP DEFAULT CURRENT_TIMESTAMP, "updatedAt" TIMESTAMP DEFAULT CURRENT_TIMESTAMP);
[2024-02-04 11:48:56.143036] : Dataloom[postgres]: SELECT tablename FROM pg_catalog.pg_tables WHERE schemaname='public';
[2024-02-04 11:48:56.212031] : Dataloom[postgres]: INSERT INTO "users" ("username") VALUES (%s) RETURNING "id";
[2024-02-04 11:48:56.265028] : Dataloom[postgres]: INSERT INTO "posts" ("title", "userId") VALUES (%s, %s) RETURNING *;
[2024-02-04 11:48:56.294165] : Dataloom[postgres]: UPDATE "posts" SET "title" = %s WHERE "userId" = %s;
[2024-02-04 11:48:56.318024] : Dataloom[postgres]: UPDATE "posts" SET "title" = %s WHERE "userId" = %s;
[2024-02-04 11:48:56.339029] : Dataloom[postgres]: UPDATE "posts" SET "userId" = %s WHERE "userId" = %s;
[2024-02-04 11:48:56.383051] : Dataloom[sqlite]: DROP TABLE IF EXISTS users;
[2024-02-04 11:48:56.430084] : Dataloom[sqlite]: DROP TABLE IF EXISTS users;
[2024-02-04 11:48:56.471966] : Dataloom[sqlite]: DROP TABLE IF EXISTS users;
[2024-02-04 11:48:56.509625] : Dataloom[sqlite]: CREATE TABLE IF NOT EXISTS `users` (`id` INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL, `name` VARCHAR, `username` TEXT NOT NULL);
[2024-02-04 11:48:56.538687] : Dataloom[sqlite]: DROP TABLE IF EXISTS posts;
[2024-02-04 11:48:56.563618] : Dataloom[sqlite]: CREATE TABLE IF NOT EXISTS `posts` (`id` INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL, `title` TEXT NOT NULL);
[2024-02-04 11:48:56.585623] : Dataloom[sqlite]: SELECT name FROM sqlite_master WHERE type='table';
[2024-02-04 11:48:56.620622] : Dataloom[sqlite]: DROP TABLE IF EXISTS users;
[2024-02-04 11:48:56.665627] : Dataloom[sqlite]: CREATE TABLE IF NOT EXISTS `users` (`id` INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL, `name` VARCHAR UNIQUE, `username` TEXT NOT NULL DEFAULT 'Hello there!!');
[2024-02-04 11:48:56.704193] : Dataloom[sqlite]: DROP TABLE IF EXISTS posts;
[2024-02-04 11:48:56.744187] : Dataloom[sqlite]: CREATE TABLE IF NOT EXISTS `posts` (`completed` BOOLEAN DEFAULT False, `id` INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL, `title` VARCHAR NOT NULL);
[2024-02-04 11:48:56.781250] : Dataloom[sqlite]: SELECT name FROM sqlite_master WHERE type='table';
[2024-02-04 11:48:56.826225] : Dataloom[sqlite]: DROP TABLE IF EXISTS posts;
[2024-02-04 11:48:56.873305] : Dataloom[sqlite]: CREATE TABLE IF NOT EXISTS `posts` (`completed` BOOLEAN DEFAULT False, `id` INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL, `title` VARCHAR NOT NULL, `createdAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP, `updatedAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP, `userId` INTEGER NOT NULL REFERENCES `users`(`id`) ON DELETE CASCADE ON UPDATE CASCADE);
[2024-02-04 11:48:56.914277] : Dataloom[sqlite]: DROP TABLE IF EXISTS users;
[2024-02-04 11:48:56.954225] : Dataloom[sqlite]: CREATE TABLE IF NOT EXISTS `users` (`id` INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL, `name` TEXT NOT NULL DEFAULT 'Bob', `username` VARCHAR UNIQUE, `createdAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP, `updatedAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP);
[2024-02-04 11:48:57.008670] : Dataloom[sqlite]: SELECT name FROM sqlite_master WHERE type='table';
[2024-02-04 11:48:57.051739] : Dataloom[sqlite]: INSERT INTO `users` (`username`) VALUES (?);
[2024-02-04 11:48:57.106229] : Dataloom[sqlite]: INSERT INTO `posts` (`title`, `userId`) VALUES (?, ?);
[2024-02-04 11:48:57.171223] : Dataloom[sqlite]: DROP TABLE IF EXISTS posts;
[2024-02-04 11:48:57.246810] : Dataloom[sqlite]: CREATE TABLE IF NOT EXISTS `posts` (`completed` BOOLEAN DEFAULT False, `id` INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL, `title` VARCHAR NOT NULL, `createdAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP, `updatedAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP, `userId` INTEGER NOT NULL REFERENCES `users`(`id`) ON DELETE CASCADE ON UPDATE CASCADE);
[2024-02-04 11:48:57.301809] : Dataloom[sqlite]: DROP TABLE IF EXISTS users;
[2024-02-04 11:48:57.384367] : Dataloom[sqlite]: CREATE TABLE IF NOT EXISTS `users` (`id` INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL, `name` TEXT NOT NULL DEFAULT 'Bob', `username` VARCHAR UNIQUE, `createdAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP, `updatedAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP);
[2024-02-04 11:48:57.425354] : Dataloom[sqlite]: SELECT name FROM sqlite_master WHERE type='table';
[2024-02-04 11:48:57.452442] : Dataloom[sqlite]: INSERT INTO `users` (`username`) VALUES (?);
[2024-02-04 11:48:57.484344] : Dataloom[sqlite]: INSERT INTO `posts` (`title`, `userId`) VALUES (?, ?);
[2024-02-04 11:48:57.525152] : Dataloom[sqlite]: DROP TABLE IF EXISTS posts;
[2024-02-04 11:48:57.563152] : Dataloom[sqlite]: CREATE TABLE IF NOT EXISTS `posts` (`completed` BOOLEAN DEFAULT False, `id` INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL, `title` VARCHAR NOT NULL, `createdAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP, `updatedAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP, `userId` INTEGER NOT NULL REFERENCES `users`(`id`) ON DELETE CASCADE ON UPDATE CASCADE);
[2024-02-04 11:48:57.587873] : Dataloom[sqlite]: DROP TABLE IF EXISTS users;
[2024-02-04 11:48:57.610871] : Dataloom[sqlite]: CREATE TABLE IF NOT EXISTS `users` (`id` INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL, `name` TEXT NOT NULL DEFAULT 'Bob', `username` VARCHAR UNIQUE);
[2024-02-04 11:48:57.634872] : Dataloom[sqlite]: SELECT name FROM sqlite_master WHERE type='table';
[2024-02-04 11:48:57.659976] : Dataloom[sqlite]: INSERT INTO `users` (`username`) VALUES (?);
[2024-02-04 11:48:57.689874] : Dataloom[sqlite]: INSERT INTO `posts` (`title`, `userId`) VALUES (?, ?);
[2024-02-04 11:48:57.716877] : Dataloom[sqlite]: SELECT `completed`, `createdAt`, `id`, `title`, `updatedAt`, `userId` FROM `posts` WHERE `id` = ? AND `userId` = ?;
[2024-02-04 11:48:57.742873] : Dataloom[sqlite]: SELECT `id`, `name`, `username` FROM `users`;
[2024-02-04 11:48:57.768017] : Dataloom[sqlite]: SELECT `id`, `name`, `username` FROM `users` WHERE `id` = ?;
[2024-02-04 11:48:57.800476] : Dataloom[sqlite]: SELECT `id`, `name`, `username` FROM `users` WHERE `id` = ?;
[2024-02-04 11:48:57.828474] : Dataloom[sqlite]: SELECT `id`, `name`, `username` FROM `users` WHERE `id` = ?;
[2024-02-04 11:48:57.856479] : Dataloom[sqlite]: SELECT `id`, `name`, `username` FROM `users` WHERE `id` = ?;
[2024-02-04 11:48:57.884135] : Dataloom[sqlite]: SELECT `id`, `name`, `username` FROM `users` WHERE `id` = ? AND `name` = ?;
[2024-02-04 11:48:57.903040] : Dataloom[sqlite]: SELECT `id`, `name`, `username` FROM `users` WHERE `id` = ? AND `username` = ?;
[2024-02-04 11:48:57.928045] : Dataloom[sqlite]: SELECT `id`, `name`, `username` FROM `users` WHERE `name` = ? AND `username` = ?;
[2024-02-04 11:48:57.947040] : Dataloom[sqlite]: SELECT `id`, `name`, `username` FROM `users` WHERE `id` = ?;
[2024-02-04 11:48:57.980044] : Dataloom[sqlite]: SELECT `id`, `name`, `username` FROM `users` WHERE `id` = ?;
[2024-02-04 11:48:58.012098] : Dataloom[sqlite]: SELECT `id`, `name`, `username` FROM `users` WHERE `id` = ? AND `name` = ?;
[2024-02-04 11:48:58.042104] : Dataloom[sqlite]: SELECT `id`, `name`, `username` FROM `users` WHERE `id` = ? AND `username` = ?;
[2024-02-04 11:48:58.073059] : Dataloom[sqlite]: SELECT `id`, `name`, `username` FROM `users` WHERE `name` = ? AND `username` = ?;
[2024-02-04 11:48:58.103291] : Dataloom[sqlite]: SELECT `completed`, `createdAt`, `id`, `title`, `updatedAt`, `userId` FROM `posts`;
[2024-02-04 11:48:58.152371] : Dataloom[sqlite]: DROP TABLE IF EXISTS posts;
[2024-02-04 11:48:58.202978] : Dataloom[sqlite]: CREATE TABLE IF NOT EXISTS `posts`
 (`completed` BOOLEAN DEFAULT False, `id` INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL,
  `title` VARCHAR NOT NULL, `createdAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP, `updatedAt`
   TIMESTAMP DEFAULT CURRENT_TIMESTAMP, `userId` INTEGER NOT NULL REFERENCES `users`(`id`) ON DELETE CASCADE ON UPDATE CASCADE);
[2024-02-04 11:48:58.240048] : Dataloom[sqlite]: DROP TABLE IF EXISTS users;
[2024-02-04 11:48:58.278033] : Dataloom[sqlite]: CREATE TABLE IF NOT EXISTS `users` (`id` INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL, `name` TEXT NOT NULL DEFAULT 'Bob', `username` VARCHAR UNIQUE, `createdAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP, `updatedAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP);
[2024-02-04 11:48:58.329710] : Dataloom[sqlite]: SELECT name FROM sqlite_master WHERE type='table';
[2024-02-04 11:48:58.366705] : Dataloom[sqlite]: INSERT INTO `users` (`username`) VALUES (?);
[2024-02-04 11:48:58.411525] : Dataloom[sqlite]: INSERT INTO `posts` (`title`, `userId`) VALUES (?, ?);
[2024-02-04 11:48:58.511497] : Dataloom[sqlite]: UPDATE `users` SET `updatedAt` = ? WHERE `id` = ?;
[2024-02-04 11:48:58.560486] : Dataloom[sqlite]: UPDATE `users` SET `updatedAt` = ? WHERE `id` = ?;
[2024-02-04 11:48:58.594482] : Dataloom[sqlite]: SELECT `createdAt`, `id`, `name`, `updatedAt`, `username` FROM `users` WHERE `id` = ?;
[2024-02-04 11:48:58.637129] : Dataloom[sqlite]: DROP TABLE IF EXISTS posts;
[2024-02-04 11:48:58.686159] : Dataloom[sqlite]: CREATE TABLE IF NOT EXISTS `posts` (`completed` BOOLEAN DEFAULT False, `id` INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL, `title` VARCHAR NOT NULL, `createdAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP, `userId` INTEGER NOT NULL REFERENCES `users`(`id`) ON DELETE CASCADE ON UPDATE CASCADE);
[2024-02-04 11:48:58.731125] : Dataloom[sqlite]: DROP TABLE IF EXISTS users;
[2024-02-04 11:48:58.770736] : Dataloom[sqlite]: CREATE TABLE IF NOT EXISTS `users` (`id` INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL, `name` TEXT NOT NULL DEFAULT 'Bob', `username` VARCHAR UNIQUE, `createdAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP, `updatedAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP);
[2024-02-04 11:48:58.807933] : Dataloom[sqlite]: SELECT name FROM sqlite_master WHERE type='table';
[2024-02-04 11:48:58.833933] : Dataloom[sqlite]: INSERT INTO `users` (`username`) VALUES (?);
[2024-02-04 11:48:58.868398] : Dataloom[sqlite]: INSERT INTO `posts` (`title`, `userId`) VALUES (?, ?);
[2024-02-04 11:48:58.955453] : Dataloom[sqlite]: 
        UPDATE `posts` SET `title` = ? WHERE `id` = (
            SELECT `id` FROM  `posts` WHERE `userId` = ? LIMIT 1
        );
        
[2024-02-04 11:48:59.002420] : Dataloom[sqlite]: 
        UPDATE `posts` SET `title` = ? WHERE `id` = (
            SELECT `id` FROM  `posts` WHERE `userId` = ? LIMIT 1
        );
        
[2024-02-04 11:48:59.041677] : Dataloom[sqlite]: SELECT `completed`, `createdAt`, `id`, `title`, `userId` FROM `posts` WHERE `id` = ?;
[2024-02-04 11:48:59.091433] : Dataloom[sqlite]: DROP TABLE IF EXISTS posts;
[2024-02-04 11:48:59.133917] : Dataloom[sqlite]: CREATE TABLE IF NOT EXISTS `posts` (`completed` BOOLEAN DEFAULT False, `id` INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL, `title` VARCHAR NOT NULL, `createdAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP, `userId` INTEGER NOT NULL REFERENCES `users`(`id`) ON DELETE CASCADE ON UPDATE CASCADE);
[2024-02-04 11:48:59.165418] : Dataloom[sqlite]: DROP TABLE IF EXISTS users;
[2024-02-04 11:48:59.194416] : Dataloom[sqlite]: CREATE TABLE IF NOT EXISTS `users` (`id` INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL, `name` TEXT NOT NULL DEFAULT 'Bob', `username` VARCHAR UNIQUE, `createdAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP, `updatedAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP);
[2024-02-04 11:48:59.217417] : Dataloom[sqlite]: SELECT name FROM sqlite_master WHERE type='table';
[2024-02-04 11:48:59.238421] : Dataloom[sqlite]: INSERT INTO `users` (`username`) VALUES (?);
[2024-02-04 11:48:59.277422] : Dataloom[sqlite]: INSERT INTO `posts` (`title`, `userId`) VALUES (?, ?);
[2024-02-04 11:48:59.368686] : Dataloom[sqlite]: UPDATE `posts` SET `title` = ? WHERE `userId` = ?;
[2024-02-04 11:48:59.406422] : Dataloom[sqlite]: UPDATE `posts` SET `title` = ? WHERE `userId` = ?;
[2024-02-04 11:48:59.435720] : Dataloom[sqlite]: SELECT `completed`, `createdAt`, `id`, `title`, `userId` FROM `posts` WHERE `id` = ?;
