db.createUser(
    {
        user: "root",
        pwd: "example",
        roles: [
            {
                role: "readWrite",
                db: "rent_me"
            }
        ]
    }
)
