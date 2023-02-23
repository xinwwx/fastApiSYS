TORTOISE_ORM = {
    "connections": {"default": "sqlite://sqlite3"},
    "apps": {
        "models": {
        	# models对应上面创建的models.py
            "models": ["aerich.models", "app.models.models"],
            "default_connection": "default",
        },
    },
}