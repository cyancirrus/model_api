insert into person (
    id_person,
    id_demographic 
) values 
    (0, 0),
    (1, 0),
    (2, 0),
    (3, 1),
    (4, 1),
    (5, 1),
    (6, 1),
    (7, 2),
    (8, 2),
    (9, 2)
;

insert into demographic(
    id_demographic,
    id_offer,
    rank_offer
) values
    /* demographic 0 */
    (0, 5, 1),
    (0, 4, 2),
    (0, 3, 3),
    (0, 2, 4),
    (0, 1, 5),
    /* demographic 1 */
    (1, 5, 2),
    (1, 4, 3),
    (1, 3, 4),
    (1, 2, 5),
    (1, 1, 1),
    /* demographic 2 */
    (2, 5, 3),
    (2, 4, 4),
    (2, 3, 5),
    (2, 2, 1),
    (2, 1, 2)
;

insert into offer (
    id_offer,
    disp_offer
) values
    (1, 'a'),
    (2, 'b'),
    (3, 'c'),
    (4, 'd'),
    (5, 'e')
;
