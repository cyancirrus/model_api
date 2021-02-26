create table if not exists person (
    id_person int,
    id_demographic int,
    key person (id_person)
);

create table if not exists demographic (
    id_demographic int,
    id_offer int,
    rank_offer int,
    key demo_rank (id_demographic, rank_offer)
);

create table if not exists offer (
    id_offer int,
    disp_offer varchar(20),
    key vendor (id_offer)
);

/* clear database */
/*
drop table person;
drop table demographic;
drop table offer;
*/