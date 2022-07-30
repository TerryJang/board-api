-- BOARD --
DROP SCHEMA IF EXISTS develop;
CREATE SCHEMA develop;

DROP TABLE IF EXISTS develop.board;

-- BOARD --
CREATE TABLE develop.board (
                              id BIGINT NOT NULL AUTO_INCREMENT COMMENT '아이디',
                              title VARCHAR (255) NOT NULL COMMENT '제목',
                              content TEXT NOT NULL COMMENT '내용',
                              writer VARCHAR (255) NOT NULL COMMENT '작성자',
                              password VARCHAR (255) NOT NULL COMMENT '비밀번호',
                              is_deleted BOOLEAN NOT NULL DEFAULT false COMMENT '삭제여부',
                              deleted_at  DATETIME COMMENT '삭제일',
                              created_at DATETIME NOT NULL DEFAULT NOW() COMMENT '생성일',
                              updated_at DATETIME NOT NULL DEFAULT NOW() COMMENT '변경일',
    -- PRIMARY KEY --
                              CONSTRAINT PK_BOARD_ID PRIMARY KEY(ID)
    -- FOREIGN KEY --
    -- UNIQUE --
    -- CHECK --
)
;

CREATE INDEX IDX_BOARD_TITLE ON develop.board (title ASC);
CREATE INDEX IDX_BOARD_WRITER ON develop.board (writer ASC);
CREATE INDEX IDX_BOARD_IS_DELETED ON develop.board (is_deleted ASC);
CREATE INDEX IDX_BOARD_CREATED ON develop.board (created_at DESC);


DROP TABLE IF EXISTS develop.comment;

-- COMMENT --
CREATE TABLE develop.comment (
                               id BIGINT NOT NULL AUTO_INCREMENT COMMENT '아이디',
                               board_id BIGINT NOT NULL COMMENT '게시판 글 아이디',
                               writer VARCHAR (255) NOT NULL COMMENT '작성자',
                               content TEXT NOT NULL COMMENT '내용',
                               password VARCHAR (255) NOT NULL COMMENT '비밀번호',
                               is_deleted BOOLEAN NOT NULL DEFAULT false COMMENT '삭제여부',
                               deleted_at  DATETIME COMMENT '삭제일',
                               created_at DATETIME NOT NULL DEFAULT NOW() COMMENT '생성일',
                               updated_at DATETIME NOT NULL DEFAULT NOW() COMMENT '변경일',
    -- PRIMARY KEY --
                               CONSTRAINT PK_COMMENT_ID PRIMARY KEY(ID),
    -- FOREIGN KEY --
                               CONSTRAINT FK_COMMENT_BOARD_ID FOREIGN KEY (BOARD_ID) references develop.board (ID)
    -- UNIQUE --
    -- CHECK --
)
;

CREATE INDEX IDX_COMMENT_BOARD_ID ON develop.comment (BOARD_ID ASC);
CREATE INDEX IDX_BOARD_IS_DELETED ON develop.comment (is_deleted ASC);