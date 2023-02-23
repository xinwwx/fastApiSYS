aerich init -t config.database.TORTOISE_ORM
 aerich init-db
aerich migrate --name update_user
aerich upgrade
aerich downgrade