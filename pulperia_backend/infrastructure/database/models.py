from sqlalchemy import Column, Integer, String, Float, Text,ForeignKey, DateTime, CheckConstraint, UniqueConstraint
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from datetime import datetime

Base = declarative_base()

class UserModel(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    email = Column(String(100), unique=True, index=True, nullable=False)
    password_hash = Column(String(255), nullable=False)
    role = Column(String(20), nullable=False)  # 'admin', 'pulpero', 'cliente'
    created_at = Column(DateTime, default=datetime.utcnow)

    stores = relationship("StoreModel", back_populates="owner", cascade="all, delete-cascade")

class StoreModel(Base):
    __tablename__ = 'stores'

    id = Column(Integer, primary_key=True, index=True)
    owner_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    name = Column(String(150), nullable=False)
    address = Column(Text, nullable=False)
    latitude = Column(Float, nullable=False)
    longitude = Column(Float, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)

    owner = relationship("UserModel", back_populates="stores")
    inventory = relationship("StoreInventoryModel", back_populates="store", cascade="all, delete-cascade")

class GlobalProductModel(Base):
    __tablename__ = "global_products"

    id = Column(Integer, primary_key=True, index=True)
    barcode = Column(String(50), unique=True, index=True, nullable=True)
    name = Column(String(150), nullable=False)
    category = Column(String(50), nullable=True)
    image_url = Column(Text, nullable=True) # 'admin', 'pulpero', 'cliente'
    created_at = Column(DateTime, default=datetime.utcnow)
class StoreInventoryModel(Base):
    __tablename__ = "store_inventory"

    id = Column(Integer, primary_key=True, index=True)
    store_id = Column(Integer, ForeignKey("stores.id", ondelete="CASCADE"), nullable=False)
    product_id = Column(Integer, ForeignKey("global_products.id", ondelete="CASCADE"), nullable=False)
    stock = Column(Integer, default=0, nullable=False)
    min_stock = Column(Integer, default=5, nullable=False)
    cost_price = Column(Float, nullable=False)
    sale_price = Column(Float, nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    store = relationship("StoreModel", back_populates="inventory")
    product = relationship("GlobalProductModel")

    __table_args__ = (
        UniqueConstraint('store_id', 'product_id', name='uq_store_product'),
    )