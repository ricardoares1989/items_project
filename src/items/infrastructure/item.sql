CREATE TABLE items (
    uuid UUID PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    quantity INTEGER,
    description TEXT,
    planned_purchase_date TIMESTAMP,
    created_datetime TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    modified_datetime TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Trigger para actualizar las fechas de creación y modificación
CREATE OR REPLACE FUNCTION set_timestamp()
RETURNS TRIGGER AS $$
BEGIN
    IF TG_OP = 'INSERT' THEN
        NEW.created_datetime := CURRENT_TIMESTAMP;
        NEW.modified_datetime := CURRENT_TIMESTAMP;
    ELSIF TG_OP = 'UPDATE' THEN
        NEW.modified_datetime := CURRENT_TIMESTAMP;
    END IF;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER items_timestamp_trigger
BEFORE INSERT OR UPDATE ON items
FOR EACH ROW EXECUTE FUNCTION set_timestamp();