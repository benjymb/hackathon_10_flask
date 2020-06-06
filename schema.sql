-- Table: public.companies

-- DROP TABLE companies;

CREATE TABLE companies
(
    id SERIAL NOT NULL,
    name VARCHAR(50),
    ruc integer,
    status boolean DEFAULT true,
    CONSTRAINT companies_pkey PRIMARY KEY (id)
)
