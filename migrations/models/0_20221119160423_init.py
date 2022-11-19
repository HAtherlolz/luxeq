from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        CREATE TABLE IF NOT EXISTS "category" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "name" VARCHAR(50) NOT NULL UNIQUE
);
CREATE TABLE IF NOT EXISTS "article" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "title" VARCHAR(50) NOT NULL,
    "image" VARCHAR(500),
    "writer" VARCHAR(50) NOT NULL,
    "time_of_read" SMALLINT NOT NULL,
    "date_created" TIMESTAMPTZ NOT NULL  DEFAULT CURRENT_TIMESTAMP,
    "category_id" INT REFERENCES "category" ("id") ON DELETE SET NULL
);
CREATE INDEX IF NOT EXISTS "idx_article_title_97ff44" ON "article" ("title");
CREATE TABLE IF NOT EXISTS "block" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "title" VARCHAR(50) NOT NULL,
    "article_id" INT NOT NULL REFERENCES "article" ("id") ON DELETE CASCADE
);
CREATE TABLE IF NOT EXISTS "paragraph" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "paragraph" TEXT NOT NULL,
    "block_id" INT NOT NULL REFERENCES "block" ("id") ON DELETE CASCADE
);
CREATE TABLE IF NOT EXISTS "aerich" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "version" VARCHAR(255) NOT NULL,
    "app" VARCHAR(100) NOT NULL,
    "content" JSONB NOT NULL
);"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        """
