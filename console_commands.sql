SELECT * FROM user;

ALTER TABLE user ADD online BOOLEAN;

delete from user where id = 7;


CREATE TABLE message (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    body TEXT,
    sender_id INTEGER,
    FOREIGN KEY (sender_id) REFERENCES user(id)
);


INSERT INTO message (body, sender_id) VALUES
('Hejsan', 'Hur är laget?', 1);

SELECT * FROM message;

ALTER TABLE message ADD read boolean;


SELECT * FROM message_recv;

CREATE TABLE message_recv(
    user_id INTEGER,
    message_id INTEGER,
    PRIMARY KEY (user_id, message_id),
    FOREIGN KEY (user_id) REFERENCES user(id),
    FOREIGN KEY (message_id) REFERENCES message(id)
)

INSERT INTO message_recv (user_id, message_id) VALUES 
(2, 1);

SELECT msg.title sender.name, recv.name FROM user sender
JOIN message msg on sender.id = msg.sender_id 
JOIN message_recv mr on msg.id = mr.message_id
JOIN user recv on mr.user_id = recv.id;