from app.database import Base, engine, SessionLocal
from app import models

Base.metadata.create_all(bind=engine)

def seed():
    db = SessionLocal()
    try:
        # create users
        u1 = models.User(name="Alice", email="alice@example.com", phone="+911234567890")
        u2 = models.User(name="Bob", email="bob@example.com", phone="+919876543210")
        db.add_all([u1, u2])
        db.commit()
        db.refresh(u1)
        db.refresh(u2)

        # transactions
        t1 = models.Transaction(user_id=u1.id, amount=100.0, description="initial topup")
        t2 = models.Transaction(user_id=u1.id, amount=-20.0, description="purchase")
        t3 = models.Transaction(user_id=u2.id, amount=50.0, description="initial topup")
        db.add_all([t1, t2, t3])
        db.commit()
        print("Seeded DB with sample users and transactions")
    finally:
        db.close()

if __name__ == '__main__':
    seed()