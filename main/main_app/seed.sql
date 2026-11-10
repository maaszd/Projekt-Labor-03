-- Alapadatok (csak akkor fut le, ha az Item tábla még üres)

INSERT INTO Item (id, nev, tipus, ritkasag, bonus_tamadas, bonus_vedekezes, arany_ertek, kep_utvonal, slot) VALUES
 (1, 'Kard',     'WEAPON', 'COMMON', 5,  0, 50, 'assets/sword.png',      'kard'),
 (2, 'Mellvért', 'ARMOR',  'COMMON', 0, 10, 60, 'assets/chestplate.png', 'mellvert'),
 (3, 'Sisak',    'ARMOR',  'COMMON', 0, 15, 45, 'assets/helmet.png',     'sisak'),
 (4, 'Pajzs',    'ARMOR',  'COMMON', 0, 15, 45, 'assets/shield.png',     'pajzs'),
 (5, 'Kesztyű',  'ARMOR',  'COMMON', 0,  2, 25, 'assets/gloves.png',     'kesztyu'),
 (6, 'Csizma',   'ARMOR',  'COMMON', 0,  1, 25, 'assets/boots.png',      'cipo');

INSERT INTO Szorny (id, nev, alap_hp, tamadas, vedekezes, kezdemenyezes, is_boss, titulus_jutalom) VALUES
 (1, 'Goblin',   30,  8,  2, 0.4, 0, NULL),
 (2, 'Farkas',   45, 10,  3, 0.6, 0, NULL),
 (3, 'Sárkány', 300, 40, 20, 0.3, 1, 'Sárkányölő');

INSERT INTO Map (id, nev, leiras, palya_fajl) VALUES
 (1, 'Sötét erdő', 'Goblinok és farkasok lakta erdő.', 'palya_1.json');

INSERT INTO Kuldetes (id, cim, leiras, jutalom_arany, jutalom_xp) VALUES
 (1, 'Goblinvadászat',      'Győzz le 5 goblint a Sötét erdőben.', 100,  80),
 (2, 'A sárkány barlangja', 'Győzd le a sárkányt.',               1000, 500);
