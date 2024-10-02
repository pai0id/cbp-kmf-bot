-- +goose Up
-- +goose StatementBegin

CREATE TABLE IF NOT EXISTS member (
    id serial PRIMARY KEY,
    chat_id BIGINT NOT NULL UNIQUE,
    tg text NOT NULL,
    class text,
    info text
);

-- +goose StatementEnd

-- +goose Down
-- +goose StatementBegin
-- +goose StatementEnd
