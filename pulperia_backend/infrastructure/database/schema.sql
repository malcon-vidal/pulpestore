-- 1. Usuarios y Roles (Admin, Pulpero, Cliente)
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    role VARCHAR(20) CHECK (role IN ('admin', 'pulpero', 'cliente')) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- 2. Pulperías (Tiendas asociadas)
CREATE TABLE stores (
    id SERIAL PRIMARY KEY,
    owner_id INT REFERENCES users(id) ON DELETE CASCADE,
    name VARCHAR(150) NOT NULL,
    address TEXT NOT NULL,
    latitude DECIMAL(10, 8) NOT NULL,
    longitude DECIMAL(11, 8) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- 3. Catálogo Maestro Global (Administrado por ti)
CREATE TABLE global_products (
    id SERIAL PRIMARY KEY,
    barcode VARCHAR(50) UNIQUE, -- Código de barras UPC/EAN
    name VARCHAR(150) NOT NULL,
    category VARCHAR(50),
    image_url TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- 4. Inventario Local por Pulpería (Stock, Costos y Precios propios de cada tienda)
CREATE TABLE store_inventory (
    id SERIAL PRIMARY KEY,
    store_id INT REFERENCES stores(id) ON DELETE CASCADE,
    product_id INT REFERENCES global_products(id) ON DELETE CASCADE,
    stock INT NOT NULL DEFAULT 0,
    min_stock INT NOT NULL DEFAULT 5, -- Para alertas de stock bajo
    cost_price DECIMAL(10, 2) NOT NULL, -- Precio de compra
    sale_price DECIMAL(10, 2) NOT NULL, -- Precio de venta al público
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UNIQUE(store_id, product_id)
);

-- 5. Ventas y Encargos (Pedidos)
CREATE TABLE orders (
    id SERIAL PRIMARY KEY,
    store_id INT REFERENCES stores(id) ON DELETE CASCADE,
    client_id INT REFERENCES users(id) ON DELETE SET NULL,
    order_type VARCHAR(20) CHECK (order_type IN ('venta_directa', 'encargo')) NOT NULL,
    status VARCHAR(20) CHECK (status IN ('pendiente', 'listo', 'completado', 'cancelado')) DEFAULT 'pendiente',
    total DECIMAL(10, 2) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- 6. Detalle del Pedido / Venta
CREATE TABLE order_items (
    id SERIAL PRIMARY KEY,
    order_id INT REFERENCES orders(id) ON DELETE CASCADE,
    product_id INT REFERENCES global_products(id) ON DELETE CASCADE,
    quantity INT NOT NULL,
    unit_price DECIMAL(10, 2) NOT NULL
);