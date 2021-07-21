PRAGMA
foreign_keys = ON;

/* product info */
CREATE TABLE IF NOT EXISTS product
(
    id               INTEGER PRIMARY KEY AUTOINCREMENT,
    date_of_creation timestamp NOT NULL,
    title            TEXT      NOT NULL
);

/* Table contains list of product images */
CREATE TABLE IF NOT EXISTS img_list
(
    product_id INTEGER NOT NULL,
    img        BLOB    NOT NULL,
    FOREIGN KEY (product_id) REFERENCES product (id)
);

/* seller info */
CREATE TABLE IF NOT EXISTS seller
(
    id       INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL,
    phone    TEXT NOT NULL,
    email    TEXT NOT NULL,
    address  TEXT NOT NULL
);

/* seller products */
CREATE TABLE IF NOT EXISTS product_seller
(
    seller_id  INTEGER NOT NULL,
    product_id INTEGER NOT NULL,
    FOREIGN KEY (seller_id) REFERENCES seller (id),
    FOREIGN KEY (product_id) REFERENCES product (id)
);

/* category table */
CREATE TABLE IF NOT EXISTS category
(
    name TEXT NOT NULL
);

/* product category */
CREATE TABLE  IF NOT EXISTS  product_category
(
    category   TEXT    NOT NULL,
    product_id INTEGER NOT NULL,
    FOREIGN KEY (category) REFERENCES category (name),
    FOREIGN KEY (product_id) REFERENCES product (id)
);
