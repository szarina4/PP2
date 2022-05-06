
CREATE OR REPLACE FUNCTION search (p_pattern VARCHAR)
    RETURNS TABLE (
        first_name VARCHAR,
        phone_num VARCHAR
)
AS $$
BEGIN
    RETURN QUERY SELECT
        phonebook.first_name,
        phonebook.phone_num
    FROM
        phonebook
    WHERE
        phonebook.first_name ILIKE p_pattern ;
END; $$

LANGUAGE 'plpgsql';

SELECT
    search('Ai%');


---------------------------------------

CREATE OR REPLACE PROCEDURE new_user(name varchar(20),phone varchar(12))
AS $$
BEGIN
    IF EXISTS(SELECT 1 FROM phonebook WHERE first_name=name) THEN
        UPDATE phonebook SET phone_num=phone WHERE first_name=name;
    ELSE
        INSERT INTO phonebook(first_name, phone_num) VALUES(name,phone);

    end if;
END;
$$
    LANGUAGE 'plpgsql';

CALL new_user('new','766-665-3343');
SELECT * FROM phonebook WHERE first_name='new';

CALL new_user('Aidos', '676-434-3434');
SELECT * FROM phonebook WHERE first_name='Aidos';
------------------------------------------------------






-------------------------------------------------------
CREATE OR REPLACE FUNCTION paginated_func (lim integer,offe integer)
    RETURNS TABLE (
        first_name VARCHAR,
        phone_num VARCHAR
)
AS $$
BEGIN
    RETURN QUERY SELECT
        phonebook.first_name,
        phonebook.phone_num
    FROM
        phonebook
    LIMIT lim OFFSET offe;
END; $$

LANGUAGE 'plpgsql';

SELECT
    paginated_func(5,3);

---------------------------------------------------

CREATE OR REPLACE PROCEDURE delete_by_name(name VARCHAR)
AS
$$
BEGIN
    DELETE
    FROM phonebook p
    where p.first_name = $1;
END;
$$
    LANGUAGE plpgsql;

CALL delete_by_name('Pip');
SELECT * FROM phonebook;
SELECT 1 FROM phonebook WHERE phonebook.first_name='Pip';
--

CREATE OR REPLACE PROCEDURE delete_by_phone(phone VARCHAR)
AS
$$
BEGIN
    DELETE
    FROM phonebook p
    where p.phone_num = $1;
END;
$$
    LANGUAGE plpgsql;

CALL delete_by_phone('805-997-9780');
SELECT * FROM phonebook;
SELECT 1 FROM phonebook WHERE phonebook.phone_num='805-997-9780';
----------------------------------------------