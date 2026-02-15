from gym_saas.app import create_app
from gym_saas.app.extensions import db
from sqlalchemy import text   # ✅ IMPORTANT

app = create_app()

with app.app_context():
    db.session.execute(text("DROP TABLE IF EXISTS alembic_version;"))
    db.session.commit()

    print("✅ alembic_version table reset")
