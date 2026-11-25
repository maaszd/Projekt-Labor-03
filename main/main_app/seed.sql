-- Alapadatok. A fájl többször is lefuthat: minden sor INSERT OR IGNORE, a meglévő adatot nem írja felül.
-- (A db.py a PRAGMA user_version alapján futtatja; ha új adatot adsz hozzá, emeld a SEED_VERZIO-t.)

INSERT OR IGNORE INTO Item (id, nev, tipus, ritkasag, bonus_tamadas, bonus_vedekezes, arany_ertek, kep_utvonal, slot) VALUES
 (1, 'Kard',     'WEAPON', 'COMMON', 5,  0, 50, 'assets/sword.png',      'kard'),
 (2, 'Mellvért', 'ARMOR',  'COMMON', 0, 1, 60, 'assets/chestplate.png', 'mellvert'),
 (3, 'Sisak',    'ARMOR',  'COMMON', 0, 1, 45, 'assets/helmet.png',     'sisak'),
 (4, 'Pajzs',    'ARMOR',  'COMMON', 0, 1, 45, 'assets/shield.png',     'pajzs'),
 (5, 'Kesztyű',  'ARMOR',  'COMMON', 0,  1, 25, 'assets/gloves.png',     'kesztyu'),
 (6, 'Csizma',   'ARMOR',  'COMMON', 0,  1, 25, 'assets/boots.png',      'cipo');

-- Zsákmány tárgyak (szörnyek dobják)
INSERT OR IGNORE INTO Item (id, nev, tipus, ritkasag, bonus_tamadas, bonus_vedekezes, arany_ertek, kep_utvonal, slot) VALUES
 (7,  'Goblin tőr',        'WEAPON', 'COMMON',     6, 0,  70, 'assets/common_sword.png', 'kard'),
 (8,  'Zombi bőrpáncél',   'ARMOR',  'UNCOMMON',   0, 2,  90, 'assets/uncommon_armor.png',  'mellvert'),
 (9,  'Csontkard',         'WEAPON', 'UNCOMMON',   9, 0, 120, 'assets/uncommon_sword.png',    'kard'),
 (10, 'Pókselyem kesztyű', 'ARMOR',  'UNCOMMON',   0, 2,  90, 'assets/uncommon_gloves.png', 'kesztyu'),
 (11, 'Árnyék csizma',     'ARMOR',  'RARE',       0, 3, 150, 'assets/rare_boots.png',  'cipo'),
 (12, 'Démoni kard',       'WEAPON', 'EPIC',      16, 0, 600, 'assets/epic_sword.png',   'kard'),
 (13, 'Démoni korona',     'ARMOR',  'LEGENDARY',  0, 5, 800, 'assets/legendary_crown.png',   'sisak');

INSERT OR IGNORE INTO Szorny (id, nev, alap_hp, tamadas, vedekezes, kezdemenyezes, is_boss, titulus_jutalom) VALUES
 (1, 'Goblin',   30,  12,  2, 0.4, 0, NULL),
 (2, 'Farkas',   45, 15,  3, 0.6, 0, NULL),
 (3, 'Sárkány', 300, 40, 20, 0.3, 1, 'Sárkányölő');

-- A palya_1.json szörnyei (a név egyezik a JSON-ban lévő "nev" mezővel – ez alapján keresi a játék a dropokat)
INSERT OR IGNORE INTO Szorny (nev, alap_hp, tamadas, vedekezes, kezdemenyezes, is_boss, titulus_jutalom) VALUES
 ('Zombi',                  45, 10, 1, 0.4, 0, NULL),
 ('Csontváz Harcos',        40, 14, 4, 0.4, 0, NULL),
 ('Pók',                    25, 14, 0, 0.4, 0, NULL),
 ('Árnyék',                 50, 11, 3, 0.4, 0, NULL),
 ('BOSS: Demonic Overlord', 250, 25, 8, 0.4, 1, NULL);

-- Zsákmány: esely 0.25 = 25%, 1.0 = mindig; a mennyiség min..max között sorsolódik
INSERT OR IGNORE INTO Szorny_Drop (szorny_id, item_id, esely, min_mennyiseg, max_mennyiseg)
SELECT s.id, d.item_id, d.esely, 1, 1 FROM Szorny s JOIN (
          SELECT 'Goblin'                  AS nev,  7 AS item_id, 0.25 AS esely
    UNION ALL SELECT 'Zombi',                       8, 0.25
    UNION ALL SELECT 'Csontváz Harcos',             9, 0.20
    UNION ALL SELECT 'Pók',                        10, 0.25
    UNION ALL SELECT 'Árnyék',                     11, 0.20
    UNION ALL SELECT 'BOSS: Demonic Overlord',     12, 1.00
    UNION ALL SELECT 'BOSS: Demonic Overlord',     13, 0.60
) d ON d.nev = s.nev;

INSERT OR IGNORE INTO Map (id, nev, leiras, palya_fajl) VALUES
 (1, 'Sötét erdő', 'Goblinok és farkasok lakta erdő.', 'palya_1.json');

INSERT OR IGNORE INTO Kuldetes (id, cim, leiras, jutalom_arany, jutalom_xp) VALUES
 (1, 'Goblinvadászat',      'Győzz le 5 goblint a Sötét erdőben.', 100,  80),
 (2, 'A sárkány barlangja', 'Győzd le a sárkányt.',               1000, 500);