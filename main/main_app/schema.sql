CREATE TABLE IF NOT EXISTS Jatekos (
    id                  INTEGER PRIMARY KEY AUTOINCREMENT,
    nev                 VARCHAR(50) NOT NULL,
    szint               INTEGER NOT NULL DEFAULT 1   CHECK (szint >= 1),
    tapasztalati_pont   INTEGER NOT NULL DEFAULT 0   CHECK (tapasztalati_pont >= 0),
    aktualis_eletero    INTEGER NOT NULL DEFAULT 100 CHECK (aktualis_eletero >= 0),
    max_eletero         INTEGER NOT NULL DEFAULT 100 CHECK (max_eletero > 0),
    tamadoero           INTEGER NOT NULL DEFAULT 15  CHECK (tamadoero >= 0),
    vedekezes           INTEGER NOT NULL DEFAULT 5   CHECK (vedekezes >= 0),
    kezdemenyezes       FLOAT   NOT NULL DEFAULT 0.4,
    arany               INTEGER NOT NULL DEFAULT 0   CHECK (arany >= 0),
    mentes_slot         INTEGER NOT NULL DEFAULT 1   CHECK (mentes_slot >= 1),
    utolso_mentes       DATETIME DEFAULT CURRENT_TIMESTAMP,
    CHECK (aktualis_eletero <= max_eletero)
);

CREATE TABLE IF NOT EXISTS Item (
    id                  INTEGER PRIMARY KEY AUTOINCREMENT,
    nev                 VARCHAR(100) NOT NULL,
    tipus               VARCHAR(30)  NOT NULL CHECK (tipus IN ('ARMOR','WEAPON','ITEM')),         -- item.py: ItemType
    ritkasag            VARCHAR(20)  NOT NULL DEFAULT 'COMMON'
                        CHECK (ritkasag IN ('COMMON','UNCOMMON','RARE','EPIC','LEGENDARY')),      -- item.py: ItemRarity
    bonus_tamadas       INTEGER NOT NULL DEFAULT 0,
    bonus_vedekezes     INTEGER NOT NULL DEFAULT 0,
    arany_ertek         INTEGER NOT NULL DEFAULT 0 CHECK (arany_ertek >= 0),
    kep_utvonal         VARCHAR(200) NOT NULL DEFAULT '',   -- Item.image_path (pl. assets/sword.png)
    slot                VARCHAR(20)                         -- melyik felszerelés-gombra kerül (kard, sisak...); NULL = nem felszerelhető
);

CREATE TABLE IF NOT EXISTS Inventory (
    id                  INTEGER PRIMARY KEY AUTOINCREMENT,
    jatekos_id          INTEGER NOT NULL REFERENCES Jatekos(id) ON DELETE CASCADE,
    item_id             INTEGER NOT NULL REFERENCES Item(id)    ON DELETE CASCADE,
    fel_van_szerelve    BOOLEAN NOT NULL DEFAULT 0 CHECK (fel_van_szerelve IN (0,1)),
    mennyiseg           INTEGER NOT NULL DEFAULT 1 CHECK (mennyiseg >= 1),
    UNIQUE (jatekos_id, item_id)
);

CREATE TABLE IF NOT EXISTS Szorny (
    id                  INTEGER PRIMARY KEY AUTOINCREMENT,
    nev                 VARCHAR(50) NOT NULL UNIQUE,
    alap_hp             INTEGER NOT NULL CHECK (alap_hp > 0),
    tamadas             INTEGER NOT NULL DEFAULT 5 CHECK (tamadas >= 0),
    vedekezes           INTEGER NOT NULL DEFAULT 0 CHECK (vedekezes >= 0),
    kezdemenyezes       FLOAT   NOT NULL DEFAULT 0.4,
    is_boss             BOOLEAN NOT NULL DEFAULT 0 CHECK (is_boss IN (0,1)),
    titulus_jutalom     VARCHAR(100)
);

CREATE TABLE IF NOT EXISTS Kuldetes (
    id                  INTEGER PRIMARY KEY AUTOINCREMENT,
    cim                 VARCHAR(100) NOT NULL,
    leiras              TEXT,
    jutalom_arany       INTEGER NOT NULL DEFAULT 0 CHECK (jutalom_arany >= 0),
    jutalom_xp          INTEGER NOT NULL DEFAULT 0 CHECK (jutalom_xp >= 0)
);

CREATE TABLE IF NOT EXISTS Map (
    id                  INTEGER PRIMARY KEY AUTOINCREMENT,
    nev                 VARCHAR(100) NOT NULL UNIQUE,
    leiras              TEXT,
    palya_fajl          VARCHAR(100)                        -- a pálya szobáit leíró JSON (pl. palya_1.json)
);

-- Játékmező = mentett játékállás (játékosonként egy sor)

CREATE TABLE IF NOT EXISTS Jatekmezo (
    id                  INTEGER PRIMARY KEY AUTOINCREMENT,
    jatekos_id          INTEGER NOT NULL REFERENCES Jatekos(id)  ON DELETE CASCADE,
    item_id             INTEGER          REFERENCES Item(id)     ON DELETE SET NULL,
    szorny_id           INTEGER          REFERENCES Szorny(id)   ON DELETE SET NULL,
    kuldetes_id         INTEGER          REFERENCES Kuldetes(id) ON DELETE SET NULL,
    map_id              INTEGER          REFERENCES Map(id)      ON DELETE SET NULL,
    aktualis_hp         INTEGER NOT NULL CHECK (aktualis_hp >= 0),
    aktualis_map_id     INTEGER          REFERENCES Map(id)      ON DELETE SET NULL,
    kor                 INTEGER NOT NULL DEFAULT 1 CHECK (kor >= 1),
    aktualis_szoba      VARCHAR(100),                       -- melyik szobában van a hős (pl. 'Folyoso')
    hos_x               REAL,                               -- a hős pozíciója a szobában
    hos_y               REAL
);

CREATE INDEX IF NOT EXISTS idx_inventory_jatekos  ON Inventory(jatekos_id);
CREATE INDEX IF NOT EXISTS idx_inventory_item     ON Inventory(item_id);
CREATE INDEX IF NOT EXISTS idx_jatekmezo_jatekos  ON Jatekmezo(jatekos_id);
CREATE INDEX IF NOT EXISTS idx_jatekmezo_szorny   ON Jatekmezo(szorny_id);
CREATE INDEX IF NOT EXISTS idx_jatekmezo_kuldetes ON Jatekmezo(kuldetes_id);
CREATE INDEX IF NOT EXISTS idx_jatekmezo_map      ON Jatekmezo(map_id);
