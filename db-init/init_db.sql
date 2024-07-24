CREATE DATABASE IF NOT EXISTS my_database;

USE my_database;

CREATE TABLE IF NOT EXISTS my_movies (
    ID INT AUTO_INCREMENT PRIMARY KEY,
    pelicula VARCHAR(100),
    director VARCHAR(100),
    descripcion VARCHAR(500),
    Fechaestreno DATE
);


INSERT INTO my_movies (pelicula, director, descripcion, Fechaestreno) VALUES
    ("Leaving Las Vegas", "Mike Figgis", "Ben Sanderson, an alcoholic Hollywood screenwriter who lost everything because of his drinking, arrives in Las Vegas to drink himself to death.", "1995-10-27"),
    ("Othello", "Oliver Parker", "The evil Iago pretends to be friend of Othello in order to manipulate him to serve his own end in the film version of this Shakespeare classic.", "1995-12-15"),
    ("Now and Then", "Lesli Linka Glatter", "Waxing nostalgic about the bittersweet passage from childhood to puberty in this tender coming-of-age tale, four childhood girlfriends -- Teeny, Chrissy, Samantha and Roberta", "1995-10-20"),
    ("Persuasion", "Roger Michell", "This film adaptation of Jane Austen's last novel follows Anne Elliot, the daughter of a financially troubled aristocratic family, who is persuaded to break her engagement to Frederick Wentworth", "1995-09-27"),
    ("The City of Lost Children", "Marc Caro y Jean-Pierre", "A scientist in a surrealist society kidnaps children to steal their dreams, hoping that they slow his aging process.", "1995-05-16"),
    ("Shanghai Triad", "Zhang Yimou", "A provincial boy related to a Shanghai crime family is recruited by his uncle into cosmopolitan Shanghai in the 1930s to be a servant to a ganglord's mistress.", "1995-04-30");
